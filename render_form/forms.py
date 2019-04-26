from django import forms
from orm.models import ProjectDetail


class ProjectDetailForm(forms.ModelForm):
    optional_fields = ('Location two', 'Location three')

    class Meta:
        model = ProjectDetail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for key in self.fields:
            field = self.fields[key]
        
            if field.label not in self.optional_fields:
                field.label += '*'
            else:
                field.required = False

            field.widget.attrs.update({'class': 'form-control'})
        cost = self.fields['project_cost'].label
        self.fields['project_cost'].label = f'(crores) {cost}'
