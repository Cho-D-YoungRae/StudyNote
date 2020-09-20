#### Chapter 2. 파이썬 프로그래밍
---
##### 2.6 모듈과 패키지
---
###### 2.6.1 모듈
---

**help()**

- `help('modules')`: 설치된 모듈 목록
- `help('modules 키워드')`: 키워드가 포함된 모듈
- `help('모듈')`: 해당 모듈에 대한 설명

###### 2.6.2 패키지
---

여러 모듈(.py 파일)을 특정 디렉터리에 모아놓은 것. 패키지명 뒤에 '.'을 붙이고 모듈명을 붙여 import 할 수 있다.

**패키지 생성하기**

디렉터리 안에 여러 모듈 파일(.py 파일)을 넣는 것만으로도 패키지 생성은 완료된다.

**__pychche__ 디렉터리**

임포트하는 순간 현재 디렉터리의 하위에 `__pycache__`라는 디렉터리가 생기고 그 안에 .pyc(Compiled Python File)이 자동으로 생성된다. 한 번 컴파일한 모듈을 캐시로 해놓고, 다음 번에 모듈을 임포트할 떄 컴파일 작업 없이 이 파일을 사용함으로써 속도를 높인다.

**__init__.py 패키지 초기화 파일**

디렉토리에 여러 모듈을 추가한 뒤, `__init__.py`라는 파일을 생성하면, 파이썬은 해당 디렉터리를 패키지로 인식한다. 이때 `__init__.py__` 파일을 패키지 초기화 파일이라고 부르며, 파일 내용은 비어 있어도 상관없다. 만일 패키지 내의 모든 모듈에서 공통적으로 사용할 속성이 있다면 패키지 초기화 파일에 정의하면 된다.

파이썬 3.3 버전부터는 `__init__.py`파일을 굳이 생성하지 않아도 패키지로 인식한다. 하지면 `from 패키지명 import *`로 패키지 하부의 모든 객체를 한 번에 임포트 하려면 여전히 이 파일이 필요하다. 이 파일을 생성한 뒤 `__all__ = ['모듈1', '모듈2']`로 가능.

##### 2.7 객체지향 프로그래밍
---
###### 2.7.4 클래스 메서드

**__del__소멸자**

인스턴스가 메모리에서 제거될 때 자동으로 호출되는 함수로서 소멸자라고 부른다. 명시적으로 메모리에서 인스턴스를 제거할 때 `del()`함수를 사용한다.

**__doc__독스트링**

독스트링은 클래스나 메서드를 설명하는 문자열이다. 클래스나 메서드명 바로 아랫줄에 위치한다.
```python
def __del__(self):
    """Destructor"""
    ...
```
`help()`함수에서 클래스나 메서드 설명을 출력하는데 쓰인다. 클래스 객체나 메서드 객체 다음에 `.__doc__`를 붙여서도 확인할 수 있다.

##### 2.8 파일 처리 및 외부 라이브러리 활용
---
###### 2.8.1 리퀘스트로 인터넷에서 이미지 파일 가져오기
---
>  `requests`패키지에서 제공하는 `get()`함수와 `post()`함수를 사용하면 자유자재로 HTTP패킷을 주고받을 수 있다.
```python
import requests

url = "http://bit.ly/2JnsHnt"
r = requests.get(url, stream=True).raw
```

###### 2.8.2 필로로 이미지 보여주기
---
> 이미지 처리 패키지 `pillow`

```python
from PIL import Image
img = Image.open(r)
img.show()
img.save('src.png')
```
img객체의 `get_format_mimetype`속성을 통해 PNG포맷, RGB모드, 크기 를 알 수 있다.

###### 2.8.3 `with ~ as 파일 객체`로 이미지 파일 복사
---
```python
BUF_SIZE = 1024
# 그림 파일은 바이너리 형식이므로 'rb', 'wb'
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
        df.write(data)
```
`read()` 함수나 `write()` 함수에 인수를 주지 않으면 한꺼번에 모든 내용을 읽거나 쓸 수 있다. 하지만 파일 크기가 커지면 문제가 발생할 수 있기 때문에 일정한 길이로 나눠서 읽고 쓰도록 처리하는 것이 좋다.

###### 2.8.4 SHA-256으로 파일 복사 검증하기
---
> 해시값을 이용하여 두 파일의 내용이 동일한지 비교. SHA-2는 해시 함수들의 집합. SHA-256은 256비트 해시값을 반환.

```python
import hashlib

sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

with open('src.png', 'rb') as sf, open('dst.png', 'rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())

print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dst.png's hash : {}".format(sha_dst.hexdigest()))
```

###### 2.8.5 맷플롯립으로 이미지 가공하기
---
> `matplotlib`은 파이썬의 대표적인 데이터 시각화 라이브러리로서 각종 그래프를 그리거나 이미지 처리에 사용된다. 지형도나 기상도 등의 이미지를 기반으로 데이터를 시각화할 때도 자주 쓰인다.
- PNG 이미지 포맷만 지원한다.
- RGB 값을 0.0 ~ 1.0 사이의 부동소수점 데이터로 재조정해서 기록한다.
```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

dst_img = mpimg.imread('dst.png')
print(dst_img)
```

**의사 색상 적용하기**
> 의사 색상이란 이미지의 색상 대비를 향상시켜서 데이터를 쉽게 시각화하는 용도로 사용된다.

사본 이미지에 의사 색상을 적용하려면 다음처럼 이미지 객체에서 인덱싱을 이용해 RGB채널 중에서 한 가지 채널만 선택하면 된다.

```python
pseudo_img = dst_img[:, :, 0]
```
RGB 채널 중 첫 번째 채널(0)만 슬라이싱해서 저장한 관계로 부동소수점 데이터가 2차원으로 변경되었다.

**이미지 비교**

```python
plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1,2,1)  # 1행 2열의 행렬에서 1번째 그림을 설정
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))

plt.subplot(122)    # 1행 2열의 행렬에서 2번쨰 그림. (,)없이 가능
plt.title('Pseudocolor Image')
dst_img = mpimg.imread('dst.png')
pseudo_img = dst_img[:,:,0]
plt.imshow(pseudo_img)
plt.show()
```