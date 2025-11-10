import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model


import exercise_4_expenses as exercise_4
import exercise_5_linear_regression as exercise_5


budget = 100
duration = 12


for source in ["miguel", "student"]:

    if "miguel" == source:
        projects = exercise_5.helper_generate_data_miguel(duration)
    else:
        projects = exercise_5.generate_data_student(duration)

        # Students: the next 8 lines convert a list of lists into a format
        # suitable for regression, where y is the expense (scaled to the new
        # budget), and x contains the month. By distributing data like this, we
        # break the iid assumption required for linear regression.

    x = []
    y = []
    for project in projects:
        project_budget = sum(project)
        y.extend([budget * element / project_budget for element in project])
        x.extend(list(range(len(project))))
    x = np.asarray(x).reshape(-1, 1)

    reg = sklearn.linear_model.LinearRegression()
    reg.fit(x, y)
    linear_prediction = reg.predict(x)

    conditional_mean = exercise_4.predict_expenses(budget=budget,
                                                   duration=duration,
                                                   past_projects=projects)

    plt.scatter(x, y)
    plt.plot(x, linear_prediction, c="r")
    plt.plot(range(duration), conditional_mean, c="g")
    plt.xlabel("months")
    plt.ylabel("expenses")
    if "student" == source:
        plt.savefig("linear-regression.png")
    plt.show()
