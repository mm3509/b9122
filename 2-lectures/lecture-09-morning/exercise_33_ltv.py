import sklearn.metrics
import sklearn.neighbors
import matplotlib.pyplot as plt

import tqdm


import exercise_31_ltv


range_k = range(5, 41)

score_list = []

df_train, df_test = exercise_31_ltv.get_data()
features = exercise_31_ltv.get_features(df_train)

# tqdm is a nice wrapper that shows a progress bar.
for k in tqdm.tqdm(range_k):

    # TODO: complete this to run kNN with k neighbors, predict on the test
    # dataset into the variable `predictions`, to calculate the r2 with the next line below


    r2 = sklearn.metrics.r2_score(df_test.ltv, predictions)

    score_list.append(r2)


plt.plot(range_k, score_list)
plt.xlabel('k')
plt.ylabel('Out of Sample R-squared')
plt.savefig("bias-variance-tradeoff.png")
plt.show()
