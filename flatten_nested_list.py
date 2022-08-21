# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list_obj = nestedList[:]
        self.iterator = None

    def next(self):
        """
        :rtype: int
        """
        if isinstance(self.iterator, int):
            return self.iterator
        else:
            # it is list
            if len(self.iterator) > 0:
                return self.iterator.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.list_obj.isInteger():
            self.iterator = self.list_obj.getInteger()
        else:
            if self.list_obj.getList():
                self.iterator = self.list_obj.getList()
            else:
                return False
        return True


# Your NestedIterator object will be instantiated and called as such:
nestedList = [[1, 1], 2, [1, 1]]
i, v = NestedIterator(nestedList), []
while i.hasNext():
    v.append(i.next())
