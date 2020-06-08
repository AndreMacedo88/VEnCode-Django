from django import forms
from .models import Promoters154CellsBinarized

DATA_CHOICES = [("promoters", "Promoters"), ("enhancers", "Enhancers")]
REG_EL_CHOICES = [field.get_attname_column() for field in Promoters154CellsBinarized._meta.fields[1:]]
ALGORITHM_CHOICES = [("heuristic", "Heuristic Method"), ("sampling", "Sampling Method")]
k_CHOICES = [tuple([x, x]) for x in range(1, 16)]


class FantomForm(forms.Form):
    data_type = forms.CharField(label='Type of regulatory elements to use',
                                widget=forms.Select(choices=DATA_CHOICES))
    cell_type = forms.CharField(label='Target cell type',
                                widget=forms.Select(choices=REG_EL_CHOICES))
    algorithm = forms.CharField(label='Algorithm',
                                widget=forms.Select(choices=ALGORITHM_CHOICES))
    k = forms.IntegerField(label="Number of regulatory elements to use in a VEnCode",
                           widget=forms.Select(choices=k_CHOICES), initial=4)
    num_ven = forms.IntegerField(initial=2)


class UploadFileForm(forms.Form):
    file = forms.FileField()
    cell_type = forms.CharField(label='Target cell type',
                                help_text="Please write the exact cell type name")
    algorithm = forms.CharField(label='Algorithm',
                                widget=forms.Select(choices=ALGORITHM_CHOICES))
    k = forms.IntegerField(label="Number of regulatory elements to use in a VEnCode",
                           widget=forms.Select(choices=k_CHOICES), initial=4)
    num_ven = forms.IntegerField(initial=2)
