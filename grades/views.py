from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from teachers.models import Teacher
from .models import Grade
from .forms import GradeForm
from .mixins import AddTeachersMixin

@method_decorator(login_required, name='dispatch')
class GradeListView(ListView):
    """ Get list of grades """
    model = Grade
    template_name = "grades/grades_list.html"
    context_object_name = 'grades'


@method_decorator(login_required, name='dispatch')
class GradeCreate(AddTeachersMixin, CreateView):
    form_class = GradeForm
    success_url = reverse_lazy('grades:list')
    template_name = 'grades/grades_form.html'


@method_decorator(login_required, name='dispatch')
class GradeUpdate(AddTeachersMixin, UpdateView):
    model = Grade
    form_class = GradeForm
    success_url = reverse_lazy('grades:list')
    template_name = 'grades/grades_form.html'


@method_decorator(login_required, name='dispatch')
class GradeDelete(DeleteView):
    model = Grade
    success_url = reverse_lazy('grades:list')
    template_name = 'core/delete.html'
