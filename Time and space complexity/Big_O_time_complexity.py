#constant O(1)
def const_fun(lst):
  #print the first value of item
  print(lst[0])
  
const_fun([1,2,3,4,5,6])

#output 1

#otput will always be 1
#so no matter how many elements are there in list. It will always print 1 value.
#this is an example of constant time.




#linear O(n)

def lin_fun(lst):
  for item in lst:
    print(item, end=' ')
    
lin_fun([1,2,3,4])

#output 1 2 3 4

#the function runs O(n) time.It will every item in the list. If you have 1000 item
#it will 1000 item. If you have n items it will print n values.





#Quadric O(n^2)

def quad_fun(lst):
  for i in lst:
    for j in lst:
      print ("%d %d",%(i, j), end = ':')
      
quad_fun([1,2,3])

#output 1 1:1 2:1 3:2 1:2 2:2 3:3 1:3 2:3 3

#here we see if we have list of n items it will perform n operations for evey item in the list.


#some more examples to check knowledge

#example 1

def print_lst_check(lst):
    for i in lst:
        print(i) #O(n)
        
    for j in lst:
        print(j) #O(n)
        
    for k in lst:
        print(k) #O(n)
       
print_lst_check([1,2,3])
#find the output by yourself

#So run time will be O(n) + O(n) + O(n) = O(3n). Which is still O(n).
#because no matter how many times you multiply infinity it doesn't matter.


#example 2

def example_2(lst):
    print lst[0]  #O(1)
    half = len(lst)/2
    
    for i in lst[:half]:
        print i #O(n/2)
        
    for x in range(10):
        print('One to ten') #O(10)
        
example_2([1,2,3,4])
#find the output by yourself

#So the run time = O(1+n/2+10) = O(11+n/2). Which is still O(n)

#HappyCoding
