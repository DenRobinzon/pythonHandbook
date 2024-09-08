def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    numbers_sorted = []
    i_1 = i_2 = 0
    mid = len(numbers) // 2
    nums_1 = merge_sort(numbers[:mid])
    nums_2 = merge_sort(numbers[mid:])

    while i_1 < len(nums_1) and i_2 < len(nums_2):
        if nums_1[i_1] < nums_2[i_2]:
            numbers_sorted.append(nums_1[i_1])
            i_1 += 1
        else:
            numbers_sorted.append(nums_2[i_2])
            i_2 += 1
    numbers_sorted.extend((nums_1[i_1:] + nums_2[i_2:]))
    return numbers_sorted


print(merge_sort([3, 1, 5, 3]))