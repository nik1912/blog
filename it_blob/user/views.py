from django.shortcuts import render
from user.forms import UserSignIn






def signin(request):
    print(request.POST)
    context = {
        "singin_form": UserSignIn()
    }
    return render(request, "sign_in.html", context)

