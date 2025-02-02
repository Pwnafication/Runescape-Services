# Example API function to simulate isBadVersion
def isBadVersion(version):
    # Replace `first_bad_version` with the first version that is "bad"
    first_bad_version = 4
    return version >= first_bad_version

def findFirstBadVersionGivenisBadVersionAPIFunction(n, isBadVersion):
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            if mid == 1 or not isBadVersion(mid - 1):
                return mid
            else:
                right = mid
        else:
            left = mid + 1
    return left

# Example call
n = 10  # Total versions
print(findFirstBadVersionGivenisBadVersionAPIFunction(n, isBadVersion))  # Output: 4
