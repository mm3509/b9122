def predict(budget, duration, month_to_predict):

    with open("expenses.json") as f:
        past_projects = json.load(f)

    # In assignment 4, you'll have to complete this function.
