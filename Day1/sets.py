def contains_duplicate_iterative(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def contains_duplicate_pythonic(nums):
    return len(set(nums)) != len(nums)

def main():
    # Example Usage:
    nums1 = [6, 6, 8, 11]
    print(f"Nums: {nums1}, Contains Duplicate (Iterative): {contains_duplicate_iterative(nums1)}") # Expected: True
    print(f"Nums: {nums1}, Contains Duplicate (Pythonic): {contains_duplicate_pythonic(nums1)}") # Expected: True

    nums2 = [6, 8, 10, 11]
    print(f"Nums: {nums2}, Contains Duplicate (Iterative): {contains_duplicate_iterative(nums2)}") # Expected: False
    print(f"Nums: {nums2}, Contains Duplicate (Pythonic): {contains_duplicate_pythonic(nums2)}") # Expected: False

    nums3 = []
    print(f"Nums: {nums3}, Contains Duplicate (Iterative): {contains_duplicate_iterative(nums3)}") # Expected: False
    print(f"Nums: {nums3}, Contains Duplicate (Pythonic): {contains_duplicate_pythonic(nums3)}") # Expected: False

if __name__=="__main__":
    main()