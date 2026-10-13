# Sample array for the range sum queries.
a = [2, -1, 7, 2, -3, -2, 4]


def range_sum_query(a, l, r):
    sum = 0

    # Include the left boundary and exclude the right boundary.
    for i in range(l, r):
        sum = sum + a[i]
    return sum


# Read the boundaries as array indices starting at 0.
l = int(input("Enter left boundary: "))
r = int(input("Enter right boundary: "))

print("Range Sum Query:", range_sum_query(a, l, r))
