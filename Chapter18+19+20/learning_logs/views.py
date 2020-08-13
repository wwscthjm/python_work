from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics_p."""
    topics_p = Topic.objects.order_by('date_added')
    context = {'topics': topics_p}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic_p, and all its entries."""
    topic_p = Topic.objects.get(id=topic_id)
    entries = topic_p.entry_set.order_by('-date_added')
    context = {'topic': topic_p, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


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


def new_entry(request, topic_id):
    """Add a new entry at a specific topic."""
    topic_p = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry_p = form.save(commit=False)
            new_entry_p.topic = topic_p
            new_entry_p.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic_p, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic_p = entry.topic

    if request.method != 'POST':
        # Request at the first time, fill the form with existing entries.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_p.id]))

    context = {'entry': entry, 'topic': topic_p, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
