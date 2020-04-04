from django.urls import reverse_lazy

from students.models import Student


class AddStudentsMixin():
    """ Used in create and update views """
    def get_context_data(self, **kwargs):
        """ Return students without an assigned grade """
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.filter(assignment__grade__isnull=True)
        return context
    
    def get_success_url(self):
        """ after save the object it will redirect to assignments list with a confirmation in URL """
        return  reverse_lazy('assignments:list') + '?ok'
