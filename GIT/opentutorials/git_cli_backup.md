#### GIT3 - CLI 백업

###### 6. 원격저장소와 연결
- `git remote add 원격저장소_별칭 원격저장소_주소`
  - 지역 저장소를 원격 저장소와 연결한다.
  - 원격저장소 별칭으로 보통 origin 사용
- `git remote`
  - 원격 저장소 목록
  - `-v` 붙여주면 원격 저장소 주소 확인할 수 있다.

###### 7. push
- `git` 
  - 명령어 확인할 수 있다.
- `git push`
  - `git push -u origin master`
    - 지역 저장소의 브랜치를 원격 저장소의 master에 연결. 처음 한번만 하면 된다.
  - `git push --set-upstream origin master`
    - 다음부터 push 하면 기본적으로 origin 의 master 에 push 한다.
  - `git push origin 브랜치명`
    - origin에 브랜치 푸시

###### 8. 복제
- `git clone 원격저장소_주소 디렉토리명`
  - 현재 원격저장소에 있는 것을 복제한다.
  - 디렉토리명 생략하면 저장소 이름과 같은 디렉토리 생성
  - 디렉토리명 . 이면 현재 디렉토리

###### 9. pull
- `git pull`
  - `git pull origin master`
    - origin의 내용을 master로
    - 기본 원격 저장소가 origin이고, 기본 지역 저장소 브랜치가 master이므로 뒤는 생략 가능
