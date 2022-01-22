# This still about for loop you can make delay or counter that counting with delay

import time

# 10 is for counting start and 0 is counting end, then decrement the value
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(2) # Delay you can change how long you want this delay to be. (s)

print("Happy New Year")