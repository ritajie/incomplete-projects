import enum

from django.db import models


class BuildingStatus(enum.IntEnum):
    UNDER_CONSTRUCTION = 0
    CONSTRUCTION_COMPLETED = 1
    ABANDON_CONSTRUCTION = -1
    PEOPLE_STOP_REPAYMENT = -2


class Building(models.Model):
    class Meta:
        db_table = "building"

    id = models.AutoField(primary_key=True, db_column="id")
    name = models.CharField(
        max_length=255, db_column="name",
    )  # Github ‘weneedname’ 仓库中提供的 name
    full_name = models.CharField(
        max_length=255, db_column="full_name",
    )  # 来自高德地图查询到的 name
    status = models.IntegerField(
        db_column="status",
        choices=[
            (0, "Under construction"),
            (1, "Construction completed"),
            (-1, "Abandon construction"),
            (-2, "People stop repayment"),
        ],
    )
    address = models.CharField(max_length=255, db_column="address")
    city = models.CharField(max_length=255, db_column="city")
    province = models.CharField(max_length=255, db_column="province")
    telephone = models.CharField(max_length=255, db_column="telephone")
    photos = models.TextField(db_column="photos")
    position_longitude = models.CharField(
        max_length=255, db_column="position_longitude",
    )
    position_latitude = models.CharField(max_length=255, db_column="position_latitude")
    description = models.TextField(db_column="description")

    def __str__(self):
        return f"Building<name={self.name}, city={self.city}, province={self.province}, telephone={self.telephone}, photos={self.photos}, position_longitude={self.position_longitude}, position_latitude={self.position_latitude}, description={self.description}>"
