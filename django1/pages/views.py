from django.shortcuts import render


# Create your views here.
def home(request):
    # books = get books from db
    username = request.GET.get("username", "default user")
    return render(
        request,
        "home.html",
        {
            "username": username,
            "nums": [i for i in range(0, 1000)],
        },
    )


def about(request):
    return render(request, "about.html")
