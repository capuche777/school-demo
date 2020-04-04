from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Assignment
from .forms import AssignmentForm
from .mixins import AddStudentsMixin


@method_decorator(login_required, name='dispatch')
class AssignmentListView(ListView):
    model = Assignment
    template_name = "assignments/assignments_list.html"
    context_object_name = 'assignments'


@method_decorator(login_required, name='dispatch')
class AssignmentCreate(AddStudentsMixin, CreateView):
    form_class = AssignmentForm
    success_url = reverse_lazy('assignments:list')
    template_name = 'assignments/assignments_form.html'


@method_decorator(login_required, name='dispatch')
class AssignmentUpdate(AddStudentsMixin, UpdateView):
    model = Assignment
    form_class = AssignmentForm
    success_url = reverse_lazy('assignments:list')
    template_name = 'assignments/assignments_form.html'


@method_decorator(login_required, name='dispatch')
class AssignmentDelete(DeleteView):
    model = Assignment
    success_url = reverse_lazy('assignments:list')
    template_name = 'core/delete.html'

