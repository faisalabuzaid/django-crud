from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["name", "purchaser", "description"]


class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["name", "description"]


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")
