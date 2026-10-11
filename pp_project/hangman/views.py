from django.shortcuts import render
from .models import HangmanWord
import random


# Create your views here.

def index(request):
    # Pick up difficulty from URL or fall back to session or default to 'medium'
    difficulty = request.GET.get('difficulty') or request.session.get('difficulty', 'medium')
    
    # Only reset the queue if difficulty changed or queue is empty
    prev_difficulty = request.session.get('difficulty')
    difficulty_changed = prev_difficulty != difficulty
    request.session['difficulty'] = difficulty

    remaining = request.session.get('remaining', [])
    
    # If empty list or user changed difficulty selection, create list
    if not remaining or difficulty_changed:
        unique_list = list(
            HangmanWord.objects.filter(difficulty=difficulty)
                               .values_list('id', flat=True)
        )
        random.shuffle(unique_list)
        remaining = unique_list

    # Pop the next word off the queue
    word_id = remaining.pop()
    request.session['remaining'] = remaining
    request.session.modified = True

    entry = HangmanWord.objects.get(id=word_id)

    context = {
        'word': entry.word,
        'hint': entry.hint,
        'difficulty': difficulty,
    }
    return render(request, 'hangman/index.html', context)