import unittest

class MiniPriorityQueue:
    def __init__(self):
        self.heapArray = [(0, 0)]
        self.currentSize = 0

    def buildHeap(self, alist):
        self.currentSize = len(alist)
        self.heapArray = [(0, 0)] + alist[:]
        i = len(alist) // 2
        while i > 0:
            self.percDown(i)
            i -= 1

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if mc == -1:  # 如果没有孩子，直接返回
                break
            if self.heapArray[i][0] > self.heapArray[mc][0]:
                self.heapArray[i], self.heapArray[mc] = self.heapArray[mc], self.heapArray[i]
            i = mc

    def minChild(self, i):
        if i * 2 > self.currentSize:
            return -1
        elif i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapArray[i * 2][0] < self.heapArray[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i // 2][0]:
                self.heapArray[i], self.heapArray[i // 2] = self.heapArray[i // 2], self.heapArray[i]
            i //= 2

    def add(self, k, order):
        self.heapArray.append((k, order))
        self.currentSize += 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize -= 1
        self.heapArray.pop()
        self.percDown(1)
        return retval

    def isEmpty(self):
        return self.currentSize == 0

    def decreaseKey(self, val, amt):
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i += 1
        if myKey > 0:
            self.heapArray[myKey] = (amt, self.heapArray[myKey][1])
            self.percUp(myKey)

    def __contains__(self, vtx):
        return any(pair[1] == vtx for pair in self.heapArray)

    def check_first(self):
        return self.heapArray[1][1]

    def traverse(self):
        return [pair[1] for pair in self.heapArray[1:]]


class MaxPriorityQueue:
    def __init__(self):
        self.heapArray = [(0, 0)]
        self.currentSize = 0

    def buildHeap(self, alist):
        self.currentSize = len(alist)
        self.heapArray = [(0, 0)] + alist[:]
        i = len(alist) // 2
        while i > 0:
            self.percDown(i)
            i -= 1

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if mc == -1:  # 如果没有孩子，直接返回
                break
            if self.heapArray[i][0] < self.heapArray[mc][0]:
                self.heapArray[i], self.heapArray[mc] = self.heapArray[mc], self.heapArray[i]
            i = mc

    def maxChild(self, i):
        if i * 2 > self.currentSize:
            return -1
        elif i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapArray[i * 2][0] > self.heapArray[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapArray[i][0] > self.heapArray[i // 2][0]:
                self.heapArray[i], self.heapArray[i // 2] = self.heapArray[i // 2], self.heapArray[i]
            i //= 2

    def add(self, k, order):
        self.heapArray.append((k, order))
        self.currentSize += 1
        self.percUp(self.currentSize)

    def delMax(self):
        retval = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize -= 1
        self.heapArray.pop()
        self.percDown(1)
        return retval

    def isEmpty(self):
        return self.currentSize == 0

    def decreaseKey(self, val, amt):
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i += 1
        if myKey > 0:
            self.heapArray[myKey] = (amt, self.heapArray[myKey][1])
            self.percUp(myKey)

    def __contains__(self, vtx):
        return any(pair[1] == vtx for pair in self.heapArray)

    def check_first(self):
        return self.heapArray[1][1]

    def traverse(self):
        return [pair[1] for pair in self.heapArray[1:]]

# 单元测试
class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.minPQ = MiniPriorityQueue()
        self.maxPQ = MaxPriorityQueue()

    def test_min_pq(self):
        self.minPQ.add(3, "task1")
        self.minPQ.add(1, "task2")
        self.minPQ.add(2, "task3")
        self.assertEqual(self.minPQ.delMin(), "task2")
        self.assertEqual(self.minPQ.delMin(), "task3")
        self.assertEqual(self.minPQ.delMin(), "task1")
        self.assertTrue(self.minPQ.isEmpty())

    def test_max_pq(self):
        self.maxPQ.add(1, "task1")
        self.maxPQ.add(3, "task2")
        self.maxPQ.add(2, "task3")
        self.assertEqual(self.maxPQ.delMax(), "task2")
        self.assertEqual(self.maxPQ.delMax(), "task3")
        self.assertEqual(self.maxPQ.delMax(), "task1")
        self.assertTrue(self.maxPQ.isEmpty())

if __name__ == "__main__":
    unittest.main()
