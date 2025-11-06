import json


import numpy
import matplotlib.pyplot as plt


def kNN(training_input, training_output, x, k):

    # Use absolute distance or squared distance between target and inputs.
    distances = [abs(xx - x) for xx in training_input]

    # To save time, use numpy.argpartition. It does not sort the
    # entire array; it only guarantees that the k-th element
    # is in sorted position and all smaller elements will be
    # moved before that. So the first k elements will be the
    # k-smallest elements.
    argsorted = numpy.argpartition(distances, k)

    closest_k_neighbor_indices = argsorted[:k]

    # Students: you can compute the average with a for loop like this:

    # total = 0
    # for i in closest_k_neighbor_indices:
    #     total += training_output[i]
    # 
    # average_at_x = total / k

    # Or with a list comprehension like this:

    # return sum([training_output[i] for i in closest_k_neighbor_indices]) / k

    average_at_x = numpy.mean([training_output[j]
                               for j in closest_k_neighbor_indices])

    return average_at_x



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
    plt.show()
