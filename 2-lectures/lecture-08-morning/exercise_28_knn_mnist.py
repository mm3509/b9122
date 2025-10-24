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

    # TODO: implement 1-nearest neighbor here.

    # Return a tuple, with the label of the nearest neighbor, and its position
    # in the training data (for plotting).

    return training_y[nearest], nearest


def kNN(x, k, training_X, training_y):
    """
    Nearest-neighbors for the general case of k.
    """
    # TODO (at home, if interested): implement k-nearest-neighbors here.

    # Also return a tuple, as above.
    
    return 
