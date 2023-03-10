from django.views.generic import ListView, DetailView

from issue_tracker.models import Project


class ProjectListView(ListView):
    template_name = 'project_list_page.html'
    model = Project
    context_object_name = 'projects'
    ordering = ('start_date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['projects'] = Project.objects.filter(is_deleted=False)
        return context


