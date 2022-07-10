from platform import release
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the 
import uuid
# Create your models here.

class movies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    movie_name = models.CharField(max_length=40, help_text='Enter Movie')
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    Actorname=models.CharField(max_length=25,help_text='Enter Actors name')
    release_date=models.DateField(null=True, blank=True)

    

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.movie_name