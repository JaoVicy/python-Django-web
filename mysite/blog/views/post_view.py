from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post


class PostView(generic.View):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"

def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order.by("-created_on")
    new_comment = None

    if request.method == "POST":
        comments_form = CommentForm(data=request.POST)
        if comments_form.is_valid():
            new_comment = comments_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comments_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comments_form": comments_form,
        },
    )