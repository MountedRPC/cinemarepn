from django.db import models
from django.contrib.auth.models import User
from home.models import *
from django.db.models import DateTimeField


# Create your models here.

class Sales(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sessions_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    dataSales = DateTimeField(blank=True)
    countTicket = models.IntegerField()
    price_session = models.IntegerField()
