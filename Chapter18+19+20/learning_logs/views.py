from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from .forms import TopicForm


# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics_p."""
    topics_p = Topic.objects.order_by('date_added')
    context = {'topics_p': topics_p}
    return render(request, 'learning_logs/topics_p.html', context)


def topic(request, topic_id):
    """Show a single topic_p, and all its entries."""
    topic_p = Topic.objects.get(id=topic_id)
    entries = topic_p.entry_set.order_by('-date_added')
    context = {'topic_p': topic_p, 'entries': entries}
    return render(request, 'learning_logs/topic_p.html', context)


def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
