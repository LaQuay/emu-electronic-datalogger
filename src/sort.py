def _sort_by_label(flat):
    return flat.label


def order_flats(building_data):
    building_data.flats.sort(key=_sort_by_label)
