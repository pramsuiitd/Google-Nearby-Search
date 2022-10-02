class PointDatabase:
    def __init__(self, pointlist):
        """
        pointlist - list of 2 tuples, size n
        Time complexity - O(nlogn)
        """
        self.x_sort = sorted(pointlist)
        self.y_sort = sorted(pointlist, key = lambda x : x[1])

    def binary_search(self, val):
        return (0,0)

    def searchNearby(self, q, d):
        """
        Return - List of 2 tuples
        q - a 2 tuple, d - l_inf distance
        """
        i,j = self.binary_search(self.x_sort, q)

c = PointDatabase([(1,2),(3,4),(0,2),(2,7),(2,5)])