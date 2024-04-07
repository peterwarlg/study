import matplotlib.pyplot as plt
import numpy as np

# x1 = np.loadtxt(
#     './tmp_results/baselines_epochs-120_no-ep_netnode-256_workers-32/baseline_seed_2.csv')
# x2 = np.loadtxt('./tmp_results/baselines_epochs-120_no-ep_netnode-256_workers-32/baseline.csv')
# x3 = np.loadtxt('./tmp_results/filter_new_ep.csv')
# x4 = np.loadtxt('./tmp_results/baseline_seed_1.csv')
# plt.plot(x1, color='red')
# # plt.plot(x2, color='blue')
# # plt.plot(x3, color='y')
# plt.plot(x4, color='g')
import os
# file_list  = os.listdir('./tmp_results/my_algo')
# data = []
# for l in file_list:
#     if l[-3:] == 'csv':
#         data.append(np.loadtxt('./tmp_results/my_algo/' + l))
# for i in data:
#     plt.plot(i)
seed = 1
p1 = './tmp_results/baselines_epochs-120_no-ep_netnode-256_workers-32/baseline_seed_' + str(seed) +'.csv'
p1 = './tmp_results/baselines_epochs-120_no-ep_netnode-256_workers-32/baseline.csv'


p2 = './tmp_results/my_algo/MyAlgo_seed_' + str(seed) +'.csv'
d1 = np.loadtxt(p1)
d2 = np.loadtxt(p2)
plt.plot(d1,'r')
plt.plot(d2,'y')
plt.show()