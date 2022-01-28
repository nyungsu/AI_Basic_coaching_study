#counter 라는 컬렉션을 배울 수 있었음
#dict 다룰 때는 collection 모듈의 counter 객체를 사용하자
#그냥 더해도 key 중복 검사 해주네 

from collections import Counter


dict_first = {'사과':30, "배":15, '감':10, '포도':10}
dict_second ={'사과':5, '감':25, "배":15, '귤':25}

def merge_dict(dict_first, dict_second):
    final_dict = dict(Counter(dict_first)+Counter(dict_second))     #한줄로 줄여봄
    # final_dict = {}
    # f = Counter(dict_first)
    # s = Counter(dict_second)
    # final_dict = dict(f+s)
    print(final_dict)
    
merge_dict(dict_first,dict_second)
    

#맨 처음하다가 실패했던 거
# dict_final ={}
# # def merge_dict(dict_first, dict_second):
# k1 =[k for k in dict_first.keys()]
# v1 =[v for v in dict_first.values()]
# k2 =[k for k in dict_second.keys()]
# v2 =[v for v in dict_second.values()]


# #dict에 key만 먼저 넣어보자
# for i in range(0,len(k1)):     
#     for j in range(0,len(k2)):
#         if k1[i] == k2[j]:
#             dict_final[k1[i]] = None
#         else:
#             dict_final[k2[j]] = None
            
         
        
# print(dict_final)