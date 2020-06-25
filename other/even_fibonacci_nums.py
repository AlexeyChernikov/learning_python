fib1 = fib2 = 1
new_num = 0
sum_nums = 0

while new_num <= 4000000:
    new_num = fib1 + fib2
    
    if new_num % 2 == 0:
        sum_nums += new_num

    fib1, fib2 = fib2, new_num

print(sum_nums)