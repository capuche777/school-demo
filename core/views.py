from django.views.generic import RedirectView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class Index(RedirectView):
    template_name = "core/index.html"
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        url = self.get_redirect_url(*args, **kwargs)
        
        if request.user.is_authenticated:
            url = reverse_lazy('students:list')
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect(url)
