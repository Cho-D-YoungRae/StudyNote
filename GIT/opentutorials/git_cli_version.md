#### GIT - CLI 버전관리

###### 3. 버전관리의 시작
- `git init`

###### 4. 버전 만들기
- `git status`
- `git add 파일명`
- `git commit -m "commit message"`
  - \-m 뒤에 없이 써도 이후에 메세지 작성할 수 있다.
    - 여러줄의 커밋 메세지 쓸 수 있다.
- `git commit --amend`
  - 이전 커밋메세지 수정

###### 5. 여러개의 파일을 버전으로 만들기
- `git log --stat`
  - 커밋마다 어떤 파일이 연루되었는지 확인

###### 6. 버전간의 차이점 비교
- `git diff`
  - 이전 버전과 차이점 비교
- `git log -p`
  - 버전마다 차이를 비교

###### 7. chechout과 시간여행
- `git checkout 커밋해쉬`
  - 해당 커밋을 돌아간다.
  - HEAD를 해당 커밋으로 옮긴다.
  - `git checkout master`
    - 다시 최신으로 돌아간다.
  - `git checkout -- 파일이름`
    - 작업트리의 파일 수정된 내용을 취소하고 가장 최신 버전 상태로
  - `git checkout -b 브랜치명`
    - 브랜치 없으면 생성 후 이동


###### 8. 보충수업
- `git commit -am "commit message"`
  - add와 commit 동시에
  - untracked 상태 파일은 자동으로 add 안된다.
###### 9. 삭제 - git reset
- `git reset --hard 커밋해시` 
  - 해당 커밋이 되겠다. 
- `git reset HEAD 파일이름`
  - 스테이징된 파일을 스테이징 취소. 파일 이름 안 쓰면 스테이지 모든 파일
- `git reset HEAD^`
  - 가장 마지막 커밋 취소. 취소한 파일이 작업트리에만 남는다.
  - `HEAD~3`: 최근 3개 커밋
  - `--soft HEAD^`
    - 작업트리를 최근 커밋 하기 전 상태로
  - `--mixed HEAD^`
    - 최근 커밋과 스테이징을 하기 전 상태로 (default)
  - `--hard HEAD^`
    - 최근 커밋과 스테이징, 파일 수정을 하기 전 상태로
###### 10. 되돌리기 - git revert
- `git revert 커밋해시`
  - 해당 커밋에 적용되었던 것을 취소.
  - 이전 단계로 새로운 커밋이 생성된다.
  - 어느 특정 커밋으로 돌아가려면 역순으로 단계별로 커밋
  - 커밋 삭제하지 않고 되돌리기

###### stash 수정중인 파일 감추기 (나의 추가 내용)
- `git stash`
  - 수정 중인 파일 감추기
  - 파일이 tacked 상태여야 한다.
- `git stash list`
- `git stash pop`
- `git stash apply`
  - 가장 최근 항목 되돌리지만 삭제 안 함
- `git stash drop`
  - 가장 최근 항복 삭제