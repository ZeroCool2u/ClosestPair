__author__ = 'Theo Linnemann'

def closestPair():
    """

    :rtype : tuple
    """
    import random  #import random for use in generating our sorted list.
    sortedList = [] #init empty list
    randomlength = random.randint(10,50) #randomly generate the length of the sorted list between 10 & 50.
    while len(sortedList) < randomlength: #while loop creates concatenates a list of 1 element that is a random int.
        sortedList += [random.randint(0, 10000)] #Creates a list of 10<len(list)<50.

    sortedList.sort() #Sorts the set for processing.

    print(sortedList) #Prints the sorted set for sanity check.

    smallestdif = abs(sortedList[0] - sortedList[1]) #Inits the variable retaining the smallest difference.
    CP = (sortedList[0], sortedList[1]) #Inits the tuple containing the first 2 items in the list.
    for i in range(0, len(sortedList) - 1): #for loop executes the length of the list - 1.
        if smallestdif > abs(sortedList[i] - sortedList[i + 1]): #compares the current smallest difference to the next iteration.
            smallestdif = abs(sortedList[i] - sortedList[i + 1]) #Executes reassignment when new smallest difference is encountered.
            CP = (sortedList[i], sortedList[i+1]) #Reassigns the output tuple to the values used to calculate the new smallest difference.
    return CP, smallestdif #Returns a tuple of the form: ((cp value 1, cp value 2), difference between cpv1 and cpv 2.)

print(closestPair()) #Prints function output.