from django.shortcuts import render
from pytube import YouTube

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request,"index.html")

def download(request):
	val1= request.GET['videourl']
	yt = YouTube(val1)
	stream = yt.streams.first()
	x=stream.download('/Downloads')
	if(x):
		print("hrllhfu")
		return render(request,"download1.htmls")


	

