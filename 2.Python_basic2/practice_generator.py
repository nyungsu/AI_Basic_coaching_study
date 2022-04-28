#https://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A0%9C%EB%84%88%EB%A0%88%EC%9D%B4%ED%84%B0-


# def square_numbers(nums):
#     for i in nums:
#         yield i*i


# my_nums1 = square_numbers([1,2,3,4,5])

# print(next(my_nums1))
# print(next(my_nums1))
# print(next(my_nums1))
# print(next(my_nums1))
# print(next(my_nums1))
# print(next(my_nums1))

'''
갯수를 넘어가면 stopiteration이라는 예외가 발생하며
프로그램이 죽는다
'''

my_nums2 = (x*x for x in [1,2,3,4,5])
print(my_nums2)
for num in my_nums2:
    print(num)

for num in my_nums2:
    print(num)

'''
위를 보면 생성한 generator를 두 번 출력 되게 구성하였지만
generator를 한 바퀴 다 돌고 나면
다음 값을 출력하지 않는다
'''

print(list(my_nums2))
'''
list를 이용하면 제너레이터를 한 번에 다 출력 가능하지만,
list로 변형 해버리면 제너레이터가 갖고 있는 장점을 모두 잃게됨

메모리 소비를 줄여야 하는 상황이라면 제너레이터를
실행 시간을 줄여야 한다면 리스트를

보통 약간의 시간을 줄이기 보단 한정적인 메모리를 효율적으로
다루는 것이 우선시 된다
'''




