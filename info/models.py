from django.db import models

class NumberModer(models.Model):
  id = models.AutoField(primary_key=True)
  guessNumber = models.DecimalField(max_digits=10,decimal_places=2)