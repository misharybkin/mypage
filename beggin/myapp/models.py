from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255)
    text = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='myapp/static/uploaded')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(null=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')

class Stewardesses(models.Model):
    nr_ewidencyjny = models.TextField(primary_key=True)
    imie = models.TextField(max_length=255)
    nazwisko = models.TextField(max_length=255)
    crewlink_id = models.TextField(max_length=255)
    crewlink_password = models.TextField(max_length=255)
    LOT_password = models.TextField(max_length=255)

    def __str__(self):
        return self.nr_ewidencyjny

class Artykuly(models.Model):
    artykul_id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255)
    text = models.TextField(max_length=5000)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(null=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artykuly')


class Guidy(models.Model):
    guide_id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255)
    link = models.TextField(max_length=1000)



