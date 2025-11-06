import matplotlib.pyplot as plt

import sklearn.metrics
import sklearn.neighbors


import exercise_31_ltv


def knn():

    df_train, df_test = exercise_31_ltv.get_data()
    features = exercise_31_ltv.get_features(df_train)

    # TODO: nothing, just read this file and the three lines below, which show how to run kNN

    knn = sklearn.neighbors.KNeighborsRegressor()
    knn.fit(df_train[features], df_train["ltv"])

    y_test_predicted = knn.predict(df_test[features])

    for ft in exercise_31_ltv.get_features(df_train):
        x = df_train[ft]
        y = df_train["ltv"]
        plt.scatter(x, y)
        plt.title("Feature: " + ft)
        plt.show()

    return sklearn.metrics.r2_score(df_test["ltv"], y_test_predicted)


print(f"R2 from k-nearest neighbors: {knn():.2f}")
