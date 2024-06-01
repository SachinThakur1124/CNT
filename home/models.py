from django.db import models

# Create your models here.
class Courses(models.Model):
    CourseName = models.CharField(max_length=90)
    CourseDesc = models.TextField()
    CourseImg = models.ImageField(upload_to='gallery')
    CourePng = models.ImageField(upload_to='gallery/png')
    CoursePrice = models.IntegerField()
 