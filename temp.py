import re
import sys

for line in sys.stdin:
    line = line.strip()
    result = re.match(r"^(1(01*0)*1|0)+$", line)
    if result is not None:
        print(line)
