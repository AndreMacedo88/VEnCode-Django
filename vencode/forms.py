from django import forms
from .models import Promoters154CellsBinarized, Enhancers154CellsBinarized

promoter_list = [field.get_attname_column() for field in Promoters154CellsBinarized._meta.fields[1:]]
enhancer_list = [field.get_attname_column() for field in Enhancers154CellsBinarized._meta.fields[1:]]


class FantomForm(forms.Form):
    cell_type = forms.CharField(label='Target cell type:',
                                widget=forms.Select(choices=promoter_list))
