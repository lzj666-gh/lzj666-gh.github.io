# 0x03-前缀和与差分-最高的牛 (翻译版)

## 题目描述

### 题目描述：

FarmerJohn 有n头牛，它们按顺序排成一列。 FarmerJohn 只知道其中最高的奶牛的序号及它的高度，其他奶牛的高度都是未知的。现在 FarmerJohn 手上有$R$条信息，每条信息上有两头奶牛的序号（$a$和$b$），其中$b$奶牛的高度一定大于等于$a$奶牛的高度，且$a$，$b$之间的所有奶牛的高度都比$a$小。现在$FarmerJohn$想让你根据这些信息求出每一头奶牛的可能的最大的高度。（数据保证有解）

### 输入格式：

第1行：四个以空格分隔的整数：$n$，$i$，$h$和$R$（$n$和$R$意义见题面; $i$ 和 $h$ 表示第 $i$ 头牛的高度为 $h$ ，他是最高的奶牛）

接下来R行：两个不同的整数$a$和$b$（1 ≤ $a$，$b$ ≤ n）

### 输出格式：

一共n行，表示每头奶牛的最大可能高度.

### 数据范围：

1 ≤ n ≤ 10000 ; 1 ≤ h ≤ 1000000 ; 0 ≤ R ≤ 10000)



## 输入格式

Line 1: Four space-separated integers: N, I, H and R


Lines 2..R+1: Two distinct space-separated integers A and B (1 ≤ A, B ≤ N), indicating that cow A can see cow B.


## 输出格式

Lines 1..N: Line i contains the maximum possible height of cow i.


## 时空限制

时间限制: 1000 ms
内存限制: 64 MB
