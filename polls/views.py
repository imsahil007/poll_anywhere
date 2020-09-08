from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from ipware import get_client_ip
from .models import Poll, Choices
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PollCreateForm, ChoiceCreateForm

import hashlib
public_user = User.objects.filter(username='public').first()
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



        
class PollDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Poll
    success_url='/'

    def test_func(self):
        poll = self.get_object()
        if self.request.user == poll.author:
            return True
        return False

def add_poll(request):
    if request.user.is_anonymous:
        current_user = public_user
    else:
        current_user = request.user
    n=3
    if request.method == 'POST':
        p_form = PollCreateForm(request.POST,request.FILES, instance=Poll())
        c_form = [ChoiceCreateForm(request.POST,request.FILES, prefix = str(x), instance=Choices()) for x in range(0,n)]
        if p_form.is_valid() and all([cf.is_valid() for cf in c_form]):
            # print(p_form.cleaned_data)
            # for cf in c_form:
            #     print(cf.cleaned_data)
            new_poll = p_form.save()
            for cf in c_form:
                new_choice = cf.save(commit=False)
                new_choice.poll = new_poll
                new_choice.save()
            messages.success(request, f'You have successfuly created a poll')
            return redirect('home')
            #change this
    else:
        p_form = PollCreateForm(instance=Poll())
        c_form = [ChoiceCreateForm( prefix = str(x), instance=Choices()) for x in range(0,2)]
        ''' We need atleast 2 choices for a poll '''
    context = {
        'p_form':p_form,
        'c_form':c_form
    }
    return render(request, 'polls/new_poll.html',context)

        