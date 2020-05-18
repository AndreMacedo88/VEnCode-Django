from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import ast
from .models import Promoters154CellsBinarized


# Create your views here.
def home(request):
    return render(request, "home.html",
                  {'date': datetime.now().year})


def index(request):
    return HttpResponse("Under construction!")


def promoter_data_all(request):
    qs = Promoters154CellsBinarized.pdobjects.all()
    df = qs.to_dataframe()
    df = df.iloc[:5]
    template = 'pd_dataframe.html'
    html_table = df.to_html(index=False)
    html_table = "\n".join(html_table.split('\n')[1:-1])
    return render(request, template, {'html_table': html_table})


def get_vencodes(request):
    qs = Promoters154CellsBinarized.pdobjects.all()
    df = qs.to_dataframe(index='index')
