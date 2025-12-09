from sklearn.linear_model import LogisticRegression

import solution_6_knn as exercise_6


def predict_logistic(x_as_list):

    # Students: underscore variables are silent variables, that we do not use.
    X_train, y_train, _, _ = exercise_6.helper_prepare_data()
    columns = X_train.columns
    x_as_dataframe = exercise_6.helper_convert_list_to_dataframe(x_as_list,
                                                                 columns)

    log_reg = LogisticRegression()
    log_fit = log_reg.fit(X_train, y_train)

    predicted_probability = log_fit.predict_proba(x_as_dataframe)
    return predicted_probability[0][1]


# Students: this is how you can run code when the file is run directly as a
# script, but not when it's imported as a module. It uses a "dunder" variable,
# `__name__`, which equals `"__main__"` when called directly, and the file's
# name when imported. This way, when Autograder imports your file, it doesn't
# print any output.
if __name__ == "__main__":
    _, _, X_test, y_test = exercise_6.helper_prepare_data()

    # Students: this code gets the first row from the test data and converts it
    # to a list.
    x_as_list = list(X_test.iloc[0])
    print("Predicted probability: ", predict_logistic(x_as_list))
