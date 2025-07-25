# 「SFMOI Round I」Strange Cake Game

## 题目描述


有一块面积为 $n\times m$ 的矩形蛋糕。记其左上角顶点为 $(0,0)$，右下角顶点为 $(n,m)$，右上角顶点为 $(0,m)$。

蛋糕上分布着 $k$ 块巧克力，第 $i$ 块的位置为 $(x_i-0.5,y_i-0.5)$。**一个点上可能有不止一块巧克力。**

小 M 和 小 W 要切蛋糕。蛋糕刀起初在 $(0,0)$，小 W 先手，轮流移动蛋糕刀。设蛋糕刀在 $(x,y)$，则它可以被移动到 $(x,y+1)$ 或 $(x+1,y)$。

在若干步后，蛋糕会被切割轨迹完全分成两个部分——右上角的部分归小 W，左下角的部分归小 M。小 W 和小 M 都想吃到最多的巧克力，请帮他们计算：如果双方都按照最优策略行动，小 W 能分到几块巧克力。

如下是蛋糕的示例和一种可能的切蛋糕的方式。

![蛋糕示例](https://cdn.luogu.com.cn/upload/image_hosting/er9wuv91.png?x-oss-process=image/resize,m_lfit,h_500)
![切蛋糕示例](https://cdn.luogu.com.cn/upload/image_hosting/9o6ntvlb.png?x-oss-process=image/resize,m_lfit,h_500)

## 输入格式

第一行，两个正整数 $n,m$，含义见题面。

第二行，一个整数 $k$ ，表示巧克力块数。

接下来 $k$ 行，每行两个正整数 $x_i,y_i$，表示第 $i$ 块巧克力的坐标为 $(x_i-0.5,y_i-0.5)$。

注意：第 $i$ 块巧克力的坐标为 $(x_i-0.5,y_i-0.5)$。**一个格子上可能有多块巧克力。**

## 输出格式

输出一个整数，代表小 W 最多能拿到的巧克力块数。

## 提示

### 数据范围

**本题采用捆绑测试。**

- Subtask 1（5 pts）：$n=m=1$；
- Subtask 2（10 pts）：$1 \le n \times m \le 60$；
- Subtask 3（15 pts）：$1 \le n \times m \le 10^5$；
- Subtask 4（20 pts）：$k=1$；
- Subtask 5（50 pts）：无特殊限制。


对于 $100\%$ 的数据，保证：

- $0 \le k \le 2 \times 10^5$；
- $1 \le n,m \le 10^{18}$；
- $1 \le x_i \le n$，$1 \le y_i \le m$。


## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
