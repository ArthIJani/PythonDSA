"""
Bubble Sort
Time Complexity
Best Case : O(n)
Worst Case : O(n^2)
"""

def bubble(l):
    for i in range(len(l)):
        swapped = False
        for j in range(1,len(l)-i):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1],l[j]
                swapped = True
        if not swapped:
            break
    return l
            

l = [2,1,5,3,4,8,7,0,6]
ans = bubble(l)
print(ans)
