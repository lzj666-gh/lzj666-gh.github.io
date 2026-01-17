# P2147 题解

一看就知道是 LCT 裸题，直接上模板。。。

这年头，题解怎么都喜欢用数组，唯一的结构体题解还用了指针，郁闷ing。。。

所以，我来一发 无指针结构体，自我感觉挺好。。。

还有那啥，不要用 STL 的栈，会 RE/WA 的。。。

附上代码（紧紧凑凑80+行）：

```cpp
#include<iostream>
#include<algorithm>
#include<cstdio>
#define MAXN 10010//数组大小
#define MAX 999999999//极值
using namespace std;
int n,m;
struct node{//有父无指针结构体
    int son[2];
    int f,flag;
}a[MAXN];
inline int read(){//读优
    int date=0,w=1;char c=0;
    while(c<'0'||c>'9'){if(c=='-')w=-1;c=getchar();}
    while(c>='0'&&c<='9'){date=date*10+c-'0';c=getchar();}
    return date*w;
}
inline int isroot(int rt){//是否是根
    return a[a[rt].f].son[0]!=rt&&a[a[rt].f].son[1]!=rt;
}
inline void pushdown(int rt){//标记下传
    if(!rt||!a[rt].flag)return;
    a[a[rt].son[0]].flag^=1;a[a[rt].son[1]].flag^=1;a[rt].flag^=1;
    swap(a[rt].son[0],a[rt].son[1]);//别忘了交换左右节点。。。
}
inline void turn(int rt){//旋转，改进版
    int x=a[rt].f,y=a[x].f,k=a[x].son[0]==rt?0:1;
    if(!isroot(x)){//就是这里，判断是否是根
        if(a[y].son[0]==x)a[y].son[0]=rt;
        else a[y].son[1]=rt;
    }
    a[rt].f=y;a[x].f=rt;a[a[rt].son[!k]].f=x;
    a[x].son[k]=a[rt].son[!k];a[rt].son[!k]=x;
}
void splay(int rt){//伸展，也是改进版，应为要适应LCT。。。
    int top=0,stack[MAXN];//果断手写栈
    stack[++top]=rt;//第一个一定是根
    for(int i=rt;!isroot(i);i=a[i].f)stack[++top]=a[i].f;
    while(top)pushdown(stack[top--]);//暴力修改
    while(!isroot(rt)){//这里就基本无大改了
        int x=a[rt].f,y=a[x].f;
        if(!isroot(x)){
            if((a[x].son[0]==rt)^(a[y].son[0]==x))turn(rt);
            else turn(x);
        }
        turn(rt);//注意，是最后才进行，当初我把这句放到里面，然后就 WA 了。。。
    }
}
void access(int rt){//将 x 与 x所在树的根 连一条链
    for(int i=0;rt;i=rt,rt=a[rt].f){//暴力修改，耗时贼多，没有之一。。。
        splay(rt);
        a[rt].son[1]=i;
    }
}
inline void makeroot(int rt){access(rt);splay(rt);a[rt].flag^=1;}//将 x 变为树根
int find(int rt){//找树根
    access(rt);splay(rt);
    while(a[rt].son[0])rt=a[rt].son[0];//一直往左走
    return rt;
}
inline void split(int x,int y){makeroot(x);access(y);splay(y);}搞出 x与y的链
inline void cut(int x,int y){//割 x与y的链
    split(x,y);
    a[y].son[0]=a[x].f=0;
}
inline void link(int x,int y){makeroot(x);a[x].f=y;}//连 x与y的链
int main(){
    char ch[10];
    int x,y;
    n=read();m=read();
    while(m--){
        scanf("%s",ch);x=read();y=read();
        if(ch[0]=='C')link(x,y);
        if(ch[0]=='D')cut(x,y);//基本操作不再多说。。。
        if(ch[0]=='Q'){
            if(find(x)==find(y))printf("Yes\n");//判断联通
            else printf("No\n");
        }
    }
    return 0;//终于敲完了（累死我了。。。）
}

```