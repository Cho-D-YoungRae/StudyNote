#### 3. 팬더스를 활용한 데이터 분석
---
###### 3.1 넘파이 배열
---
###### 3.1.1 배열 생성
---
```python
import numpy as np

# 2차원 배열
A = np.array([[1, 2], [3, 4]])
```

###### 3.1.2 배열 정보 보기
---
```python
type(A)
<class 'numpy.ndarray'>

A.ndim  # 배열의 차원
2

A.shape # 배열의 크기
(2, 2)

A.dtype # 원소 자료형
dtype('int32')

print(A.max(), A.mean(), A.min(), A.sum())
4 2.5 1 10
```

###### 3.1.3 배열의 접근
---
```python
A[0]
array([1, 2])

A[0][0]
1

A[1, 1] # 이런 형태로도 접근 가능
4

A[A>1]  # 원소중 1보다 큰 것들 출력
array([2, 3, 4])
```

###### 3.1.4 배열 형태 바꾸기
---
```python
# 배열의 요소 위치를 주대각선을 기준으로 뒤바꾼다.
A.T # A.transpose() 와 같다.
array([[1, 3],
       [2, 4]])

# 다차원 배열을 1차원 배열 형태로 바꾼다. 평탄화.
A.flatten()
array([1, 2, 3, 4])
```

###### 3.1.5 배열의 연산
---
같은 크기의 행렬끼리는 사칙 연산을 할 수 있다. 두 행렬에서 같은 위치에 있는 원소끼리 연산을 하면 된다.
```python
A + A   # np.add(A, A)
array([[2, 4],
       [6, 8]])
A - A   # np.subtract(A, A)
array([[0, 0],
       [0, 0]])
A * A   # np.multiply(A, A)
array([[ 1,  4],
       [ 9, 16]])
A / A   # np.divide(A, A)
array([[1., 1.],
       [1., 1.]])
```       

###### 3.1.6 브로드캐스팅
---
수학에서는 크기(shape 속성)가 같은 행렬끼리만 연산할 수 있다. 하지만 넘파이에서는 행렬크기가 달라도 연산할 수 있게 크기가 작은 행렬을 확장해주는데, 이를 브로드캐스팅이라고 한다.
```python
B = np.array([10, 100])
A * B
array([[ 10, 200],
       [ 30, 400]])
```

###### 3.1.7 내적 구하기
---
행력 A가 m\*k 행렬이고 행렬 B가 k\*n 행렬이라고 할 때, 행렬 A와 행렬 B를 곱한 행렬 C는 m*n 행렬이 된ㄷ. 이때 행렬 C의 i행 j열에 해당하는 원소를 행렬 A의 i행과 행렬 B의 j열의 내적이라고 한다.
```python
A.dot(B)
array([210, 430])
```

##### 3.2 팬더스 시리즈
---
시리즈는 인덱스 처리가 된 1차원 벡터 형태의 자료형이다. 시간의 흐름에 따라 기록한 데이터를 시계열(time series)이라고 부르는데, 시리즈는 이러한 시계열 데이터를 다루는데 적합하다. 데이터프레임은 여러 시리즈가 한 가지 인덱스를 기준으로 합쳐진 형태이다.

###### 3.2.1 시리즈 생성
---
```python
import pandas as pd

s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0])

s   # 인덱스를 별도로 지정하지 않으면, 정수형 인덱스 0부터
0    0.0
1    3.6
2    2.0
3    5.8
4    4.2
5    8.0
dtype: float64
```

###### 3.2.2 시리즈의 인덱스 변경
---
```python
s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8])
s.index.name = 'MY_IDX'
s.name = 'MY_SERIES'

s
MY_IDX
0.0    0.0
1.2    3.6
1.8    2.0
3.0    5.8
3.6    4.2
4.8    8.0
Name: MY_SERIES, dtype: float64
```

###### 3.2.3 데이터 추가
---
```python
s[5.9] = 5.5
ser = pd.Series([6.7, 4.2], index=[6.8, 8.0])
s = s.append(ser)

s
0.0    0.0
1.2    3.6
1.8    2.0
3.0    5.8
3.6    4.2
4.8    8.0
5.9    5.5
6.8    6.7
8.0    4.2
dtype: float64
```

###### 3.2.4 데이터 인덱싱
---
```python
# 맨 마지막 인덱스 값
s.index[-1]
8.0
# 맨 마지막 값
s.values[-1]
4.2
# 로케이션 인덱서
s.loc[8.0]
4.2
# 인티저 로케이션 인덱서
s.iloc[-1]
4.2
# 배열로 반환
s.values[:]
array([0. , 3.6, 2. , 5.8, 4.2, 8. , 5.5, 6.7, 4.2])
# 시리즈로 반환
s.iloc[:]
0.0    0.0
1.2    3.6
1.8    2.0
3.0    5.8
3.6    4.2
4.8    8.0
5.9    5.5
6.8    6.7
8.0    4.2
dtype: float64
```

