# P3803 题解

# [更好的阅读体验点这里](http://www.cnblogs.com/zwfymqz/p/8244902.html)




# 多项式

## 系数表示法

设$A(x)$表示一个$n-1$次多项式

则$A(x)=\sum_{i=0}^{n} a_i * x^i$

例如：$A(3)=2+3*x+x^2$

利用这种方法计算多项式乘法复杂度为$O(n^2)$

（第一个多项式中每个系数都需要与第二个多项式的每个系数相乘）

## 点值表示法

将$n$互不相同的$x$带入多项式，会得到$n$个不同的取值$y$

则该多项式被这$n$个点$(x_1,y_1),(x_2,y_2),\dots,(x_n,y_n)$唯一确定

其中$y_i=\sum_{j=0}^{n-1} a_j*x_i^j$

例如：上面的例子用点值表示法可以为$(0,2),(1,5),(2,12)$

利用这种方法计算多项式乘法的时间复杂度仍然为$O(n^2)$

（选点$O(n)$，每次计算$O(n)$）

 

我们可以看到，两种方法的时间复杂度都为$O(n^2)$，我们考虑对其进行优化

对于第一种方法，由于每个点的系数都是固定的，想要优化比较困难

对于第二种方法，貌似也没有什么好的优化方法，不过当你看完下面的知识，或许就不这么想了

 

#　复数

在介绍复数之前，首先介绍一些可能会用到的东西

## 向量

同时具有大小和方向的量

在几何中通常用带有箭头的线段表示

## 圆的弧度制

等于半径长的圆弧所对的圆心角叫做1弧度的角，用符号rad表示，读作弧度。用弧度作单位来度量角的制度叫做弧度制

公式:

$1^{\circ }=\dfrac{\pi}{180}rad$

$180^{\circ }=\pi rad$

## 平行四边形定则

平行四边形定则：AB+AD=AC

## 复数

### 定义

设$a,b$为实数，$i^2=-1$，形如$a+bi$的数叫负数，其中$i$被称为虚数单位，复数域是目前已知最大的域

在复平面中，$x$代表实数，$y$轴（除原点外的点）代表虚数，从原点$(0,0)$到$(a,b)$的向量表示复数$a+bi$

模长：从原点$(0,0)$到点$(a,b)$的距离，即$\sqrt{a^2+b^2}$

幅角：假设以逆时针为正方向，从$x$轴正半轴到已知向量的转角的有向角叫做幅角

### 运算法则

加法：

因为在复平面中，复数可以被表示为向量，因此复数的加法与向量的加法相同，都满足平行四边形定则（就是上面那个）

乘法：

几何定义：复数相乘，模长相乘，幅角相加

代数定义：$$(a+bi)*(c+di)$$

$$=ac+adi+bci+bdi^2$$

$$=ac+adi+bci-bd$$

$$=(ac-bd)+(bc+ad)i$$

 

单位根

下文中，默认$n$为$2$的正整数次幂

在复平面上，以原点为圆心，$1$为半径作圆，所得的圆叫单位圆。以圆点为起点，圆的$n$等分点为终点，做$n$个向量，设幅角为正且最小的向量对应的复数为$\omega_n$，称为$n$次单位根。

根据复数乘法的运算法则，其余$n-1$个复数为$\omega_n^2,\omega_n^3,\ldots,\omega_n^n$

注意$\omega_n^0=\omega_n^n=1$（对应复平面上以$x$轴为正方向的向量）

那么如何计算它们的值呢？这个问题可以由欧拉公式解决$$\omega_{n}^{k}=\cos\ k *\frac{2\pi}{n}+i\sin k*\frac{2\pi}{n}$$

 

单位根的幅角为周角的$\dfrac{1}{n}$

在代数中，若$z^n=1$，我们把$z$称为$n$次单位根

单位根的性质

$\omega _{n}^{k}=\cos k\dfrac{2\pi}{n}+i\sin k\dfrac {2\pi }{n}$（即上面的公式）
$\omega _{2n}^{2k}=\omega _{n}^{k}$
证明：

$$\omega _{2n}^{2k}=\cos 2k*\frac{2\pi}{2n}+i\sin2k*\frac{2\pi}{2n}$$

$$=\omega _{n}^{k}$$

$\omega _{n}^{k+\frac{n}{2}}=-\omega _{n}^{k}$
$$\omega _{n}^{\frac{n}{2}}=\cos\frac{n}{2}*\frac{2\pi}{n}+i\sin\frac{n}{2}*\frac{2\pi}{n}$$

$$=\cos \pi+i\sin\pi$$

$$=-1$$

