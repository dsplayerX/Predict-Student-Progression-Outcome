# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1867214

# Date: 07/12/2021


# list to store input progression data for printing list and output as a text file
input_progress_list = []
# variables for counting stars for histograms
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0


def user_inputs():
    """getting user inputs with validation"""
    try:
        cred_range = range(0, 121, 20)

        pass_cred = int(input("\nPlease enter your credits at pass: "))
        while pass_cred not in cred_range:
            print("Out of range")
            pass_cred = int(input("Please enter your credits at pass: "))
        defer_cred = int(input("Please enter your credits at defer: "))
        while defer_cred not in cred_range:
            print("Out of range")
            defer_cred = int(input("Please enter your credits at defer: "))
        fail_cred = int(input("Please enter your credits at fail: "))
        while fail_cred not in cred_range:
            print("Out of range")
            fail_cred = int(input("Please enter your credits at fail: "))

        if pass_cred + defer_cred + fail_cred != 120:
            print("Total incorrect")
            print("Try again...")
            pass_cred, defer_cred, fail_cred = user_inputs()  # will assign returned values into three variables
            return pass_cred, defer_cred, fail_cred
            # will discard last entered set of credits and give a new input prompt to enter a new set of data.
        else:
            return pass_cred, defer_cred, fail_cred

    except ValueError:
        print("Integer Required")
        print("Try again...")
        pass_cred, defer_cred, fail_cred = user_inputs()
        return pass_cred, defer_cred, fail_cred


def progress_outcomes(pass_cred, defer_cred, fail_cred):
    """finding progress outcomes and appending to lists for staff version part of the program."""
    global progress_count, trailer_count, retriever_count, exclude_count
    if pass_cred == 120:
        print("Progress")
        progress_count += 1
        input_data = ("Progress -", pass_cred, ",", defer_cred, ",", fail_cred)
        input_progress_list.append(input_data) # appends progression data stored in above variable to the input progress list

    elif pass_cred == 100 and (defer_cred == 20 or fail_cred == 20):
        print("Progress (module trailer)")
        trailer_count += 1
        input_data = ("Progress (module trailer) -", pass_cred, ",", defer_cred, ",", fail_cred)
        input_progress_list.append(input_data)

    elif pass_cred == 40 and fail_cred == 80:
        print("Exclude")
        exclude_count += 1
        input_data = ("Exclude -", pass_cred, ",", defer_cred, ",", fail_cred)
        input_progress_list.append(input_data)

    elif pass_cred == 20 and (fail_cred == 80 or fail_cred == 100):
        print("Exclude")
        exclude_count += 1
        input_data = ("Exclude -", pass_cred, ",", defer_cred, ",", fail_cred)
        input_progress_list.append(input_data)

    elif pass_cred == 0 and (defer_cred == 40 or defer_cred == 20):
        print("Exclude")
        exclude_count += 1
        input_data = ("Exclude -", pass_cred, ",", defer_cred, ",", fail_cred)
        input_progress_list.append(input_data)

    elif fail_cred == 120:
        print("Exclude")
        exclude_count += 1
        input_data = ("Exclude -", pass_cred, ",", defer_cred, ",", fail_cred)
        input_progress_list.append(input_data)

    else:
        # after all the above conditions and validation, remaining possible outcomes are all "Module Retriever"
        print("Module retriever")
        retriever_count += 1
        input_data = ("Module Retriever -", pass_cred, ",", defer_cred, ",", fail_cred)
        input_progress_list.append(input_data)
    return progress_count, trailer_count, retriever_count, exclude_count


def clear_stored_data():
    """setting all count variables to "0" and clear input progress list to accept new sets of data"""
    global progress_count, trailer_count, retriever_count, exclude_count  # to change the value of the global variables inside the function
    progress_count = 0
    trailer_count = 0
    retriever_count = 0
    exclude_count = 0
    input_progress_list.clear()


