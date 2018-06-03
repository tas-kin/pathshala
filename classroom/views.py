from django.shortcuts import render
from .models import Post


def discussion(request):
   posts=Post.objects.all().order_by('date')
   return render(request,"classroom/discussion.html",{'posts':posts})	