###### 3.2.5 데이터 삭제
---
```python
# 인덱스값을 통해 해당 원소 삭제된 시리즈 반환
# 실제 s에는 반영되지 않는다.
s.drop(8.0) 

# 실제 s에도 반영하려면
s = s.drop(8.0)
```

###### 3.2.6 시리즈 정보 보기
---
```python
s.describe()
count    8.000000   # 원소 개수
mean     4.475000   # 평균
std      2.596013   # 표준편차
min      0.000000   # 최솟값
25%      3.200000   # 제1 사분위수
50%      4.850000   # 제2 사분위수
75%      6.025000   # 제3 사분위수
max      8.000000   # 최댓값
dtype: float64
```

###### 3.2.7 시리즈 출력하기
---
```python
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0, 5.5, 6.7, 4.2])
    s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8, 5.9, 6.8, 8.0])

    s.index.name = "MY_IDX"
    s.name = "MY_SERIES"

    plt.title("ELLIOTT WAVE")
    # 시리즈를 bs--(푸른 사각형과 점선) 형태로 출력
    plt.plot(s, 'bs--')
    # x축의 눈금값을 s 시리즈의 인덱스값으로 설정
    plt.xticks(s.index)
    # y축의 눈금값을 s 시리즈의 데이터값으로 설정
    plt.yticks(s.values)
    plt.grid(True)  # 그래프 내 눈금
    plt.show()
```    

##### 3.3 팬더스 데이터프레임
---
시리즈는 단일 변수의 관측값을 기록하기에는 적합하지만, 여러 변수에 대한 관측값을 함께 기록하기에는 적합하지 않다. 이때 데이터 프레임을 사용하는게 효율적이다. 데이터프레임은 인덱스 하나와 여러 시리즈를 합친 자료형이라고 할 수 있다.

팬더스 라이브러리를 사용하여 엑셀, HTML, 데이터베이스로부터 데이터를 읽어와 데이터프레임 형태로 가공할 수 있으며, 반대로 데이터프레임을 가공하여 엑셀, HTML, 데이터베이스 등으로 저장할 수 있다.

###### 3.3.1 딕셔너리를 이용한 데이터프레임 생성
---
```python
import pandas as pd
df = pd.DataFrame({'KOSPI': [1915, 1961, 2026, 2467, 2041],
...                    'KOSDAQ': [542, 682, 631, 798, 675]},
...                   index=[2014, 2015, 2016, 2017, 2018])
df  # 인덱스를 지정하지 않으면 정수형 인덱스 0부터
      KOSPI  KOSDAQ
2014   1915     542
2015   1961     682
2016   2026     631
2017   2467     798
2018   2041     675
```

```python
df.describe()
             KOSPI      KOSDAQ
count     5.000000    5.000000
mean   2082.000000  665.600000
std     221.117616   92.683871
min    1915.000000  542.000000
25%    1961.000000  631.000000
50%    2026.000000  675.000000
75%    2041.000000  682.000000
max    2467.000000  798.000000

df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 5 entries, 2014 to 2018
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   KOSPI   5 non-null      int64
 1   KOSDAQ  5 non-null      int64
dtypes: int64(2)
memory usage: 120.0 bytes
```

###### 3.3.2 시리즈를 이용한 데이터프레임 생성
```python
if __name__ == '__main__':
    kospi = pd.Series([1915, 1961, 2026, 2467, 2041],
                      index=[2014, 2015, 2016, 2017, 2018], name='KOSPI')
    kosdaq = pd.Series([542, 682, 631, 798, 675],
                       index=[2014, 2015, 2016, 2017, 2018], name='KOSDAQ')

    df = pd.DataFrame({kospi.name: kospi, kosdaq.name: kosdaq})
    print(df)
```

###### 3.3.3 리스트를 이용한 데이터 프레임 생성
---
```python
if __name__ == '__main__':
    columns = ['KOSPI', 'KOSDAQ']
    index = [2014, 2015, 2016, 2017, 2018]
    rows = [[1915, 542], [1961, 682], [2026, 631], [2467, 798], [2041, 675]]
    df = pd.DataFrame(rows, columns=columns, index=index)
```

