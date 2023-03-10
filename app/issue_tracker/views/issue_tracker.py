from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import TemplateView, ListView, UpdateView, DetailView, DeleteView
from issue_tracker.models import Issue, Status, Type, Project

from issue_tracker.forms import IssueForm

from issue_tracker.forms import SearchForm


class IssueTrackerView(ListView):
    template_name = 'issue_tracker_list_page.html'
    model = Issue
    context_object_name = 'issues'
    ordering = ('created_at')
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        self.project_pk = kwargs['project_pk']
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().filter(project=self.project_pk)
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        context['project'] = Project.objects.get(id=self.project_pk)
        if self.search_value:
            context['query']: urlencode({'search': self.search_value})
        if len(context.get('issues')) == 0:
            context['404_error'] = True
        return context


class IssueDetailView(DetailView):
    template_name = 'issue_detail_page.html'
    model = Issue


class IssueUpdateView(UpdateView):
    template_name = 'issue_update_page.html'
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueAddView(TemplateView):
    template_name = 'issue_create_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.get(id=kwargs['project_pk'])
        context['form'] = IssueForm()
        return context

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)
        if form.is_valid():
            form.project = kwargs['project_pk']
            issue = form.save()
            return redirect('project_detail', project_pk=kwargs['project_pk'])
        return render(request, 'issue_create_page.html', context={'form': form})


class IssueDeleteView(DeleteView):
    template_name = 'issue_delete_page.html'
    model = Issue
    success_url = reverse_lazy('issues_list')
