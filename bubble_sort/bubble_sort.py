def bubble_sort(unsorted_list):
    """
    Sorts a list using the bubble sort algorithm.
    
    Args:
        unsorted_list: List of comparable elements to sort
        
    Returns:
        A new sorted list in ascending order
    """
    # Create a copy to avoid modifying the original list
    sorted_list = unsorted_list.copy()
    n = len(sorted_list)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize - if no swapping occurs, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements and swap if they're in wrong order
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                swapped = True
        
        # If no swaps happened, the list is sorted
        if not swapped:
            break
    
    return sorted_list