from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostArchivedListView,
    PostDraftListView
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),

    path("archived/", PostArchivedListView.as_view(), name="post_archived"),

    path("draft/", PostDraftListView.as_view(), name="post_draft"),

    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),

    path("new/", PostCreateView.as_view(), name="post_new"),

    path("edit/<int:pk>/", PostUpdateView.as_view(), name="post_edit"),

    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
]