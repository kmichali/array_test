import numpy as np
import os
import time

start_time = time.time()


#trials = int(1e6)
trials = 123456789

rng = np.random.default_rng()
x, y = rng.random((2, trials))
area = 4*(np.sum(x**2 + y**2 <= 1) / trials)

duration = time.time() - start_time
try:
    filename = 'pi.' + str(os.environ['PBS_ARRAY_INDEX'])
    f = open(filename,'a')
    f.write(str(area)+'\n')
    f.close()
    print(trials, "   ", area, "   ", duration)
except:
    print(trials, "   ", area, "   ", duration)


