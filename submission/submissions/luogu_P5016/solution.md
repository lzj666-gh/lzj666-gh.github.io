# P5016 题解

# 此题解很长，请做好心理准备

首先……这题我在考场上打了一个暴力

当时我觉得这题很简单，就是先输入，p1位置加s1个工兵，然后依次枚举把s2个工兵放在所有的兵营里，每次算一遍双方势力之差，取最小就行了

然而我万万没想到竟然超时了……

详见代码，接下来解释为什么超时

```
#include <cstdio>

int m, p1, s1, s2, a[1000005];
int n;

int compute (int x) {//计算双方势力之差
    int sum1 = 0, sum2 = 0;//计算左边和右边
    a[x] += s2;//先假设位置x加上s2个工兵
    for(int i = 1; i <= n; i ++ ) {
        if(i == m) continue;//m号兵营跳过
        else if(i < m) sum1 += (m - i) * a[i];//m左边的兵营
        else sum2 += (i - m) * a[i];
    }
    a[x] -= s2;//再减去s2个，因为是假设加上了s2个工兵
    if(sum1 >= sum2) return sum1 - sum2; return sum2 - sum1;
}

int main () {
    
    int min = 2e8, where;
    
    scanf("%d", &n);
    for(int i = 1; i <= n; i ++ )
        scanf("%d", &a[i]);
    scanf("%d%d%d%d", &m, &p1, &s1, &s2);
    
    a[p1] += s1;//加上s1个工兵
    
    for(int i = 1; i <= n; i ++ ) {
        int tmp = compute(i);//算一下势力之差
        if(min > tmp) {//如果比之前的最小还小（因为如果势力之差一样小就取编号小的，所以没等号）
            min = tmp;
            where = i;
        }
    }
    
    printf("%d", where);
    
    return 0;
}
```

为什么超时了呢？原因在于每次都算了一遍势力之差。

时间复杂度是$O(n^2)$

啥？那咋办？

就提前算好龙方和虎方的势力之差，每次枚举的时候就直接算一下新的势力之差就行了

别着急，没完呢，别抄这个，~~因为也是错的~~

```
#include <cstdio>

inline int abs (int x, int y) {//相减后再算绝对值
    if(x >= y) return x - y;
    return y - x;
}

int m, p1, s1, s2, a[1000005];
int n;

int main () {
    
    int min = 2e8, where;
    int sum1 = 0, sum2 = 0;//分别提前算好左边和右边的势力
    
    scanf("%d", &n);
    for(int i = 1; i <= n; i ++ ) {
        scanf("%d", &a[i]);
    }
    scanf("%d%d%d%d", &m, &p1, &s1, &s2);
    
    a[p1] += s1;
    
    for(int i = 1; i <= n; i ++ ) {
        if(i < m) sum1 += (m - i) * a[i];
        else if(i > m) sum2 += (i - m) * a[i];//这是预处理，算好左边和右边的势力之差
    }
    
    for(int i = 1; i <= n; i ++ ) {
        if(i < m) sum1 += (m - i) * s2;
        else if(i > m) sum2 += (i - m) * s2;//算出新的双方势力
        int tmp = abs(sum1, sum2);//相减后算绝对值
        if(min > tmp) {
            min = tmp;
            where = i;
        }
        if(i < m) sum1 -= (m - i) * s2;
        else if(i > m) sum2 -= (i - m) * s2;//退栈
    }
    
    printf("%d", where);
    
    return 0;
}
```

满怀激动地提交，结果，后五个点WA了。。。

问题出在哪里？

原因是没开$long$ $long$。。。

因为虽然一个数$int$存的下，但加起来可是会超过$int$的啊！

（估算了下，在$1e18$ ~ $9e18$之间，$long$ $long$刚好够）

~~ 可恶的CCFNOI，竟然卡你$long$ $long$ ~~

于是，开成$long$ $long$就过了：

