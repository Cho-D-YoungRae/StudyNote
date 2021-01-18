#### GIT - Reset & Revert

###### 3. reset vs checkout
|reset|checkout|
|---|---|
|HEAD가 가리키고 있는 브랜치가 가르키는 것을 바꾼다.|HEAD가 가르키는 것을 바꾼다.|
|이전 버전으로 넘어가면 만들어진 다음 버전은 삭제된다.|삭제되지 않는다.|
|삭제된 버전의 커밋 해시를 알고 있으면 복원 가능|브랜치말고 커밋을 직접 가르킬 수 있고 이 상태를 detached 상태라 한다.|

###### 4. reset --soft vs --mixed vs --hard
|-|`--soft`|`--mixed`|`--hard`|
|---|---|---|---|
|repository|O|O|O|
|stage area|X|O|O|
|working dir|X|X|O|


> `git reflog`: 이전 커밋들 확인

###### 5. revert
- 해당 버전의 변경 사항을 커밋하고 그 변경사항이 취소된 새로운 버전으로