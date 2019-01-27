# Python program to find maximum sum path

# This function returns the sum of elements on maximum path from
# beginning to end
def maxPathSum(ar1, ar2, m, n):
    # initialize indexes for ar1[] and ar2[]
    i, j = 0, 0

    # Initialize result and current sum through ar1[] and ar2[]
    result, sum1, sum2 = 0, 0, 0

    # Below 3 loops are similar to merge in merge sort
    while (i < m and j < n):

        # Add elements of ar1[] to sum1
        if ar1[i] < ar2[j]:
            sum1 += ar1[i]
            i += 1

        # Add elements of ar2[] to sum1
        elif ar1[i] > ar2[j]:
            sum2 += ar2[j]
            j += 1

        else:  # we reached a common point

            # Take the maximum of two sums and add to result
            result += max(sum1, sum2)

            # Update sum1 and sum2 for elements after this intersection point
            sum1, sum2 = 0, 0

            # Keep updating result while there are more common elements
            while (i < m and j < n and ar1[i] == ar2[j]):
                result += ar1[i]
                i += 1
                j += 1

    # Add remaining elements of ar1[]
    while i < m:
        sum1 += ar1[i]
        i += 1
    # Add remaining elements of b[]
    while j < n:
        sum2 += ar2[j]
        j += 1

    # Add maximum of two sums of remaining elements
    result += max(sum1, sum2)

    return result


# Driver function
size1 = int(input())
n1= input()
n1 = n1.strip()
b1 = n1.split(" ")
for i in range(0, size1):
    b1[i] = int(b1[i])
size2 = int(input())
n2 = input()
n2 = n2.strip()
b2 = n2.split(" ")
for i in range(0, size2):
    b2[i] = int(b2[i])
b1.sort()
b2.sort()
print(maxPathSum(b1,b2,len(b1),len(b2)))
