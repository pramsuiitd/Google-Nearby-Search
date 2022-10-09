"""
Idea ->
Create a x-range tree, how so ever
Then at every point store a sorted array -> in y(By merging bottom down), as well as the faster lookup array
Now create a faster lookup binary search at each of the locations
"""
class Node:
    def __init__(self, val, is_leaf, x_range) -> None:
        self._is_leaf = is_leaf
        self._val = val
        self._left = None
        self._right = None
        self._y_sort = None
        self._y_execution_list = None #This is smaller (n)^1/2 list
        self._x_range = x_range
        
    def printNode(self):
        print(self._val)
        print(self._y_sort)
        print(self._x_range)
        if not self._is_leaf:
            print(self._left._val)
            print(self._right._val)

class PointDatabase:
    def __init__(self, pointlist):
        """
        pointlist - list of 2 tuples, size n
        Time complexity - O(nlogn)
        """
        self.sorted_x_list = sorted(pointlist, key = lambda x : x[0])
        self.sorted_y_list = sorted(pointlist, key = lambda x : x[1])
        self._range_tree = self.BuildXTree(0,len(self.sorted_x_list)-1)
        self._answer = []

    def BuildXTree(self, l, r):
        # Terminating Condition
        if l == r:
            val = self.sorted_x_list[l]
            c = Node(val,True, (val[0],val[0]))
            c._y_sort = [self.sorted_x_list[l]]
            # c.printNode()
            return c

        if l > r : return

        median = (r + l)//2
        c = Node(self.sorted_x_list[median],False,(self.sorted_x_list[l][0],self.sorted_x_list[r][0]))
        c._left = self.BuildXTree(l,median)
        c._right = self.BuildXTree(median+1,r)
        c._y_sort = self.merge_list(c._left._y_sort, c._right._y_sort)
        # c.printNode()
        return c

    def searchRange(self, l, r, arr):
        # Sanity check
        if(arr[0][1] > r):
            return (-1,-1)
        if(arr[len(arr)-1][1] < l):
            return (-1,-1)
        
        # Binary search for l
        start,end = 0,len(arr) - 1
        left_limit = -1
        while (start <= end):
            mid = (start + end) // 2
    
            # Move to right side if target is
            # greater.
            if (arr[mid][1] < l):
                start = mid + 1
    
            # Move left side.
            else:
                left_limit = mid
                end = mid - 1

        # Binary search for r
        start,end = 0,len(arr) - 1
        right_limit = -1
        while(start <= end):
            mid = (start + end) // 2
    
            # Move to left side if target is
            # smaller.
            if (arr[mid][1] > r):
                end = mid - 1
    
            # Move left side.
            else:
                right_limit = mid
                start = mid + 1
        return (left_limit,right_limit)

    def merge_list(self, arr1, arr2):
        n1,n2 = len(arr1), len(arr2)
        arr3 = [None] * (n1 + n2)
        i,j,k = 0,0,0
        while i < n1 and j < n2:
            if arr1[i][1] < arr2[j][1]:
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
        return arr3


    def searchNearbyHelper(self,rX,rY,ptr):
        
        pass

    def searchNearby(self, q, d):
        """
        Return - List of 2 tuples
        q - a 2 tuple, d - l_inf distance
        """
        search_range_x = (q[0]-d, q[0]-d)
        search_range_y = (q[1]-d, q[1]-d)
        self._answer = []
        self.searchNearbyHelper(search_range_x,search_range_y,self._range_tree)
        return self._answer


if __name__ == '__main__':
    # c = PointDatabase([(1,2),(3,4),(0,2),(4,7),(2,5)])
    c = PointDatabase([(1,1),(3,3),(0,0),(4,4),(2,2)])
    # print(c.searchRange(5,9,[(1,2),(3,3),(0,4),(2,5),(2,7)]))
    # print(c.merge_list([(1,5),(6,6),(3,7)],[(1,2),(3,3),(0,4),(2,5),(2,7)]))
    d = PointDatabase([])
    x = c._range_tree
    print(x._val,x._x_range,";", x._left._val,x._left._x_range,";",x._right._val, x._right._x_range)
    x = x._left
    print(x._left._val,x._left._x_range,";",x._right._val, x._right._x_range)
    x = x._left
    print(x._left._val,x._left._x_range,";",x._right._val, x._right._x_range)
    x = c._range_tree._right
    print(x._left._val,x._left._x_range,";",x._right._val, x._right._x_range)