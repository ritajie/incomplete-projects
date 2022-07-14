from django.views.generic import View
from incomplete_projects.models import BuildingStatus
from incomplete_projects.service.building import BuildingService
from incomplete_projects.utils.http import http_response


class BulidingView(View):
    def get(self, request):
        buildings = BuildingService.get_list(
            building_statuses=[BuildingStatus.ABANDON_CONSTRUCTION],
        )

        return http_response(
            data=[
                {
                    "id": building.id,
                    "name": building.name,
                    "address": building.address,
                    "city": building.city,
                    "description": building.description,
                    "postion_longitude": building.postion_longitude,
                    "position_latitude": building.position_latitude,
                }
                for building in buildings
            ],
        )
