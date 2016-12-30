from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
# Green pk 1
class Capital(models.Model):
    color = models.CharField(max_length=100)
    capital_title = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('co2:detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.capital_title + ' - ' + self.color


class Impact(models.Model):
    capital = models.ForeignKey(Capital, on_delete=models.CASCADE)
    footprint = models.CharField(max_length=100)
    impact_title = models.CharField(max_length=200)
    valuation = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.impact_title

