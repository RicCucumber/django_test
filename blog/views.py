from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.urls import reverse

from .utils import ObjectDetailMixin, ObjCreateMixin, ObjUpdateMixin
from .models import Post, Tag
from .forms import PostForm, TagForm



def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class PostCreate(ObjCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create.html'

class PostUpdate(ObjUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'


class TagCreate(ObjCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'

class TagUpdate(ObjUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'


class TagDelete(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, template_name='blog/tag_delete_form.html', context={'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect(reverse('tags_list_url'))

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
