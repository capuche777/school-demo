from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Teacher
from .forms import TeacherForm


@method_decorator(login_required, name='dispatch')
class TeacherListView(ListView):
    model = Teacher
    template_name = "students/teacher_list.html"
    context_object_name = 'teachers'

    """ Enable to add extra content to context """
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = "Teachers"
    #     return context


@method_decorator(login_required, name='dispatch')
class TeacherCreate(CreateView):
    form_class = TeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/teachers_form.html'

    def get_success_url(self):
        return  reverse_lazy('teachers:list') + '?ok'


@method_decorator(login_required, name='dispatch')
class TeacherUpdate(UpdateView):
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/teachers_form.html'

    def get_success_url(self):
        return  reverse_lazy('teachers:list') + '?ok'


@method_decorator(login_required, name='dispatch')
class TeachertDelete(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'core/delete.html'
