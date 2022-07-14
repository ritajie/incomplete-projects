import enum

from django.db import models


class BuildingStatus(enum.IntEnum):
    UNDER_CONSTRUCTION = 0
    CONSTRUCTION_COMPLETED = 1
    ABANDON_CONSTRUCTION = -1


class Building(models.Model):
    class Meta:
        db_table = "building"

    id = models.AutoField(primary_key=True, db_column="id")
    name = models.CharField(max_length=255, db_column="name")
    status = models.IntegerField(
        db_column="status",
        choices=[
            (0, "Under construction"),
            (1, "Construction completed"),
            (-1, "Abandon construction"),
        ],
    )
    address = models.CharField(max_length=255, db_column="address")
    city = models.CharField(max_length=255, db_column="city")
    description = models.TextField(db_column="description")
    postion_longitude = models.FloatField(db_column="position_longitude")
    position_latitude = models.FloatField(db_column="position_latitude")
