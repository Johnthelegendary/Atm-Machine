balance = 23500
pin = 1234
savings = "1"
current = "2"
pin_trail_count = 0
enter_sav_acc_num = 0
enter_curr_acc_num = 0
amount = 0
max_pin_trail = 3
acc_type = current
all_good = True


def welcome():
    enter_pin()


def enter_pin():
    global pin_trail_count
    try:
        print("Welcome To GTBank ATM Gallery\n\n       please\n")
        entered_pin = int(input("Enter Your 4 Digit Pin: "))
        while entered_pin != pin:
            pin_trail_count += 1
            if pin_trail_count != max_pin_trail:
                print("\nWrong Pin, Try Again! \nYou Have", max_pin_trail - pin_trail_count, "Trail Left\n")
                print("Welcome To GTBank ATM Gallery\n\n       please\n")
                entered_pin = int(input("Enter Your 4 Digit Pin: "))
            elif pin_trail_count == max_pin_trail:
                print("\nYou Have No Trail Left\n3 Wrong Attempt.\n Take Your Card!")
                break
        if entered_pin == pin:
            task()
    except:
        print("Invalid Input!")
        enter_pin()


def task():
    global enter_sav_acc_num, enter_curr_acc_num, amount, all_good
    the_choice = input(
        "\nWhat will You Like To Do?\n Type \"A\" To Check Balance\n Type \"B\" To Withdraw\n Type \"C\" To Transfer\n "
        "Type \"D\" To Do Nothing Else: ")
    if the_choice in "A,a":
        print("\nYour Balance is", balance, " Naira")
        task()
    elif the_choice in "B, b":
        select_acc_type = input(
            "\n Choose Your Account Type!\n Type \"1\" For Savings Account\n Type \"2\" For Current Account: ")
        while select_acc_type != acc_type:
            print("\nInvalid Account Selected")
            select_acc_type = input(
                "\n Choose Your Account Type!\n Type \"1\" For Savings Account\n Type \"2\" For Current Account: ")
        while select_acc_type == acc_type:
            try:
                amount = int(input("\nHow Much Will You Like To Withdraw? "))
                if amount < balance:
                    print("\n   Transaction Successful\n      Take Your Cash!\n")
                    task()
                elif amount > balance:
                    print("\n     Insufficient Fund!\n Your Balance is", balance, " Naira")
                    task()
                break
            except:
                print("Invalid Amount Entered, Try Again!")
    elif the_choice in "C, c":
        select_acc_type = input(
            "\n  Seclect Your Account Type!\n Type \"1\" For Savings Account\n Type \"2\" For Current Account: ")
        while select_acc_type != acc_type:
            print("\n   Invalid Account Selected!")
            select_acc_type = input(
                "\n  Seclect Your Account Type!\n Type \"1\" For Savings Account\n Type \"2\" For Current Account: ")
        if select_acc_type == acc_type:
            select_dest_acc_type = input(
                "\n Select The Destination Account Type!\n Type \"1\" For Savings Account\n Type \"2\" For Current Account: ")
            while all_good:
                if select_dest_acc_type == "1":
                    while all_good:
                        try:
                            enter_sav_acc_num = int(input("\nEnter The Savings Account Number: "))
                            all_good = False
                        except:
                            print("\nInvalid Input, Try Again!")
                        try:
                            amount = int(input("\nEnter The Amount to Transfer: "))
                        except:
                            print("\nInvalid Input, Try Again")
                            all_good = True
                    confirmation = input(
                        "Are You Sure You Want To Transfer " + str(amount) + " Naira To " + str(enter_sav_acc_num) + " ? \n Type \"Y\" To Confirm\n Type \"N\" To Cancel: ")
                    if confirmation in "Y,y":
                        enter_sav_acc_num = str(enter_sav_acc_num)
                        amount = int(amount)
                        if amount < balance:
                            print("\nTransfer Successful!")
                            task()
                        elif amount > balance:
                            print("\n   Insufficient Fund!\n Your Balance is", balance, " Naira")
                            task()
                    elif confirmation in "N, n":
                        task()
                elif select_dest_acc_type == "2":
                    while all_good:
                        try:
                            enter_curr_acc_num = int(input("\nEnter The Current Account Number: "))
                            all_good = False
                        except:
                            print("\nInvalid Input, Try Again!")
                        try:
                            amount = int(input("\nEnter The Amount to Transfer: "))
                        except:
                            print("\nInvalid Input, Try Again")
                            all_good = True
                    confirmation = input(
                        "\nAre You Sure You Want To Transfer " + str(
                            amount) + " Naira To " + str(enter_curr_acc_num) + " ? \n Type \"Y\" To Confirm\n Type \"N\" To Cancel: ")
                    if confirmation in "Y,y":
                        enter_curr_acc_num = str(enter_curr_acc_num)
                        amount = int(amount)
                        if amount < balance:
                            print("\nTransfer Successful!")
                            task()
                        elif amount > balance:
                            print("\n    Insufficient Fund!\n Your Balance is", balance, " Naira")
                            task()
                    elif confirmation in "N, n":
                        task()
                else:
                    print("\n   Invalid Account Type Selected!")
                    select_dest_acc_type = input(
                        "\n Select The Destination Account Type!\n Type \"1\" For Savings Account\n Type \"2\" For Current Account: ")

    elif the_choice in "D,d":
        print("\nTake Your Card!")


    else:
        print("\nInvalid Selection!")
        task()


welcome()