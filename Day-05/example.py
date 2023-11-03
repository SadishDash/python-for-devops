import sys
import os

def add(a,b):
    return a+b;

def sub(a,b):
    return abs(a-b);

def mul(a,b):
    return a*b;

num = int(sys.argv[1])
num2 = int(sys.argv[3])
op = sys.argv[2]

#print(num, num2, op)

if op == 'add':
    print(add(num,num2))
elif op== 'sub':
    print(sub(num,num2))
else:
    print(mul(num,num2))

print(os.getenv("name"))


# @SadishDash ➜ /workspaces/python-for-devops/Day-05 (main) $ export name="Sadish"
# @SadishDash ➜ /workspaces/python-for-devops/Day-05 (main) $ python example.py 12 add 2
# @SadishDash ➜ /workspaces/python-for-devops/Day-05 (main) $ python example.py 12 add 2
# 14
# Sadish