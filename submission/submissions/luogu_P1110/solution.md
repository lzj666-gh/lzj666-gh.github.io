# P1110 题解

```plain
首先这题不用手写平衡树，不用堆，只用两个数组，两个multiset和一个变量就好了......
然而语文神题不好看懂......
首先理解题意：我们无非就是把这个序列分成n段，在每一段结尾插入新元素。
比如说样例，我们可以理解为：
[5][3,9,6][1]。
其中括号括起来的为每一段所含的元素。
我们首先维护两个数组，st[]和ed[]表示每一段开头的元素和结尾的元素。我们在更新相邻差值的时候只用考虑新插入的值和原结尾的差以及和下一段开头的差就好了。
这样，我们维护两个 multiset<int> ，一个叫 full ，表示全部 元素(存在的数值)。另一个叫 delta ，表示全部 差值 。
插入新元素的时候，我们把他在 full 中找到前驱后继分别作差，更新 排序后最小差 。
然后在 delta 中删除 现在本段结尾与下一段开头的差 ，插入 新值与当前本段结尾的差 和 新值与下一段开头的差 。
注意必须用 multiset ， 因为同样的键值可能出现多次。
另外删除时要 erase 掉 find 后的 iterator ，不能直接 erase 数值，否则就把出现多次的同一个数值全删了......
最后上代码。大牛分站O2信仰跑。
```
```cpp
#include<cstdio>
#include<set>
#include<cstdlib>
#include<cctype>
using namespace std;
const int maxn=5e5+1e2;
const int inf=0x3f3f3f3f;

multiset<int> delta,full;
int st[maxn],ed[maxn];
int srt=inf;
int n,m;

inline void update_srt(int x)
{
    multiset<int>::iterator it = full.lower_bound(x);
    int nw = *it - x;
    --it;
    nw = min( nw , x - *it );
    srt = min( srt , nw );
    full.insert(x);
}

inline void replac(int pos,int x)
{
    delta.insert( abs( x - ed[pos] ) );
    if( pos != n )
        delta.erase( delta.find( abs( st[pos+1] - ed[pos] ) ) ),
        delta.insert( abs( st[pos+1] - x ) );
    ed[pos] = x;
}

inline int getint()
{
    int ret = 0 , fix = 1;
    char ch = getchar();
    while( !isdigit(ch) )
    {
        if( ch == '-' )
            fix = -1;
        ch = getchar();
    }
    while( isdigit(ch) )
        ret = ret * 10 + ( ch - '0' ),
        ch = getchar();
    return ret * fix;
}

int main()
{
    static char str[1<<5];
    n = getint() , m = getint();
    for(int i=1;i<=n;i++)
        st[i] = ed[i] = getint();
    
    full.insert(inf),
    full.insert(-inf);
    for(int i=1;i<n;i++)
        delta.insert( abs( st[i+1] - ed[i] ) );
    for(int i=1;i<=n;i++)
        update_srt(st[i]);
    for(int i=1,pos,x;i<=m;i++)
    {
        scanf("%s",str);
        if( *str == 'I' )
        {
            pos = getint() , x = getint();
            update_srt(x);
            replac(pos,x);
        }
        else if( str[4] == 'S' )
            printf("%d\n",srt);
        else
            printf("%d\n",*delta.begin());
    }
    return 0;
}
```