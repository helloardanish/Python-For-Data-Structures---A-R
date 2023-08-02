from collections import deque

#list

my_stack = []


#push operation

my_stack.append(6)
my_stack.append(7)
my_stack.append(8)
my_stack.append(9)

#print(my_stack)

# pop operation

my_stack.pop()

my_stack.pop()

#print(my_stack)


my_stack2 = deque()

my_stack2.append(11)
my_stack2.append(12)
my_stack2.append("A R")
my_stack2.append(14)

my_stack2.pop()

print(my_stack2)

print(my_stack2[-1])

print(my_stack2[1]) #stack
