from collections import Counter

def isSubset(a1, a2, n, m):
    # Count occurrences of elements in both arrays
    count_a1 = Counter(a1)
    count_a2 = Counter(a2)

    # Check if counts of elements in a2 are less than or equal to counts in a1
    for key in count_a2:
        if count_a2[key] > count_a1[key]:
            return "No"  # If any count exceeds, a2 is not a subset of a1

    return "Yes"


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1