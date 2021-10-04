from typing import Text
from django.shortcuts import render
from django.http import  Http404 ,HttpResponse , HttpResponseNotFound , HttpResponseRedirect

from django.urls import reverse

from django.template.loader import render_to_string 



# Create your views here.

# def january(request):
#     return HttpResponse("this is january!!")

# def february(request):
#     return HttpResponse("this is february!!")


dict_challenges = {
    "january" : "this is january!!",
    "february": "this is february!!",
    "march" :  "this is march!!",
    "april" : "this is april!!",
    "may":"this is may",
    "june":"this is june",
    "august": None
}

def index(request):
    months =list( dict_challenges.keys())
    return render(request,"challenge/index.html",{
        "months":months
    })

def month_challenge_by_number(request,month):
    months =list( dict_challenges.keys())
    if month > len(months) :
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    forward_month = months[month-1]
    forward_path = reverse("month-challenge",args=[forward_month])
    return HttpResponseRedirect(forward_path)


def month_challenge(request,month):
    try:
        result=dict_challenges[month]
        return render(request,"challenge/temp.html",{
            "text" : result,
            "month_name" : month
        })
        
    except:
        httpData = render_to_string("404.html")
        return HttpResponseNotFound(httpData)

        

    # if month=="january" :
    #     result="this is january!!"
    # elif month=="february":
    #     result="this is february!!"
    # elif month=="march":
    #     result="this is march!!"
    # else:
    #     return HttpResponseNotFound("this is not month")
    