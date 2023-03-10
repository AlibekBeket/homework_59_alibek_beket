from django.views.generic import ListView, DetailView

from issue_tracker.models import Project


class ProjectListView(ListView):
    template_name = 'project_list_page.html'
    model = Project
    context_object_name = 'projects'
    ordering = ('start_date')