$\omega _{n}^{0}=\omega _{n}^{n}=1$
 讲了这么多，貌似跟我们的正题没啥关系啊。。

 OK！各位坐稳了，前方高能！

# 快速傅里叶变换

我们前面提到过，一个$n$次多项式可以被$n$个点唯一确定。

那么我们可以把单位根的$0$到$n-1$次幂带入，这样也可以把这个多项式确定出来。但是这样仍然是$O(n^2)$的呀！

我们设多项式$A(x)$的系数为$(a_o,a_1,a_2,\ldots,a_{n-1})$

那么$$A(x)=a_0+a_1*x+a_2*{x^2}+a_3*{x^3}+a_4*{x^4}+a_5*{x^5}+ \dots+a_{n-2}*x^{n-2}+a_{n-1}*x^{n-1}$$

将其下标按照奇偶性分类

$$A(x)=(a_0+a_2*{x^2}+a_4*{x^4}+\dots+a_{n-2}*x^{n-2})+(a_1*x+a_3*{x^3}+a_5*{x^5}+ \dots+a_{n-1}*x^{n-1})$$

设

 

$$A_1(x)=a_0+a_2*{x}+a_4*{x^2}+\dots+a_{n-2}*x^{\frac{n}{2}-1}$$

$$A_2(x)=a_1*x+a_3*{x}+a_5*{x^2}+ \dots+a_{n-1}*x^{\frac{n}{2}-1}$$

那么不难得到

$$A(x)=A_1(x^2)+xA_2(x^2)$$

我们将$\omega_n^k (k<\frac{n}{2}) $代入得

$$A(\omega_n^k)=A_1(\omega_n^{2k})+\omega_n^kA_2(\omega_n^{2k})$$

$$=A_1(\omega_{\frac{n}{2}}^{k})+\omega_n^kA_2(\omega_{\frac{n}{2}}^{k})$$

同理，将$\omega_n^{k+\frac{n}{2}}$代入得

$$A(\omega_n^{k+\frac{n}{2}})=A_1(\omega_n^{2k+n})+\omega_n^{k+\frac{n}{2}}(\omega_n^{2k+n})$$

$$=A_1(\omega_n^{2k}*\omega_n^n)-\omega_n^kA_2(\omega_n^{2k}*\omega_n^n)$$

$$=A_1(\omega_n^{2k})-\omega_n^kA_2(\omega_n^{2k})$$

 

大家有没有发现什么规律？

没错！这两个式子只有一个常数项不同！

那么当我们在枚举第一个式子的时候，我们可以$O(1)$的得到第二个式子的值

又因为第一个式子的$k$在取遍$[0,\frac{n}{2}-1]$时，$k+\frac{n}{2}$取遍了$[\frac{n}{2},n-1]$

所以我们将原来的问题缩小了一半！

而缩小后的问题仍然满足原问题的性质，所以我们可以递归的去搞这件事情！

直到多项式仅剩一个常数项，这时候我们直接返回就好啦

 

## 时间复杂度：

不难看出FFT是类似于线段树一样的分治算法。

因此它的时间复杂度为$O(nlogn)$

 

# 快速傅里叶逆变换

不要以为FFT到这里就结束了。

我们上面的讨论是基于点值表示法的。

但是在平常的学习和研究中很少用点值表示法来表示一个多项式。

所以我们要考虑如何把点值表示法转换为系数表示法，这个过程叫做傅里叶逆变换

 

$(y_0,y_1,y_2,\dots,y_{n-1})$为$(a_0,a_1,a_2,\dots,a_{n-1})$的傅里叶变换（即点值表示）

设有另一个向量$(c_0,c_1,c_2,\dots,c_{n-1})$满足

$$c_k=\sum_{i=0}^{n-1}y_i(\omega_n^{-k})^i$$

即多项式$B(x)=y_0,y_1x,y_2x^2,\dots,y_{n-1}x^{n-1}$在$\omega_n^{0},\omega_n^{-1},\omega_n^{-2},\dots,\omega_{n-1}^{-(n-1)}$处的点值表示

emmmm又到推公式时间啦

$(c_0,c_1,c_2,\dots,c_{n-1})$满足
$$c_k=\sum_{i=0}^{n-1}y_i(\omega_n^{-k})^i$$

$$=\sum_{i=0}^{n-1}(\sum_{j=0}^{n-1}a_j(\omega_n^i)^j)(\omega_n^{-k})^i$$

$$=\sum_{i=0}^{n-1}(\sum_{j=0}^{n-1}a_j(\omega_n^j)^i)(\omega_n^{-k})^i$$

$$=\sum_{i=0}^{n-1}(\sum_{j=0}^{n-1}a_j(\omega_n^j)^i(\omega_n^{-k})^i)$$

