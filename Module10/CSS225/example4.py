#Example1: Using continue statement

print("Example 1: Using continue statement")
i=0
while i<5:
    i+=1
    if i==3:
        continue #Skip the rest of the loop body and continue with the next interation
    print(i)