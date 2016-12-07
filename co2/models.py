from django.db import models

# Create your models here.
# Green pk 1
class Capital(models.Model):
    color = models.CharField(max_length=100)
    capital_title = models.CharField(max_length=200)

    def __str__(self):
        return self.capital_title + ' - ' + self.color


class Impact(models.Model):
    capital = models.ForeignKey(Capital, on_delete=models.CASCADE)
    footprint = models.CharField(max_length=100)
    impact_title = models.CharField(max_length=200)
    valuation = models.CharField(max_length=100)

    def __str__(self):
        return self.impact_title

