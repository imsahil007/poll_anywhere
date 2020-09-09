from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from ipware import get_client_ip
from .models import Poll, Choice
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PollCreateForm, ChoiceCreateForm
from django.contrib.auth import login, logout



import uuid

public_user = User.objects.filter(username='public').first()

    
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


class UserPollListView(LoginRequiredMixin,ListView):
    model = Poll
    template_name = 'poll/poll_list.html'
    context_object_name = 'polls'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Poll.objects.filter(author = user).order_by('time_posted')

class PollUpdateView(UpdateView):
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
    success_message = "Poll has been deleted successfully"
    success_url='/'
    template_name = 'polls/poll_delete.html'

    def test_func(self):
        poll = self.get_object()
        if self.request.user == poll.author:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message )
        return super(PollDeleteView, self).delete(request, *args, **kwargs)

def add_poll(request):
    if request.user.is_anonymous:
        current_user = public_user
    else:
        current_user = request.user
    if request.method == 'POST':
        p_form = PollCreateForm(request.POST,request.FILES, instance=Poll())
        n_Choice = int(request.POST['counter'])
        c_form = [ChoiceCreateForm(request.POST,request.FILES, prefix = str(x), instance=Choice()) for x in range(0,n_Choice)]
        if p_form.is_valid() and all([cf.is_valid() for cf in c_form]):
            
            new_poll = p_form.save(commit=False)
            new_poll.author = current_user
            poll_link = uuid.uuid1().hex[0:9]
            new_poll.link = poll_link
            new_poll.save()
            for cf in c_form:
                new_choice = cf.save(commit=False)
                new_choice.poll = new_poll
                new_choice.save()
            messages.success(request, f'You have successfuly created a poll')
            return redirect('poll-detail', link = poll_link)
            #change this
    else:
        p_form = PollCreateForm(instance=Poll())
        c_form = [ChoiceCreateForm( prefix = str(x), instance=Choice()) for x in range(0,2)]
        ''' We need atleast 2 Choice for a poll '''
    context = {
        'p_form':p_form,
        'c_form':c_form
    }
    return render(request, 'polls/new_poll.html',context)

def poll_detail(request, link='new'):
    is_fake = False
    if request.user.is_anonymous:
        create_fake_user(request)
        is_fake = True


    if request.method == 'POST' and request.user not in Poll.objects.get(link=link).voters.all():
        option = Poll.objects.get(link=link).choice_set.get(id=int(request.POST["choice"]))
        option.choice_count= option.choice_count + 1
        Poll.objects.get(link=link).voters.add(request.user)
        option.save()
        if is_fake:
            logout(request, request.user)
        return redirect('poll-result', link)
    else:
        if request.user in Poll.objects.get(link=link).voters.all():
            messages.warning(request, 'You have already voted')
            if is_fake:
                logout(request, request.user)
            return redirect('poll-result', link)
        context={
            "poll": Poll.objects.get(link=link),
            "choices": Poll.objects.get(link=link).choice_set.all()
        }
        if is_fake:
                logout(request, request.user)
        return render(request, 'polls/poll_detail.html',context)

def result(request, link='new'):
    if link =='poll/result':
        return redirect('poll-create')
    labels = []
    data = []
    queryset = Poll.objects.get(link= link).choice_set.order_by('-choice_count')
    for choice in queryset:
        labels.append(choice.choice_text)
        data.append(choice.choice_count)
    context = {
        'poll':Poll.objects.get(link= link),
        'labels': labels,
        'data': data,
    }
    return  render(request, 'polls/poll_result.html',context)

        
def create_fake_user(request):
    request.session.save()
    username = str(request.session.session_key) + '@anonyvoter'
    try:
        user = User.objects.create_user(username)
    except:
        user = User.objects.get(username=username)
    login(request, user)