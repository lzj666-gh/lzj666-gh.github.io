# P1982 题解

~~额这道题着实恶心qwq~~

---

刚看到这个题目的时候就感到题面深深的~~**恶心**~~， ~~（好吧是我语文太差qwq）~~，但是还是要做啊，所以说先把这道题中的几个关系在草稿纸上列了一下草稿qwq：

首先我们要明确：这题有三个值，分别是：

1.**每个小朋友手上的牌的数字，简称“手牌值”**

2.**特征值**：第$i$个小朋友的**特征值** $ = $ 排在他前面（包括他本人）的小朋友中，连续若干个（最少有一个）小朋友**手牌值**的和的最大值

3.**分数**：第$i$个小朋友的**分数** 等于：

如果 $i = 1$ 那么： 这个小朋友的分数 = 这个小朋友的特征值

否则： 这个小朋友的分数 = 前面所有小朋友中，**任意一个**小朋友的分数加上这个小朋友本身的特征值

~~python中文编程（雾~~

算了我把这三个值多少解释表示一下吧qwq：

1.手牌值。~~这个东西的获取靠读入不说了吧qwq~~


2.特征值：在实现的时候，借鉴了一下icy的思路，用两个数组维护，分别是：

$w$数组：以i为结尾的最长连续子段和（icy原话）

$q$数组：1~i中的最长连续子段和（个人认为q数组对应的是特征值）

3.分数：这个根据上面的定义~~乱搞~~一下即可，~~（上面写的那么python应该能懂吧qwq）~~

最后，**溢出**怎么办？

~~开_int128~~

正解：两个long long当高精度用，

附AC代码：

```
#include<bits/stdc++.h>
#define ll long long
const ll MaxN = 1e6;
const ll Base = (ll)1e9;

struct pii {
    ll high, low;
    friend inline pii operator +(const pii &a, const pii &b) {
        pii c; c.high = a.high + b.high; c.low = a.low + b.low;
        if (c.high >= 0 && c.low >= Base) {
            c.high += c.low / Base; c.low = c.low % Base;
        }
        if (c.high <= 0 && c.low <= -Base) {
            c.high += c.low / Base; c.low = c.low % Base;
        }
        if (c.high > 0 && c.low < 0) {
            c.high--; c.low += Base;
        }
        if (c.high < 0 && c.low >= Base) {
            c.high++; c.low -= Base;
        }
        return c;
    }
    friend inline bool operator <(const pii &a, const pii &b) {
        if (a.high == b.high) return a.low < b.low; else return a.high < b.high;
    }
    friend inline pii max(const pii &a, const pii &b) {
        if (a < b) return b; else return a;
    }
};

ll N, P;

inline void getInt(ll &ans) {
    int f = 1; long long x = 0; char ch;
    do {ch = getchar(); if (ch == '-') f = -1;} while (ch < '0' || ch > '9');
    do {x = x*10 + ch - '0'; ch = getchar();} while (ch >= '0' && ch <= '9');
    ans = (f == 1) ? x : -x;
}

pii w[MaxN], q[MaxN], s[MaxN], data[MaxN], 
    ans;


int main() {
    getInt(N); getInt(P);
    for (int i = 1; i <= N; ++i) {
        getInt(data[i].low);
    }	
    
    ans = s[1] = q[1] = w[1] = data[1];
    for (int i = 2; i <= N; ++i) {
        w[i] = max(w[i - 1] + data[i], data[i]);
        q[i] = max(q[i - 1], w[i]);
        s[i] = (i == 2) ? s[1] + s[1] : max(s[i - 1], s[i - 1] + q[i - 1]);
        ans = max(ans, s[i]); 
        // debug1();        
    }
    std::cout << (((ans.high%P)*Base)%P + (ans.low%P))%P << std::endl;
    return 0;
}

```