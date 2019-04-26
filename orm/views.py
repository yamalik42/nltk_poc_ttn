from django.shortcuts import render
from .models import ProjectDetail


# Create your views here.
def save_new_project(request):
    if request.method == 'POST':
        import pdb;pdb.set_trace()


def get_similar_projects(**kwargs):
    projects = ProjectDetail.objects.filter(**kwargs)
    import pdb;pdb.set_trace()