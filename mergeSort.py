#Goal: Sort an array called "nums" which has n integers: num[0...n-1]
#Merge sort
    
def mergeAux(inputArray, startIndex, endIndex):
    # Base Case: If the array size = 0 or 1 then no action required.
    if startIndex >= endIndex:
        return
        
    # Recursive logic
    # Find mid point of the array
    midIndex = (startIndex + endIndex)//2 # // is to avoid RecursionError: maximum recursion depth exceeded in comparison
    """Call recursive function to Sort left array"""
    mergeAux(inputArray, startIndex, midIndex)
    """Call recursive function to Sort Right array"""
    mergeAux(inputArray, midIndex+1, endIndex)
        
    # Merge the two sorted arrays 
    s = startIndex
    m = midIndex+1
        
    aux = []        
    while s <= midIndex and m <= endIndex:
        if inputArray[s] <= inputArray[m]:
            aux.append(inputArray[s])
            s += 1
        elif inputArray[m] < inputArray[s]:
            aux.append(inputArray[m])
            m += 1
    while s <= midIndex:
        aux.append(inputArray[s])
        s += 1
    while m <= endIndex:
        aux.append(inputArray[m])
        m += 1
            
        
    inputArray[startIndex:endIndex+1] = aux
    return aux

def mergeSort(arr):
    mergeAux(arr, 0, len(arr)-1)
    return arr



# print(mergeSort([3,4,6,22,8,1,2,9,1]))
