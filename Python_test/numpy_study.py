'''
Numpy는 대용량의 배열과 행렬연산을 빠르게 수행하며, 
고차원적인 수학 연산자와 함수를 포함하고 있는 파이썬 라이브러리이다.

ndarray 객체 제공 -> n차원 배열

배열
    단일 타입만 저장가능
    저장 공간에 연속적으로 저장 -> 임의 접근 -> direct access
    
Numpy array는 배열과 배열의 대응되는 값을 사칙연산을 통해 연산할 수 있다.

.ndim - 배열 축 혹은 차원의 개수
.shape - 배열의 차원으로 (m, n) 형식의 튜플 형이다. m, n은 각 차원의 원소의 크기
.size - 배열 원소의 개수
.dtype - 배열내의 원소의 타입을 반환하는 객체
.itemsize - 배열내의 원소의 크기를 바이트 단위로 기술

Numpy는 배열의 특성을 가지고 있기 때문에 속도가 엄청 빠름

인덱싱과 슬라이싱 가능

논리적 인덱싱
    
    a = [1,2,3,4,5,6,7,8,9]
    
    print(a[a>5]) -> [6,7,8,9]
    
    y = a > 5
    
    print(y) -> [False, False, False, False, False, True, True, True, True]
    
Numpy 2차원 배열을 수학에서의 행렬과 같이 다룰 수 있다.
따라서 역행렬이나 행렬식을 구하는 등의 행렬 연산들이 넘파이 배열에 쉽게 적용될 수 있다.
    
    -> np_array[row,col] 로 인덱스 해서 값 꺼내오기 가능
                                        값 변경도 가능
    
    np_array = np.array([1,2,3,4],[5,6,7,8])  
                                      
    -> np_array[0:2, 2:4] -> [[3,4],[7,8]]
    
        0~1 행에서 2~3까지의 열로 이루어진 행렬
        
** np_array[::2][::2]  -> 슬라이싱 여러번 하면 차원이 낮아질 수 있음 (2차원 -> 1차원)

arange() -> range() 함수와 비슷하지만 넘파이 배열을 만든다.
            사용법은 range와 동일
            
linspace(start, stop, num=n) -> start ~ stop까지의 실수 데이터를 간격을 균일하게 쪼개어 num개 생성한다.

logspace(start, stop, num=n) -> 10**start ~ 10**stop까지의 실수를 로그 스케일로 볼 때 
                                균등한 간격으로 num개수만큼 생성한다.
                                
.reshape(m,n) -> 1차원 배열을 m행 n열의 2차원 배열로 바꿔준다. 
                n에 인수로 -1을 전달하면 데이터 개수에 맞춰서 자동으로 배열의 형태가 결정된다.
        
.flatten() -> 고차원 배열을 1차원 배열로 만들어준다.

.random.rand(m,n) -> 0.0 ~ 1.0 사이의 값으로 생선된다.
                    n은 생략가능 m X n 크기의 2차원 배열 생성

.random.randint(a,b,size =(m,n)) -> a ~ b 사이의 난수를 생성하여 반환한다.
                            n은 생략가능 m X n 크기의 2차원 배열 반환
                            
함수	분포 형태	값 범위	자주 나오는 값

rand()	균등 분포	0 ~ 1	전체 고르게

randn()	정규 분포	-∞ ~ ∞	0 근처에 집중됨


np.mean(배열) -> 평균
np.median(배열) -> 중앙값 -> 비정상적으로 큰 이상치 값으로 인해 전체의 평균 값이 
                            전체의 대표성을 가지지 못하는 경우를 막기위해서 사용된다.
                            
np.zeros(m,n) -> 배열을 0으로 채워서 만들어줌
np.sum() -> 배열의 합 반환, ()안에 axis=1 행끼리 더 해줌 axis=0 열끼리 더 해줌

** corrocef(x, y) -> 요소들의 상관관계 계산 (다차원도 가능)
    결과는 x와x의 상관관계 Cxx, x와y Cxy, y와x Cyx, y와y Cyy
    
    [[Cxx, Cxy],
     [Cyx, Cyy]] 반환
    
    완전한 음의 상관관계일 경우 -1, 상관관계가 전혀 없을 때 0, 양의 상관관계를 가질 때 1
    자기 자신과의 상관관계는 1이므로 대각선은 언제나 1 (Cxx, Cyy)
'''


import numpy as np

x1 = [i for i in range(100)]
x2 = [i + np.random.randint(1,10) for i in range(100)]
x3 = [i + np.random.randint(1,50) for i in range(100)]
x4 = [np.random.randint(1,100) for i in range(100)]

print(np.corrcoef([x1,x2,x3,x4]))