def main_menu():
    """main menu with 5 options, a clear all function and a quit function"""
    global progress_count, trailer_count, retriever_count, exclude_count
    print()
    print("="*50)
    print("PREDICT PROGRESSION OUTCOMES".center(50))
    print("="*50)
    print("MAIN MENU".center(50))
    print("-"*15, "student version".center(18), "-"*15)
    print("   1. Student Version")
    print("-"*16, "staff version".center(16), "-"*16)
    print("   2. Staff Version with Histogram \n   3. Vertical Histogram (extension) \n   4. Input progression data list (extension) \n   5. Output to a text file (extension)")
    print("-"*19, "optional".center(10), "-"*19)
    print("   c. Clear all entered data \n   q. Quit")
    print("-"*50)
    menu_option = input("Select option: ")

    if menu_option == "1":
        print("-" * 50)
        print("Student Version")
        print("-" * 50)
        pass_cred, defer_cred, fail_cred = user_inputs()  # will assign returned values from function, user_inputs(), into three variables
        progress_outcomes(pass_cred, defer_cred, fail_cred)  # takes in above variables as parameters for the function
        clear_stored_data()  # to stop the influence of student version's data to histogram and list extensions.
        print("\nReturning to main menu...")
        main_menu()

    elif menu_option == "2":
        print("-"*50)
        print("Staff Version with Horizontal Histogram")
        print("-"*50)

        run_again = "y"
        while run_again == "y":

            pass_cred, defer_cred, fail_cred = user_inputs()
            progress_outcomes(pass_cred, defer_cred, fail_cred)
            print("\nWould you like to enter another set of data?")
            run_again = input("Enter 'y' for yes or 'q' to view results and go back to main menu: ")

            if run_again == "q":
                # printing horizontal histogram on quitting the loop
                print("-"*50)
                print("Horizontal Histogram")
                print()
                print("Progress".ljust(10), progress_count, ":", "* " * progress_count)
                print("Trailer".ljust(10), trailer_count, ":", "* " * trailer_count)
                print("Retriever".ljust(10), retriever_count, ":", "* " * retriever_count)
                print("Excluded".ljust(10), exclude_count, ":", "* " * exclude_count)
                print()
                print((progress_count + trailer_count + retriever_count + exclude_count), "outcomes in total.")
                print("-"*50)
                print("Returning to main menu...")
                break

            elif run_again != "q" and run_again != "y":  # breaks out of the loop and goes back to main menu.
                print("-"*50)
                print("Wrong input \nSaved entered data (select option '2' again to continue)\nReturning to main menu...")
                break

        main_menu()
        # saved counts and progress data isn't affected, so you can select option 2 again from main menu to continue entering more data.
        # but all saved data will get cleared when running student version or option 'c'.

    elif menu_option == "3":

        # printing a vertical histogram from the data entered in option 1.
        print("-"*50)
        print("Vertical Histogram\n")
        
        print("Progress".center(10), progress_count ,"| Trailer".center(10), trailer_count ,"| Retriever".center(10), retriever_count ,"| Excluded".center(10), exclude_count )

        # assigns count variable values to temporary variables to keep count for the while loop.
        progress_count_temp = progress_count
        trailer_count_temp = trailer_count
        retriever_count_temp = retriever_count
        exclude_count_temp = exclude_count

        # calculate sum of all the count values and print stars or blank spaces until the temporary counters are zero.
        i = 0
        while i < (progress_count + trailer_count + retriever_count + exclude_count):
            i += 1
            progress_count_temp -= 1
            trailer_count_temp -= 1
            retriever_count_temp -= 1
            exclude_count_temp -= 1
            if progress_count_temp >= 0:
                print("*".center(12), end='')  # prints a star.
            else:
                print(" ".center(12), end="")  # prints a blank space when the condition is false.
            if trailer_count_temp >= 0:
                print("*".center(13), end='')
            else:
                print(" ".center(13), end="")
            if retriever_count_temp >= 0:
                print("*".center(15), end='')
            else:
                print(" ".center(15), end="")
            if exclude_count_temp >= 0:
                print("*".center(13))
            else:
                print(" ".center(13))
        print((progress_count + trailer_count + retriever_count + exclude_count), "outcomes in total.")
        print("-"*50)
        print("Returning to main menu...")
        main_menu()

    elif menu_option == "4":
        print("-"*50)
        print("List of input progression data")
        print("-" * 50)
        for i in range(len(input_progress_list)):
            print(*input_progress_list[i])  # prints only the elements (without ',' or '()') from the list
        print("-"*50)
        print("Returning to main menu...")
        main_menu()

    elif menu_option == "5":
        print("-"*50)
        print("Save input progression data as a text file")
        print("-"*50)
        # printing only the elements of the input progress list to a file, with correct formatting.
        file = open("Saved input progression data.txt", "w") # creates or truncates the text file before appending progress data to it
        for i in range(len(input_progress_list)):
            print(*input_progress_list[i], file=open("Saved input progression data.txt", "a"))
            # prints directly to a text file, appending each element in the list to the file without brackets or commas.
        file.close()
        print("File saved successfully.")
        print("Preview of saved text file.")
        print("-"*50)
        # reading the saved text file and printing all lines
        f = open("Saved input progression data.txt", "r")
        lines = f.read()
        print(lines)
        f.close()
        print("=" * 50)
        print("Returning to main menu...")
        main_menu()

    elif menu_option == "c":
        # clearing all lists and stored data to accept new sets of data.
        clear_stored_data()
        print("-" * 50)
        print("Cleared all entered data.")
        print("Returning to main menu...")
        main_menu()

    elif menu_option == "q":
        print("-"*50)
        print("Quitting the program")

    else: # will reopen main menu when input doesn't satisfy given conditions
        print("-"*50)
        print("Wrong input. Reopening main menu...")
        main_menu()


main_menu()
