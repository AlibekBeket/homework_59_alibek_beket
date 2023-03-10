from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from issue_tracker.models import Project

from issue_tracker.forms import ProjectForm


class ProjectListView(ListView):
    template_name = 'project_list_page.html'
    model = Project
    context_object_name = 'projects'
    ordering = ('start_date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['projects'] = Project.objects.filter(is_deleted=False)
        return context


class ProjectAddView(CreateView):
    template_name = 'project_create_page.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'project_id': self.object.pk})
