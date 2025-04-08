'''
데이터 시각화는 점이나 선, 막대 그래프 등의 시각적 이미지를 사용하여 데이터를 화면에 표시하는 것

matplotlib 

### 선형 차트
.plot(x,y  ,color='',marker='',linestyle='') -> 선형 차트를 만들어줌
            선의 색, 마크의 표시방법, 선의 두께 등을 키워드 인자로 줄 수 있음

.title() -> 제목 레이블을 설정함, 차트의 최상단에 표시

.ylable() -> y축 레이블 설정
.xlable() -> x축 레이블 설정

.savefig("저장할 파일명.확장자명",dpi='') -> 파일의 이름과 해상도를 dpi 단위로 지정하여 이미지 저장해줌

.show() -> 화면에 차트를 표시

.axis() -> 그림 범위 지정

.legend() -> 디폴드 위치에 범례 표시

### 막대차트
.bar(range(len(x)), y) -> 막대형 차트를 그려줌

.xticks(range(len(x)),x) -> 가로축 범위의 눈금마다 부여할 눈금값을 지정한다.

##  산포도 차트 
.scatter(x,y) -> 개별 데이터 포인트를 그리는 차트

## 파이 차트
.pie(data, label=datalabels, autopct='%.2f') -> 파이 차트를 그려줌
        데이터들에 레이블을 붙이는 것이 중요하다.
        
        영역의 비중을 백분율로 표시하고 싶으면 
        autopct 키워드 배개변수에 출력 형식을 지정하면 된다 ex) autopct = '%.2f'

## 히스토그램 
.hist(x, bins=len(x))

# plt.figure(figsize=(10,6)) -> 화면 사이즈

## 상자차트
.boxplot(data)

## 한 화면에 여러 그래프 그리기
.subplots(row,col)
ex)
data = np.random.randn(2,100)

fig, axs = plt.subplots(2,2,figsize=(5,5))

axs[0,0].hist(data[0],bins=10,alpha=0.3,color="red")
axs[0,0].hist(data[1],bins=10,alpha=0.3)
axs[0,1].plot(data[0],data[1])
axs[1,0].scatter(data[0],data[1])
axs[1,1].hist2d(data[0],data[1])
'''

import matplotlib.pyplot as plt
import numpy as np


dogs_leng = [77,78,85,83,73,77,73,80]
dogs_height=[25,28,19,30,21,22,17,35]

samo_leng = [75,77,86,86,79,83,83,88]
samo_height = [56,57,50,53,60,53,49,61]

malti_leng = [34,38,38,41,30,37,41,35]
malti_height = [22,25,19,30,21,24,28,18]


plt.scatter(dogs_leng,dogs_height,color="red",label="Dachshund")
plt.scatter(samo_leng,samo_height,color="blue",marker='^',label='Samoyed')
plt.scatter(malti_leng,malti_height,color="green",marker='s',label="Maltese")
plt.title("Dog Size")
plt.ylabel("Height")
plt.xlabel("Lenght")
plt.legend()
plt.show()
