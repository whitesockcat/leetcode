
import sys
data = sys.stdin.readline().strip().split()[0]
 
data_length = len(data)
result = 0
str_data = ['0','1','2','3','4','5','6','7','8','9']
flag = 1
if data[0] == '+':
    data = data[1:]
elif data[0] == '-':
    flag = -1
    data = data[1:]
for i in data:
    assert i in str_data
    num = str_data.index(i)
    result *= 10
    result  += num
print(result*flag)