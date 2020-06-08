from __future__ import absolute_import, unicode_literals
from os import remove

from celery import shared_task

from VEnCode import DataTpm, Vencodes

from .models import Promoters154CellsBinarized, Enhancers154CellsBinarized
from .utils_views import *


# Create your tasks here

@shared_task
def fantom_results_task(data_type, cell_type, algorithm, k, num_ven):
    k_int = int(k)
    num_ven_int = int(num_ven)
    if data_type == "promoters":
        qs = Promoters154CellsBinarized.pdobjects.all()
    elif data_type == "enhancers":
        qs = Enhancers154CellsBinarized.pdobjects.all()
    else:
        raise TypeError("Wrong data_type, please check the form data.")
    df = qs.to_dataframe(index='index')
    return prep_and_get_ven(df, cell_type, algorithm, k_int, num_ven_int)


@shared_task
def uploaded_results_task(file_name, cell_type, algorithm, k, num_ven):
    k_int = int(k)
    num_ven_int = int(num_ven)
    result = prep_and_get_ven(file_name, cell_type, algorithm, k_int, num_ven_int)
    remove(file_name)
    return result


def prep_and_get_ven(file_name, cell_type, algorithm, k, num_ven):
    data = DataTpm(file_name)
    data.load_data()
    data.make_data_celltype_specific(cell_type, replicates=True)
    data.filter_by_target_celltype_activity(threshold=0.9)
    vencodes = Vencodes(data, algorithm=algorithm, number_of_re=k)
    vencodes.next(num_ven)
    vencode = vencodes.get_vencode_data(method="return")
    ven_html = list()
    for ven in vencode:
        ven.reset_index(level=0, inplace=True)
        ven_html.append(prepare_df(ven))
    vencodes.determine_e_values()
    result = [ven_html, vencodes.e_values]
    return result

