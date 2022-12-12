import os

with open('.env') as handle:
    lines = handle.readlines()

try:
    for line in lines:
        equal = line.find('=')
        key = line[:equal]
        os.environ[key] = line[equal + 1:]
        print(equal, key, os.environ[key])
except ValueError:
    pass

SECRET = os.environ['SECRET']
print(SECRET)
