
'''
Sets:
initialized as
mySet = set()

sets store values but if you try to add a value to a set thats already in there,
it wont do shit

also the order of items in a set doesnt matter

unlike lists, where order matters and u can have duplicates

to add num to a set, do mySet.add(num)

we want to find intersection of sets, NOT Union

t convert a list to a set, mySet = set(myList)

to do intersection, intersectionSet = SetA.intersection(setB)
'''

def listIntersection():
    list1 = [3,1,1,2,10,12,17]
    list2 = [1,2,3,10,18,21,0,2]

    mySet1 = set(list1)
    mySet2 = set(list2)

    mySet3 = mySet1.intersection(mySet2)

    myList3 = list(mySet3)

    print(myList3)
