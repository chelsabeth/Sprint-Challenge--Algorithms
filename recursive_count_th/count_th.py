'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word): # passes in word = theodor
    if len(word) <= 1: # checks to see if length is less than or equal to 1, because if so, cannot contain "th"
        return 0 # base case - keeps calling function until meets this 
    else: 
        th_exists = 0 # sets th_exists to 0 first loop
        if word[0:2] == 'th': # if the first 2 letters are "th"
            th_exists = 1 # change count to 1 

        return th_exists + count_th(word[1:]) # shortens name by 1 every time - "heodor"

# say the word was "theodor"

# python tutor: http://pythontutor.com/live.html#code=def%20count_th%28word%29%3A%0A%20%20%20%20if%20len%28word%29%20%3C%3D%201%3A%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20th_exists%20%3D%200%0A%20%20%20%20%20%20%20%20if%20word%5B0%3A2%5D%20%3D%3D%20'th'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20th_exists%20%3D%201%0A%0A%20%20%20%20%20%20%20%20return%20th_exists%20%2B%20count_th%28word%5B1%3A%5D%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Acount_th%28'theodor'%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
    
