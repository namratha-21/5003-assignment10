from itertools import zip_longest 
test_list = [1, 4, 4, 4, 5, 6, 7, 4, 3, 3, 9]  
print ("The original list is : " + str(test_list)) 
res = [i for i, j in zip_longest(test_list, test_list[1:])     if i != j]
print ("List after removing consecutive duplicates : " +  str(res)) 

