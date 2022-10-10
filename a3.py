"""
Create a x-range tree
Then at every point store a sorted array -> in y(By merging bottom down), as well as the faster lookup array
Now create a faster lookup binary search at each of the locations
"""
class Node:
    def __init__(self, val, is_leaf, x_range) -> None:
        self._is_leaf, self._val, self._x_range = is_leaf, val, x_range
        self._left, self._right, self._y_sort = None, None, None
        
    def printNode(self):
        print(self._val, self._y_sort, self._x_range)
        if not self._is_leaf: print(self._left._val, self._right._val)

class PointDatabase:
    def __init__(self, pointlist):
        self.sorted_x_list = sorted(pointlist)
        self._range_tree = self.BuildXTree(0,len(self.sorted_x_list)-1)
        self._answer = []

    def BuildXTree(self, l, r):
        if l == r: # Terminating Condition
            val = self.sorted_x_list[l]
            c = Node(val,True,(val[0],val[0]))
            c._y_sort = [val]
            return c

        if l > r : return # Safe Check

        median = (r + l)//2
        x_list = self.sorted_x_list
        c = Node(x_list[median],False,(x_list[l][0],x_list[r][0]))
        c._left, c._right = self.BuildXTree(l,median), self.BuildXTree(median+1,r)
        c._y_sort = self.merge_list(c._left._y_sort, c._right._y_sort)
        return c

    def searchRange(self, range, arr):
        l,r = range[0],range[1] # Sanity check
        if(arr[0][1] > r): return (-1,-1)
        if(arr[len(arr)-1][1] < l): return (-1,-1)

        start, end, left_limit = 0,len(arr) - 1, -1 # Binary search for l
        while (start <= end):
            mid = (start + end) // 2
            if (arr[mid][1] < l): start = mid + 1
            else: left_limit, end = mid, mid - 1

        start, end, right_limit = 0,len(arr) - 1, -1 # Binary search for r
        while(start <= end):
            mid = (start + end) // 2
            if (arr[mid][1] > r): end = mid - 1
            else: right_limit, start = mid, mid + 1
        return (left_limit,right_limit)

    def merge_list(self, arr1, arr2):
        n1,n2 = len(arr1), len(arr2)
        arr3 = [None] * (n1 + n2)
        i,j,k = 0,0,0
        while i < n1 and j < n2:
            if arr1[i][1] < arr2[j][1]:
                arr3[k] = arr1[i]
                k, i = k + 1, i + 1
            else:
                arr3[k] = arr2[j]
                k, j = k + 1, j + 1

        while i < n1:
            arr3[k] = arr1[i]
            k, i = k + 1, i + 1

        while j < n2:
            arr3[k] = arr2[j]
            k, j = k + 1, j + 1
        return arr3

    def searchNearbyHelper(self,rX,rY,ptr: Node):
        if ptr._is_leaf:
            # Guard method to avoid nested if-else
            if ptr._val[0] < rX[0] or ptr._val[0] > rX[1]: return
            if ptr._val[1] < rY[0] or ptr._val[1] > rY[1]: return
            self._answer.append(ptr._val)
            return
        if ptr._x_range[1] < rX[0] or ptr._x_range[0] > rX[1]: return # Completly outside
        
        if ptr._x_range[0] >= rX[0] and ptr._x_range[1] <= rX[1]: # Completly inside
            l,r = self.searchRange(rY,ptr._y_sort)
            if l == -1 or r == -1: return
            for i in range(l,r+1): self._answer.append(ptr._y_sort[i])
            return

        self.searchNearbyHelper(rX,rY,ptr._left) # Intersection
        self.searchNearbyHelper(rX, rY, ptr._right)
        return

    def searchNearby(self, q, d):
        if self._range_tree == None:
            return []
        search_range_x = (q[0]-d, q[0]+d)
        search_range_y = (q[1]-d, q[1]+d)
        self._answer = []
        self.searchNearbyHelper(search_range_x,search_range_y,self._range_tree)
        return self._answer

if __name__ == '__main__':
    # c = PointDatabase([(1,2),(3,4),(0,2),(4,7),(2,5)])
    c = PointDatabase([(1,1),(3,3),(0,0),(4,4),(2,2)])
    # print(c.searchRange(5,9,[(1,2),(3,3),(0,4),(2,5),(2,7)]))
    # print(c.merge_list([(1,5),(6,6),(3,7)],[(1,2),(3,3),(0,4),(2,5),(2,7)]))
    d = PointDatabase([(1,5)])
    print(d.searchNearby((2,4),0.6))
    # x = c._range_tree
    # print(x._val,x._x_range,";", x._left._val,x._left._x_range,";",x._right._val, x._right._x_range)
    # x = x._left
    # print(x._left._val,x._left._x_range,";",x._right._val, x._right._x_range)
    # x = x._left
    # print(x._left._val,x._left._x_range,";",x._right._val, x._right._x_range)
    # x = c._range_tree._right
    # print(x._left._val,x._left._x_range,";",x._right._val, x._right._x_range)
    pointDbObject = PointDatabase([(1,6), (2,4), (3,7), (4,9), (5,1), (6,3), (7,8), (8,10), (9,2), (10,5)])
    print(pointDbObject.searchNearby((5,5), 1))
    print(pointDbObject.searchNearby((4,8), 2))
    print(pointDbObject.searchNearby((10,2), 1.5))