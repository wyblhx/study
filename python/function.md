## 函数
**函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。**
### 定义
1. 语法
<font size=5>

```python
def 函数名([参数1,参数2,...]):
  函数体 #代码段
```

</font>

2. 例子
函数功能：打印数字

<font size=5>

```python
import random
def print_num():
  ran=random.randint(1,10) #生成1-10之间的随机整数
  print(ran)
```

</font>

### 函数调用
函数名([参数1,参数2,...])

### 函数参数
1. 不变参数
2. 可变参数
def functionnname(*args)

<font size=5>

```python
def add(*args):
    # print(args)  # ()空元组

    # 求和
    sum_ = 0
    if len(args) <= 0:
        print('没有元素传入')
    else:
        for i in args:
            sum_ += i

    print('所有元素的和是', sum_)
#调用函数
add(1,2,3)
add(1)
add(1,2,3,4,5)
  ```

</font>

**注意：**

- *args-系统会默认准备一个元组

- 调用-functionnname()

3. 关键字参数：不变关键字参数、可变关键字参数
def functionnname(**kwargs)
**注意：**
- **kwargs-系统会默认准备一个字典,当 **出现再函数定义时，是将关键字（a=1,b=2）装成字典（{a:1,b:2}）,当 **出现再调用函数时，是将字典拆分成关键字

4. 列表参数
