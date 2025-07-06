# P1892 题解

萌新刚AC了本题，谈下心得吧~

以下代码






```cpp
#include<iostream>
#include<string>
using namespace std;
int n,m,f[1001],enm[1001];  //f存放节点的父亲，enm存放每个人的敌人 
int find(int x)            //寻找x的祖先 
{
    while(f[x]!=x) x=f[x]; //不断更新寻找祖先
    return x;
}
void hebing(int x,int y)    //中文看得懂吧 
{
    x=find(x);y=find(y);  //无判定超简单合并_(:з」∠)_照顾一下和我一样的萌新
    if(x==y) return;
    f[y]=x;
    return;
}
int main()
{
     cin>>n>>m;
     for(int i=1;i<=n;i++)
        f[i]=i;
    for(int i=1;i<=m;i++)
    {
        int p,q;
        char c;
        cin>>c>>p>>q;
        if(c=='F') hebing(p,q);  //是朋友就合并 
        else {
                if(enm[p]==0) enm[p]=find(q);
              else hebing(q,enm[p]);  //一个人有两个或更多敌人，合并他们 
              if(enm[q]==0) enm[q]=find(p);
              else hebing(p,enm[q]);
            } 
    }
    int count[1001]={0};
    for(int i=1;i<=n;i++)
        count[find(i)]++;
    int cnt=0;
    for(int i=1;i<=n;i++)
        if(count[i]) cnt++; //统计，做得不是很简洁 
    cout<<cnt;
 } 
```
首先，要充分理解题目。
“敌人的敌人就是朋友”可以这么理解：如果一个人有两个或更多敌人，这些敌人就应该被合并。

代码中的enm数组就是记录了每个人的第一个敌人，再遇到敌人时就把这两个敌人合并。

没想出这点的话还是蛮难做的。

路径优化什么的，咳咳，都说是萌新了。


另外致萌新：如果错了一定优先检查循环条件\_(:з」∠)\_本人调了一小时才发现是某循环条件的“==”打成“=”了……以前学pascal的后遗症啊


至于代码注释不够清晰等问题欢迎提出~

讲得可能比那些高估咱萌新实力的大牛们稍微易懂点吧，人生中第一个题解，希望能过⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄
