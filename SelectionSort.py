"""
Selection Sort
Time Complexity
Best Case : O(n^2)
Worst Case : O(n^2)
"""

def selection(l):
    for i in range(len(l)):
        last = len(l)-i-1
        maxIndex = getMaxIndex(l, 0, last)
        swap(l, maxIndex, last)
    return l

def swap(l, first, second):
    l[first], l[second] = l[second], l[first]

def getMaxIndex(l, start, end):
    max = start
    for i in range(start, end):
        if l[max] < l[i]:
            max = i
    return max

if __name__ == "__main__":
    l = [5, 3, 4, 1, 2]
    ans = selection(l)
    print(ans)