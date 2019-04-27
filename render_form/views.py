from django.views.generic import TemplateView
from .forms import ProjectDetailForm


# Create your views here.
class RenderFormView(TemplateView):
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_issue_form'] = ProjectDetailForm()

        matches = self.request.session.get('matches', False)
        if matches:
            context['matches'] = matches
            form = self.request.session.get('form_persistent_data')
            context['project_issue_form'] = ProjectDetailForm(initial=form)
            del self.request.session['matches']
        elif self.request.session.get('success', False):
            context['success'] = True

        return context