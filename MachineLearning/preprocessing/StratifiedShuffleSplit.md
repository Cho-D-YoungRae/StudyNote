# 사용법
```python
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['income_cat']):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]
```


# 매개변수
- `random_state` : 난수 초깃값 지정
- `test_size` :  테스트세트로 나눌 비율.
- `n_splits` : 분할할 train/test set 개수

# 참고
- `핸즈온 머신러닝` - 89pg
- [공식문서](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit)
