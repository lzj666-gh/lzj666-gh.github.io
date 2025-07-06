# P4342 题解

事实上，这道题，绝大多数题解都有疏漏，原因是这道题的数据是真的水。。毕竟连最小值不要都可以得到$80$。。至于错误的原因在下文有说明。

让我们重新开始吧，看到这道题，我们首要的两个问题：

1.如何处理这样一个环。

2.如何得到最开始删除的边。

对于第一个问题，很轻易地就可以想到断环成链，同时我们还可以发现，通过断环成链，我们把第二个问题就解决了，我们可以通过对最后的结果再来一次对最大值的遍历，输出即可。

开始考虑$DP$，首先我们可以很显然的得到一个区间$DP$的板子：

设$f[i][j]$表示$[i,j]$这一个区间内可以得到的最大得分，转移方程如下：

加法：$f[i][j]=max(f[i][k]+f[k+1][j])$

乘法：$f[i][j]=max(f[i][k]\times f[k+1][j])$

但是我们更往深入思考，因为有乘法的存在，且有负数，那就肯定会有一个负负得正的情况，所以我们还需要维护一个最小值。设这个最小值为$g[i][j]$

然后就是分情况讨论的时间：

首先对于加法的情况，因为不存在负负得正一类的情况存在，所以两者的转移方程是基本一样的，大区间的最大值等于合并的两个区间的最大值之和，最小值等于合并的两个区间的最小值之和：

$f[i][j]=max(f[i][k]+f[k+1][j])$

$g[i][j]=min(g[i][k]+g[k+1][j])$

其次对于乘法，这里就很容易有很多遗漏点，让我们一种种分情况讨论：

（啊这里原意想画图，但考虑到手画太丑，用软件又麻烦，实在不理解可以拿着笔画一下各种情况）

$1.f[i][k],g[i][k],f[k+1][j],g[k+1][j] > 0$时：

$f[i][j]=max(f[i][k]\times f[k+1][j])$

$g[i][j]=min(g[i][k]\times g[k+1][j])$

$2.f[i][k],g[i][k],f[k+1][j] > 0,g[k+1][j] < 0$时：

$f[i][j]=max(f[i][k]\times f[k+1][j])$

$g[i][j]=min(f[i][k]\times g[k+1][j])$

$3.f[i][k],g[i][k] > 0,f[k+1][j],g[k+1][j] < 0$时：

$f[i][j]=max(g[i][k]\times f[k+1][j])$

$g[i][j]=min(f[i][k]\times g[k+1][j])$

$4.f[i][k],f[k+1][j],g[k+1][j] > 0,g[i][k] < 0$时：

$f[i][j]=max(f[i][k]\times f[k+1][j])$

$g[i][j]=min(g[i][k]\times f[k+1][j])$


$5.f[i][k],f[k+1][j] > 0,g[i][k],g[k+1][j] < 0$时：

$f[i][j]=max(f[i][k]\times f[k+1][j],g[i][k]\times g[k+1][j])$

$g[i][j]=min(f[i][k]\times g[k+1][j],g[i][k]\times f[k+1][j])$

（此处就没分绝对值大小的情况了，可以感性理解一下。）

$6.f[i][k] > 0,g[i][k],f[k+1][j],g[k+1][j] < 0$时：

$f[i][j]=max(g[i][k]\times g[k+1][j])$

$g[i][j]=min(f[i][k]\times g[k+1][j])$

$7.f[k+1][j],g[k+1][j] > 0,f[i][k],g[i][k] < 0$时：

$f[i][j]=max(f[i][k]\times g[k+1][j])$

$g[i][j]=min(g[i][k]\times f[k+1][j])$

$8.f[k+1][j] > 0,f[i][k],g[i][k],g[k+1][j] < 0$时：

$f[i][j]=max(g[i][k]\times g[k+1][j])$

$g[i][j]=min(g[i][k]\times f[k+1][j])$

$9.f[i][k],g[i][k],f[k+1][j],g[k+1][j] < 0$时：

$f[i][j]=max(g[i][k]\times g[k+1][j])$

$g[i][j]=min(f[i][k]\times f[k+1][j])$

（~~做了一个下午脑袋都要炸了，~~如果有$BUG$欢迎指出）

虽然说情况很多，但事实上你可以压成两行，不用特判。。（懒）

$f[i][j]=max(f[i][j],max(f[i][k]\times f[k+1][j],max(g[i][k]\times g[k+1][j],max(f[i][k]\times g[k+1][j],g[i][k]\times f[k+1][j]))))$

$g[i][j]=min(g[i][j],min(f[i][k]\times f[k+1][j],min(g[i][k]\times g[k+1][j],min(f[i][k]\times g[k+1][j],g[i][k]\times f[k+1][j]))))$

记得初始化长度为$1$的情况，至于区间端点为$0$的情况，由于上面的这个式子里面四种组合都全部考虑到了就可以不管了。

然后就可以愉快的$A$掉啦!

$Code$：

```cpp
#include<bits/stdc++.h>
#define lcy AKIOI
#define ll long long
const int inf=0x3f3f3f3f;
int n,ans=-inf;
int a[105];
int f[150][150],g[150][150];
char c[105];
int max(int x,int y){return (x>y)?(x):(y);}
int min(int x,int y){return (x<y)?(x):(y);}
int main(){
    scanf("%d\n",&n);//读入很诡异
    for(int i=1;i<=n;i++){
        scanf("%c %d",&c[i],&a[i]);getchar();
        a[n+i]=a[i];c[n+i]=c[i];//断环为链
    }
    for(int i=1;i<=(n<<1);i++){
        for(int j=1;j<=(n<<1);j++){
            f[i][j]=-inf,g[i][j]=inf;
        }
    }
    for(int i=1;i<=(n<<1);i++)f[i][i]=g[i][i]=a[i];
    for(int len=2;len<=n;len++){
        for(int i=1,j=len;j<=(n<<1);i++,j++){
            for(int k=i;k<j;k++){
                if(c[k+1]=='x'){
                    f[i][j]=max(f[i][j],max(f[i][k]*f[k+1][j],max(g[i][k]*g[k+1][j],max(f[i][k]*g[k+1][j],g[i][k]*f[k+1][j]))));
                    g[i][j]=min(g[i][j],min(f[i][k]*f[k+1][j],min(g[i][k]*g[k+1][j],min(f[i][k]*g[k+1][j],g[i][k]*f[k+1][j]))));
                }
                else if(c[k+1]=='t'){
                    f[i][j]=max(f[i][j],f[i][k]+f[k+1][j]);
                    g[i][j]=min(g[i][j],g[i][k]+g[k+1][j]);
                }
            }
        }
    }
    for(int i=1;i<=n;i++)ans=max(ans,f[i][i+n-1]);printf("%d\n",ans);
    for(int i=1;i<=n;i++)if(f[i][i+n-1]==ans)printf("%d ",i);
    return 0;
}

```