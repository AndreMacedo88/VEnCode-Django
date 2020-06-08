from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from VEnCode_Django.celery import app, debug_task

from .models import Promoters154CellsBinarized
from .utils_views import *
from .forms import FantomForm, UploadFileForm
from .tasks import fantom_results_task, uploaded_results_task


# Create your views here.
def home(request):
    template = "home.html"
    return render(request, template)


def fantom_options(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FantomForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            args = [
                form.cleaned_data.get('data_type'),
                form.cleaned_data.get('cell_type'),
                form.cleaned_data.get('algorithm'),
                form.cleaned_data.get('k'),
                form.cleaned_data.get('num_ven')
            ]
            task = fantom_results_task.delay(*args)
            task_id = task.id
            request.session['task_id'] = task_id
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('find_ven_results'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FantomForm()
    template = 'fantom_options.html'
    return render(request, template, {'form': form})


def find_ven_results(request):

    template = 'vencode_results.html'
    context = {
        "check_status": 1,
    }
    return render(request, template, context)


def find_ven_status(request):
    task_id = request.session.get('task_id')
    celery_task_results = app.AsyncResult(task_id)
    status = celery_task_results.status
    json_data = {'status': status}
    return JsonResponse(json_data)


def get_vencodes(request):
    task_id = request.session.get('task_id')
    task_results = app.AsyncResult(id=task_id)
    results_tuple = task_results.get()
    task_results.forget()
    template = "vencode.html"
    return render(request, template, {"vencode_html": results_tuple[0]})


def get_e_values(request):
    task_id = request.session.get('task_id')
    task_results = app.AsyncResult(id=task_id)
    results_tuple = task_results.get()
    task_results.forget()
    template = "e_values.html"
    return render(request, template, {"e_values": results_tuple[1]})


def upload_file_ven(request):
    def handle_uploaded_file(f):
        _file_name = '_temp_uploaded.txt'
        with open(_file_name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return _file_name

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = handle_uploaded_file(request.FILES['file'])
            args = [
                form.cleaned_data.get('cell_type'),
                form.cleaned_data.get('algorithm'),
                form.cleaned_data.get('k'),
                form.cleaned_data.get('num_ven')
            ]
            task = uploaded_results_task.delay(file_name, *args)
            task_id = task.id
            request.session['task_id'] = task_id
            return HttpResponseRedirect(reverse('find_ven_results'))
    else:
        form = UploadFileForm()
    template = 'upload_ven_options.html'
    return render(request, template, {'form': form})


def promoter_data_all(request):
    qs = Promoters154CellsBinarized.pdobjects.all()
    df = qs.to_dataframe()
    df = df.iloc[:5]
    template = 'pd_dataframe.html'
    html_table = prepare_df(df)
    return render(request, template, {'html_table': html_table})


def test_celery(request):
    res = debug_task.delay()
    print(res.get())
    return HttpResponse("Hi there fella!")
