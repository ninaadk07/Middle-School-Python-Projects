"""import turtle
for z in range (0,4):
    f = ["red","green","blue","yellow"]
turtle.forward(250)
turtle.backward(500)
b = 1000
def koch(a,b):
    g = 0  
    
    if (a==0):
        turtle.forward(b)
        b = b - 0.8
        
    else:
        q = [60,-120,60,0]
        g = g + 1
        
    
    for k in q:
        return (koch(a-1,b))
        turtle.left(k)
        turtle.pencolor(f[g%z])
        turtle.forward(b/3)
        
    
            
   
            
                
   
          
        
print (koch(4,8))"""



    
