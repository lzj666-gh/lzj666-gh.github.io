# P1725 题解




先无良宣传一下博客 $wwwwww$    
[文章列表 - 地灵殿 - 洛谷博客](https://www.luogu.org/blog/koishikoishi/)

$\text{Updata on 2019.11.10}$ : 全部重构   
感谢 胖虎x 与 Grass2_Ofalen  提出问题 $\sim$   
删除了之前由于数据水卡过去的 优先队列做法   

---

## 知识点 : $DP$ , 单调队列优化   

### [原题面](https://www.luogu.org/problem/P1725)   

### 题目要求 :   
  
  给定一长度为 $N + 1$ 的数列 $A$ , 第 $1$ 项为 $0$    
  以第一项为起点 ,  对于当前的位置 $i$    
  可以转移到: $(i + L, i + R)$ 中任意一位置       
  并且获得当前位置上 数的价值  .    
  
  求 : 当位置 $\ge N + 1$ 时可以取得的 最大价值和   
  
---

### 分析题意:   

  很显然的 $DP$ .   
  设 $f[i]$ 为: 到达位置 $i$ 时最大的价值和 , 则状态转移方程如下 :    
  $f[i] = \max(f[j]) + A[i]\ \ (i -R \le j \le i - L)$    
  
- 我会暴力 $!$     
  枚举每一位置 , 枚举每一可转移到该位置的 位置, 暴力进行转移   
  复杂度 $O(n ^ 2)$ , 取得了 $60$ 分的好成绩 (大雾)   
 
考虑优化 :   
 
   1. 转移到 位置 $i$ 的位置 ,  为区间 $\underline{[i-R,i+L]}$ 中 , $f[]$ 最大的位置   
  
   2. 转移到 位置 $i + 1$ 的位置 ,  为区间 $\underline{[i-R + 1,i-L + 1]}$ 中 , $f[]$ 最大的位置   
  
   3. 转移到 位置 $i + 2$ 的位置 ,  为区间 $\underline{[i - R + 2,i - L + 2]}$ 中 , $f[]$ 最大的位置   
  
后两个区间 ,  都可以通过 上一个区间 **右移一个单位** 得到    
这不禁让我们想到了另一道题 :    [P1886 滑动窗口](https://www.luogu.org/problemnew/show/P1886)  
如果您还未学习过单调队列 , 推荐这篇文章:     
[【洛谷日报﻿#9】 [Sweetlemon] 朝花中学OI队的奋斗历程——浅谈单调队列](https://sweetlemon.blog.luogu.org/dan-diao-dui-lie)    
  
这种 **滑动窗口型** 最值问题 ,  显然 , 可以通过 单调队列 来进行维护  .   
由上 ,  我们便找到了一种合适 $DP$ 优化方法 : 单调队列优化 .   

---

### 算法实现 :

顺序枚举 $[L, N]$ 的每一个位置 $i$.   
1. 将能够转移到 $i$ 的最靠右的位置 插入单调队列中   
2. 删除 单调队列首 不能转移到 $i$ 的位置   
3. 查询当前单调队列首的位置 , 即为能够转移到 $i$ 的价值最大的位置   
4. 若 $i + R > N$ , 说明位置 $i$ 能够跳到对岸 , 对此类位置的权值和取最大值, 即为答案   

---

附 $AC$ 代码 : 

```cpp
//By:Luckyblock
//バカって言うなぁ
#include <cstdio>
#include <cstring>
#include <ctype.h>
#define max(a, b) (a > b ? a : b)
const int MARX = 2e5 + 10;
const int INF = 2e9;
//=============================================================
int N, L, R, A[MARX], ans, f[MARX];//设 f[i]: 到达位置 i 时最大的价值和
int que[MARX], head = 1, tail = 1;//单调队列, 内部元素为位置 
//=============================================================
inline int read()
{
    int s = 1, w = 0; char ch = getchar();
    for(; !isdigit(ch); ch = getchar()) if(ch == '-') s = -1;
    for(; isdigit(ch); ch = getchar()) w = (w << 1) + (w << 3) + (ch ^ '0');
    return s * w;
}
void Insert(int i)//插入操作 
{
	for(; f[i] >= f[que[tail]] && tail >= head; ) tail --;//弹出权值和较小的 队尾元素 
	que[++ tail] = i;//入队 
}
int query(int x)
{
	for(; que[head] + R < x; ) head ++;//弹出队首 不可到达x位置的 不合法元素 
	return que[head];//回答询问 
}
//=============================================================
int main()
{
	memset(f, 128, sizeof(f));//初始化极小值 (每个字节赋128会导致自然溢出 
	f[0] = 0, ans = - INF; //初始化, 将0位置权值和 赋为0  
	N = read(), L = read(), R = read();
	for(int i = 0; i <= N; i ++) A[i] = read();
	
	for(int i = L; i <= N; i ++)
	{
	  Insert(i - L); //将最后一个 能够转移到i的位置 加入单调队列 
	  int from = query(i);//找到队首 权值和最大的位置 
	  f[i] = f[from] + A[i];//进行转移 
	  if(i + R > N) ans = max(ans, f[i]);//判断i能够跳到对岸, 计算答案 
	}
	printf("%d", ans);
	return 0;
}
```

---

附评论区的 $\text{Hack}$ 数据 , 重构题解后已过  


testdata1.in:   
```
5 3 4 0 1 2 3 4 5
```

testdata1.out   
```
4
```

testdata2.in:   
```
7 4 4 0 1 -4 -2 2 -5 3 2
```
testdata2.out:   
``` 
2
```

---

完成了这篇题解 , 东方众信仰 $++$  