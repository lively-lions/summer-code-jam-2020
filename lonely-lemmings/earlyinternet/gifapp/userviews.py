import logging

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    FormView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Project
from .forms import UserRegisterForm, ProjectForm

logger = logging.getLogger(__name__)


def home(request: HttpRequest) -> HttpResponse:
    """
    Handles feed home GET request
    :param request:
    :return: Feed home with context
    """
    context = {
        "feed": Project.objects.all()
    }
    return render(request, 'home.html', context)


def about(request: HttpRequest) -> HttpResponse:
    """
    Handles feed home GET request
    :param request:
    :return: Feed home with context
    """
    return render(request, 'about.html')


def register(request: HttpRequest) -> HttpResponse:
    """
    Handles register endpoint POST request
    :param request: HttpRequest object containing form data for registering a new user
    :return: redirect if successful account formation, else the same RegisterForm
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'profile.html')


class ProjectCreateView(LoginRequiredMixin, FormView):
    template_name = "project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy("project-detail")

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


def create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data["project_name"]
            Project.objects.create(name=project_name, user_id=request.user)
            return HttpResponseRedirect(f"/project/{project_name}")
        else:
            return HttpResponseRedirect("/")

    else:
        return HttpResponseRedirect("/")


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'


# class ProjectCreateView(LoginRequiredMixin, FormView):
#     template_name = "project_form.html"
#     form_class = ProjectForm
#     success_url = reverse_lazy("project-detail")
#
#     def form_valid(self, form):
#         form.instance.user_id = self.request.user
#         return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = Project
    fields = ['name', 'upload_version', 'is_gif']


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'upload_version', 'is_gif']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.user_id


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.user_id
