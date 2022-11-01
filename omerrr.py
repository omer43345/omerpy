def sum_of_list():
    sum=0
    length=int(input("enter a number\n"))
    lst=[]
    for x in range(0,length):
        lst.append(int(input("enter a number\n")))
        sum+=lst[x]

    print(f"list:  {lst}\nsum:  {sum}")
sum_of_list()