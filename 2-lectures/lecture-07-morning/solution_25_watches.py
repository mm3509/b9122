import json
import math
import statistics


# This is a dictionary three lists give the time in minutes since the start of the day.
with open("watches.json") as f:
    time = json.load(f)

true_time = time["true_time"]


n = len(true_time)
for watch in ["c", "d"]:
    measurement = time["watch_" + watch]
    assert n == len(measurement)

    diff = [measurement[i] - true_time[i] for i in range(n)]

    mad = statistics.mean([abs(d) for d in diff])
    rmse = math.sqrt(statistics.mean([d ** 2 for d in diff]))

    print(f"Watch {watch}:")
    print(f"  Mean Absolute Deviation (MAD) = {mad:.2f}")
    print(f"  root-Mean Squared Error (rMSE) = {rmse:.2f}")
