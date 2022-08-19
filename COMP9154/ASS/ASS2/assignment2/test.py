import os
import sys
count = 0
try:
    TOTAL_RUN = int(sys.argv[3])
except:
    TOTAL_RUN = 10

for i in range(TOTAL_RUN):
    try:
        data = os.popen(f"dart king.dart {int(sys.argv[1])} {int(sys.argv[2])}").read()
        if 'true' in data:
            count += 1
    except:
        try:
            data = os.popen(f"dart king.dart").read()
            if 'true' in data:
                count += 1
        except:
            break
print('Number of success: ',count)
print('Number of failure: ',TOTAL_RUN-count)