def this_recursion(t):
    if (t > 0):
        ans = t + this_recursion(t-1)
        print (ans)
    else:
        ans = 0
    return ans
print ("\nRecursion Example Results")
this_recursion(4)

# 4 + (3 + (2 + (1 + (0))))
