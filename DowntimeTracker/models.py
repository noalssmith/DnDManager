from django.db import models
from django.urls import reverse


class Player(models.Model):
    name = models.CharField(max_length=30, help_text='Name of this type of Activity')
    saved_downtime = models.TimeField()

    class Meta: ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Activity(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    title = models.CharField(max_length=30, help_text='Name of this type of Activity')
    #TODO: make time count down
    duration = models.TimeField() #TODO: Figure out params
    time_remaining = models.TimeField() #TODO: Figure out params

    #TODO: Serialize the List of contributers
    contributers = models.ManyToManyField(Player)
    # contributers = models.ForeignKey('Player', on_delete=models.RESTRICT, null=True)

    hidden = models.BooleanField(default=False, help_text="Can all players see this activity?")

    # Metadata
    class Meta: ordering = ['-title']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.title
    

