def simple_interest(principle, intrest, time):
    return(principle*interest*time)/100
if_name_ == "_main_":
    p = int(input("enter principal amt"))
    i = int(input("enter interest"))
    t = int(input("enter time in months"))
    print("simple interest is:", simple_interest(p,i,t))