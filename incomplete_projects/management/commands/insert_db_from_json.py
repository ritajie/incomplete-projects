import json
from typing import Dict, List

from django.core.management import BaseCommand
from incomplete_projects.models import Building


class Command(BaseCommand):
    def handle(self, *args, **options):
        building_data_filepath = options["building_data_filepath"]
        buildings_data: List[Dict] = json.load(open(building_data_filepath))
        buildings: List[Building] = []

        self.check_positon_unique(buildings_data)

        for building_data in buildings_data:
            github_raw_data = building_data["Github.WeNeedHome.rawData"]
            amap_data = building_data["amap.data"]["pois"][0]
            building = Building(
                name=github_raw_data["name"],
                full_name=amap_data["name"],
                status=options["building_status"],
                address=amap_data["address"],
                city=amap_data["cityname"],
                province=amap_data["pname"],
                telephone=amap_data["tel"],
                photos=json.dumps(amap_data["photos"] or []),
                position_longitude=amap_data["location"].split(",")[0],
                position_latitude=amap_data["location"].split(",")[1],
            )
            buildings.append(building)

        if not options["dry_run"]:
            Building.objects.bulk_create(buildings)
        for building in buildings:
            print(building)

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run", dest="dry_run", action="store_true", help="空跑，只打印中间数据，不做 DML",
        )
        parser.add_argument(
            "--building-data-filepath",
            dest="building_data_filepath",
            required=True,
            help="JSON 文件路径",
        )
        parser.add_argument("--building-status", type=int, required=True, help="楼盘状态")

    def check_positon_unique(self, buildings_data) -> None:
        position_set = set()
        repeat_posions = []
        for building_data in buildings_data:
            amap_data = building_data["amap.data"]["pois"][0]
            position = amap_data["location"]
            if position in position_set:
                repeat_posions.append(position)
            position_set.add(position)

        if repeat_posions:
            for position in repeat_posions:
                print(position)
            raise Exception(f"重复的位置：{len(repeat_posions)}")
