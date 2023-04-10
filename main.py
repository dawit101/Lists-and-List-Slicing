#Lists 
#list is a form of array, which is a collection of data
#List is a data structure, whic is a way to organize info and data.

li = [1, #you can also write a list going down instead
      2,
      3,
      4,
      5
] 
li2 = ['a', 'b', 'c']
li3 = [1,2,'a',True]
#Lines 5-13 are all different ways to write a list

amazon_cart = ['iPad','notebook']

print(amazon_cart[0]) #list starts from 0 not 1
print(amazon_cart[1])

print('----------------------')

#List Slicing
#Which is the same as string slicing, [0:1:2] 0 = starting point, 1 = stop before and 2 = stepover

walmartList = [ 'catfood','fishtank','xbox','toothbrush']

print(walmartList[0:2])
print(walmartList[0::2])

print('----------------------')

walmartList[0] = 'laptop' #this changes the catfood to laptop
print(walmartList[1:3])
print(walmartList)

print('----------------------')

targetList = ['catfood','fishtank','xbox','toothbrush']

targetList[0] = 'laptop'
newList = targetList[:] #use list slicing to copy the targetList to equal newList, so targetList stays the same and newList is now something different due to input in line 42
newList[0] = 'gum'
print(newList)
print(targetList)

print('----------------------')
#List slicing practice
#Return the answers b, b, ['b','c'], ['z','b','c'], ['z','2','3'], [1,2,3,5]

alist = ['a','b','c']

print(alist[1]) #b
print(alist[1]) #b
print(alist[1:3]) #b,c
alist[0] = 'z'
print(alist[0:3]) #z,b,c
alist[1] = 2
alist[2] = 3
print(alist)
list = [1,2,3,5]
print(list)


