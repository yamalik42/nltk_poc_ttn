from django.views.generic import TemplateView
from .forms import ProjectDetailForm


# Create your views here.
class RenderFormView(TemplateView):
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_issue_form'] = ProjectDetailForm()
        return context