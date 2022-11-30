from django.db import models


class Building(models.Model):
    address = models.CharField(max_length=255)
    type_of_building = models.CharField(max_length=255)
    count_floor = models.IntegerField(default=1)
    date = models.DateField()
    center = models.JSONField()
    coordinates = models.JSONField()

    def __str__(self):
        return self.type_of_building
