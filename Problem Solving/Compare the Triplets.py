def compareTriplets(a, b):
    # Write your code here
    c1, c2 = 0,0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            c1 += 1
        if a[i] < b[i]:
            c2 += 1
        
    return c1,c2
