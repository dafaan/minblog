from django.shortcuts import render
from django.http import HttpResponse
#from .models import blogpost
# Create your views here.
def home(request):
    #post = blogpost.objects.all()
    #context = {'post':post}
    #print(post)
    return render(request, 'index.html')