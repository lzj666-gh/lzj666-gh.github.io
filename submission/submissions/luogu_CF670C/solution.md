# CF670C 题解

### CF670C 【Cinema】

这道题我只用了sort，其它东西都是自己手写的，代码可读性应该比其他人高一点，希望这篇题解管理员可以通过。

先说一下我这道题的思路吧：

**1.因为这道题语言种类的范围是int，所以直接暴力统计是不行的，所以我们要将数据离散化一下，当然也可以map或者hash之类的，不过我感觉离散化不是太难，就直接写了个离散化。**

**2.将所有语言离散化后我们可以通过二分搜索直接去找每一个科学家会的语言，并开一个数组存下每种语言有几个人会。**

**3.分别搜索并计录配音语言和字幕语言，通过对比判断出选择哪一个才是最佳的选择。**

想这道题的思路其实并~~不难~~，我也就只WA了两遍（QAQ）
只要细节多注意一点过这道题还是不难的。

附上我的代码（**时间复杂度为O((n + m)log(n + m**）:
```cpp
#include <cstdio>
#include <algorithm>

using namespace std;
const int N = 400005;

int n, m;
int a[N], b[N], c[N], d[N + N / 2], e[N + N / 2], k[N];
int ans = 1, ans1, ans2;
//离散化 
inline void discrete(int x) {
    int t = 0;
    sort(d + 1, d + 1 + x);
    for(int i = 1; i <= x; ++i)
        if(i == 1 || d[i] != d[i - 1]) e[++t] = d[i];//去重+离散 
    e[0] = t;//将去重后的长度直接保存在e[0]里面。 
}
//二分搜索 
inline int query(int x) {
    
    int l = 1, r = e[0], mid;//自己写的二分 
    while(l < r) {
        mid = (l + r) >> 1;
        if(e[mid] >= x) r = mid;
        else l = mid + 1;
    }
    return l;
}

int main() {
//	freopen("in.txt", "r", stdin);
    int t = 0;
    scanf("%d", &n);
    for(int i = 1; i <= n; ++i) {
        scanf("%d", a + i);
        d[++t] = a[i];
    }
    scanf("%d", &m);
    for(int i = 1; i <= m; ++i) {
        scanf("%d", b + i);
        d[++t] = b[i];
    }
    for(int i = 1; i <= m; ++i) {
        scanf("%d", c + i);
        d[++t] = c[i];
    }
    
    discrete(t);//把所有语言离散化一遍

    for(int i = 1; i <= n; ++i) k[query(a[i])]++;//暴力统计
    
    for(int i = 1; i <= m; ++i) {
        int x = k[query(b[i])], y = k[query(c[i])];
        if(x > ans1 || (x == ans1 && y > ans2)){//与上一个答案对比选出最佳 
            ans = i;
            ans1 = x;
            ans2 = y;//为了下一次比较，保存这一次答案 
        }
    }
    
    printf("%d\n", ans);
    return 0;
}
```

