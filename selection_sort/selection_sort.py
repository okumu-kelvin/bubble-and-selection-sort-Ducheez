def selection_sort(arr):
    """
    Sorts a list using the selection sort algorithm.
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        A new sorted list in ascending order
    """
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        
        for j in range(i + 1, n):
            # If we find a smaller element, update min_index
            if sorted_arr[j] < sorted_arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        sorted_arr[i], sorted_arr[min_index] = sorted_arr[min_index], sorted_arr[i]
    
    return sorted_arr