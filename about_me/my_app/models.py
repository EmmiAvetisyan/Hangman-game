from django.db import models

class Contactmessage(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    message = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.name
    
class ProjectLinks(models.Model):
    link = models.URLField(max_length=200)
    project_name = models.CharField(max_length=100)

    def __str__(self):
        # Ensure this method returns a string
        return f"{self.project_name}: {self.link}"
