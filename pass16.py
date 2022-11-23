def pass16():
    list=[]
    print("Wow, this is double the minimum needed in order \n"
        "to deter brute force hackers from getting access\n"
        " to your accounts. This will be a legit and secure\n"
        " password. Make sure to enter a minimum of 4 characters\n"
        " for each question going forward.\n\n\n")

      #This section will allocate the choices a user enters. Which append to one list.
    aa = input("Please enter a word or name that you find important or memorable while being creative with the which letters you choose to capitalize: \n")
    b = input("Please enter a second word that you find important or memorable while again being creative with the which letters you choose to capitalize: \n")
    c = str(input("Now enter a number that is significant to you: \n"))
    d = input("Lastly, enter a random series of special characters: \n")
    print(f"The following is your secret phrase to be scrambled: \n\n {aa}  {b}  {c}    {d}")

    #This section is where the appending takes place.
    list.append(aa)
    list.append(b)
    list.append(c)
    list.append(d)


  #This is dedicated lists based off the following if statements.
    list1=[]
    list2=[]
    list3=[]
    list4=[]


  #This here are the parameters that will keep our count of the list in line in combo with the
  #parts of the list so to stay in sync and create our password in correct order.
    count = -1
    t = 0
    tt = 0

    for lists in range(0, 4, 1):
        count += 1
        t = 0
        tt = count
        a = list[tt][t]
        list1.append(a)
    L1 = "".join(list1)
    print(list1)

    count = -1

    for lists in range(0, 4, 1):
        count += 1
        t = 1
        tt = count
        a = list[tt][t]
        list2.append(a)

    L2 = "".join(list2)
    print(list2)

    count = -1

    for lists in range(0, 4, 1):
        count += 1
        t = 2
        tt = count
        a = list[tt][t]
        list3.append(a)

    L3 = "".join(list3)

    print(list3)

    count = -1

    for lists in range(0, 4, 1):
        count += 1
        t = 3
        tt = count
        a = list[tt][t]
        list4.append(a)

    L4 = "".join(list4)
    print(list4)
    print(L1 + L2 + L3 + L4)
pass16()
