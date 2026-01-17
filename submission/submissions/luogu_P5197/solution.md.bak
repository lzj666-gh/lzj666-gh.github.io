# P5197 题解

考虑在一个点的父节点，子节点，这个点本身涂不同的颜色。而在这个点的孙节点（或祖节点）可以用同一个颜色集合来涂色。 

所以统计每个点的度，找到度最大的点，输出 这个点的度+1。
```cpp
#include<cstdio>
int x,y,ans,n,deg[100007];
int main() {
    scanf("%d",&n);
    for(int i=1;i<n;i++) {
        scanf("%d%d",&x,&y);
        if(++deg[x]>ans)ans=deg[x];
        if(++deg[y]>ans)ans=deg[y];
    }
    printf("%d",ans+1);
    return 0;
}
```