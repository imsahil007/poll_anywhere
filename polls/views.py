from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from ipware import get_client_ip
from .models import Poll, PollChoices
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import hashlib
public_user = User.objects.filter(username='public')
def create_hash(title):
    hash = hashlib.sha1(title.encode("UTF-8")).hexdigest()
    return str(hash[:10])
    
def get_ip_address(request):
    # return HttpResponse("<h1>THIs is it</h1>")
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    ip, is_routable = get_client_ip(request)
    return ip
# Create your views here.
def home(request):

    return render(request,'polls/home.html')

class PollDetailView(DetailView):
    model = Poll
    # def get_context_data(self,**args, **kwargs):
    #     return True

class UserPollListView(LoginRequiredMixin,ListView):
    model = Poll
    template_name = 'poll/poll_list.html'
    context_object_name = 'polls'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Poll.objects.filter(author = user).order_by('time_posted')

class PollUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Poll
    fields = ['title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        poll = self.get_object()
        if self.request.user == poll.author:
            return True
        return False

class PollCreateView( CreateView):
    model = Poll
    fields = ['title', 'question', 'question_image']

    def form_valid(self, form):
        if self.request.user:
            form.instance.author = self.request.user
        else:
            form.instance.author = public_user
        return super().form_valid(form)
        
class PollDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Poll
    success_url='/'

    def test_func(self):
        poll = self.get_object()
        if self.request.user == poll.author:
            return True
        return False