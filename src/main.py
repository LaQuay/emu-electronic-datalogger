import csv
from datetime import datetime
from typing import List

from src.file_parser import get_flat_door_from_filename, read_data_from_json, dot_to_comma_decimals
from src.models.Building import Building, Flat
from src.models.Consumption import MonthlyVolume
from src.models.FileJson import FileJsonDump
from src.sort import order_flats

FILENAME = "05Agosto2024"
CSV_HEADER = "Hoja de consumos de agua caliente por piso"

READ_FOLDER = "../in/"
WRITE_FOLDER = "../out/"


def save_to_csv(folder: str, filename: str, data):
    with open(f"{folder}{filename}.csv", "wt", newline="") as csvfile:
        writer = csv.writer(csvfile, dialect='excel', delimiter=";", quoting=csv.QUOTE_MINIMAL)
        writer.writerow([CSV_HEADER])

        day_labels = []
        for consumption in data.flats[0].consumption:
            day_labels.append(datetime.utcfromtimestamp(consumption.day).strftime('%Y-%m-%d'))

        writer.writerow(["Piso", f"Diferencia de consumo (m3)", *day_labels])

        for flat in data.flats:
            consumptions_labels = []
            for consumption in flat.consumption:
                consumptions_labels.append(dot_to_comma_decimals(consumption.volume))
            if len(consumptions_labels) != len(day_labels):
                writer.writerow(f"Piso {flat.label} contiene un error en los datos proporcionados")

            consumption_diff = round(flat.consumption[-1].volume - flat.consumption[0].volume, 4)
            writer.writerow([flat.label, dot_to_comma_decimals(consumption_diff), *consumptions_labels])


def create_building_structure(data_dump: List[FileJsonDump]) -> Building:
    building = Building()

    for flat_file in data_dump:
        device = flat_file.flat_json.get("Device")

        flat = Flat(id=device["Id"], label=get_flat_door_from_filename(flat_file.file_name), serial=device["Serial"])

        for value in device["ValueDesc"]:
            if value["DescriptionStr"] == "Volume" and value["StorageNum"] == 0:
                for volume_value in value["Value"]:
                    day_volume = MonthlyVolume(day=volume_value["TimeStamp"], volume=volume_value["Val1"])
                    flat.consumption.append(day_volume)

        building.flats.append(flat)

    return building


if __name__ == "__main__":
    file_json_data = read_data_from_json(READ_FOLDER)

    building_data = create_building_structure(file_json_data)

    order_flats(building_data)

    save_to_csv(WRITE_FOLDER, FILENAME, building_data)
