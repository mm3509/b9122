import json


import numpy
import matplotlib.pyplot as plt


def kNN(training_input, training_output, x, k):

    # TODO: complete this function to implement kNN (without using
    # SciKit-learn).

    return


# Students: open the data this way:
with open("time-series.json", encoding='utf-8') as f:
    training_output = json.load(f)

training_input = list(range(len(training_output)))
    

# Students: this is a more fine-grained range for inputs, so we can see the
# contours of the outputs.
prediction_input = numpy.arange(0, len(training_output), 0.1)

for k in range(1, 9, 2):
    prediction_output = []

    for week in prediction_input:
        prediction_output.append(kNN(training_input, training_output, week, k))

    plt.figure()
    plt.scatter(training_input, training_output)
    plt.plot(prediction_input, prediction_output, color="c")
    plt.xlabel("time (weeks)")
    plt.ylabel("sales")
    plt.title(f"kNN for k = {k}")
    plt.savefig(f"kNN-{k}.png")
