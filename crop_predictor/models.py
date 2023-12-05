from django.db import models

class CropPrediction(models.Model):
    n = models.FloatField()
    p = models.FloatField()
    k = models.FloatField()
    rain = models.FloatField()
    ph = models.FloatField()
    temp = models.FloatField()
    hum = models.FloatField()

    class Meta:
        app_label = 'crop_predictor'

