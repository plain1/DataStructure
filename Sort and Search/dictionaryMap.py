#2017025073 강병욱
#딕셔너리를 이용한 맵
d={}    #딕셔너리 객체를 만듬
d['data']='자료'    #맵에 엔트리를 삽입
d['structure']='구조'
d['sequential search']='선형탐색'
d['game']='이진탐색'
print("나의 단어장:")
print(d)    #맵 출력

if d.get('game') : print("탐색:game --> ",d['game'])    #탐색
if d.get('over') : print("탐색:over --> ",d['over'])    #탐색
if d.get('data') : print("탐색:data --> ",d['data'])    #탐색

d.pop('game')
print("나의단어장:")
print(d)