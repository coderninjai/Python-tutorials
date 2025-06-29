# # MAP

# # def cube (x):

# #     return x*x*x
# # print (cube(2))

# l=[1,3,4,5,8]

# cube =lambda x:x*x*x

# newl=[]
# # for item in l :
# #     newl.append(cube(item))

# # print (newl)

# newl=list(map(cube,l))

# print(newl)


# # filter 

# def filter_function (a):
#     return a>4

# newnewl =list(filter(filter_function,l))
# print(newnewl)


from functools import reduce

numbers=[1,2,3,4,5]

def mysum (x,y):
    return x+y
sum =reduce(mysum,numbers)

print(sum)