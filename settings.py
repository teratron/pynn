import os

with open('.env') as handle:
    lines = handle.readlines()

try:
    for line in lines:
        ind = line.find('=')
        key = line[:ind]
        os.environ[key] = line[ind + 1:]
        print(ind, key, os.environ[key])
except ValueError:
    pass

SECRET = os.environ['SECRET']
print(SECRET)
