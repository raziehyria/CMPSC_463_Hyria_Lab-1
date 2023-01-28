Razie Hyria
Lab #1 - GS matching code
CMPSC 463
1/13/2022


GS Algorithm

Initialize each person to be free.
while (some man is free and hasn't proposed to every woman) {
    Choose such a man m
    w = 1st woman on m's list to whom m has not yet proposed
    if (w is free)
        assign m and w to be engaged
    else if (w prefers m to her fiancé m')
        assign m and w to be engaged, and m' to be free
    else
        w rejects m

Resources:
https://www.youtube.com/watch?v=FhRf0j068ZA
https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm
'''
