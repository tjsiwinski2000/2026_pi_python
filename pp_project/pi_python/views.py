from django.shortcuts import render, redirect
from .get_weather_now import get_weather
from .models import Topic
from .forms import TopicForm

def index(request):
    weather = get_weather('F')
    context = {'weather_report' : weather,'unit' : 'F'}
    return render(request, 'pi_python/index.html', context)

def temp(request):
    weather = get_weather('F')
    context = {'weather_report' : weather,'unit' : 'F'}
    return render(request, 'pi_python/index.html', context)

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'pi_python/topics.html', context)

def topic(request, topic_id):
    """ Show a single topic and all it's entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' :entries}
    return render(request, 'pi_python/topic.html', context)

def new_topic(request):
    """ Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data = request.POST)
        if form.is_valid():
            form.save() # saves to dB
            return redirect('pi_python:topics')
    
    # Display a blank or invalid form.
    context = {'form' : form}
    return render(request, 'pi_python/new_topic.html', context)    
    