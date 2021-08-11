from django.shortcuts import render
from random import randint
from deep_translator import GoogleTranslator

# Create your views here.
quotes = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "The way to get started is to quit talking and begin doing.",
    "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
    "If life were predictable it would cease to be life, and be without flavor.",
    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.Oprah Winfrey",
    "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
    "Life is what happens when you're busy making other plans.",
    "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
    "Don't judge each day by the harvest you reap but by the seeds that you plant.",
]

authors = [
    "Nelson Mandela",
    "Walt Disney",
    "Steve Jobs",
    "Eleanor Roosevelt",
    "Oprah Winfrey",
    "James Cameron",
    "John Lennon",
    "Mother Teresa",
    "Robert Louis Stevenson",
]

##  main page  ##


def mainpage(request):
    return render(request, 'quotePage.html', {'quote': 'Random Quote Generator', 'lang': 'en'})

##  generating random quote  ##


def generateQuote(request):
    randomquote = randint(0, len(quotes)-1)
    quote = quotes[randomquote]
    author = authors[randomquote]
    return render(request, 'quotePage.html', {'quote': quote, 'author': author, 'lang': 'en', 'id': id})


def translate(request, id, lang):
    translated = GoogleTranslator(
        source='auto', target=lang).translate(quotes[id])
    author = authors[id]
    if lang == 'en':
        lang = 'sr'
    else:
        lang = 'en'
    return render(request, 'quotePage.html', {'quote': translated, 'author': author, 'lang': lang, 'id': id})
