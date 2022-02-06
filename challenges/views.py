import imp
from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
monthly_challenges = {
    "january":"Eat no meat for the entire month!",
    "february":"Walk for at least 20 minutes every day!",
    "march":"Learn Django for al least 20 minutes every day!",
    "april":"Eat no meat for the entire month!",
    "may":"Walk for at least 20 minutes every day!",
    "june":"Learn Django for al least 20 minutes every day!",
    "july":"Eat no meat for the entire month!",
    "august":"Walk for at least 20 minutes every day!",
    "september":"Learn Django for al least 20 minutes every day!",
    "october":"Eat no meat for the entire month!",
    "november":"Walk for at least 20 minutes every day!",
    "december":None,
}
def index(request):    
    months= list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path =reverse('month-challenge',args = [month])
    #     available_months+=f"<li><a href={month_path}>{capitalized_month}</a></li> "
    # available_months+="/ul"
    # return HttpResponse(available_months)
    return render(request,"challenges/index.html",{
        "months":months
    })
def monthly_challenge_by_number(request,month,):
    months = list(monthly_challenges.keys())
    if(month<1 or month>len(months)):
        return HttpResponseNotFound("This month is not supported!")

    rediretc_month = months[month-1]
    rediretc_path = reverse('month-challenge',args = [rediretc_month])
    return HttpResponseRedirect(rediretc_path)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,'challenges/challenge.html',{
            "month":month,
            "challengeText":challenge_text
        })
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
    except:
       response_data =  render_to_string("404.html")
       #       HttpResponseRedirect(reverse('index'))
       return HttpResponseNotFound(response_data)
      #raise Http404()
  