###### 3.3.4 데이터프레임 순회 처리
---
```python
for i in df.index:
    print(i, df['KOSPI'][i], df['KOSDAQ'][i])

for row in df.itertuples():
    print(row[0], row[1], row[2])
    
# iterrows() 는 각 행을 인덱스와 시리즈의 조합으로 반환
for idx, row in df.iterrows():
    print(idx, row[0], row[1])

2014 1915 542
2015 1961 682
2016 2026 631
2017 2467 798
2018 2041 675

# itertuples() 는 각 행을 이름있는 튜플 형태로 반환
for row in df.itertuples(name='KRX'):
    print(row)

KRX(Index=2014, KOSPI=1915, KOSDAQ=542)
KRX(Index=2015, KOSPI=1961, KOSDAQ=682)
KRX(Index=2016, KOSPI=2026, KOSDAQ=631)
KRX(Index=2017, KOSPI=2467, KOSDAQ=798)
KRX(Index=2018, KOSPI=2041, KOSDAQ=675)


```
- 이름있는 튜플(namedtuple)은 인덱스 뿐 아니라 키 값을 통해 데이터에 접근할 수 있다.


##### 3.4 주식 비교하기
---
###### 3.4.1 야후 파이낸스로 주식 시세 구하기
---
```python
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2020-09-25')
msft = pdr.get_data_yahoo('MSFT', start='2020-09-25')
```
- `get_data_yahoo(조회할 주식 종목 [, start=조회 기간의 시작일] [, end=조회 기간의 종료일])`
  - 주식 종목: 문자열 혹은 리스트
    - 국내 기업 주식 데이터: `.KS`(코스피), `.KQ`(코스닥) 을 붙여준다.
    - 미국 기억의 주식 데이터: `AAPL`(애플) 처럼 심볼을 이용
      - www.nasdaq.com/screening/company-list.aspx
  - 조회 기간을생략하면 야후가 보유한 데이터에서 제일 오래된 일자부터 제일 최신 일자까지 설정된다.

```python
# 맨 앞 10행. 인수를 생략하면 기본 값 5
sec.head(10)

# 거래량(Volume) 칼럼을 제거한 새로운 데이터프레임 생성
tmp_msft = msft.drop(columns='Volume')
# 제일 뒤 5행
tmp_msft.tail()

sec.index       # 인덱스 확인
sec.columns     # 칼럼 확인
```

```python
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    yf.pdr_override()

    sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
    msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

    plt.plot(sec.index, sec.Close, 'b', label='Samsung Electronics')
    plt.plot(msft.index, msft.Close, 'r--', label='Microsoft')
    plt.legend(loc='best')
    plt.show()
```
- `plot(x, y, 마커 형태 [, label='Label'])`
- 50000원의 삼성과 130달러 대의 마이크로소프트 주가를 한 번에 표시하다 보니 비교가 잘 되지 않는다.


###### 3.4.2 일간 변동률로 주가 비교하기
---
> 일간 변동률(daily percent change)을 구하면 가격이 다른 두 주가의 수익률을 비교할 수 있다.<br>`Rt1(오늘 변동률) = ((Rt(오늘 종가) - Rt-1(어제 종가) / Rt-1(어제 종가))) * 100`

```python
# 위의 식을 파이썬으로 옮긴 것
# shift() 함수는 데이터를 n행씩 뒤로 이동
sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100

# 위에서 shift로 한 칸씩 미뤄서 첫 번째 값이 NaN이 된다.
# 그렇기 때문에 0으로 변경
sec_dpc.iloc[0] = 0
sec_dpc.head()
```
- 데이터 프레임의 한 칼럼은 시리즈

###### 3.4.3 주가 일간 변동률 히스토그램
---
> 히스토그램은 도수 분포를 나타내는 그래프로서, 데이터값들에 대한 구간별 빈도수를 막대 현태로 나타낸다. 이때 구간 수를 bins라고 한다.
```python
sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100
sec_dpc.iloc[0] = 0
plt.hist(sec_dpc, bins=18)
plt.grid(True)
plt.show()
```
- `hist()`: 히스토그램
  - `bins` 기본값 10

###### 3.4.4 일간 변동률 누적합 구하기
---
> 전체적인 변동률을 비교해보려면 일간 변동률의 누적합을 계산해야한다. 시리즈의 `cumsum()` 함수를 이용하여 구할 수 있다.
```python
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    yf.pdr_override()

    sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
    msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

    sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100
    sec_dpc.iloc[0] = 0
    sec_dpc_cs = sec_dpc.cumsum()   # 일간 변동률의 합

    msft_dpc = (msft['Close'] / msft['Close'].shift(1) - 1) * 100
    msft_dpc.iloc[0] = 0
    msft_dpc_cs = msft_dpc.cumsum() # 일간 변동률의 합

    plt.plot(sec.index, sec_dpc_cs, 'b', label='Samsung Electronics')
    plt.plot(msft.index, msft_dpc_cs, 'r--', label='Microsoft')
    plt.ylabel('Change %')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()
```

##### 3.5 최대 손실 낙폭
---