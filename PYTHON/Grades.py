x = int(input("enter grades : "))

def a():
    return "Grade A"
def b():
    return "Grade B"
def c():
    return "Grade C"
def d():
    return "Grade D"
def f():
    return "Grade F(ail)"

if (x>=90 and x<=100):
    print (a())
elif (x>=80 and x<=89):
    print (b())
elif (x>=70 and x<=79):
    print (c())
elif (x>=60 and x<=69):
    print (d())
elif (x>=0 and x<=59):
    print (f())
else:
    print ("What?")
