# built on code by: Manas Sharma
# Website: www.bragitoff.com
# Email: manassharma07@live.com
# License: MIT
# Value of Pi using Monte carlo

import numpy as np
import os
import time


start_time = time.time()
# Input parameters
#nTrials = int(10E4)
nTrials = 123456789
radius = 1

#-------------
# Counter for thepoints inside the circle
nInside = 0

# Generate points in a square of side 2 units, from -1 to 1.
XrandCoords = np.random.default_rng().uniform(-1, 1, (nTrials,))
YrandCoords = np.random.default_rng().uniform(-1, 1, (nTrials,))

for i in range(nTrials):
    x = XrandCoords[i]
    y = YrandCoords[i]
    # Check if the points are inside the circle or not
    if x**2+y**2<=radius**2:
        nInside = nInside + 1

area = 4*nInside/nTrials

duration = time.time() - start_time
try:
    filename = 'pi.' + str(os.environ['PBS_ARRAY_INDEX'])
    f = open(filename,'a')
    f.write(str(area)+'\n')
    f.close()
    print(nTrials, "   ", area, "   ", duration)
except:
    print(nTrials, "   ", area, "   ", duration)
