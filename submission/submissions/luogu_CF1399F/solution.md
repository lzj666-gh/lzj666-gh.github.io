# CF1399F 题解

我们可以先求出每条线段至多可以包含的线段数 $c_i$，然后定义 $dp_i$ 为在 $[1,i]$ 这个范围上我们至多能选出多少条满足题意的线段数，我们枚举不被包含的线段，由于不能与其他线段相交，故状态转移为

$$dp_{r_i} = \max\{dp_{r_i-1},dp_{l_i-1}+c_i\}$$

$c_i$ 的求法类似，为保证状态转移的正确性，我们需要从将所有线段按照其长度排序，这样可以从短线段转移到长线段。排序后，对每条线段，在其对应的范围上跑一遍上述转移。

注意到 $l_i$ 和 $r_i$ 范围比较大，需要先离散化之后再计算。这样复杂度是 $O(n^2)$ 的。

AC 代码 (Golang)

```go
package main

import (
	"bufio"
	. "fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	type segment struct{ l, r, contains int }

	var T, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		seg := make([]segment, n)
		a := []int{}
		for i := range seg {
			Fscan(in, &seg[i].l, &seg[i].r)
			a = append(a, seg[i].l, seg[i].r)
		}
		sort.Ints(a)
		k := 1
		kth := map[int]int{a[0]: k}
		for i := 1; i < len(a); i++ {
			if a[i] != a[i-1] {
				k++
				kth[a[i]] = k
			}
		}
		for i, s := range seg {
			seg[i].l = kth[s.l]
			seg[i].r = kth[s.r]
		}
		sort.Slice(seg, func(i, j int) bool { a, b := seg[i], seg[j]; return a.r-a.l < b.r-b.l })

		k++
		ids := make([][]int, k)
		for i, s := range seg {
			ids[s.r] = append(ids[s.r], i)
		}
		for i, s := range seg {
			dp := make([]int, k)
			for j := s.l; j <= s.r; j++ {
				dp[j] = dp[j-1]
				for _, id := range ids[j] {
					if t := seg[id]; t.l >= s.l {
						dp[j] = max(dp[j], dp[t.l-1]+t.contains)
					}
				}
			}
			seg[i].contains = dp[s.r] + 1
		}

		rseg := make([][]segment, k)
		for _, s := range seg {
			rseg[s.r] = append(rseg[s.r], s)
		}
		dp := make([]int, k)
		for i := 1; i < k; i++ {
			dp[i] = dp[i-1]
			for _, s := range rseg[i] {
				dp[i] = max(dp[i], dp[s.l-1]+s.contains)
			}
		}
		Fprintln(out, dp[k-1])
	}
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```
