# Test Case for MR 1
def merge_sort(collection):
    if len(collection) <= 1:
        return collection
    mid_index = len(collection) // 2
    left = merge_sort(collection[:mid_index])
    right = merge_sort(collection[mid_index:])
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

source_input = [4, 2, 7, 1, 3]
source_output = merge_sort(source_input)
follow_up_input = source_output
follow_up_output = merge_sort(follow_up_input)
print(source_output == follow_up_output)  # Output: True
