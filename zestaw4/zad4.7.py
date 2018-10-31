def flatten(sequence):
    flatList = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flatList += flatten(item)
        else:
            flatList.append(item)

    return flatList


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(seq))  # [1,2,3,4,5,6,7,8,9]
