# P3599 题解

# 题解-Koishi Loves Construction

**[博客中阅读](https://www.cnblogs.com/Wendigo/p/12497075.html)**

**前缀知识**
> 质数
> 逆元
> 暴搜

---

> [Koishi Loves Construction](https://www.luogu.com.cn/problem/P3599)

> 给定 $X$，$T$ 组测试数据，每次给一个 $n$。
> 1. 如果 $X=1$，构造一个 $1\sim n$ 的排列使得前缀和模 $n$ 互不相同。
> 2. 如果 $X=2$，构造一个 $1\sim n$ 的排列使得前缀积模 $n$ 互不相同。

> 数据范围：$1\le T\le 10$，$1\le n\le 10^5$，$X\in\{1,2\}$。

---

属于“思维体操”，做之前会异常兴奋，做之后会只想睡觉。

---

设序列为 $a\{n\}$，前缀和/积为 $sum\{n\}$。

分类讨论：

## $X=1$

**初步发现：**

1. 不能有区间 $[L,R](L\neq 1)$ 和是 $n$ 的倍数，否则 $sum_{L-1}\equiv sum_R\pmod n$。

2. 设 $a_i=n$，必须 $i=1$，否则 $sum_i\equiv sum_{i-1}\pmod n$。

3. $\therefore n\in \mathbb{even}\cup {1}$，因为如果 $n\in \mathbb{odd}$：

$$\sum\limits_{i=1}^{n-1}=\frac{(1+n-1)\times(n-1)}{2}=n\times(\frac{n-1}{2})\equiv 0\pmod n$$

然后由此判断输出 $0\&1$，交了一发，$15$ 分——很明显判断对了。

**于是开始打暴力：**

```cpp
#include <bits/stdc++.h>
using namespace std;

//&Start
#define lng long long
#define lit long double
#define re register
#define kk(i,n) " \n"[i==n]
const int inf=0x3f3f3f3f;
const lng Inf=0x3f3f3f3f3f3f3f3f;

//&Data
const int N=1e5;
int a[N+10],n;
bool vis[N+10],use[N+10];
void dfs(int x,int sm){
    if(x==n+1){
        for(int i=1;i<=n;i++)
            printf("%d%c",a[i],kk(i,n));
        return ;
    }
    for(int i=1;i<=n;i++)
    if(!use[i]){
        use[i]=1;
        if(!vis[(sm+i)%n]){
            vis[(sm+i)%n]=1;
            a[x]=i;
            dfs(x+1,(sm+i)%n);
            vis[(sm+i)%n]=0;
        }
        use[i]=0;
    }
}

//&Main
int main(){
    scanf("%d",&n);
    dfs(1,0);
    return 0;
}


/***
input
6
output
6 1 4 3 2 5
6 2 5 3 1 4
6 4 1 3 5 2
6 5 2 3 4 1
***/
```

输入 $6$ 后，看这个输出：

```cpp
6 1 4 3 2 5
```

得出规律：

1. 如果 $i\in \mathbb{odd}$，$a_i=n+1-i$。
2. 如果 $i\in \mathbb{even}$，$a_i=i-1$。


```cpp
//&Solve1
void solve1(){
    memset(a,0,sizeof a);
    memset(sum,0,sizeof sum);
    if((n&1)&&(n^1)) return puts("0"),void();
    else {
        putchar('2'),putchar(' ');
        for(int i=1;i<=n;i++)
            printf("%d%c",(i&1)?n+1-i:i-1,kk(i,n));
    }
}
```

提交后得到 $50$ 分，说明对了。

**证明：**

模 $n$ 意义下，上述序列可以看成：

``` cpp
0 1 -2 3 -4 5
```

很明显：

1. 如果 $i\in\mathbb{odd}$，$sum_i\in\{0,-1,-2,...\}$。
2. 如果 $i\in\mathbb{even}$，$sum_i\in\{1,2,3,...\}$。

最后在模 $n$ 意义下还原成正数，

$$\{sum_1,sum_2,...,sum_n\}=\{1,2,...,n\}$$

## $X=2$

**初步发现：**

1. 不能有区间 $[L,R](L\neq 1)$ 的积 $\equiv 1\pmod n$。
2. 不能有区间 $[L,R](R\neq n)$ 的积 $\equiv 0\pmod n$。
3. $\therefore a_1=1$。
4. $\therefore a_n=n$。
5. 还有如果 $n|\prod\limits_{i=1}^{n-1}i$ 也不行，很明显。 

然后由此判断输出 $0\&1$，交了一发，$65$ 分——很明显判断对了

**至于序列长什么样，暴力再来一发：**

```cpp
#include <bits/stdc++.h>
using namespace std;

//&Start
#define lng long long
#define lit long double
#define re register
#define kk(i,n) " \n"[i==n]
const int inf=0x3f3f3f3f;
const lng Inf=0x3f3f3f3f3f3f3f3f;

//&Data
const int N=1e5;
int a[N+10],n;
bool vis[N+10],use[N+10];
void dfs(int x,int sm){
    if(x==n+1){
        for(int i=1;i<=n;i++)
            printf("%d%c",a[i],kk(i,n));
        return ;
    }
    for(int i=1;i<=n;i++)
    if(!use[i]){
        use[i]=1;
        if(!vis[(sm*i)%n]){
            vis[(sm*i)%n]=1;
            a[x]=i;
            dfs(x+1,(sm*i)%n);
            vis[(sm*i)%n]=0;
        }
        use[i]=0;
    }
}

//&Main
int main(){
    scanf("%d",&n);
    dfs(1,1);
    return 0;
}
/***
input
7
output
1 2 5 6 3 4 7
1 3 4 6 2 5 7
1 4 3 6 5 2 7
1 5 2 6 4 3 7
input
11
output
try it by yourself!
***/
```

进一步推测：如果 $n$ 是质数或者 $n=1$ 或者 $n=4$，可以构造。

由此判断输出 $0\& 1$ 提交一发，$65$ 分，很明显对了（然而没什么用啊。

> 然后我下了一下数据，竟然发现输出数据只有 $0\&1$。
> 
> 再进一步发现：第二个数只能是 $2$，没用。

这时看输出（我看了 $20$ 分钟）

```cpp
1 2 5 6 3 4 7

//前缀积%n：
1 2 3 4 5 6 0
```

有一个发现： $sum_i\equiv i\pmod n$。

然后我茅塞顿开：可以试试逆元求序列使得 $sum_i\equiv i\pmod n$（当然 $1$ 或 $4$ 要特判）：

```cpp
void solve2(){
	if(np[n]&&(n^1)&&(n^4)) return puts("0"),void();
	else {
		if(n==1) return puts("2 1"),void();
		if(n==4) return puts("2 1 3 2 4"),void();
		putchar('2');
		for(int i=1,tmp=1,sum=1;i<=n-1;i++){
			printf(" %d",tmp);
			tmp=1ll*Pow(sum,n-2)*(i+1)%n;
			sum=1ll*sum*tmp%n;
		}
		printf(" %d",n),putchar('\n');
	}
}
```

提交了一发，$\texttt{AC}$ 了。

**证明：**

$$\because (i-1)\times a_i\equiv i\pmod n$$

很明显，对于每个 $i$，$a_i$ 是唯一的，只需证明：对于每个 $a_i$，$i$ 是唯一的。

反证：假设对于每个 $a_i$，$i$ 不唯一，设 $a_x=a_y=k(x>y)$。

$$\therefore k(x-1)\bmod n=x,k(y-1)\bmod n=y$$

$$\therefore k(x-y)\bmod n=(x-y)$$

因为 $(x-y)\in\{1,2,...,n\}$，所以必定有 $k(x-y)\bmod n=(x-y+1)$。

**矛盾！**故对于每个 $a_i$，$i$ 是唯一的。

## $\texttt{code}$

```cpp
#include <bits/stdc++.h>
using namespace std;

//&Start
#define lng long long
#define lit long double
#define re register
#define kk(i,n) " \n"[i==n]
const int inf=0x3f3f3f3f;
const lng Inf=0x3f3f3f3f3f3f3f3f;

//&Data
const int N=1e5;
int X,T,n;

//&Solve1
void solve1(){
	if((n&1)&&(n^1)) return puts("0"),void();
	else {
		putchar('2'),putchar(' ');
		for(int i=1;i<=n;i++)
			printf("%d%c",(i&1)?n+1-i:i-1,kk(i,n));
	}
}

//&Solve2
bitset<N+10> np;
int p[N+10],cnt;
void Prime(){
	np[1]=true;
	for(int i=1;i<=N;i++){
		if(!np[i]) p[++cnt]=i;
		for(int j=1;j<=cnt&&i*p[j]<=N;j++)
			np[i*p[j]]=1;
	}
}
int Pow(int a,int x){
	int res=1;
	for(;x;a=1ll*a*a%n,x>>=1)
		if(x&1) res=1ll*res*a%n;
	return res;
}
void solve2(){
	if(np[n]&&(n^1)&&(n^4)) return puts("0"),void();
	else {
		if(n==1) return puts("2 1"),void();
		if(n==4) return puts("2 1 3 2 4"),void();
		putchar('2');
		for(int i=1,tmp=1,sum=1;i<=n-1;i++){
			printf(" %d",tmp);
			tmp=1ll*Pow(sum,n-2)*(i+1)%n;
			sum=1ll*sum*tmp%n;
		}
		printf(" %d",n),putchar('\n');
	}
}

//&Main
int main(){
	scanf("%d%d",&X,&T);
	if(X==2) Prime();
	for(int ti=1;ti<=T;ti++){
		scanf("%d",&n);
		if(X==1) solve1();
		else solve2();
	}
	return 0;
}
```

---

**祝大家学习愉快！**
