n = int(input())
array = list(map(int, input()))

index_list = []
count = 0

for i in array:
    if i == 1:
        count += 1
    else:
        index_list.append(count)
        count += 1

def func1(n):
    result = 0  # 결과값
    n1 = n - 3  # 1칸의 개수를 저장하고 있는 변수
    n2 = 1  # 2칸의 개수를 저장하고 있는 변수
    if n % 2 == 1:  # n이 홀수일 때
        if n == 1:
            result = 1
            return result
        elif n == 3:
            result = n // 2 + n % 2
            return result
        else:
            while True:
                if n1 >= 2:
                    result += n1 + n2
                    n2 += 1
                    n1 -= 2
                else:
                    result += 2
                    return result
                    break
    else:  # n이 짝수일 때
        if n == 2:
            result = 1
            return result
        else:
            while True:
                if n1 >= 1:
                    result += n1 + n2
                    n2 += 1
                    n1 -= 2
                else:
                    result += 1
                    return result
                    break


if len(index_list) == 0:
    print(func1(n))
else:
    hh = 0
    all_result = 1
    for zero_index in index_list:
        if hh == 0:
            all_result *= func1(zero_index - hh)
            hh = zero_index + 1
        else:
            all_result *= func1(zero_index - hh)
            hh = zero_index + 1

    if zero_index < n-1:
        all_result *= func1(n - zero_index-1)
    print(all_result)

'''
3
1101
'''
