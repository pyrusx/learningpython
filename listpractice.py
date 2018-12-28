def replace():
    myArray = [3,2,1,5,2,3,1,2,1,12,4,4,31,321]

    newNumber = int(input('Type in a number that you want to replace in the original array. \n'))

    index = 0
    while index < len(myArray):
        if myArray[index] == newNumber:
            myArray[index] = -1
            
        index = index + 1

    print(myArray)


def lessThanWithInput():
    # problem 2: given a user input
    # create a list of elements that are less than the inputted number, out of a given list
    # dont just print the elements less than the number, but make a new list of them

    '''
    to create a new list: newList = []
    newList.append(num)
    '''

    myList = [10,5,100,25, 0, 10]
    maxNumber = int(input('Type a number to find the elements in the list smaller than it. \n'))
    newList = []

    for currentNum in myList:
        if maxNumber > currentNum:
            newList.append(currentNum)

    print(newList)

def lessthan():
    myList = [1,3,4,2,5,12,134,4,53,34]
    for i in myList: 
        if i < 10:
            print(i)  


def findmin():
                
    myArray = [5,3,34,234,2,41,455342,342]

    smallNumber = 10000000000000000000000000000000000
    for currentNum in myArray:
        if currentNum < smallNumber:
            smallNumber = currentNum

    print(smallNumber)


def commonItems():
    list1 = [3,1,1,2,10,12,17]
    list2 = [1,2,3,10,18,21,0,2]
    list3 = []
    for currentNum1 in list1:
        for currentNum2 in list2:
            if currentNum1 == currentNum2 and currentNum1 not in list3:
                list3.append(currentNum1)

    print(list3)