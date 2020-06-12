def search():
    nums = []

    for i in range(999, 99, -1):
        if i % 10 == 0:
            continue

        for j in range(i, 99, -1):
            num = str(i * j)

            if num == num[::-1]:
                nums.append(int(num))
                break

    return nums


print(max(search()))