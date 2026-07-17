from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .get_weather_now import get_weather
from .models import Topic,Entry
from .forms import TopicForm, EntryForm
from django.http import Http404

def check_topic_owner(topic_owner, current_user):
    print('in check_topic_owner')
    if topic_owner == current_user:
        return True
    else:
        return False

def index(request):
    weather = get_weather('F')
    context = {'weather_report' : weather,'unit' : 'F'}
    return render(request, 'pi_python/index.html', context)

def temp(request):
    weather = get_weather('F')
    context = {'weather_report' : weather,'unit' : 'F'}
    return render(request, 'pi_python/index.html', context)

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'pi_python/topics.html', context)

@login_required
def topic(request, topic_id):
    """ Show a single topic and all it's entries."""
    topic = Topic.objects.get(id=topic_id)
    if check_topic_owner(topic.owner,request.user) == False:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' :entries}
    return render(request, 'pi_python/topic.html', context)

@login_required
def new_topic(request):
    """ Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data = request.POST)
        if form.is_valid():
            new_topic = form.save(commit = False) # delay
            new_topic.owner = request.user
            new_topic.save()            
            return redirect('pi_python:topics')
    
    # Display a blank or invalid form.
    context = {'form' : form}
    return render(request, 'pi_python/new_topic.html', context)    

@login_required
def new_entry(request, topic_id):
    """ Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST' :
        # No data submitted ; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('pi_python:topic', topic_id = topic_id)
    
    # Display a blank or invalid form
    context = {'topic' : topic, 'form' : form}
    return render(request, 'pi_python/new_entry.html', context)  

@login_required
def edit_entry(request, entry_id):
    """ Edit an existing entry."""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if check_topic_owner(topic.owner,request.user) == False:
        raise Http404
     
    if request.method != 'POST':
        # Initial request; pre-fill form with current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('pi_python:topic', topic_id = topic.id)
            
    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request, 'pi_python/edit_entry.html', context)
 
      