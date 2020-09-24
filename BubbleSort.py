books = {"GOT": 2001, "LOTR": 1976, "Inferno": 1983}
myList = list(books.values())
def bubbleSort(myList):
    for i in range (1, len(myList)):
        for j in range (len(myList) - i):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList


print(bubbleSort(myList))
