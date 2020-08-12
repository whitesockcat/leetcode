from math import sqrt
import copy

def isPrimes(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for x in range(3, int(sqrt(n) + 1), 2):
            if n % x == 0:
                return False
        return True
    return False

def is_prime(n):
    '''
    此法算大于100的会出错 eg:121
    '''
    if n>1:
        if n == 2 or n == 3: # 小于5且大于1的数中，只有2和3是质数
            return True
        # n = 6x+1 或 n = 6x+5 (6x-1), 质数一定在6倍数的两侧
        elif n % 6 == 1 or n % 6 ==5:
            # 去掉5和7的倍数
            if n % 5 !=0 and n % 7 !=0:
                return True
    return False


def listPrimes(n):
    if n < 3:
        if n == 2:
            return [2]
        return None
    num_list = [x for x in range(2, n) if x%2 != 0]
    new_list = copy.copy(num_list)
    # new_list = []
    for i in num_list:
        # new_list.append(i)
        for d in range(3, int(sqrt(i)) + 1,2):
            if i%d == 0:
                new_list.remove(i)
                break
    return [2] + new_list