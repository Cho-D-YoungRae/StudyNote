#### GIT - CLI 협업

###### 4. push & pull
- 원격 저장소에 수정된 사항이 있을 수 있으므로 `pull`을 해준 후 작업을 시작한다.
  - 그렇지 않을 경우 `push`가 거부된다.
  - 거부된 후 `pull`을 하면 원격저장소의 내용과 지역 저장소 내용이 병합된다.
    - 충돌이 일어난 부분이 있으면 수정해주고 새로 커밋과 푸시 해준다.

###### 5. 원격 브랜치와 FETCH
- `git fetch`
  - 원격 브랜치의 변화 정보 가져온다.
  - 지역 저장소에 바로 반영 안된다.
- `git checkout FETCH_HEAD`
- `git merge FETCH_HEAD`
  - `git pull`과 동일
  - `git merge origin/master`과 동일

###### fetch (나의 추가 내용)
- `git fetch`
  - 원격 브랜치의 변화 정보 가져온다.
  - 지역 저장소에 바로 반영 안된다.
- `git checkout FETCH_HEAD`
- `git merge FETCH_HEAD`
  - `git pull`과 동일