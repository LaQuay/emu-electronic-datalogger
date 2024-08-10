import json
from typing import List

from src.models.FileJson import FileJsonDump


def get_flat_door_from_filename(file_name):
    """Extracts the flat door code from a filename.

    Args:
        file_name: The input filename. e.g.: DataExport_123467_PL5G_25_1_2024_8_56_30

    Returns:
        The extracted flat door code as a string. e.g. 05G
    """
    full_name = file_name.split("_")[2]  # PL5G
    full_name = full_name.replace("PL", "")  # 5G
    if len(full_name) == 2:
        full_name = "0" + full_name  # 05G

    return full_name


def dot_to_comma_decimals(number: float) -> str:
    """
    # Returns 0,123 from 0,123
    """
    return str(number).replace(".", ",")


def read_data_from_json(containing_folder: str) -> List[FileJsonDump]:
    """
    Reads JSON files from a specified folder and returns a list of FileJsonDump.
    """
    import os

    files_in_folder = os.listdir(containing_folder)
    data = []
    for file in files_in_folder:
        with open(f"{containing_folder}{file}") as fp:
            data.append(FileJsonDump(file_name=file, flat_json=json.load(fp)))

    return data
