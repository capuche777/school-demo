from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import StudentForm


@method_decorator(login_required, name='dispatch')
class StudentListView(ListView):
    model = Student
    template_name = "students/students_list.html"
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Students"
        return context


@method_decorator(login_required, name='dispatch')
class StudentCreate(CreateView):
    form_class = StudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/students_form.html'

    def get_success_url(self):
        return  reverse_lazy('students:list') + '?ok'


@method_decorator(login_required, name='dispatch')
class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/students_form.html'

    def get_success_url(self):
        return  reverse_lazy('students:list') + '?ok'


@method_decorator(login_required, name='dispatch')
class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'core/delete.html'
