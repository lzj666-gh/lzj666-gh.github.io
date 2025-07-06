# P1955 题解

这道题呢，其实就是一个小小的并查集啦。
### # **并查集的Get操作**
```cpp
int get(int x){
	if(x==fa[x])	return x;
    return fa[x]=get(fa[x]);//路径压缩
}
```
### # 并查集的Merge操作
```cpp
void merge(int x,int y){
	fa[get(x)]=get(y);
} // 可以直接写在程序里
```
# 特别提醒

	并查集一定要初始化，即fa[i]=i，表示i的爹是它自己
    嗯！一定要记得啊！
先排序，**把所有e==1的操作放在前面，然后再进行e==0的操作**，**在进行e==1的操作的时候**，我们只要把它约束的两个变量放在同一个集合里面即可。**在e==0**，即存在一条不相等的约束条件，对于它约束的两个变量，如果在一个集合里面，那就不可能满足！如不相等的约束条件都满足，那就YES。

还有啊，**我们要关注一下数据范围**，是有10的9次方那么大，如果开一个10的9次方大的fa数组的话，空间肯定超限，超限就凉凉（**亲身经历，请勿模仿，谢谢配合！！！**）所以，各位亲爱的小伙伴们，我们需要用到[离！散！化！](https://www.cnblogs.com/cytus/p/8933597.html)。

总得来说离散化有三步走战略：

1.去重（可以用到unique去重函数）

2.排序

3.二分索引（可以用到lower_bound函数）

**放代码**
```cpp
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
using namespace std;
int t,n,f[1000007],book[1000007*3];  //t表示t组数据，n表示有n个操作，f[]是我们并查集的数字，book[]是离散化的数组 
struct node{
    int x,y,e;
}a[1000001];  
bool cmp(node a,node b){
    return a.e>b.e;
}//排 序将e==1的放在前面 
inline void first(int kkk){
    for(int i=1;i<=kkk;i++)  f[i]=i;
}//初 始 化 
int get(int x){
    if(x==f[x]) return x;
    return f[x]=get(f[x]);
}
int main(){
    scanf("%d",&t);
    while(t--){
      int tot=-1;
      memset(book,0,sizeof(book));
      memset(a,0,sizeof(a));
      memset(f,0,sizeof(f));
    int flag=1;
        scanf("%d",&n);
       
        for(int i=1;i<=n;i++){
            scanf("%d %d %d",&a[i].x,&a[i].y,&a[i].e);
            book[++tot]=a[i].x;
            book[++tot]=a[i].y;
        }
        sort(book,book+tot);//排序 
        int reu=unique(book,book+tot)-book;  //去重 
        for(int i=1;i<=n;++i){
           a[i].x=lower_bound(book,book+reu,a[i].x)-book;
           a[i].y=lower_bound(book,book+reu,a[i].y)-book;   
        } 
        first(reu);   //初始化 
        sort(a+1,a+n+1,cmp);  //按e排序 
        for(int i=1;i<=n;i++){
            int r1=get(a[i].x);
            int r2=get(a[i].y);
            if(a[i].e){
                f[r1]=r2;  //就是我们的merge操作 
            }else if(r1==r2){
                printf("NO\n");
                flag=0;  //如果不满足条件，标记为否 
                break;
            }
        }
        if(flag)    printf("YES\n");   //都满足条件了 
    }
    return 0;
}
```
不懂的小伙伴可以私信我，感谢您的阅读！