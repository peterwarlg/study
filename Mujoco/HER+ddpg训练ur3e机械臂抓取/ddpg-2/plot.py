import matplotlib.pyplot as plt
import numpy as np

x1 = np.loadtxt('./tmp_results/pick-baseline-hidden-256/scores_FetchPickAndPlace-v1_1_256.csv')
x2 = np.loadtxt('./tmp_results/pick-baseline-hidden-256/baseline.csv')
x3 = np.loadtxt('./tmp_results/filter_new_ep.csv')
x4 = np.loadtxt('./tmp_results/filter_2phase.csv')
plt.plot(x1, color='red')
plt.plot(x2,color='blue')
plt.plot(x3, color='y')
plt.plot(x4, color='g')
plt.show()