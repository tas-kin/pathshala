from django.db import models
from django.contrib.auth.models import User

#Post-----------------
class Post(models.Model):
  title=models.CharField(max_length=120)
  slug=models.SlugField()
  body=models.TextField()
  date=models.DateTimeField(auto_now_add=True)
  author=models.ForeignKey(User,default=None)

  def __str__(self):
    return self.title

  def snippet(self):
    return self.body[0:100]


#course---------------------

class Course(models.Model):
  course_name=models.CharField(max_length=50)
  syllabus=models.TextField()
  pass_key=models.CharField(max_length=10)
  date=models.DateTimeField(auto_now_add=True)
  creator=models.ForeignKey(User,default=None)


  def __str__(self):
    return self.course_name



