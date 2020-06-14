from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class BMI(models.Model):
	name=models.CharField(max_length=100, default="NA")
	height_in_cms=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5000)], default="1");
	weight=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)], default="1");
	
