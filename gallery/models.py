from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save()
    

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
