from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=20)
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add = True)
    starting_date = models.DateField()
    
    def __str__(self):
        return self.title
