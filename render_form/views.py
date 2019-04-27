from django.views.generic import TemplateView
from .forms import ProjectDetailForm


# Create your views here.
class RenderFormView(TemplateView):
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['matches'] = self.request.session.pop('matches', False)
        context['no_match'] = self.request.session.pop('no_match', False)

        form = self.request.session.pop('form_persistent_data', {})
        context['project_issue_form'] = ProjectDetailForm(initial=form)
            
        return context