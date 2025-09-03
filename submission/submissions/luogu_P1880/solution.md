# P1880 题解

如果对于任意的a1≤a2< b1≤b2，有m[a1,b1]+m[a2,b2]≤m[a1,b2]+m[a2,b1]，那么m[i,j]满足四边形不等式。


所以这是一个求(xuan)骗(xue)的东西。

*******************

#定理

[](http://blog.163.com/dqx\_wl/blog/static/2396821452015111133052112/)


对方程$$m(i,j)=\min\{m(i,k-1),m(k,j)\}+w(i,j)          (i≤k≤j)$$

且s(i,j)表示m(i,j)取得最优值时对应的下标，有：


- 区间包含的单调性：如果对于i≤i'< j≤j'，有w(i',j)≤w(i,j')，那么说明w具有区间包含的单调性。

![区间包含的单调性](http://img.blog.csdn.net/20171220095805272?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfNDEyNTI4OTI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

- 四边形不等式：如果对于i≤i'< j≤j'，有w(i,j)+w(i',j')≤w(i',j)+w(i,j')，我们称函数w满足四边形不等式。

![四边形不等式](http://img.blog.csdn.net/20171220100013699?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfNDEyNTI4OTI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

蓝线长和≤红线长和

- 定理一：如果上述的w函数同时满足区间包含单调性和四边形不等式性质，那么函数m也满足四边形不等式性质。


- 定理二：假如m(i,j)满足四边形不等式，那么s(i,j)单调，即s(i,j)≤s(i,j+1)≤s(i+1,j+1)。


然后k的范围就从 [ i , j ] 变成了[ s(i,j-1) , s(i+1,j) ]，像这样：

![表](http://img2.ph.126.net/JuoBJNeFqkb342wbFNg3UA==/6631278871933975781.jpg)

m[1,3]取s[1,2]和s[2,3]，

m[2,5]取s[ 2,4]=3，s[3,5]=3，相当于直接取3。

（然后记s[2,5]=3）

少了一重循环！！！


**完美解释了OBST问题！！！**

~~（其实就是套定理）~~


#题目


[NOI 1995 石子合并](https://www.luogu.org/problemnew/show/1880)

(洛谷  P1880)

n<=100……如果n<=1000呢？

100的$O(n^3)$还能过，1000的就得$O(n^2)$了。


环形的……也不惧……

***但最大值不单调，不能用四边形不等式***

不过最大值可以两个端点的最大者取得。

![最大值不单调](http://img.blog.csdn.net/20171221171418185?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfNDEyNTI4OTI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

[详解](http://www.eefocus.com/chs4444/blog/11-12/235769\_83fc1.html)


题解 by myself


```cpp
#include<iostream>
#include<cstdio>
using namespace std;
int a[2005],sum[2005];
int fmi[2005][2005],fma[2005][2005],
    smi[2005][2005];

int main(){
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d",&a[i]);
        a[i+n]=a[i];
        sum[i]=sum[i-1]+a[i];
        smi[i][i]=i;
        }
    for(int i=1+n;i<=(n<<1);i++){
        sum[i]=sum[i-1]+a[i];
        smi[i][i]=i;
        }
    for(int i=(n<<1)-1;i;i--)
        for(int j=i+1;j<=(n<<1);j++){
            int jc=0,tmp=0x3f3f3f3f;
            fma[i][j]=max(fma[i][j-1],fma[i+1][j])+sum[j]-sum[i-1];
            /*注意这句，
              求最大值不能用四边形不等式，
              因为最大值不满足单调性，
              但最大值有一个性质，
              即总是在两个端点的最大者中取到。
            */
            for(int k=smi[i][j-1];k<=smi[i+1][j];k++){
                int tt=fmi[i][k]+fmi[k+1][j]+(sum[j]-sum[i-1]);
                if(tt<tmp){
                    tmp=tt;
                    jc=k;
                    }
                }
            smi[i][j]=jc;
            fmi[i][j]=tmp;
            }
    int ama=0,ami=0x3f3f3f3f;
    for(int i=1;i<=n;i++){
        ama=max(ama,fma[i][i+n-1]);
        ami=min(ami,fmi[i][i+n-1]);
        }
    printf("%d\n%d",ami,ama);
    
    return 0;
    }
```