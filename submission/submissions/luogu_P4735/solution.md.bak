# P4735 题解

可持久化 $Trie$ 真好写...

我们看两个操作，添加操作没什么好说的，查询操作看起来很奇怪，但是如果转为前缀异或和数组$s[i]$，并把 $x$ 异或上 $s[n]$ 的话...

我们发现实际上就是考虑一个区间的数和 $x$ 异或后的最大异或和。

这样我们建一棵可持久化 $Trie$ ,每个节点存它的数字个数，查询的时候从高位到低位贪心走路就好。

另外注意一个坑点，就是如果查询区间左端点是1的话， $x$ 异或上 $0$ 可能是最大的，要把这种情况考虑进去。

最后，如果不知道可持久化Trie的话，其实根据主席树的建树方法脑补一下就好，还是很好写的。

```cpp
// luogu-judger-enable-o2
#include <bits/stdc++.h>
using namespace std;
#define maxn 600009
int rt[maxn],cnt[maxn*28];
int ch[maxn*28][2];
int qz[maxn];
int tt=1;
int n,m;
void ins(int a,int b,int t,int x) {
    if(t<0) return;
    int i=(x>>t)&1;
    ch[a][!i]=ch[b][!i];
    ch[a][i]=tt++;
    cnt[ch[a][i]]=cnt[ch[b][i]]+1;
    ins(ch[a][i],ch[b][i],t-1,x);
}
int qu(int a,int b,int t,int x) {
    if(t<0) return 0;
    int i=(x>>t)&1;
    if(cnt[ch[b][!i]]>cnt[ch[a][!i]]) {
        return (1<<t)+qu(ch[a][!i],ch[b][!i],t-1,x);
    }
    else {
        return qu(ch[a][i],ch[b][i],t-1,x);
    }
}
int main(){
    scanf("%d%d",&n,&m);
    int a,b,c,i,j;
    char s[5];
    rt[0]=tt++;
    ins(rt[0],0,25,0);
    for(a=1;a<=n;a++) {
        scanf("%d",&b);
        qz[a]=qz[a-1]^b;
        rt[a]=tt++;
        ins(rt[a],rt[a-1],25,qz[a]);
    }
    for(a=1;a<=m;a++) {
        scanf("%s",s);
        if(s[0]=='A') {
            scanf("%d",&b);
            n++;
            qz[n]=qz[n-1]^b;
            rt[n]=tt++;
            ins(rt[n],rt[n-1],25,qz[n]);
        }
        else {
            scanf("%d%d%d",&i,&j,&b);
            i--;j--;
            if(i==0) printf("%d\n",qu(0,rt[j],25,b^qz[n]));
            else printf("%d\n",qu(rt[i-1],rt[j],25,b^qz[n]));
        }
    }
    return 0;
}
```