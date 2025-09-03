# Convex Hull of the Polygon (翻译版)

## 题目描述

### 题目描述
给出一个整点多边形 (可能会有**重复的坐标**)
$$\left\{(x_0, y_0),\ (x_1,y_1),\ \dots,(x_n,y_n),\ (x_0,y_0)\right\}$$
求出它的最小凸包.

### 诡异的输入格式
输入包含多组数据, 以**一空行分隔**. 每组数据包含若干行 $x_i, y_i$ (未给出 $n$).  

数据保证多边形至少有三个不同的点

### 奇怪的输出格式
以若干行 $x_i, y_i$ 的格式输出凸包.  
第一个坐标必须是**按输入顺序的第一个是凸包的点**, 且逆时针输出.  
每组输出以一个空行分隔, 不要有多余的空行和字符.

可以在 [uDebug](https://www.udebug.com/UVa/675) 上检测格式是否正确

## 输入格式

![](https://cdn.luogu.com.cn/upload/vjudge_pic/UVA675/0e78b11131d61b112b529e60666fb52b5042d06f.png)

## 输出格式

![](https://cdn.luogu.com.cn/upload/vjudge_pic/UVA675/6ef41450e4b310b42abc3825ecd73acf2b7c2971.png)

## 时空限制

时空限制信息获取失败
