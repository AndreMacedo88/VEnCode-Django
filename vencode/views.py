from django.shortcuts import render
from django.http import HttpResponseRedirect

from VEnCode import DataTpm, Vencodes

from .models import Promoters154CellsBinarized
from .utils_views import *
from .forms import FantomForm
from .tasks import sleepy


# Create your views here.
def home(request):
    return render(request, "home.html")


def vencode_fantom_options(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FantomForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            request.session['cell_type'] = request.POST['cell_type']
            # redirect to a new URL:
            return HttpResponseRedirect('results/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FantomForm()
    return render(request, 'fantom_options.html', {'form': form})


def vencode_fantom_results(request):
    cell_type = request.session.get('cell_type')
    template = 'vencode_results.html'
    qs = Promoters154CellsBinarized.pdobjects.all()
    df = qs.to_dataframe(index='index')
    data = DataTpm(df)
    data.load_data()
    data.make_data_celltype_specific(cell_type, replicates=True)
    data.filter_by_target_celltype_activity(threshold=0.9)
    vencodes = Vencodes(data, algorithm="heuristic")
    vencodes.next(2)
    vencode = vencodes.get_vencode_data(method="return")
    ven_html = list()
    for ven in vencode:
        ven.reset_index(level=0, inplace=True)
        ven_html.append(prepare_df(ven))
    vencodes.determine_e_values()
    return render(request, template, {"vencode_html": ven_html, "e_values": vencodes.e_values})


def get_vencodes(request):
    vencodes = request.POST.get('vencodes')
    template = "vencode.html"
    vencode = vencodes.get_vencode_data(method="return")
    ven_html = list()
    for ven in vencode:
        ven.reset_index(level=0, inplace=True)
        ven_html.append(prepare_df(ven))
    return render(request, template, {"vencode_html": ven_html})


def promoter_data_all(request):
    qs = Promoters154CellsBinarized.pdobjects.all()
    df = qs.to_dataframe()
    df = df.iloc[:5]
    template = 'pd_dataframe.html'
    html_table = prepare_df(df)
    return render(request, template, {'html_table': html_table})


from django.http import HttpResponse


def test_celery(request):
    soda = sleepy.delay(20, 3, 8)
    return HttpResponse(f'Donee!')
