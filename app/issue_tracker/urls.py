from django.urls import path

from issue_tracker.views.issue_tracker import IssueTrackerView, IssueDetailView, IssueUpdateView, IssueAddView, \
    IssueDeleteView

from issue_tracker.views.project import ProjectListView


urlpatterns = [
    path('', IssueTrackerView.as_view()),
    path('issue_tracker/', IssueTrackerView.as_view(), name='issues_list'),
    path('issue_tracker/<int:pk>', IssueDetailView.as_view(), name='issue_detail'),
    path('issue_tracker/<int:pk>/update', IssueUpdateView.as_view(), name='issue_update'),
    path('issue_tracker/add', IssueAddView.as_view(), name='issue_add'),
    path('issue_tracker/<int:pk>/delete', IssueDeleteView.as_view(), name='issue_delete'),
    path('project/', ProjectListView.as_view(), name='projects_list'),
    path('project/<int:project_pk>', IssueTrackerView.as_view(), name='project_detail'),
    path('project/<int:project_pk>/add', IssueAddView.as_view(), name='project_issue_add'),
    path('project/<int:project_pk>/<int:pk>', IssueDetailView.as_view(), name='project_issue_detail'),
    path('project/<int:project_pk>/<int:pk>/delete', IssueDeleteView.as_view(), name='project_issue_delete'),
    path('project/<int:project_pk>/<int:pk>/update', IssueUpdateView.as_view(), name='project_issue_update'),
]
