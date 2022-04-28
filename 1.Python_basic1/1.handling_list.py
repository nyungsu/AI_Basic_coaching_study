#list comprehension에 익숙해지자
#list comprehension 뒤에 조건 많이 붙일 수 있음

num_list = [1,5,7,15,16,22,28,29]

def get_odd_num(num_list : list) ->list:
    result =[i for i in num_list if i%2 !=0]
    return result

print(get_odd_num(num_list))


#처음했던 거
#for + append
# def get_odd_num(num_list : list) ->list:
#     result =[]
#     for i in num_list:
#         if i % 2 != 0:
#             result.append(i)
#     return result