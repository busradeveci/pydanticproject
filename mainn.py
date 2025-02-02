import time


def my_func_1():
    print(f"first function starts.")
    time.sleep(5)
    print(f"firs function ends.")
    return 5  #x degeri 5 olacak.

def my_func_2():
    print(f"second function starts.")
    time.sleep(5)
    print(f"second function ends.")
    return 10  #y degeri 10 olacak.

if __name__ == '__main__':
    x = my_func_1()
    y = my_func_2()

    print(f"my function 1's working result x's value {x}")
    print(f"my function 2's working result y's value {y}")