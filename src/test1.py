
import math
import random

print("begin")

bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']
joe = ['Joe Biden', 78, 25000, 'vice prez']

print(bob[0], sue[2])

people = [bob, sue, joe]
for person in people:
    print(person)
    
print(math.pi)
print(random.choice(people))

s = 'spam'
print(len(s))
print(s[-1])
