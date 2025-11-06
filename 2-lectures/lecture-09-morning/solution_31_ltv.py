import pathlib

import pandas as pd
import sklearn.model_selection as sk_ms

import sklearn.linear_model
import sklearn.metrics


DATA_FILENAME = 'B2B-sales.csv'


def get_data_filepath_robust():

    this_dir = pathlib.Path(__file__).resolve().parent
    data_filepath = os.path.join(this_dir, DATA_FILENAME)

    return data_filepath


def get_data():

    # Students: if you call this file from the shell, outside the directory,
    # the line below will fail, because it looks for DATA_FILEPATH in the
    # current directory of the shell. So you can use this instead:
    
    # df_customers = pd.read_csv(get_data_filepath_robust())

    df_customers = pd.read_csv(DATA_FILENAME)
    print(df_customers.head())
    print(f"{len(df_customers)=}")

    df_train, df_test = sk_ms.train_test_split(df_customers,
                                               train_size = 0.7,
                                               random_state = 123,
                                               shuffle = True)
    print(f"{len(df_train)=}")
    print(f"{len(df_test)=}")

    return df_train, df_test


def get_features(df):
    features = list(df.columns)
    features.remove("ltv")  # Remember: .remove() operates in-place.
    
    return features


def linear_regression():

    df_train, df_test = get_data()

    features = get_features(df_train)

    lm = sklearn.linear_model.LinearRegression()
    lm.fit(df_train[features], df_train.ltv)

    y_test_predicted = lm.predict(df_test[features])

    return sklearn.metrics.r2_score(df_test["ltv"], y_test_predicted)


print(f"R2 from linear regression: {linear_regression():.2f}")
