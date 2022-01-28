
inputs= "cat32dog16cow5"

def find_string(inputs):
    temp =[]
    for i in inputs:
        if i.isdigit() ==False:
            temp.append(i)
        elif i.isdigit()==True:
            temp.append('_')
    result =''.join(temp).split('_')


    final_result = [i for i in result if not i =='']
    return final_result

print(find_string(inputs))




# temp = [i for i in inputs if not i.isdigit()]
# #i가 숫자면 true인데 (not true)=false라서 리스트에 안 넣음
# #i가 문자면 false인데 (not false)=true라서 리스트에 넣음 

# print(temp)

# #위 코드 밑에처럼 한 줄로 정리 가능함
# # result1=[j for j in "".join([x if not x.isdigit() else "_" for x in inputs]).split("_") if not j == ""]







