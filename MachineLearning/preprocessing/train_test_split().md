# 사용법
```python
from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

train_input, test_input, train_target, test_target = train_test_split(
	fish_data, fish_target, stratify=fish_target, random_state=42)
```
- 행의 개수가 같은 여러 개의 데이터셋을 넘겨서 같은 인덱스를 기반으로 나눌 수 있다. (데이터프레임이 레이블에 따라 여러 개로 나뉘어 있을 때 유용)


# 매개변수
- `random_state` : 난수 초깃값 지정
- `test_size` :  테스트세트로 나눌 비율. 디폴트 = 0.25
- `shuffle` : 훈련 세트와 테스트 세트로 나누기 전에 무작위로 섞을지 여부를 결정. 디폴트 = True
- `stratify` : 계층적 샘플링을 위한 데이터를 전달할 수 있다.

# 참고
- 핸즈온 머신러닝 - 87pg
- 혼자 공부하는 머신러닝 + 딥러닝 - 91, 110pg
- [공식문서](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split)
