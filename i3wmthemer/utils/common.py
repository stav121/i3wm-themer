import json


def get_colors_from_wal():
    path = "~/.cache/wal/colors.json"
    with open(path, "r") as f:
        colors_dict = json.load(f)

    return colors_dict

