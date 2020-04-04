from django.urls import reverse_lazy

from teachers.models import Teacher


class AddTeachersMixin():
    """ Used in create and update views """
    def get_context_data(self, **kwargs):
        """ Return the list of teachers without an assigned grade """
        context = super().get_context_data(**kwargs)
        context["teachers"] = Teacher.objects.filter(grade__isnull=True)
        return context

    def get_success_url(self):
        """ after save the object it will redirect to grades list with a confirmation in URL """
        return  reverse_lazy('grades:list') + '?ok'
