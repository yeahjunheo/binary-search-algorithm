# This is an attempt to make an iterative version of the binary search algorithm
def BinarySearch(search, target):
    
    # Set initial index for start and end
    start = 0
    end = len(search) - 1
    
    # Set it so that the loop will keep running until the value is found or start is greater than end
    while start <= end:
        
        # Set middle value for searching
        middle = (start + end) // 2
        
        # Check if the middle value is equal to the target value
        if target == search[middle]:
            return middle
        
        # If not, proceed to get rid of parts we know for sure won't contain the target value
        elif target < search[middle]:
            end = middle - 1
        else:
            start = middle + 1
            
    # If no value is found, then return not found
    return -1

# Just to keep note of which function we want running when we debug
if __name__ == "__main__":
    searchSeries = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target = 15
    
    index = BinarySearch(searchSeries, target)
    
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found in series")
