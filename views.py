from django.shortcuts import render

def home(request):
    return render(request,"home.html")

api ="AIzaSyB_OTwxvHudLhNj1FbPNq7UhNg0CUm3pAI"
from google import genai

client = genai.Client(api_key=api)


from . models import *
def startup(request):
    if request.method=="POST":
        nam = request.POST.get('na')
        print(nam)
        #ORM ->object relational maping
        #create
        response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=nam,
)
        print(response.text)
        data = response.text

        Startup.objects.create(u_name=nam)
    return render(request,"startup.html",{"data":data})

