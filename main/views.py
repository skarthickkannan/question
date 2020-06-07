from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Answer
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse
from .forms import AnswerForm, CommentForm, UserForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from hitcount.views import HitCountDetailView

def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'home.html', context)

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'
    paginate_by = 10

def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Answer.objects.filter(
            Q(post__question__icontains=srch)|
            Q(answer__icontains=srch)
        )
            if match:
                return render(request, 'search.html', {'sr': match})
            else:
                messages.error(request, 'No search found')

        else:
            return HttpResponseRedirect('/search/')
    context = {'answers': Answer.objects.all()}
    return render(request, 'search.html', context)

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form':form})


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_answer', args=[str(pk)]))


class PostCreateView(CreateView):
    model = Post
    fields = ['question']


def AnswerCreateView(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            new_comment = answer_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('post_answer', args=[str(id)]))
            
    else:
        answer_form = AnswerForm()

    return render(request, 'answer.html', {'post': post,
                                           'answer_form': answer_form})

@login_required
def CommentCreateView(request, id):
    answer = get_object_or_404(Answer, id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.answer = answer
            new_comment.save()
            return HttpResponseRedirect(reverse('post_answer_comment', args=[str(id)]))
            
    else:
        comment_form = CommentForm()

    return render(request, 'comment.html', {'answer': answer,
                                           'comment_form': comment_form})

class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context
    