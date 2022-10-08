"""
Idea ->
Create a x-range tree, how so ever
Then at every point store a sorted array -> in y(By merging bottom down), as well as the faster lookup array
Now create a faster lookup binary search at each of the locations
"""

class Node:
    def __init__(self, val, is_leaf) -> None:
        self._is_leaf = is_leaf
        self._val = val
        self._left = None
        self._right = None
        self._y_sort = None
        self._y_execution_list = None #This is smaller (n)^1/2 list 
        pass

class PointDatabase:
    def __init__(self, pointlist):
        """
        pointlist - list of 2 tuples, size n
        Time complexity - O(nlogn)
        """
        sorted_x_list = sorted(pointlist, key = lambda x : x[0])
        sorted_y_list = sorted(pointlist, key = lambda x : x[1])
        self._range_tree = self.BuildXTree(sorted_x_list, sorted_y_list)

    def BuildXTree(self, l_x, l_y):
        pass

    def merge_list(self, arr1, arr2):
        n1,n2 = len(arr1), len(arr2)
        arr3 = [None] * (n1 + n2)
        i,j,k = 0,0,0
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                arr3[k] = arr1[i]
                k = k + 1
                i = i + 1
            else:
                arr3[k] = arr2[j]
                k = k + 1
                j = j + 1

        while i < n1:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1

        while j < n2:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1

    def searchNearby(self, q, d):
        """
        Return - List of 2 tuples
        q - a 2 tuple, d - l_inf distance
        """
        pass


if __name__ == '__main__':
    c = PointDatabase([(1,2),(3,4),(0,2),(2,7),(2,5)])