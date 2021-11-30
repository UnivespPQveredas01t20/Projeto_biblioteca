from django.views.generic import TemplateView


# biblioteca padrão
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "home/index.html"

class ModelFullView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "home/model_full.html"

class ModelCleanView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "home/model_clean.html"



