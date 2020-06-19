#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
`The loop will run until it hits n^3, so it varys on the number of items in a list`


b) O(n log n)
`The outside loop runs n times, the inner loops runs at log(n). The sum counts how many times j is being doubled "j *= 2." This means that j would increment exponentially until it reaches n.`


c) O(n)
`Varys on the size of the input. If you were to input 4 for bunnies, the operation would run until bunnies is at zero`

## Exercise II
`THOUGHTS:`
`no way to see which floor is floor F unless...`
`you drop an egg from the floor and it breaks`
`extra: what if floor F is the bottom floor...then don't drop egg?`

`STEPS:` 
`take n and divide in half...n/2`
`if the egg breaks on that floor, eliminate that floor and all floors higher`
`take all floors after and divide those in half...n/2`
`continue process of seeing if the egg breaks from the middle floor of the remainder/or beginning`
`if the egg does not break, then break the while loop`
`determine that if no egg is broken from that floor, keep that floor and any floors below`

`RUNTIME:O(log n)`

# I sketched problem out here: https://jamboard.google.com/d/1RPRaoN4YD2JUc4-49Hwme3Zmd7wApzN-rTBVBn6nLec/edit?usp=sharing