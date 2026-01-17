# P2118 题解

这道题的L范围是很有良心的，L小于等于100，则可以直接枚举分子和分母。可以看出分子分母的枚举范围都是1到L，之后可以写一个最大公约数，判断分子分母的最大公约数是否为1（可以用辗转相除法）。然后到了本题的第一个坑：分子分母的比值要大于A和B的比值。根据小学数学的交叉相乘法，就可以将这个式子写成：现分子\*B<=现分母\*A。到了最后一个条件了，使分子分母的比值要尽可能地接近A和B的比值，可以把所有符合上面两个条件的分子分母在一起比较，选出最优解。

附上代码：



```cpp
#include<cstdio>
using namespace std;
int gcd(int x,int y)
{
    if(y==0) return x;
    return gcd(y,x%y);
}
int main()
{
        int i,j,a,b,ansa,ansb,l;
        scanf("%d%d%d",&a,&b,&l);
        ansa=l;ansb=1;
        for(i=1;i<=l;i++)
                for(j=1;j<=l;j++)
                        if(gcd(i,j)==1&&i*b>=j*a&&i*ansb<j*ansa)
                        {
                                ansa=i;
                                ansb=j;
                        }
        printf("%d %d",ansa,ansb);
        return 0;
}

```