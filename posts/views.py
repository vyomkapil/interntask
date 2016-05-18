from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView
from .forms import RegistrationForm
from .models import Post, Comment
from django.utils import timezone

def index(request):
    latest_post_list = Post.objects.order_by('-post_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'posts/index.html', context)

@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})

@login_required
def post(request):
    p = Post(post_text=request.POST['txtArea'], post_date=timezone.now(), user=request.user)
    p.save()
    return HttpResponseRedirect(reverse('posts:index'))

@login_required
def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    c = Comment(comment_text=request.POST['txtArea'], comment_date=timezone.now(), user=request.user, post=post)
    c.save()
    return HttpResponseRedirect(reverse('posts:detail',args=(post.id,)))

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('posts:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details:{0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'posts/login.html')


class RegistrationView(FormView):
    template_name = 'posts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('posts:index')
    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('posts:index'))

