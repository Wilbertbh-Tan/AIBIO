def leaky(arraymin, arraymax):
    if arraymin[-1] < 0.30 * arraymax[-1]:
        return "Not Leaky"
    else:
        return "Leaky"
    
test1= [0, 0, 0, 0 ,0 ,0 ,0 ,0.001 ,0.1]
test2= [0, 0 ,0, 0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4]

display(leaky(test1,test2))

test1= [0, 0, 0, 0 ,0 ,0 ,0 ,0.001 ,0.1]
test2= [0, 0 ,0, 0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.2]

display(leaky(test1,test2))
