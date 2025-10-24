import json


# This is a dictionary three lists give the time in minutes since the start of the day.
with open("watches.json") as f:
    time = json.load(f)

true_time = time["true_time"]

# TODO: quantify wrongness of watches A and B.
