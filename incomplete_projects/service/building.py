from typing import List, Optional

from incomplete_projects.models import Building, BuildingStatus


class BuildingService:
    @classmethod
    def get_list(
        cls, building_statuses: Optional[List[BuildingStatus]] = None,
    ) -> List[Building]:
        buildings = Building.objects.all()
        if building_statuses is not None:
            buildings = buildings.filter(status__in=building_statuses)
        return list(buildings)
