from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# from django.http import HttpResponse

# Create your views here.

# dummy data
# posts=[
#     {
#         'author':'abcd',
#         'title':'Blog Post 1',
#         'content':' First post',
#         'date_posted':'12-02-2020'
#     },
#     {
#         'author':'abd',
#         'title':'Blog Post 2',
#         'content':' second post',
#         'date_posted':'12-02-2020'
#     }
# ]
@login_required
def home(request):
    context={
        'posts':Post.objects.all() #this done in shell 
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by= 5
    
class UserPostListView(ListView):
    model=Post
    template_name='blog/user_post.html'
    context_object_name='posts'
    
    paginate_by= 5
    
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    

class DetailListView(DetailView):
    model=Post
    # template_name='blog/post_detail.html'

class CreateListView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class UpdateListView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self) :
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class DeleteListView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self) :
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
    



def about(request):
    return render(request,'blog/about.html',{'title':'about page'})