# Disturbed People

https://codeforces.com/problemset/problem/1077/B

There is a house with nn flats situated on the main street of Berlatov. Vova is watching this house every night. The house can be represented as an array of nn integer numbers a1,a2,…,ana1,a2,…,an, where ai=1ai=1 if in the ii-th flat the light is on and ai=0ai=0 otherwise.

Vova thinks that people in the ii-th flats are disturbed and cannot sleep if and only if 1<i<n1<i<n and ai−1=ai+1=1ai−1=ai+1=1 and ai=0ai=0.

Vova is concerned by the following question: what is the minimum number **k** such that if people from exactly kk pairwise distinct flats will turn off the lights then nobody will be disturbed? Your task is to find this number **k**.

### Input

The first line of the input contains one integer nn (3≤n≤1003≤n≤100) — the number of flats in the house.

The second line of the input contains nn integers a1,a2,…,ana1,a2,…,an (ai∈{0,1}ai∈{0,1}), where aiai is the state of light in the ii-th flat.

### Output

Print only one integer — the minimum number **k** such that if people from exactly **k** pairwise distinct flats will turn off the light then nobody will be disturbed.