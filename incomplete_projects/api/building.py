import json

from django.views.generic import View
from incomplete_projects.models import BuildingStatus
from incomplete_projects.service.building import BuildingService
from incomplete_projects.utils.http import http_response


class BulidingView(View):
    def get(self, request):
        buildings = BuildingService.get_list(
            building_statuses=[
                BuildingStatus.ABANDON_CONSTRUCTION,
                BuildingStatus.PEOPLE_STOP_REPAYMENT,
            ],
        )

        return http_response(
            data=[
                {
                    "id": building.id,
                    "name": building.name,
                    "address": building.address,
                    "phone": building.telephone,
                    "status": building.status,
                    "province": building.province,
                    "city": building.city,
                    "description": building.description,
                    "photos": [p["url"] for p in json.loads(building.photos or "[]")],
                    "position_longitude": float(building.position_longitude),
                    "position_latitude": float(building.position_latitude),
                }
                for building in buildings
            ],
        )
