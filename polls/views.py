from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ipware import get_client_ip
from .models import Poll
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
import hashlib

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

class UserPollListView(ListView):
    model = Poll
    template_name = 'poll/poll_list.html'
    context_object0_name = 'polls'
    paginate_by = 2

    def get_queryset(self):
        return Poll.objects.filter(author = self.request.user).order_by('time_posted')