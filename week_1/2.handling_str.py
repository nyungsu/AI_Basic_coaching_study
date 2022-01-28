#list comprehension에 익숙해지자
#list comprehension 맨뒤에 슬라이싱하는거랑 i에 슬라이싱 하는 거 다름 비교해봐라
#join함수 복습해라

sentence = "way a is there will a is there where"

def reverse_sentence(sentence: str) ->str:
    temp = [i for i in sentence.split(' ')[::-1]]
    # temp = temp[::-1]  이 줄을 없에고 위에 한 줄로
    temp = " ".join(temp)
    return temp
print(reverse_sentence(sentence))




# 처음했던 거
# for + append
# def reverse_sentence(sentence: str) ->str:
#     temp = []
#     for i in sentence.split(' '):
#         temp.append(i)
#     temp = temp[::-1]
#     temp = " ".join(temp)
#     return temp


