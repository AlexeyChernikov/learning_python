def search():
    nums = []

    i = 999
    while i > 99:
        if i % 10 == 0:
            i -= 1
            continue

        j = 999
        while j > 99:
            if j % 10 == 0:
                j -= 1
                continue

            num = str(i * j)
            if num == num[::-1]:
                nums.append(int(num))
                break
            j -= 1
        i -= 1

    return nums


print(max(search()))