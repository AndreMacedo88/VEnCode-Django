from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


# Create your views here.
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
