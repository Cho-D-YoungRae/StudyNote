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
MDD(Maximum Drawdown, 최대 손실 낙폭) 은 특정 기간에 발생한 최고점에서 최저점가지의 가장 큰 손실을 의미한다.
> MDD = (최저점 - 최고점) / 최고점

###### 3.5.2 서브프라임 당시의 MDD
---
`시리즈.rolling(윈도우 크기 [, min_periods=1]) [.집계 함수()]`
- 시리즈에서 윈도우 크기에 해당하는 개수만큼 데이터를 추출하여 집계함수에 해당하는 연산을 실시한다.
- 집계함수
  - `max()`
  - `mean()`
  - `min()`
- `min_periods` 를 지정하면 데이터 개수가 윈도우 크기에 못 미치더라도 이 개수를 만족하면 연산을 수행한다.

```python
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    yf.pdr_override()

    kospi = pdr.get_data_yahoo('^KS11', '2004-01-04')   # 1

    window = 252    # 2
    peak = kospi['Adj Close'].rolling(window, min_periods=1).max()  # 3
    drawdown = kospi['Adj Close']/peak - 1.0    # 4
    max_dd = drawdown.rolling(window, min_periods=1).min()  # 5

    plt.figure(figsize=(9,7))
    plt.subplot(211)
    kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
    plt.subplot(212)
    drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
    max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
    plt.show()
```
1. KOSPI 지수 데이터를 다운로드한다. KOSPI 지수의 심볼은 `^KS11`이다.
2. 산정 기간에 해당하는 `window`값은 1년 동안의 개장일을 252로 어림잠아 설정했다.
3. KOSPI 종가 칼럼에서 1년 (거래일 기준) 기간 단위로 최고치 peak를 구한다.
4. `drawdown`은 최고치(peak) 대비 현재 KOSPI 종가가 얼마나 하락했는지를 구한다.
5. `drawdown`에서 1년 기간 단위로 최저치 `max_dd`를 구한다. 마이너스 값이기 때문에 최저치가 바로 최대 손실 낙폭이 된다.

`max_dd.min()`
- 최저값
`max_dd[max_dd==값]`
- 인덱싱

##### 3.6 회귀 분석과 상관 관계
---
회귀 분석은 데이터의 상관관계를 분석하는 데 쓰이는 통계 분석 방법이다.

###### 3.6.1 KOSPI와 다우존스 지수 비교
---
```python
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    yf.pdr_override()

    dow = pdr.get_data_yahoo('^DJI', '2000-01-04')      # 다우존스 지수
    kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')   # 코스피

    plt.figure(figsize=(9, 5))
    plt.plot(dow.index, dow.Close, 'r--', label='Dow Jones Industrial')
    plt.plot(kospi.index, kospi.Close, 'b', label='KOSPI')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()
```

###### 3.6.2 지수화 비교
---
일별 종가만으로는 KOSPI와 다우존스 지수의 상관관계를 비교하기가 어려웠다. 현재 종가를 특정 시점의 종가로 나누어 변동률을 구해보자.

```python
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    yf.pdr_override()

    dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
    kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

    d = (dow.Close / dow.Close.loc['2000-01-04']) * 100
    k = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100

    plt.figure(figsize=(9, 5))
    plt.plot(d.index, d, 'r--', label='Dow Jones Industrial Average')
    plt.plot(k.index, k, 'b', label='KOSPI')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()
```

###### 3.6.3 산점도 분석
---
다우존스 지수와 KOSPI의 관계를 분석하는데 산점도(Scatter plot)를 사용해보자. 산점도란 독립변수 x와 종속변수 y의 상관관계를 확인할 때 쓰는 그래프다. 
```python
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt


if __name__ == '__main__':
    yf.pdr_override()

    dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
    kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

    df = pd.DataFrame({'DOW':dow['Close'], 'KOSPI': kospi['Close']})
    df = df.fillna(method='bfill')
    df = df.fillna(method='ffill')

    plt.figure(figsize=(7, 7))
    plt.scatter(df['DOW'], df['KOSPI'], marker='.')
    plt.xlabel('Dow Jones Industrial Average')
    plt.ylabel('KOSPI')
    plt.show()
```
- `len(dow)`, `len(kospi)` 를 통해 확인해보면 길이가 다른 것을 알 수 있다.
- 산점도를 그리려면 x, y의 사이즈가 동일해야 한다.
- 다우존스 지수의 종가 칼럼과 KOSPI 지수의 종가 칼럼을 합쳐서 데이터프레임 df를 생성하면 한 쪽 데이터가 없으면 NaN으로 자동으로 채워진다.
- 산점도를 출력하려면 NaN을 제거해야한다.
- 데이터프레임의 `fillna()` 함수를 이용하여 NaN을 채울 수 있다.
  - 인수로 `bfill`(backward fill)을 주면 뒤에 있는 값으로 NaN 을 덮어쓴다.
  - 인수로 `ffill`(forkward fill)을 주면 앞에 있는 값으로 NaN 을 덮어쓴다.
