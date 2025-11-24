import math
import random
import datetime
import numpy


from mnist_datasets import MNISTLoader
import matplotlib.pyplot as plt


import solution_28_knn_mnist as exercise_28_knn_mnist

# Students: if you want to run the solution, uncomment this line:

# import solution_28_knn_mnist as exercise_28_knn_mnist


def load_data():
    loader = MNISTLoader()
    train_X, train_y = loader.load()
    assert len(train_X) == 60000 and len(train_y) == 60000

    test_X, test_y = loader.load(train=False)
    assert len(test_X) == 10000 and len(test_y) == 10000

    return 255 - train_X, train_y, 255 - test_X, test_y


def save_to_disk():
    """
    Save to disk, to gauge the size of the "model": 45 MB.
    """
    print("Saving data to disk")
    with open("mnist.bin", "wb") as f:
        numpy.save(f, train_X)
        numpy.save(f, train_y)


def reshape(flat_img):
    """
    Reshape a flat image from size (784, ) to size (28, 28)
    """
    return flat_img.reshape(28, 28)


def show_sample_images(train_X, train_y):
    print("Showing sample images")
    for i in range(9):  
        plt.subplot(330 + 1 + i)
        # Remove ticks.
        plt.xticks([], [])
        plt.yticks([], [])
        j = random.randrange(len(train_y))
        plt.imshow(reshape(train_X[j]), cmap=plt.get_cmap('gray'))
        plt.title(train_y[j], color="g")
    plt.show()
    print("Shown sample images, please close graphic to proceed")


def show_single_image(data):
    x = reshape(data)
    plt.imshow(x, cmap='gray')
    plt.show()


def compute_accuracy(test_X, test_y, train_X, train_y, k):
    cnt = 0
    
    for x, label in zip(test_X, test_y):
        prediction, nearest = exercise_28_knn_mnist.kNN(x, k, train_X, train_y)
        if prediction == label:
            cnt += 1

    return cnt / len(test_y)


def sci_notation(d):
    """
    Show scientific notation, e.g. '1.1 x 10^6' instead of '1.1E+06'.
    """
    exponent = math.floor(math.log(d) / math.log(10))
    significand = "%.1f" % (d / 10 ** exponent)
    return significand + " x 10^%d" % exponent


def difference(x, y):
    """Computes difference, converting to signed integers with 32
    bits. Otherwise, with unsigned 8-bit integers, 0 - 1 = 255
    (overflow/saturation arithmetics).
    """
    return x.astype("int32") - y.astype("int32")


def show_correct_wrong(test_X, test_y, train_X, train_y, k=1, start_with=[]):

    random.seed(a=41)
    last = "wrong"
    while True:

        if 1 <= len(start_with):
            i = start_with.pop(0)
        else:
            i = random.randrange(len(test_y))

        print("Trying image i = ", i)
            
        x = test_X[i]
        y = test_y[i]
        if 1 == k:
            prediction, nearest = exercise_28_knn_mnist.kNN1(x,
                                                             train_X,
                                                             train_y)
        else:
            prediction, nearest = exercise_28_knn_mnist.kNN(x,
                                                            k,
                                                            train_X,
                                                            train_y)

        correct = prediction == y
        show = False
        if correct and last != "correct":
            show = True
            last = "correct"
            color = "g"
            other_color = "r"

            # Find another image with a different number.
            for j in range(len(train_y)):
                if train_y[j] != y:
                    break
                
            print("Correct prediction: %d" % prediction)
            
        if not correct and last != "wrong":
            show = True
            last = "wrong"
            color = "r"
            other_color = "g"

            # Find an image with the right number.
            for j in range(len(train_y)):
                if train_y[j] == y:
                    break
                
            print("Wrong prediction: %d, true label: %d" % (prediction, y))

        if show:

            try:
                d = exercise_28_knn_mnist.distance(train_X[nearest], test_X[i])
                d2 = exercise_28_knn_mnist.distance(train_X[j], test_X[i])
                
                msg = (f"Data point = {i}, prediction = {prediction},"
                       f" nearest neighbor = {nearest}, distance = {d}")
                print(msg)
                plt.subplot(231)
                plt.imshow(reshape(test_X[i]), cmap=plt.get_cmap('gray'))
                plt.title("Input" % test_y[i], color="k")
                plt.xticks([], [])
                plt.yticks([], [])
                
                plt.subplot(234)
                plt.imshow(reshape(test_X[i]), cmap=plt.get_cmap('gray'))
                plt.title("Input (same)" % test_y[i], color="k")
                plt.xticks([], [])
                plt.yticks([], [])

                plt.subplot(232)
                plt.imshow(reshape(train_X[nearest]), cmap=plt.get_cmap('gray'))
                plt.title("Nearest (%d)" % train_y[nearest], color=color)
                plt.xticks([], [])
                plt.yticks([], [])
                
                plt.subplot(233)
                diff = difference(train_X[nearest], test_X[i])
                plt.imshow(255 - numpy.abs(reshape(diff)),
                           cmap=plt.get_cmap('gray'))
                plt.title("Diff (d = %s)" % sci_notation(d), color=color)
                plt.xticks([], [])
                plt.yticks([], [])
                
                plt.subplot(235)
                plt.imshow(reshape(train_X[j]), cmap=plt.get_cmap('gray'))
                plt.title("Other (%d)" % train_y[j],
                          color=other_color)
                plt.xticks([], [])
                plt.yticks([], [])
                
                plt.subplot(236)
                diff = difference(train_X[j], test_X[i])
                plt.imshow(255 - numpy.abs(reshape(diff)),
                           cmap=plt.get_cmap('gray'))
                plt.title("Diff (d = %s)" % sci_notation(d2),
                          color=other_color)
                plt.xticks([], [])
                plt.yticks([], [])

                plt.show()
            except KeyboardInterrupt:
                return            
    

def main():

    train_X, train_y, test_X, test_y = load_data()

    print(f"{type(train_X)=}")
    print(f"{type(train_X[0])=}, {train_X[0]=}")
    print(f"{type(train_y)=}")
    print(f"{type(train_y[0])=}, {train_y[0]=}")

    input("Continue?")

    show_sample_images(train_X, train_y)
    show_correct_wrong(test_X,
                       test_y,
                       train_X,
                       train_y,
                       1,
                       start_with=[4644])

    # Compute the accuracy for k = 1..10
    for k in range(1, 11):
        start = datetime.datetime.now()
        acc = compute_accuracy(test_X, test_y, train_X, train_y, k)
        elapsed_hours = (datetime.datetime.now() - start).total_seconds() / 3600
        msg = (f"At k = {k}, accuracy = {acc * 100:2.2f}"
               f" ({elapsed_hours:.1f} hours)")
        print(msg)

"""
# Result:
At k = 1, accuracy = 96.91% (1.9 hours)
At k = 2, accuracy = 96.27% (1.9 hours)
At k = 3, accuracy = 97.05% (1.8 hours)
At k = 4, accuracy = 96.82% (1.8 hours)
At k = 5, accuracy = 96.88% (1.8 hours)
At k = 6, accuracy = 96.77% (1.8 hours)
At k = 7, accuracy = 96.94% (1.8 hours)
At k = 8, accuracy = 96.70% (1.8 hours)
At k = 9, accuracy = 96.59% (1.8 hours)
At k = 10, accuracy = 96.65% (1.8 hours)
"""

if "__main__" == __name__:
    main()
