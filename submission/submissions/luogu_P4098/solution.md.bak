# P4098 题解

[Youngsc](https://youngscc.github.io/)

** %% 楼下大佬暴力水过 **  
** 身为蒟蒻的我暴力写挂了，就码了一发可持久化权值字典树 **  
** 可持久化权值字典树和可持久化的权值线段树非常类似，会写主席树就能码出来可持久化trie **  
** 我们枚举每一个值作为次大值的情况 **  
** 不妨设当前数字左边第一个比它大的下标为$l_1$,第二个比它大的记作$l_2$ **  
** 同理设当前数字右边第一个比它大的下标为$r_1$,第二个比它大的记作$r_2$ **  
** 那么对于一个数字来说，它能作为次大值的区间有很多，但我们只取两个区间 **
** 分别是$[l_1+1,R_2-1]$和$[l_2+1,R_1-1]$，其他的区间都是这两个区间的子集**  
** 要处理这个的话我们可以借助链表，将元素按照从小到大的顺序依次删除 **  
** 每次删除之前当前位置左右一共四个元素就是上述的四个元素 **  
** 当然，如果一个元素左边没有比他大的或者右边没有比他 大的就需要特判 **  
** 然后就在区间内的trie上贪心的从高位到低位取反 **  

```cpp
# include <bits/stdc++.h>
# define R register
# define N 50010
# define inf 2000101900

using namespace std;

int n,a[N],t[N*35],ch[N*35][2],ans,pre[N],nxt[N],rt[N],cnt;

pair <int,int> b[N];

template <typename T> inline void in(R T &a){
    R char c = getchar();R T x=0,f=1;
    while(!isdigit(c)) {if(c == '-') f=-1; c=getchar();}
    while(isdigit(c)) x=(x<<1)+(x<<3)+c-'0',c = getchar();
    a=x*f;
}

template <typename T> inline void maxx(R T& a,const T b){a<b ? a=b:0;}
template <typename T> inline void minn(R T& a,const T b){a>b ? a=b:0;}

inline void insert(R int x,R int pos){
    R int now = rt[pos] = ++cnt,las = rt[pos-1];
    t[now] = t[las]+1;
    for (R int i=30; i>=0; --i)
    {
        R int tag = x>>i&1;
        ch[now][tag^1] = ch[las][tag^1];
        ch[now][tag] = ++cnt;
        now = ch[now][tag];
        las = ch[las][tag];
        t[now] = t[las]+1;
    }
}

inline int qury(R int sum,R int l,R int r){
	l--;
    R int now = rt[l],las = rt[r],ret=0;
    for (R int i=30; i>=0; --i)
    {
        R int tag = sum>>i&1;
        if (t[ch[las][tag^1]]-t[ch[now][tag^1]])
        {
            ret ^= (1<<i);
            now = ch[now][tag^1];
            las = ch[las][tag^1];
        }
        else
        {
            now = ch[now][tag];
            las = ch[las][tag];
        }
    }
    return ret;
}

int main(){
    in(n);
    R int fir=0,las=n+1;
    pre[las] = n,nxt[fir] = 1;
    a[fir] = a[las] = inf;
    for (R int i=1; i<=n; ++i) pre[i] = i-1,nxt[i] = i+1,in(a[i]),b[i] = make_pair(a[i],i),insert(a[i],i);
    sort(b+1,b+n+1);\\按从小到大排序
    for (R int i=1; i<=n; ++i)
    {
        R int x = b[i].second;
        R int l = pre[x],r = nxt[x];\\取当前位置的左右两个值
        nxt[l] = r,pre[r] = l;\\删除
        if (l != fir) maxx(ans,qury(a[x],pre[l]+1,r-1)); \\如果左边有更大的
        if (r != las) maxx(ans,qury(a[x],l+1,nxt[r]-1)); \\如果右边有更小的
    }
    printf("%d",ans);
}

```
