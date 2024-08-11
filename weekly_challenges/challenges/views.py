from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

weekly_challenges = {
    "monday" : "Eat no meat for the entire week!",
    "tuesday" : "Walk for at least 20 minutes every day!",
    "wednesday" : "Learn Django for at least 20 minutes every day!",
    "thursday" : "Eat no meat for the entire week!",
    "friday" : "Walk for at least 20 minutes every day!",
    "saturday" : "Learn Django for at least 20 minutes every day!",
    "sunday" : "Eat no meat for the entire week!"
}

# Create your views here.

def index(request):
    weeks = list(weekly_challenges.keys())

    return render(request, "challenges/index.html", {
        "weeks": weeks
    })

# def weekly_challenge_by_number(request, week):
#     weeks = list(weekly_challenges.keys())

#     if week > len(weeks):
#         return HttpResponseNotFound("Invalid week")

#     redirect_week = weeks[week - 1]
#     redirect_path = reverse("week-challenge", args=[redirect_week]) # /challenge/january
#     return HttpResponseRedirect(redirect_path)


def weekly_challenge(request, week):
    try:
        challenge_text = weekly_challenges[week]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "week_name": week
        })
    except:
        raise Http404()













# def weekly_challenges(request, week):
#     challenge_taxt = None
#     if week == "Monday":
#         challenge_taxt = "Eat on meat for the entire week!"
#     elif week == "Tuesday":
#         challenge_taxt = "Walk for at least 20 minuts day!"
#     elif  week == "Wednesday":
#         challenge_taxt = "Լearn Django for at last 6 hours every day!"
#     elif week == "Thursday":
#         challenge_taxt == "Eat on meat for the entire week!"
#     elif week == "Friday":
#         challenge_taxt = "Walk for at least 20 minuts day!"  
#     elif  week == "Saturday":
#         challenge_taxt = "Լearn Django for at last 6 hours every day!"
#     else:
#         return HttpResponseNotFound("This week is not supporrted!")
#     return HttpResponse(challenge_taxt)

