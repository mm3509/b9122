import numpy


def difference(x, y):
    """Computes difference, converting to signed integers with 32
    bits. Otherwise, with unsigned 8-bit integers, 0 - 1 = 255
    (overflow/saturation arithmetics).
    """
    return x.astype("int32") - y.astype("int32")


def distance(x, y, verbose=False):
    """Euclidean distance.
    """
    return numpy.sum(numpy.square(x - y))


def kNN1(x, training_X, training_y, verbose=False):
    """Simple 1-nearest neighbor algorithm.
    """

    # Students: this is how I coded 1-nearest-neighbor during lecture.
    
    # nearest = None
    # min_distance = None
    # for i in range(len(training_X)):
    #     training_image = training_X[i]
    #     dist = distance(x, training_image)
    #     if min_distance is None or dist < min_distance:
    #         min_distance = dist
    #         nearest = i

    distances = [distance(x, training_X[i]) for i in range(len(training_X))]
    nearest = numpy.argmin(distances)

    return training_y[nearest], nearest


def kNN(x, k, training_X, training_y):
    """
    Nearest-neighbors for the general case of k.
    """
    distances = [distance(x, training_X[i]) for i in range(len(training_X))]

    # To save time, use numpy.argpartition. It does not sort the entire
    # array; it only guarantees that the kth element is in sorted
    # position and all smaller elements will be moved before it. So
    # the first k elements will be the k-smallest elements.
    argsorted = numpy.argpartition(distances, k)

    # Find the most frequent class among the first k data points.
    classes, freq = numpy.unique(training_y[argsorted[:k]], return_counts=True)
    return classes[numpy.argmax(freq)], argsorted[0]
