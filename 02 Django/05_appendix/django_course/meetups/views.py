# V1
# from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.


# def index(request):
#     # print(request) #* <WSGIRequest: GET '/meetups/'>
#     # return HttpResponse("Hello World!")
#     return render(request, "meetups/index.html")


# def index(request):
#     meetups = [
#         {"title": "A First Meetup", "location": "New York", "slug": "a-first-meetup"},
#         {"title": "A Second Meetup", "location": "Paris", "slug": "a-second-meeetup"},
#     ]
#     return render(
#         request, "meetups/index.html", {"show_meetups": True, "meetups": meetups}
#     )


# def meetup_details(request, meetup_slug):
#     print(meetup_slug)
#     selected_meetup = {
#         "title": "A First Meetup",
#         "description": "This is the first meetup!",
#     }
#     return render(
#         request,
#         "meetups/meetup-details.html",
#         {
#             "meetup_title": selected_meetup["title"],
#             "meetup_description": selected_meetup["description"],
#         },
#     )

# * V2
from django.shortcuts import render
from .models import Meetup


# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, "meetups/index.html", {"meetups": meetups})


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(
            request,
            "meetups/meetup-details.html",
            {
                "meetup_found": True,
                "meetup_title": selected_meetup.title,
                "meetup_description": selected_meetup.description,
            },
        )
    except Exception as exc:
        return render(request, "meetups/meetup-details.html", {"meetup_found": False})
