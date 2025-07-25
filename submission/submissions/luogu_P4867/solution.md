# P4867 题解

截至目前（2020.7.21）本题所有题解都是莫队 + 值域分块 / 值域树状数组，但是这道题实际上是有 poly log 解法的

- **分析**

  注意到这题是一个带有值域限制的区间数颜色，而区间数颜色是有 poly log 解法的，可以看 [这道题](https://www.luogu.com.cn/problem/P1972) 的题解，不过这里还是稍微介绍一下
  
  那题常数较小 ~~也是唯一能过的~~ 的做法是这样的：
  
  对于所有询问按右端点 $r$ 排序，然后将 $i$ 从 $1$ 到 $n$ 扫一遍，每次在一个以原数组下标为编号的树状数组上，在 $i$ 的位置加 $1$，在 $[1,i - 1]$ 中最后一个与 $i$ 同色的位置减 $1$，$i$ 移动到 $r$ 时，查 $[l,r]$ 的和就是颜色数
  
  这实际上是一种 “同色点只数最右边一个” 的思想，每次当 $i$ 出现时，$[1,i - 1]$ 中与 $i$ 同色的点必定不是最右边一个了
  
  接下来考虑把这个做法搬到这道题上
  
  实际上并不需要做太大的改动，我们还是可以使用 “同色点只数最右边一个” 的思想，每次在遇到一个新的 $a_i$ 时加入 $a_i$，删去与 $a_i$ 值相同的上一个点
  
  原来的做法是维护一个只有 (下标) 一维信息的树状数组，改为维护两个信息 (下标,值)，然后每次查询下标在 $[l,r]$ 内，且值在 $[a,b]$ 内有多少个点就可以了
  
  注意到这题要求线性空间，可以使用 cdq分治 来解决这个问题
  
  时间复杂度：$O((n + m) \log ^ 2 n)$，空间复杂度：$O(n + m)$
  
  代码：莫得
  
  因为这题实在是太卡空间了…… 连空间消耗较小的莫队都是贴着边过的，这个做法的空间消耗肯定更大，八成过不了……