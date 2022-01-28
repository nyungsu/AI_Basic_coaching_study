#처음에는 list 안에 있는 튜플을 i[0],i[1]이런식으로 인덱싱해서 받았다
#변수로 받을 때 부터 언패킹이 된 다는 것을 알 수 있었다.
#인덱스가 필요할 때 enumerate를 이용하면 된 다는 것을 알았다.
#enumerate은 idx랑 원소를 튜플로 리턴 해줌
#언패킹해서 변수 받는 거 start 인자 복습

score = [(100,100), (95, 90), (55,60),(75,80), (70,70)]

def get_avg(score: list):  
    for idx,(x,y) in enumerate(score,start=1):      #언패킹 있을 때 enumerate idx 변수 받는 거 신경써라
        # print(idx,x,y)                            #enumerate start 인자를 이용해서 조절가능
        res = (x+y)/2                               #변수가 두 개로 고정 되어있으니까 걍 /2하자
        print(f'{idx}번, 평균 : {res}')       
        
get_avg(score)


# 처음 했던 거
# def get_avg(score: list):
#     idx = 1
#     for i in score:
#         number_of_score = len(i)
#         res = (i[0] + i[1])/number_of_score
#         print(f'{idx}번, 평균 : {res}')
#         idx += 1