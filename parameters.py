def update(a):
    a = a + 2
    return a # if no return, call update(5) will not change value of 5
             # b/c integers are considered as immutable !!!
             # so if call update(), will point to a new memory location

# if a is a list, doesn't have to return
# b/c list is mutable !!!
def update_l(a):
    a[0] = a[0] + 2
    #return a

def main():
    b = 5
    x = update(b)
    print(b)
    print(x)
    
    c = [5]
    #x = update_l(c)
    #print(c)
    #print(x) #if func has no return, x is None
    
    # can do:
    print(c)
    update_l(c)
    print(c) # [7], b/c list c is mutable, will store new val in original memory location
    
    # or add a return in function, and do:
    #print(c)
    #x = update_l(c)
    #print(x)
    

if __name__ == "__main__":
    main()
