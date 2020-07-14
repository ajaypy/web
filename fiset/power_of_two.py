def get_powers_of_two(n):

    x = 1
    low, high = 0,1
    while x < n:
        x = x << 1
        low = high
        high = x
    if ((n & (n - 1) == 0) and n!= 0):
        high = high << 1
    print ("N:",n,"LOW:",low, "HI:",high)

get_powers_of_two(5)
get_powers_of_two(15)
get_powers_of_two(19)
get_powers_of_two(1)
get_powers_of_two(2)
get_powers_of_two(0)
get_powers_of_two(16)
