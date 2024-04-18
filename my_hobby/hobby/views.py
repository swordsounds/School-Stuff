from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hobby_info_view(request):
    title = '<h1>I LOVE JENNA ORTEGA</h1>'
    img = '<img src="https://www.onthisday.com/images/people/jenna-ortega.jpg?w=720" width=250 height=800>'
    gif = '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/CG_Heart.gif/640px-CG_Heart.gif">'
    para = """<p>Please give me more Wednesday adams episodes, I love Jenna Ortega!
           I love binge watching shows made by Jenna Ortega! Please please please 
           please please give me what I want! I also love her role in the scream movies, 
           I admire her so so so much <3 <3 <3 <3 <3 <3</p>"""
    para2 = '<p>SHE IS MY SUNSHINE, MY ONLY SUNSHINE, SHE MAKES ME HAPPY WHEN SKIES ARE GREY!!!</p>'
    return HttpResponse(f"{title}{para}{img}{gif}{para2}")
def hobby_image_view(request):
    return HttpResponse('<img src="https://i.guim.co.uk/img/media/4df0f504cefb4a5a19966d7dd0f8787b45c6d4ff/259_0_3000_1800/master/3000.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=39bc597b181b507e50198d6f4984274d" width=500 height=200>')