import sys

print(max(map(float, filter(lambda x: x.isdigit(), sys.argv[1:]))))
