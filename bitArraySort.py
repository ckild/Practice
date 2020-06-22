# Given a bit array, return it sorted in-place (a bit array is simply an array that contains only bits, either a 1 or a 0).
#
# See if you can solve this in O(N) time and O(1) auxiliary space.

def bitArraySort(n):
    left, right = 0, len(n)-1

    while left < right:
        if n[left] > n[right]:
            n[left], n[right] = n[right], n[left]
            left += 1
