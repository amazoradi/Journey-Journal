from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# class Customer(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.DO_NOTHING,
#         primary_key=True,
#     )
#     address = models.CharField(max_length=80)

#     def __str__(self):
#         return self

class Entry(models.Model):
    title = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    content =  models.TextField(blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    image =  models.TextField(blank=True, null=True)
    customer = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f'{self.title}'
    
    

