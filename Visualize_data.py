from time import gmtime, strftime

import pandas as pd
from d3blocks import D3Blocks


def get_activity(code):
    code = int(code)
    if code in [101, 102, 199, 201, 202, 299, 301, 302, 399, 401, 402, 499, 502]:
        return "Work"
    elif code in [
        198,
        298,
        298,
        498,
        598,
        698,
        798,
        898,
        998,
        1098,
        1198,
        1298,
        1398,
        1498,
        1598,
    ]:
        return "Travelling"
    elif code == 501:
        return "Sell food"
    elif code in [504, 505, 506, 507, 508]:
        return "Provide services"
    elif code == 601:
        return "Housework"
    elif code == 602:
        return "Shopping"
    elif code in [701, 702]:
        return "Caring"
    elif code in [901, 902, 903]:
        return "Education"
    elif code in [1201, 1202, 1203, 1299]:
        return "Entertainment"
    elif code in [1301, 1302, 1399]:
        return "Sport"
    elif code == 1402:
        return "TV/Youtube"
    elif code == 1404:
        return "Surf web"
    elif code == 1501:
        return "Sleeping"
    elif code == 1502:
        return "Eating"
    elif code == 1503:
        return "Personal hygiene"
    elif code == 1506:
        return "Relaxing"
    else:
        return "Others"


def gmt(time):
    return strftime("%d-%m-%Y %H:%M:%S", gmtime(int(time) * 60))


def id(id):
    return "{:.0f}".format(float(id))


data = pd.read_csv(
    "C:/TDAK/Project/Vietnamese_time_usage/VNM_2022_TUS_v01_M_CSV/4_diary_main.csv",
    encoding="latin",
    usecols=["ID", "BEGIN", "Q401"],
    converters={"Q401": get_activity, "BEGIN": gmt, "ID": id},
)
data = data.rename(columns={"ID": "sample_id", "BEGIN": "datetime", "Q401": "state"})
data = data.sort_values(["sample_id", "datetime"])

chart = D3Blocks()
chart.movingbubbles(
    data,
    datetime="datetime",
    sample_id="sample_id",
    state="state",
    center="Travelling",
    cmap="hsv",
    filepath="./moving_bubbles.html",
    figsize=[780, 800]
)
