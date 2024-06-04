# Write a Python function to reverse a list at a specific location.


def list_reverser(lst, PointOfReversal):
    new_list = []
    for i, x in enumerate(lst):
        if i < PointOfReversal:
            new_list.append(lst[i])
    new_list.reverse()
    new_list = new_list + lst[PointOfReversal:]
    print(new_list)

    return

'''was not able to finsih this code
def longest_subsequence(lst):
    new_list = []
    final_lst = []
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            #print(i)
            new_list.append(i)
    print(new_list)
    return

longest_subsequence([1, 2, 3, 2, 1, 3, 4, 7])'''


def list_permutations(lst):
    from itertools import permutations
    lst_of_perms = []
    # Get all permutations of [1, 2, 3]
    perm = permutations(lst)

    # Print the obtained permutations
    for i in list(perm):
        lst_of_perms.append(i)
    print(lst_of_perms)
    return


def permutations(nums):
    # Base case: If the input list is empty, return an empty list as there are no permutations.
    if len(nums) == 0:
        return []
    # Base case: If the input list has only one element, return a list containing that element as the only permutation.
    if len(nums) == 1:
        return [nums]
    # Initialize an empty list 'result' to store permutations.
    result = []
    # Iterate over the elements of the input list.
    for i in range(len(nums)):
        # Select an element 'm' at index 'i'.
        m = nums[i]
        # Create a new list 'rem_list' that contains all elements except 'm'.
        rem_list = nums[:i] + nums[i+1:]
        # Recursively find permutations of 'rem_list'.
        for p in permutations(rem_list):
            # Add 'm' to the beginning of each permutation in 'p' and append it to the 'result' list.
            result.append([m] + p)
    # Return the list of all permutations.
    return result

# Create a list of numbers
nums = [1, 2, 3, 4]

# Print the original list
print("Original list:")
print(nums)


# Call the permutations function and print the result, which is a list of all permutations of 'nums'.
print("Permutations of the members of the said list:")
print(permutations(nums))