$$=\sum_{i=0}^{n-1}\sum_{j=0}^{n-1}a_j(\omega_n^j)^i(\omega_n^{-k})^i$$

$$=\sum_{i=0}^{n-1}\sum_{j=0}^{n-1}a_j(\omega_n^{j-k})^i$$

$$=\sum_{j=0}^{n-1}a_j(\sum_{i=0}^{n-1}(\omega_n^{j-k})^i)$$

 

设$S(x)=\sum_{i=0}^{n-1}x^i$

将$\omega_n^k$代入得

$$S(\omega_n^k)=1+(\omega_n^k)+(\omega_n^k)^2+\dots(\omega_n^k)^{n-1}$$

当$k!=0$时

等式两边同乘$\omega_n^k$得

$$\omega_n^kS(\omega_n^k)=\omega_n^k+(\omega_n^k)^2+(\omega_n^k)^3+\dots(\omega_n^k)^{n}$$

两式相减得

$$\omega_n^kS(\omega_n^k)-S(\omega_n^k)=(\omega_n^k)^{n}-1$$

$$S(\omega_n^k)=\frac{(\omega_n^k)^{n}-1}{\omega_n^k-1}$$

$$S(\omega_n^k)=\frac{(\omega_n^n)^{k}-1}{\omega_n^k-1}$$

$$S(\omega_n^k)=\frac{1-1}{\omega_n^k-1}$$

观察这个式子，不难看出它分母不为0，但是分子为0

因此，当$K!=0$时，$S(\omega^{k}_{n})=0$

那当$k=0$时呢？

很显然，$S(\omega^{0}_{n})=n$

 

继续考虑刚刚的式子

$$c_k=\sum_{j=0}^{n-1}a_j(\sum_{i=0}^{n-1}(\omega_n^{j-k})^i)$$
当$j!=k$时，值为$0$
当$j=k$时，值为$n$
因此，
$$c_k=na_k$$
$$a_k=\frac{c_k}{n}$$

这样我们就得到点值与系数之间的表示啦

 

# 理论总结

至此，FFT的基础理论部分就结束了。

我们来小结一下FFT是怎么成功实现的

 

首先，人们在用系数表示法研究多项式的时候遇阻

于是开始考虑能否用点值表示法优化这个东西。

然后根据复数的两条性质（这个思维跨度比较大）得到了一种分治算法。

最后又推了一波公式，找到了点值表示法与系数表示法之间转换关系。

 

emmmm

其实FFT的实现思路大概就是

系数表示法—>点值表示法—>系数表示法


 

当然，再实现的过程中还有很多技巧

我们根据代码来理解一下

 

# 递归实现

递归实现的方法比较简单。

就是按找我们上面说的过程，不断把要求的序列分成两部分，再进行合并

在c++的STL中提供了现成的complex类，但是我不建议大家用，毕竟手写也就那么几行，而且万一某个毒瘤卡STL那岂不是很ＧＧ？

 
```
#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
const int MAXN=2*1e6+10;
inline int read()
{
    char c=getchar();int x=0,f=1;
    while(c<'0'||c>'9'){if(c=='-')f=-1;c=getchar();}
    while(c>='0'&&c<='9'){x=x*10+c-'0';c=getchar();}
    return x*f;
}
const double Pi=acos(-1.0);
struct complex
{
    double x,y;
    complex (double xx=0,double yy=0){x=xx,y=yy;}
}a[MAXN],b[MAXN];
complex operator + (complex a,complex b){ return complex(a.x+b.x , a.y+b.y);}
complex operator - (complex a,complex b){ return complex(a.x-b.x , a.y-b.y);}
complex operator * (complex a,complex b){ return complex(a.x*b.x-a.y*b.y , a.x*b.y+a.y*b.x);}//不懂的看复数的运算那部分 
void fast_fast_tle(int limit,complex *a,int type)
{
    if(limit==1) return ;//只有一个常数项
    complex a1[limit>>1],a2[limit>>1];
    for(int i=0;i<=limit;i+=2)//根据下标的奇偶性分类
        a1[i>>1]=a[i],a2[i>>1]=a[i+1];
    fast_fast_tle(limit>>1,a1,type);
    fast_fast_tle(limit>>1,a2,type);
    complex Wn=complex(cos(2.0*Pi/limit) , type*sin(2.0*Pi/limit)),w=complex(1,0);
    //Wn为单位根，w表示幂
    for(int i=0;i<(limit>>1);i++,w=w*Wn)//这里的w相当于公式中的k 
        a[i]=a1[i]+w*a2[i],
        a[i+(limit>>1)]=a1[i]-w*a2[i];//利用单位根的性质，O(1)得到另一部分 
}
int main()
{
    int N=read(),M=read();
    for(int i=0;i<=N;i++) a[i].x=read();
    for(int i=0;i<=M;i++) b[i].x=read();
    int limit=1;while(limit<=N+M) limit<<=1;
    fast_fast_tle(limit,a,1);
    fast_fast_tle(limit,b,1);
    //后面的1表示要进行的变换是什么类型
    //1表示从系数变为点值
    //-1表示从点值变为系数 
    //至于为什么这样是对的，可以参考一下c向量的推导过程， 
    for(int i=0;i<=limit;i++)
        a[i]=a[i]*b[i];
    fast_fast_tle(limit,a,-1);
    for(int i=0;i<=N+M;i++) printf("%d ",(int)(a[i].x/limit+0.5));//按照我们推倒的公式，这里还要除以n 
    return 0;
}
 
```
这里还有一个听起来很装B的优化—蝴蝶效应

