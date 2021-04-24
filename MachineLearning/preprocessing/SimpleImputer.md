# 사용법
```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='median')
imputer.fit(housing_num)
X = imputer.transform(housing_num)
```


# 매개변수
- `strategy` : 누락된 값을 어떻게 처리할지


# 참고
- `핸즈온 머신러닝` - 99pg
- [공식문서](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer)
