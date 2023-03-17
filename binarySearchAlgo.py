# A recurssive binary search alogirthm
def BinarySearch(search, start, end, target):
    # If the start is larger than the end, the program should end itself.
    if start > end:
        return -1
    
    # Define middle index value from start to end
    middle = (start + end) // 2
    
    # Check for middle being the target value and if it is, send the index number
    if target == search[middle]:
        return middle
    
    # Compare target value with series and rearrange new binary search
    # If the target is less than the middle value, we'll set a new series that ends at the value before the middle
    elif target < search[middle]:
        return BinarySearch(search, start, middle - 1, target)
    
    # If the condition is not met above, we'll make a new series that starts at the value after the middle
    else:
        return BinarySearch(search, middle + 1, end, target)

# This will run the code from above as long as it is called
if __name__ == "__main__":
    searchSeries = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target = 8
    start = 0
    end = len(searchSeries) - 1
    
    # This will test for target1 which will search for a number within the series
    index = BinarySearch(searchSeries, start, end, target)
    
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found in series")
