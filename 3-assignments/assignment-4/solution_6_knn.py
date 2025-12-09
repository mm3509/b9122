import os
import pathlib


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


THIS_DIR = pathlib.Path(__file__).resolve().parent
DATA_FILEPATH = os.path.join(THIS_DIR, "creditcard.csv")


def helper_prepare_data():
    if not os.path.exists(DATA_FILEPATH):
        print(("Remember to unzip the file and place it in "
               "the folder where you are running this file"))
        assert False, "Filepath missing: " + DATA_FILEPATH

    data = pd.read_csv(DATA_FILEPATH)

    scaler = StandardScaler()
    columns = list(data.columns)
    columns.remove("Class")

    data[columns] = scaler.fit_transform(data[columns])

    train = data.sample(frac=0.1, random_state=42)
    remainder = data.loc[~data.index.isin(train.index)]
    test = remainder.sample(frac=0.04, random_state=42)

    X_train = train[columns]
    y_train = train["Class"]

    X_test = test[columns]
    y_test = test["Class"]

    return X_train, y_train, X_test, y_test


def helper_convert_list_to_dataframe(x_as_list, columns):
    """This function converts a list of numbers to a format suitable for
    prediction after a fit by SciKit-Learn.
    """

    return pd.DataFrame([x_as_list], columns=columns)


def predict_knn(n_neighbors, x_as_list):

    # Students: underscore variables are silent variables, that we do not use.
    X_train, y_train, _, _ = helper_prepare_data()

    x_as_dataframe = helper_convert_list_to_dataframe(x_as_list,
                                                      X_train.columns)

    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    predicted_probability = knn.predict_proba(x_as_dataframe)

    # Once you have predicted the probability from the model, you access the
    # result at index 0 (first data point, since we only pass one) and then
    # index 1 (since we want the probability of fraud).
    return predicted_probability[0][1]


# Students: this is how you can print a report of the algorithm's accuracy.

# def helper_print_report():
#
#     _, _, X_test, y_test = helper_prepare_data()
#
#     for i, row in X_test.iterrows():
#         x = X_test.loc[i, :]
#         print(x.shape)
#         print(x.to_frame().shape)
#         y_predicted = predict_knn(row)
#         print(y_predicted)
#
#     print(classification_report(y_test, predicted))
#
#
# helper_print_report()


# Students: this is how you can run code when the file is run directly as a
# script, but not when it's imported as a module. It uses a "dunder" variable,
# `__name__`, which equals `"__main__"` when called directly, and the file's
# name when imported. This way, when Autograder imports your file, it doesn't
# print any output.
if __name__ == "__main__":
    _, _, X_test, y_test = helper_prepare_data()

    # Students: this code gets the first row from the test data and converts it
    # to a list.
    x_as_list = list(X_test.iloc[0])
    k = 100
    print("Predicted probability: ", predict_knn(k, x_as_list))
