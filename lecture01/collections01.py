"""
    파이썬에서 제공하는 표준 자료구조: 리스트. 튜플. 딕셔너리(사전), 셋(집합)

    collections 모듈
     deque(양쪽이 열려있는 큐구조), defaultdict, Counter, namedtuple, OrderedDict

    array 모듈
    (동일한 데이터 타입 -> 메모리를 좀 더 효율적이게 사용할 수 있다)
     array 사용하는 방법

    heapq모듈
    (힙 생성, 힙내부자료 접근, 자료를 sort하는 과정이 필요없다->overhead를 줄일 수 있는 장점)

    bisect 모듈
    (정렬된 상태로 요소를 추가, 중복값 처리)

    Queue

    struct(바이너리 자료구조)

    copy(객체를 복사)


    [ collections ]
    Counter : 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체
"""
import collections

print(collections.Counter(['aa','cc','dd','aa','bb','ee']))
print(collections.Counter(['aaa','ddd','ccc','aaa','fff','ddd','sss','aaa','ddd','sss','ddd','fff','ddd','aaa','ddd','sss','aaa','ddd','aaa','sss','ddd']))

print(collections.Counter({"가":3, "나":2, "다":4})) # 개수 많은 순서대로 정렬됨
# 리스트,시퀀스 넣으면 리스트,시퀀스로
# 키와 값이 있는 사전 형태로 넣으면 사전 형태로 출력됨

#숫자를 문자열에 맵핑할 수 있
print(collections.Counter(a=2, b=4, c=1))


container = collections.Counter() #생성자
print(container) #컨테이너 확인

container.update("aabcdeffgg")
print (container)

container.update({'c':2, 'f':3})
print(container)
print('===============')



# Counter 접근하기

for n in "abdfe":
    print ('%s: %d' %(n,container[n]))

ct = collections.Counter("Hello jenny")
ct['x'] = 0

print(ct)

print(list(ct.elements()))
print('===================================')
# most_common(n) 사용하기: 상위 n개를 시퀀스로 만든다.

ct2 = collections.Counter()
with open('test.txt', 'rt') as f:
    for li in f:
        ct2.update(li.rstrip().lower())

for item, cnt in ct2.most_common(7):
    print('%s : %2d' %(item, cnt))

print('===================================')
print(ct2.most_common())


