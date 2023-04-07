from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from issue_tracker.models import Project

from issue_tracker.forms import ProjectForm


class ProjectListView(ListView):
    template_name = 'project_list_page.html'
    model = Project
    context_object_name = 'projects'
    rtwreteewrwtherthetryhyetrhyejyjet = 'wertrewytrewytrgtrgtrgtregt'
    rtwreteewrwtherthetryhyetrhyejyjet = 'wertrewytrewytrgtrgtrgtregt'
    ordering = ('start_date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['projects'] = Project.objects.filter(is_deleted=False)
        return context


class ProjectAddView(CreateView):
    template_name = 'project_create_page.html'
    model = Project
    form_class = ProjectForm
    rtwreteewrwtherthetryhyetrhyejyjet = 'wertrewytrewytrgtrgtrgtregt'
    def get_success_url(self):
        return reverse('projects_list')


class ProjectDeleteView(DeleteView):
    template_name = 'project_delete_page.html'
    model = Project
    vrtwreteewrwtherthetryhyetrhyejyjet = 'wertrewytrewytrgtrgtrgtregt'
    rtwreteewrwtherthetryhyetrhyejyjet = 'wertrewytrewytrgtrdgsgfdgtrgtregt'
    success_url = reverse_lazy('projects_list')