- bfill만 하면 마지막 행의 NaN은 없앨 수 없으므로 ffill도 진행한다.
- `dropna()` 함수를 사용하면 NaN이 있는 행을 한 번에 제거할 수 있지만 표본 데이터 수가 적어지므로 상황에 맞게 사용한다.

###### 3.6.4 사이파이 선형 회귀 분석
---
 사이파이(SciPy)는 파이썬 기반 수학, 과학, 엔지니어링용 핵심 패키지 모음이다. 

 ###### 3.6.5 선형 회귀 분석
 ---
 회귀 모델이란 연속적인 데이터 Y와 이 Y의 원인이 되는 X 간의 관계를 추정하는 관계식을 의미한다. 사이파이 패키지의 서브 패키지인 스탯츠(stats)는 다양한 통계함수를 제공한다. `linregress()` 함수를 이용하면 시리즈 객체 두 개만으로 간단히 선형 회귀 모델을 생성하여 분석할 수 있다.
 ```python
 from scipy import stats
 model = stats.linregress(독립변수 x, 종속변수 y)
 ```
- `slope`: 기울기
- `intercepy`: y절편
- `rvalue`: r값(상관계수)
- `pvalue`: p값
- `stderr`: 표준편차

 ##### 3.7 상관계수에 따른 리스크 완화
 ---
 상관계수(Coefficient of Correlation)란 독립변수와 종속변수 사이의 상관관계의 정도를 나타내는 수치다. 상관계수 r은 -1 <= r <= 1 을 만족시키며 상관관계가 없을 때 r = 0 이다. A자산과 B자산의 상관계수가 1이면, A자산 가치가 x%만큼 상승할 때 B자산 가치도 x%만큼 상승한다. -1이면 B자산 가치는 x%만큼 하락한다.

###### 3.7.1 데이터프레임으로 상관계수 구하기
---
`df.corr()`

###### 3.7.2 시리즈로 상관계수 구하기
---
`df['DOW'].corr(df['KOSPI'])`

###### 3.7.3 결정계수 구하기
---
결정계수(R-squared)는 관측된 데이터에서 추정한 회귀선이 실제로 데이터를 어느 정도 설명하는지를 나타내는 계수로, 두 변수의 상관관계 정도를 나타내는 상관계수(R value)를 제곱한 값이다. 결정계수가 1이면 모든 표본 관측치가 추정된 회귀선 상에만 있다는 의미다. 0이면 추정된 회귀선이 변수 사이의 관계를 전혀 설명하지 못 한다는 의미다.
```python
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
from scipy import stats


if __name__ == '__main__':
    yf.pdr_override()

    dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
    kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

    df = pd.DataFrame({'X':dow['Close'], 'Y': kospi['Close']})
    df = df.fillna(method='bfill')
    df = df.fillna(method='ffill')

    regr = stats.linregress(df.X, df.Y)     # 1
    regr_line = f'Y = {regr.slope:.2f} * X + {regr.intercept:.2f}'  # 2

    plt.figure(figsize=(7, 7))
    plt.plot(df.X, df.Y, '.')   # 3
    plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r') # 4
    plt.legend(['DOW x KOSPI', regr_line])
    plt.title(f'DOW x KOSPI (R = {regr.rvalue:.2f})')
    plt.xlabel('Dow Jones Industrial Average')
    plt.ylabel('KOSPI')
    plt.show()
```
1. 다우존스 지수 X와 KOSPI 지수 Y로 선형회귀 모델 객체 regr을 생성한다.
2. 범례에 회귀식을 표시해주는 레이블 문자다.
3. 산점도
4. 회귀선
