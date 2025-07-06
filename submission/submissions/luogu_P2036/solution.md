# P2036 题解

这是道简单dfs，但看题解写的太啰嗦，于是想水一发
```cpp
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
const int M=15;//养成良好习惯
int a[M],b[M],n,ans=0x7f;
//ans初始化为最大值
void dfs(int i,int x,int y){
//i是表示目前的配料编号，x为酸度，y为甜度
    if(i>n){
    	//注意，必须大于n才表示全部搜完
        if(x==1&&y==0)return;
        //判断清水的情况
        ans=min(abs(x-y),ans);
        //更新ans
        return;
    }
    //分两种情况搜索：1添加 2不添加
    dfs(i+1,x*a[i],y+b[i]);
    dfs(i+1,x,y); 
    //这题无需回溯，不明白为何有些题解居然还用全局变量，非得回溯-_-||
}
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d%d",&a[i],&b[i]);
        //读入，用cin太慢了
    }
    dfs(1,1,0);
    printf("%d\n",ans);
    return 0;
}
```
于是你会蜜汁WA

只因为这题数据太水（毒瘤）所以ans要初始化为0x7fffffff，否则只有42。

dfs很简单，但千万不可想复杂。

第一篇题解，求过！！