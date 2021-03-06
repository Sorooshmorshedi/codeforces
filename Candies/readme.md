# Candies

Polycarpus has got *n* candies and *m* friends (*n* ≥ *m*). He wants to make a New Year present with candies to each friend.  Polycarpus is planning to present all candies and he wants to do this in the **fairest** (that is, most equal) manner. He wants to choose such *a**i*, where *a**i* is the number of candies in the *i*-th friend's present, that the maximum *a**i* differs from the least *a**i* as little as possible.

For example, if *n* is divisible by *m*, then he is going to present the same number of candies to all his friends, that is, the maximum *a**i* won't differ from the minimum one.

### Input

The single line of the input contains a pair of space-separated positive integers *n*, *m* (1 ≤ *n*, *m* ≤ 100;*n* ≥ *m*) — the number of candies and the number of Polycarpus's friends.

### Output

Print the required sequence *a*1, *a*2, ..., *a**m*, where *a**i* is the number of candies in the *i*-th friend's present. All numbers *a**i* must be positive integers, total up to *n*, the maximum one should differ from the minimum one by the smallest possible value.