```
#include <cstdio>

inline long long abs (long long x, long long y) {
    if(x >= y) return x - y;
    return y - x;
}

long long m, p1, s1, s2, a[1000005];
int n;

int main () {
    
    long long min = 1e19, where;
    long long sum1 = 0, sum2 = 0;
    long long t1, t2;
    
    scanf("%d", &n);
    for(int i = 1; i <= n; i ++ ) {
        scanf("%lld", &a[i]);
    }
    scanf("%lld%lld%lld%lld", &m, &p1, &s1, &s2);
    
    a[p1] += s1;
    
    for(int i = 1; i <= n; i ++ ) {
        if(i < m) sum1 += (m - i) * a[i];
        else if(i > m) sum2 += (i - m) * a[i];
    }
    
    for(int i = 1; i <= n; i ++ ) {
        t1 = sum1;
        t2 = sum2;
        if(i < m) t1 += (m - i) * s2;
        else if(i > m) t2 += (i - m) * s2;
        long long tmp = abs(t1, t2);
        if(min > tmp) {
            min = tmp;
            where = i;
        }
    }
    
    printf("%lld", where);
    
    return 0;
}
```

好吧，虽然已经AC了，但是~~本人还是觉得不够快~~，于是想到了**方程法**！

啥？这题还能用方程？

是的！题目不就是求p2吗？我们把p2看成一个未知数，有了方程等式，不就行了？

可是，方程式子从哪来呢？

首先，我们用一个变量$gap$提前算好双方势力之差，大概这么写：

```
    for(int i = 1; i <= n; i ++ ) {
    	gap += (m - i) * a[i];
    }
```

然后让我们看看如何推导出方程式：

$gap+(m-p2)s2=0$

$gap+s2*m-s2*p2=0$

$gap+s2*m=s2*p2$

$gap/s2+m=p2$

这里，除了$p2$以外其他的不都是已知的吗？

对啊！这题不就能用方程解了吗？

没完呢，解出来之后还得用$double$存下来呢！

为什么呢？因为不一定正解真的有势力之差为$0$的兵营

此时就分四种情况：

- 小于等于$1$
- 大于等于$n$
- 大于$1$且小于$n$且是整数
- 大于$1$且小于$n$且是小数

这四种情况对应的操作：

- 输出$1$
- 输出$n$
- 输出$p2$
- 看的把$s2$个工兵放在向下取整和向上取整两个兵营里那个势力之差更小就输出哪个

顺便介绍下三目运算符：

```
部分1?部分2:部分3
```

的意思是如果判断条件```部分1```为真，就执行```部分2```，否则执行```部分3```

然后就是代码

```
#include <bits/stdc++.h>

inline long long read () {
    register long long x = 0 , ch = getchar();
    while( !isdigit(ch)) ch = getchar();
    while( isdigit(ch) ) x = x * 10 + ch - '0' , ch = getchar();
    return x;
}

inline long long abs (long long x) {
    if(x >= 0) return x;
    return -x;
}

long long m, p1, s1, s2, a[1000005], t1, t2;
int n;

int main () {
    
    double where;
    long long gap;
    
    n = read();
    for(int i = 1; i <= n; i ++ ) {
        a[i] = read();
    }
    m = read();
    p1 = read();
    s1 = read();
    s2 = read();//这些都是快读，不用管
    a[p1] += s1;
    
    for(int i = 1; i <= n; i ++ ) {
    	gap += (m - i) * a[i];
    }
    double dgap = gap;
    long long int ans;
    where = m + dgap / s2;//方程的解
    
    if(where >= n) {//大于等于n的情况
    	ans = n;
    }
    else if(where <= 1)//小于等于1的情况
        ans = 1;
    else {
        int iwhere = where;//判断是不是整数
        if(iwhere == where) ans = iwhere;//如果是整数
        else {
            long long ans1 = abs(gap + (m - iwhere ) * s2);
            long long ans2 = abs(gap + (m - iwhere - 1) * s2);//分别计算把s2个工兵放在向下取整和向上取整两个兵营里之后的势力之差
            ans = ans1 <= ans2 ? iwhere : iwhere + 1;//三目运算符
        }
    }
    
    printf("%lld", ans);//答案输出
    
    return 0;
}
```

以上是$O(n)$算法，$7ms$的测试点的时间都是花在输入了

//以上还得感谢[Steven_Meng](https://www.luogu.org/space/show?uid=45109)指出的错误

[评测记录](https://www.luogu.org/record/show?rid=13772274)

# 安慰一下没开$long$ $long$而丢掉20分的大佬

下面是求赞：

# 我的题解可能写得不太好，但你看的这么认真，不点个赞再走吗？