from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post, Status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


class PostListView(ListView):
    template_name = "posts/list.html"
    # model = Post

    published_status = Status.objects.get(name="published")

    # queryset attribute allow us to select data from the db using the model class
    # and also allow us to customize the data (filters)
    queryset = Post.objects.filter(status=published_status).order_by("-created_on")

    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_status"] = "All"
        return context


class PostArchivedListView(ListView):
    template_name = "posts/list.html"

    archived_status = Status.objects.get(name="archived")

    queryset = Post.objects.filter(status=archived_status)

    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_status"] = "Archived"
        return context


class PostDraftListView(ListView):
    template_name = "posts/list.html"

    context_object_name = "posts"

    def get_queryset(self):
        draft_status = Status.objects.get(name="draft")
        return Post.objects.filter(status=draft_status)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_status"] = "Drafts"
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post

    # success_url attribute allow us to redirect the user if the request was successful
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False