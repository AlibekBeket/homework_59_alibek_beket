from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from issue_tracker.models import Issue, Status, Type

from issue_tracker.forms import IssueForm


class IssueTrackerView(TemplateView):
    template_name = 'issue_tracker_list_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IssueDetailView(TemplateView):
    template_name = 'issue_detail_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context


class IssueUpdateView(TemplateView):
    template_name = 'issue_update_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        context['form'] = IssueForm(instance=context['issue'])
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_detail', pk=issue.pk)
        return render(request, 'issue_update_page.html', context={'form': form, 'issue': issue})


class IssueAddView(TemplateView):
    template_name = 'issue_create_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IssueForm()
        return context

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            return redirect('issue_detail', pk=issue.pk)
        return render(request, 'issue_create_page.html', context={'form': form})


class IssueDeleteView(TemplateView):
    template_name = 'issue_delete_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.delete()
        return redirect('issues_list')
