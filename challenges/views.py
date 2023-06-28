from django.shortcuts import render
from django.http import (
    HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
)
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}


def index(request) -> HttpResponse:
    """A view that returns a list of all challenges"""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        'months': months
    })


def monthly_challenges_by_number(request, month: int) -> HttpResponse:
    """
    A view that takes in a number and returns the challenge of that month
    """
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound(f"<h1>This month is not supported!</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month: str) -> HttpResponse:
    """
    A view that takes in a month and returns the challenge of that month
    """
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })

    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    # except Exception as e:
    #     raise Http404()
