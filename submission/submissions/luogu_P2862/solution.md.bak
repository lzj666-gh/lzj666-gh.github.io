# P2862 题解

菜鸡第一次写题解，有什么不足欢迎提出-w-。


------------

## 思路
由题面可知我们要求的问题是平面上有n个点（但是是在格子内w），在这个平面上圈出边长为len的正方形使得正方形内包含c个点。怎样圈才能使得len最小。

这道题直接做很显然是很难做的。

那么根据题意我们很容易把这个问题转化为一个判定问题：我们可以枚举边长len的正方形，判断一下边长为len的正方形内包不包含c个点。而直接枚举len的话，必然会T掉。而这个问题很明显具有单调性：即大于某个值的len都可以满足，而小于这个值的都不满足。那么我们就可以二分解决。如果记点的坐标为$(x,y)$的话，那么二分的复杂度为$O(log\ max(x,y))$。

那么我们应该如何判定呢？

1.二维前缀和:

我们可以通过$O(max(x,y)^2)$的时间预处理出二维前缀和，并可以在$O(1)$的时间内进行单点查询。如果我们枚举所有边长为len的正方形的话，判定的复杂度就近似为$O(max(x,y)^2)$

那么总复杂度为$O(max(x,y)^2\ log\ max(x,y))$ 代入最大规模可以算出最坏情况下的运算次数为$10^8*10 \ =\ 10^9$过于极限，容易被卡，因此我们在一个长度为10000的二维前缀和数组里做二分是不现实的。

那么我们需要如何处理？

2.离散化

因为$c<=n<=500$，所以至多存在1000个数，那么我们就可以通过$O(c+n)$的时间进行离散化，将数x和y的据规模虽小到$(1-1000)$并可以在$O(log\ (c+n))$的时间内查询离散化结果。

那么如果将离散化的数据规模代入一下，最坏情况下运算次数为$10^6*10=10^7$。

~~虽说还是很高而且略去了离散化的复杂度~~，这个复杂度我们还是能接受的。


那么我们就可以通过$O((c+n)\log\ (c+n))$的离散化之后通过$O(log\ (c+n))$的查询处理二维前缀和$sum$，并用长度最多为1000的二维前缀和数组$sum$进行二分，设离散化后的最大数据规模为m复杂度为$O(m^2log\ max(x,y))$。
## 代码
对于离散化，我们可以初始化一个动态数组numbers，直接在读入的时候向里面push_back(x)与push_back(y)，因为我们的目的只是缩小规模，因此我们只需要开一维，把x和y存在同一个vector内进行查找。
```cpp
for (int i = 0; i < n; i++){
        int x,y;
        cin >> x >> y;
        numbers.push_back(x);
        numbers.push_back(y);
}
```

而因为我们要进行二分查找，所以我们必须对其进行排序并去重。

```cpp
sort(numbers.begin(),numbers.end());
numbers.erase(unique(numbers.begin(),numbers.end()),numbers.end());
```
那么我们接下来就可以二分查找原坐标离散化后的位置用其初始化二维前缀和数组。

```cpp
for (int i = 0; i < n; i++){
    int x = get(points[i].first),y = get(points[i].second);
    sum[x][y]++;
}
for (int i = 1; i < numbers.size(); i++){
        for (int j = 1; j < numbers.size(); j++){
            sum[i][j] += sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];
     }
}
```
对于二分答案

如果mid合法那么最优解必然是在mid的左边，而不合法最优解则在mid的右边。
```cpp
int l = 1,r = 10000;
while (l < r){
        int mid = (l + r) >> 1;
        if (check(mid)) r = mid;
        else l = mid + 1;
}
```


而对于check，我们可以枚举所有边长为mid的矩形，通过二维前缀和判断是否存在c个目标。

而我们在枚举边长为mid的矩形时，所算的边长必须为离散化之前的边长，而离散化之前的边长就存在numbers数组内。

而以点$(i,j)$为右下角的边长为len的正方形的和$S$为

$S[i][j]-S[i - len][j] - S[i][j -len]+S[i-len][j-len]$

那么我们就可以枚举$x_1$,$x_2$与$y_1$,$y_2$。

其中$x_1$相当于$i-len$,$x_2$相当于$i$,$y_1$相当于$j-len$,$y_2$相当于$j$。

而因为目标是在格子里，所以有：

```cpp
while(numbers[x2] - numbers[x1 + 1] + 1 > len) x1++;
```

```cpp
while(numbers[y2] - numbers[y1 + 1] + 1 > len)y1++;
```


而如果$sum[x2][y2] - sum[x1][y2] - sum[x2][y1] + sum[x1][y1] >= c$
则$return\ true$否则$return\ false$

```cpp
bool check(int len){
    for (int x1 = 0,x2 = 1; x2 < numbers.size(); x2++){
        while(numbers[x2] - numbers[x1 + 1] + 1 > len)x1++;
        for (int y1 = 0, y2 = 1; y2 < numbers.size(); y2++){
            while(numbers[y2] - numbers[y1 + 1] + 1 > len)y1++;
            if (sum[x2][y2] - sum[x1][y2] - sum[x2][y1] + sum[x1][y1] >= c) return true;
        }
    }
    return false;
}
```
完整代码：
```cpp
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
typedef pair<int,int> PII;
int n,c;
PII points[1010];
vector<int> numbers;
int sum[1010][1010];
int get(int x){
    return lower_bound(numbers.begin(),numbers.end(),x) - numbers.begin();
}
bool check(int len){
    for (int x1 = 0,x2 = 1; x2 < numbers.size(); x2++){
        while(numbers[x2] - numbers[x1 + 1] + 1 > len)x1++;
        for (int y1 = 0, y2 = 1; y2 < numbers.size(); y2++){
            while(numbers[y2] - numbers[y1 + 1] + 1 > len)y1++;
            if (sum[x2][y2] - sum[x1][y2] - sum[x2][y1] + sum[x1][y1] >= c) return true;
        }
    }
    return false;
}
int main(){
    cin >> c >> n;
    numbers.push_back(0);
    for (int i = 0; i < n; i++){
        int x,y;
        cin >> x >> y;
        points[i] = {x,y};
        numbers.push_back(x);
        numbers.push_back(y);
    }
    sort(numbers.begin(),numbers.end());
    numbers.erase(unique(numbers.begin(),numbers.end()),numbers.end());
    for (int i = 0; i < n; i++){
       int x = get(points[i].first),y = get(points[i].second);
       sum[x][y]++;
    }
    for (int i = 1; i < numbers.size(); i++){
        for (int j = 1; j < numbers.size(); j++){
            sum[i][j] += sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];
        }
    }
    int l = 1,r = 10000;
    while (l < r){
        int mid = (l + r) >> 1;
        if (check(mid)) r = mid;
        else l = mid + 1;
    }
    cout << l;
    return 0;
}

```

