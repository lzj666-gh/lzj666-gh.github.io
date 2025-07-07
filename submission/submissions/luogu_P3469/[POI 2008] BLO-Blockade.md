# [POI 2008] BLO-Blockade

## 题目描述

There are exactly $n$ towns in Byteotia.

Some towns are connected by bidirectional roads.

There are no crossroads outside towns, though there may be bridges,    tunnels and flyovers. Each pair of towns may be connected by at most    one direct road. One can get from any town to any other-directly    or indirectly.

Each town has exactly one citizen.

For that reason the citizens suffer from loneliness.

It turns out that each citizen would like to pay a visit to    every other citizen (in his host's hometown), and do it    exactly once. So exactly $n\cdot (n-1)$ visits should take place.

That's right, should.

Unfortunately, a general strike of programmers, who    demand an emergency purchase of software, is under way.

As an act of protest, the programmers plan to block one town of    Byteotia, preventing entering it, leaving it, and even passing through.

As we speak, they are debating which town to choose so that    the consequences are most severe.

Task    Write a programme that:

reads the Byteotian road system's description from the            standard input,           for each town determines, how many visits could take place            if this town were not blocked by programmers,           writes out the outcome to the standard output.



## 输入格式

In the first line of the standard input there are two positive    integers: $n$ and $m$ ($1\le n\le 100\ 000$, $1\le m\le 500\ 000$) denoting the number of towns and roads, respectively.

The towns are numbered from 1 to $n$.

The following $m$ lines contain descriptions of the roads.

Each line contains two integers $a$ and $b$ ($1\le a<b\le n$) and    denotes a direct road between towns numbered $a$ and $b$.


## 输出格式

Your programme should write out exactly $n$ integers to the standard    output, one number per line. The $i^{th}$ line should contain the number    of visits that could not take place if the programmers blocked the town    no. $i$.


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
