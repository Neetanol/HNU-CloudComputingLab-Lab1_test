# Lab1测试程序说明(基于python3)

## 环境依赖

`python3`  即可

## 功能说明

本测试程序主体是 `Judgement_Lab1_czq_v1.py`
测试过程中，仅需要将你编译完成的可执行文件放到`Judgement_Lab1_czq_v1.py`的相同文件目录下。
本地测试时可以根据自己的测试需求修改测试代码和数独题目源文件。
测试包括：
+ 验证正确性
+ 相对于助教给的可执行文件的性能(运行时间之商)

测试结果仅供参考，不代表最终分数

## 使用前准备

#### 安装`python3`

安装指令 `sudo apt install python3`
检查安装好的python3版本 `python3 --version`

#### 确认运行环境

确认你准备进行测试的目录下有
`Judgement_Lab1_czq_v1.py`
`puzzles` 文件夹
`TA_sudoku_solve`
`sudoku_solve`  或者可正确执行 `make` 指令的 相关文件(如`Makefile`)

#### C++ Makefile文件写法示例

```
CXXFLAGS+=-O2 -ggdb -DDEBUG
CXXFLAGS+=-Wall -Wextra

all: sudoku_solve

sudoku_solve: ./src/remake_main.cpp ./src/sudoku_dancing_links.cpp
	g++ -std=c++11 -O2 -o $@ $^ -lpthread
```

## 执行测试

`python3 Judgement_Lab1_czq_v1.py`

一般来说本地自测就不需要动`puzzles`文件夹了，助教给的用例足够测出性能趋势

## 文件目录&说明

### 初始状态下的文件目录

```
.
├── Judgement_Lab1_czq_v1.py
├── TA_sudoku_solve         # 助教的可执行文件
├── puzzles                 # 数独题目文件的文件夹，里面的文件名字无所谓
│   ├── 7.in                # 只要内容文本能打开就行
│   ├── 70.in               # 本测试程序没有做输入文件的数独内容合理性检查
│   ├── 700.in              # 如果使用自己的数据进行测试，请确保数独题目没有多种解
│   ├── 7000.in
│   └── 70000.in
└── readme.md
```

### 运行后目录

```

.
├── Judgement_Lab1_czq_v1.py
├── TA_sudoku_solve         # 助教的可执行文件
├── sudoku_solve            # 你自己的可执行文件，如果没有则确保你在该目录下有 Makefile 文件
├── puzzles                 # 数独题目文件的文件夹
│   ├── 7.in
│   ├── 70.in
│   ├── 700.in
│   ├── 7000.in
│   └── 70000.in
├── case_info               # 测试程序根据puzzles自动生成的测试用例，供查验
│   ├── advanced_case_1.txt
│   ├── ...
│   ├── advanced_case_5.txt
│   ├── basic_case_1.txt
│   ├── ...
│   └── basic_case_5.txt
├── TA_answers              # 助教的可执行文件运算完的结果重定向到这里，供查验
│   ├── advanced_case_1.out
│   ├── ...
│   ├── advanced_case_5.out
│   ├── basic_case_1.out
│   ├── ...
│   └── basic_case_5.out
├── student_answers         # 你的可执行文件运算完的结果重定向到这里，供查验
│   ├── advanced_case_1.out
│   ├── ...
│   ├── advanced_case_5.out
│   ├── basic_case_1.out
│   ├── ...
│   └── basic_case_5.out
└── (Maybe) Makefile        # 如果你没有在这个目录下存放可执行文件，请确保你的make指令是可用的
```

## 正确运行后的情形

```
neetanol@DESKTOP-NOGOUCK:/mnt/f/workspace/Lab1_test$ python3 ./Judgement_Lab1_czq_v1.py 
Totally load 5 sudoku files.
Lab1 Basic test:
basic_case_1: state is accept! student used 10 ms. Performance score: 0.80
basic_case_2: state is accept! student used 10 ms. Performance score: 0.99
basic_case_3: state is accept! student used 15 ms. Performance score: 1.00
basic_case_4: state is accept! student used 67 ms. Performance score: 0.96
basic_case_5: state is accept! student used 595 ms. Performance score: 1.01
Accept 5/5 cases. Reference performance score is 0.952183.
Lab1 Advanced test:
advanced_case_1: state is accept! student used 9 ms. Performance score: 1.02
advanced_case_2: state is accept! student used 12 ms. Performance score: 0.91
advanced_case_3: state is accept! student used 18 ms. Performance score: 1.01
advanced_case_4: state is accept! student used 78 ms. Performance score: 0.97
advanced_case_5: state is accept! student used 644 ms. Performance score: 1.00
Accept 5/5 cases. Reference performance score is 0.981851.

```