观察合并的过程，w*a2[i] 这一项计算了两次，因为理论上来说复数的乘法是比较慢的，所以我们可以把这一项记出来
```
    for(int i=0;i<(limit>>1);i++,w=w*Wn)//这里的w相当于公式中的k 
    {
        complex t=w*a2[i];//蝴蝶效应
        a[i]=a1[i]+t,
        a[i+(limit>>1)]=a1[i]-t;//利用单位根的性质，O(1)得到另一部分     
    }

```



速度什么的才不是关键呢？

关键是我们AC不了啊啊啊

表着急，AC不了不代表咱们的算法不对，只能说这种实现方法太low了

下面介绍一种更高效的方法

 

# 迭代实现


观察一下原序列和反转后的序列

聪明的你有没有看出什么显而易见的性质？

没错！

我们需要求的序列实际是原序列下标的二进制反转！

因此我们对序列按照下标的奇偶性分类的过程其实是没有必要的

 

这样我们可以$O(n)$的利用某种操作得到我们要求的序列，然后不断向上合并就好了
```
// luogu-judger-enable-o2
#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
const int MAXN=1e7+10;
inline int read()
{
    char c=getchar();int x=0,f=1;
    while(c<'0'||c>'9'){if(c=='-')f=-1;c=getchar();}
    while(c>='0'&&c<='9'){x=x*10+c-'0';c=getchar();}
    return x*f;
}
const double Pi=acos(-1.0);
struct complex
{
    double x,y;
    complex (double xx=0,double yy=0){x=xx,y=yy;}
}a[MAXN],b[MAXN];
complex operator + (complex a,complex b){ return complex(a.x+b.x , a.y+b.y);}
complex operator - (complex a,complex b){ return complex(a.x-b.x , a.y-b.y);}
complex operator * (complex a,complex b){ return complex(a.x*b.x-a.y*b.y , a.x*b.y+a.y*b.x);}//不懂的看复数的运算那部分 
int N,M;
int l,r[MAXN];
int limit=1;
void fast_fast_tle(complex *A,int type)
{
    for(int i=0;i<limit;i++) 
        if(i<r[i]) swap(A[i],A[r[i]]);//求出要迭代的序列 
    for(int mid=1;mid<limit;mid<<=1)//待合并区间的中点
    {
        complex Wn( cos(Pi/mid) , type*sin(Pi/mid) ); //单位根 
        for(int R=mid<<1,j=0;j<limit;j+=R)//R是区间的右端点，j表示前已经到哪个位置了 
        {
            complex w(1,0);//幂 
            for(int k=0;k<mid;k++,w=w*Wn)//枚举左半部分 
            {
                 complex x=A[j+k],y=w*A[j+mid+k];//蝴蝶效应 
                A[j+k]=x+y;
                A[j+mid+k]=x-y;
            }
        }
    }
}
int main()
{
    int N=read(),M=read();
    for(int i=0;i<=N;i++) a[i].x=read();
    for(int i=0;i<=M;i++) b[i].x=read();
    while(limit<=N+M) limit<<=1,l++;
    for(int i=0;i<limit;i++)
        r[i]= ( r[i>>1]>>1 )| ( (i&1)<<(l-1) ) ;
    // 在原序列中 i 与 i/2 的关系是 ： i可以看做是i/2的二进制上的每一位左移一位得来
    // 那么在反转后的数组中就需要右移一位，同时特殊处理一下复数 
    fast_fast_tle(a,1);
    fast_fast_tle(b,1);
    for(int i=0;i<=limit;i++) a[i]=a[i]*b[i];
    fast_fast_tle(a,-1);
    for(int i=0;i<=N+M;i++)
        printf("%d ",(int)(a[i].x/limit+0.5));
    return 0;
}
```
