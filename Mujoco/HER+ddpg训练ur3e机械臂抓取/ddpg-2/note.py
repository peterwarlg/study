import numpy as np
import gym
import matplotlib.pyplot as plt

# np.savetxt(hp['results_path'] + '/scores_' + hp['env_name'] + '_' + str(hp['seed']) + '.csv',
# scores, delimiter=',')
# x = np.loadtxt('./tmp_results/scores_FetchPickAndPlace-v1_3.csv')
f = open(r'./tmp_results/2phase.txt','r')
file = f.readlines()
f.close()

file = np.array(file)
file = file[np.array(range(1, 240, 2))]
# print(file)
data = []
for l in file:
    l = l.replace(' ','')
    number = l[-7:-1]
    # print(number)
    if number[0] != '0':
        pass
    else:
        data.append(float(number))
print(len(data))
import matplotlib.pyplot as plt
plt.plot(data)
plt.show()
#
np.savetxt('./tmp_results/filter_2phase.csv', data)

