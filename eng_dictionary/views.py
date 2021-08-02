from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.


def home(request):
    return render(request, 'home.html')


def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    definition = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)
    context = {
        'search': search,
        'definition': definition,
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    return render(request, 'word.html', context)
