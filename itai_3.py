def three_times_number(lst):
    dict = {}
    for num in lst:
        if num in dict:
            dict[num] += 1
            if dict[num] == 3:
                return num
        else:
            dict[num] = 1
    return "There isn't such a number in this list"
print(three_times_number([]))
