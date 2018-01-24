from django.db import models

# Create your models here.
class TestModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='Default Name')
    description = models.CharField(max_length=255, blank=False, null=False, default='Default Description')

    class Meta:
        ordering = ('created',)