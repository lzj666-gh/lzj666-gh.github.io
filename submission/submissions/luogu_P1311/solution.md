# P1311 题解

安利一发自己的博客：[http://www.cnblogs.com/OIerShawnZhou/](http://www.cnblogs.com/OIerShawnZhou/)

（我平常写的题解都会往博客里发，欢迎各位大佬前来拍砖）

暴力好想不好写，正解好写不好想。

刚开始读题的时候总给我一个感觉，那就是k可以不用。因为我们有时根本没必要去关心它的编号具体是什么。后来发现还真是。

如果是暴力枚举客栈的话，不能同时枚举两个客栈，那样会超时，所以只能同时枚举一个。我们枚举第二个客栈，然后用第二个客栈反推出前面的方案数。

思路就是，从1到n枚举，输入color和price的值，我们需要记录一个距离第二个客栈最近的咖啡厅价钱合理的客栈位置，用一个now变量记录。

开三个辅助数组，last[i]表示最后一个以i为颜色的客栈的位置，cnt[i]表示以i为颜色的客栈总数，sum[i]可以看作是一个临时数组，用来存储当前的方案数。

可以这么想，当前枚举到一个客栈i，这个i是第二个客栈，那么显然第一个客栈一定在第二个客栈之前，编号必定是0~i-1之间的一个数。如果我发现枚举的时候在某一个客栈前面有一个价钱合理的咖啡厅，那么在这之前的任何一个同色客栈都是第一个客栈可以选的，那么统计一下数量，这就是当前的方案数。

然后更新last数组，更新ans，让cnt[color]++，这样从左到右地推过来就好了。

这个解法简化于暴力算法，暴力算法要循环三层，一层1客栈，二层2客栈，3层合理的位置，这样做显然不行，而我们做的就是去优化掉两层，而是从枚举2客栈出发推出1客栈的位置和所有可行方案，所以这样做是正确的。最后输出即可。

参考代码：

```cpp
#include <iostream>
#define maxn 200005
using namespace std;
int n,k,p;
int color,price;
int last[maxn];
int sum[maxn];
int cnt[maxn];
int ans = 0;
int now;
int main(){
    cin >> n >> k >> p;
    for (int i=1;i<=n;i++){
        cin >> color >> price;
        if (price <= p)
            now = i;
        if (now >= last[color])
            sum[color] = cnt[color];
        last[color] = i;
        ans += sum[color];
        cnt[color]++;
    }
    cout << ans << endl;
    return 0;
}
```