import unittest
def merge_sort(arr):
    """ Merge Sort
        Complexity: O(n log(n))
    """
    # Our recursive base case
    if len(arr)<= 1:
        return arr
    mid = len(arr)//2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[mid:]), merge_sort(arr[:mid])

    # Merge each side together
    return merge(left, right)

def merge(left, right):
    """ Merge helper
        Complexity: O(n)
    """
    arr = []
    left_cursor, right_cursor = 0,0
    while left_cursor < len(left) and right_cursor < len(right):
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            arr.append(left[left_cursor])
            left_cursor+=1
        else:
            arr.append(right[right_cursor])
            right_cursor+=1
   # Add the left overs if there's any left to the result
    for i in range(left_cursor,len(left)):
        arr.append(left[i])
    for i in range(right_cursor,len(right)):
        arr.append(right[i])

   # Return result
    return arr

class TestSuite(unittest.TestCase):
    """
        test suite for the function (above)
    """
    def test_merge_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         merge_sort([1, 5, 65, 23, 57, 1232]))
if __name__ == "__main__":
    unittest.main()
