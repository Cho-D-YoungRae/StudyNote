#### tkinter
> 윈도 프로그래밍

```python
import tkinter
```

##### 기본 윈도 창의 구성

```python
import tkinter

if __name__ == '__main__':

   # 기본이 되는 윈도를 반환 (Root Window, Base Window) 
    window = tkinter.Tk()
    window.title("윈도창 연습")
    window.geometry("400x100")
    window.resizable(width=False, height=True)

    window.mainloop()   # 윈도 창 실행
```

##### 라벨

```python
import tkinter

if __name__ == '__main__':

    window = tkinter.Tk()

    label1 = tkinter.Label(window, text="This is MySQL을")
    label2 = tkinter.Label(window, text="열심히", font=("궁서체", 30), fg="blue")
    label3 = tkinter.Label(window, text="공부 중입니다.", bg="magenta",
                                        width=20, height=5, anchor='se')

    label1.pack()
    label2.pack()
    label3.pack()

    window.mainloop()
```

*라벨 옵션*
- `font` : 글꼴, 크기.
- `fg` : foreground의 약자. 글자색.
- `bg` : background의 약자. 배경색.
- `anchor` : 위젯의 위치
  - `'se'` 는 `tkinter.SE` 로도 가능

##### 버튼

```python
import tkinter
from tkinter import messagebox

def clickButton():
    messagebox.showinfo('버튼 클릭', '버튼을 클릭했습니다.')

if __name__ == '__main__':

    window = tkinter.Tk()
    window.geometry("200x200")

    button1 = tkinter.Button(window, text="요기 눌러요", fg="red",
                             bg="yellow", command=clickButton)
    
    # 버튼을 화면 중앙에 표현하기 위해서 옵션 추가
    button1.pack(expand=1)

    window.mainloop()
```

*버튼정렬*

```python
button.pack(side=tkinter.LEFT)
```
- `LEFT`, `RIGHT`, `TOP`, `BOTTOM`

*위젯 사이에 여백 주기*
```python
button.pack(side.tkinter.TOP, fill=tkinter.X, padx=10, pady=10)
```
- `fill` : 남는 공간 버튼으로 채움. 글씨 크기보다 버튼이 커짐.


##### 프레임, 엔트리, 리스트박스

- 프레임(Frame): 화면의 구역을 나눈다.
- 엔트리(Entry): 입력 상자
- 리스트박스(Listbox): 목록

```python
import tkinter

if __name__ == '__main__':

    window = tkinter.Tk()
    window.geometry("200x200")

    # 구획을 나누는 것일 뿐 화면에 표시되지는 않는다.
    upFrame = tkinter.Frame(window)
    upFrame.pack()
    downFrame = tkinter.Frame(window)
    downFrame.pack()

    editBox = tkinter.Entry(upFrame, width=10, bg='green')
    editBox.pack(padx=20, pady=20)

    listbox = tkinter.Listbox(downFrame, bg='yellow')
    listbox.pack()

    # 데이터를 제일 뒤(tkinter.EXD)에 첨부
    listbox.insert(tkinter.END, "하나")
    listbox.insert(tkinter.END, "둘")

    window.mainloop()
```

##### 메뉴

```python
import tkinter
from tkinter import messagebox

if __name__ == '__main__':

    def func_open():
        messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

    def func_exit():
        window.quit()
        window.destroy()

    window = tkinter.Tk()

    # 메뉴 자체를 생성함.
    mainMenu = tkinter.Menu(window)
    # 윈도 창의 메뉴로 지정
    window.config(menu=mainMenu)

    # 상위 메뉴 생성, 메뉴 자체에 부착
    fileMenu = tkinter.Menu(mainMenu)
    mainMenu.add_cascade(label="파일", menu=fileMenu)
    # 상위 메뉴의 하위 다른 메뉴 확장
    fileMenu.add_command(label="열기", command=func_open)
    # 중간에 분리 선
    fileMenu.add_separator()
    fileMenu.add_command(label="종료", command=func_exit)

    window.mainloop()

```

##### 대화상자

```python
import tkinter
from tkinter import simpledialog

if __name__ == '__main__':


    window = tkinter.Tk()
    window.geometry("400x100")

    label1 = tkinter.Label(window, text="입력된 값")
    label1.pack()

    value = simpledialog.askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요",
                                                    minvalue=1, maxvalue=6)

    label1.configure(text=str(value))

    window.mainloop()
```

##### 캔버스

```python
import tkinter
from tkinter import simpledialog

if __name__ == '__main__':


    window = tkinter.Tk()

    canvas = simpledialog.Canvas(window, height=300, width=300)
    canvas.pack()

    canvas.create_line([[0,0], [70,70], [30, 170]], fill="blue", width=3)
    canvas.create_polygon([[100,100], [100, 150], [150, 150], [150, 100]], fill="red")
    canvas.create_text([200,200], text="이것이 MySQL이다", font=("굴림", 15))

    window.mainloop()
```