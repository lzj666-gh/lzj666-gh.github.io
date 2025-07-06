# The Wall (easy)

## 题目描述

"The zombies are lurking outside. Waiting. Moaning. And when they come..."

"When they come?"

"I hope the Wall is high enough."

Zombie attacks have hit the Wall, our line of defense in the North. Its protection is failing, and cracks are showing. In places, gaps have appeared, splitting the wall into multiple segments. We call on you for help. Go forth and explore the wall! Report how many disconnected segments there are.

The wall is a two-dimensional structure made of bricks. Each brick is one unit wide and one unit high. Bricks are stacked on top of each other to form columns that are up to $ R $ bricks high. Each brick is placed either on the ground or directly on top of another brick. Consecutive non-empty columns form a wall segment. The entire wall, all the segments and empty columns in-between, is $ C $ columns wide.

## 输入格式

The first line of the input consists of two space-separated integers $ R $ and $ C $ , $ 1<=R,C<=100 $ . The next $ R $ lines provide a description of the columns as follows:

- each of the $ R $ lines contains a string of length $ C $ ,
- the $ c $ -th character of line $ r $ is B if there is a brick in column $ c $ and row $ R-r+1 $ , and . otherwise.

 The input will contain at least one character B and it will be valid.

## 输出格式

The number of wall segments in the input configuration.

## 提示

In the first sample case, the 2nd and 3rd columns define the first wall segment, and the 5th column defines the second.

## 时空限制

时间限制: 500 ms
内存限制: 250 MB
