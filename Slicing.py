my_list = [0, 1,2,3,4,5,6,7,8,9]
#         0,1,2,3,4,5,6,7,8,9
#         -1,-2,-3,-4,-5,-6,-7,-8,-9

#list[start:end:step]

print (my_list[3:8])
print (my_list[:-1])
# means ignore this line in python and it works like a comment

print (my_list[2:-1:2])
#out of three numbers provided above inside the mylist brackets
#1st stands for starting number
#2nd stands for ending number
#3rd stands for the gap between numbers
print (my_list[-1:2:-1])
#negative numbers mean the order from right to left (in the first two)(3rd is the command to go backward in 1 dighit)



sample ='Paris Saint Germain'

#reverse string
print(sample[::-1])
#get the last word
print(sample[-7:])
#write without paris
print(sample[5:])
#write the saint alone
print(sample[5:11])
print(sample[5:-7])#these both are same output