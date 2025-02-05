import math


a=float(input("Δώσε το α "))
b=float(input("Δώσε το β "))
g=float(input("Δώσε το γ "))
if (a==0):
    print("Η εξίσωση είναι πρωτοβάθμια")
elif (a!=0):
    d=(b*b-4*a*g)
    print("Η διακρίνουσα είναι : {}".format(d))
    if (d<0):
        print("Η ρίζα είναι μυγαδική")
    elif (d>0):
        p1=(-b+ math.sqrt(d) )/(2*a)
        p2=(-b- math.sqrt(d) )/(2*a)
        print("Οι ρίζες είναι {} και {}".format(p1,p2))
    elif (d==0):
        p=(-b)/(2*a)
        print("Μια μοναδική ρίζα την {}".format(p))