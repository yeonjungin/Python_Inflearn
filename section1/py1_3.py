'''
Chpater1
Shallow copy & deep copy
'''

# 객체의 복사 종류 : copy, shallow copy, deep copy
# 가변 : list, set, dict

# Ex1 - copy (주소값을 공유)
# Call by value, Call by Refference, Call by Share

a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list

print('Ex1 >', id(a_list))
print('Ex1 >', id(b_list))

# 같은 값을 참조하고 있다.

b_list[2] = 100
print('Ex1 >', a_list)
print('Ex1 >', b_list)

# imutable : int, str, float , bool, unicode (불변형)

# Ex2 - shallow copy (얕은 복사)
import copy

c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)

print('EX2 > ', id(c_list))
print('EX2 > ', id(d_list))
# 주소 값이 다름. (같은 주소를 공유하지 않는다)

d_list[1] = 100
print('EX2 > ', c_list)
print('EX2 > ', d_list)
# d_list의 값만 변경됌

d_list[3].append(1000)
d_list[4][1] = 10000

print('EX2 > ', c_list)
print('EX2 > ', d_list)
# 첫 번째 리스트는 주소값을 서로 다르게 하지만, 이 안에 있는 리스트는 주소값을 서로 공유
# 세부 안에 있는 리스트는 복제하지 않음, 같은 참조

# Ex3 - deep copy (깊은 복사)
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)

print('EX3 > ', id(e_list))
print('EX3 > ', id(f_list))

f_list[3].append(2000)
f_list[4][1] = 20000

print('EX3 > ', e_list)
print('EX3 > ', f_list)

# 내부 요소까지 깊은 복사가 이루어졌다.
