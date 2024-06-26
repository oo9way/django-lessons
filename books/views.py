from django.shortcuts import render
from django.http import HttpResponse


kitoblar = {
        "1": "Harry Potter",
        "2": "Sariq devni minib",
        "3": "Kichkina shahzoda",
        "4": "Savdogarlar ustozi",
        "5": "Atom odatlar",
        "6": "Deep work"
}

def books(request):
    return render(request, "book.html")


def book_details(request):
    return render(request, "index.html")