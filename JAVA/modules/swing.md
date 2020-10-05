#### swing

```java
import java.awt.*;
import javax.swing.*;

public class MyGUI {

    public static void main(String[] args){
        // heavyweight container
        // 메모리에 생성된다.
        JFrame frame = new JFrame("My GUI Example");    // title
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);   // 윈도 창을 x버튼으로 닫으면 프로그램 종료

        // lightwight container
        JPanel primary = new JPanel();
        primary.setPreferredSize(new Dimension(400, 300));  // width, height
        primary.setBackground(Color.yellow);

        // layout manager disable
        // add 하는 component 의 크기와 위치를 직접 정해줘야한다.
        primary.setLayout(null);

        // component
        JLabel lbl1, lbl2;

        // lightweight container는 그냥 add 한다
        // container 에는 (flow)layout manager 가 있어서 자동으로 조정
        // 먼저 add 된 것 먼저
        lbl1 = new JLabel("SKKU University");   // text

        // 아래 매개변수에서와 같은 객체를
        // anonymous object 라고 한다.
        // 같은 매개 변수가 lbl1과 lbl2에 전달되었으므로
        // Font fnt = new Font("Verdana", Font.BOLD, 20);   // name, font, size
        // 객체 생성해서 전달하는것 권장된다.
        lbl1.setFont(new Font("Verdana", Font.BOLD, 20));
        lbl1.setForeground(Color.red);

        // layout manager가 없을 때 직접 크기와 위치를 결정
        // width 가 글자 크기보다 작으면 ... 으로 표현된다.
        lbl1.setBounds(100, 50, 200, 50);   // x, t, width, height
        primary.add(lbl1);


        lbl2 = new JLabel("Hong, gildong");
        lbl2.setFont(new Font("Verdana", Font.BOLD, 20));
        lbl2.setForeground(Color.magenta);
        lbl2.setBounds(100, 110, 200, 50);
        primary.add(lbl2);


        // heavyweight container에 add 할 때 아래 함수를 써야한다.
        frame.getContentPane().add(primary);
        frame.pack();
        frame.setVisible(true); // 메모리에 있던 프레임이 보이도록, false 하면 안보이게 된다.
    }   // main()
}   // MYGUI class


```
##### Nested Panel

```java
import java.awt.*;
import javax.swing.*;

public class NestedPanel {

    public static void main(String[] args) {
        JFrame frame = new JFrame("Nested Panel Test");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 각각의 container의 layout manager 는 독립적이다.
        // 중첩된 panel 의 layout manager 도 없애려면 각각 set 해줘야 한다.
        JPanel primaryPanel = new JPanel();
        primaryPanel.setBackground(Color.white);
        primaryPanel.setPreferredSize(new Dimension(630, 420));
        primaryPanel.setLayout(null);

        JPanel leftPanel, rightPanel;
        leftPanel = new JPanel();
        leftPanel.setBounds(10, 10, 300, 400);
        leftPanel.setBackground(Color.pink);
        leftPanel.setLayout(null);
        primaryPanel.add(leftPanel);

        rightPanel = new JPanel();
        rightPanel.setBounds(320, 10, 300, 400);
        rightPanel.setBackground(Color.cyan);
        primaryPanel.add(rightPanel);

        Font fnt = new Font("Verdana", Font.BOLD, 30);

        JLabel lblOne, lblTwo;
        lblOne = new JLabel("ONE");
        lblOne.setFont(fnt);

        // leftPanel 을 기준으로 좌표를 설정해줘야 한다.
        // Label의 크기는 커졌지만
        // font 의 size 는 30 이므로 수직에 대해 가운데에 놓인다.
        lblOne.setBounds(0, 0, 300, 400);
        // 수평에 대해 가운데로
        lblOne.setHorizontalAlignment(SwingConstants.CENTER);
        // 수직에 대해 바닥으로
        lblOne.setVerticalAlignment(SwingConstants.BOTTOM);
        leftPanel.add(lblOne);

        lblTwo = new JLabel("TWO");
        lblTwo.setFont(fnt);
        rightPanel.add(lblTwo);


        frame.getContentPane().add(primaryPanel);
        frame.pack();
        frame.setVisible(true);
    }   // main()
}   // NestedPanel class
```

##### ImageIcon

```java
import java.awt.*;
import javax.swing.*;

public class NestedPanel {

    public static void main(String[] args) {
        JFrame frame = new JFrame("Nested Panel Test");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel primaryPanel = new JPanel();
        primaryPanel.setBackground(Color.white);
        primaryPanel.setPreferredSize(new Dimension(630, 420));
        primaryPanel.setLayout(null);

        JPanel leftPanel, rightPanel;
        leftPanel = new JPanel();
        leftPanel.setBounds(10, 10, 300, 400);
        leftPanel.setBackground(Color.white);
        leftPanel.setLayout(null);
        primaryPanel.add(leftPanel);

        rightPanel = new JPanel();
        rightPanel.setBounds(320, 10, 300, 400);
        rightPanel.setBackground(Color.cyan);
        primaryPanel.add(rightPanel);

        Font fnt = new Font("Verdana", Font.BOLD, 30);

        ImageIcon icon = new ImageIcon("images/testimage.png");

        JLabel lblOne, lblTwo;
        lblOne = new JLabel("ONE", icon, SwingConstants.CENTER);
        // text에 대한 정렬
        lblOne.setHorizontalTextPosition(SwingConstants.CENTER);
        lblOne.setVerticalTextPosition(SwingConstants.BOTTOM);
        lblOne.setFont(fnt);
        lblOne.setBounds(0, 0, 300, 400);
        leftPanel.add(lblOne);

        lblTwo = new JLabel("TWO");
        lblTwo.setFont(fnt);
        rightPanel.add(lblTwo);


        frame.getContentPane().add(primaryPanel);
        frame.pack();
        frame.setVisible(true);
    }   // main()
}   // NestedPanel class
```