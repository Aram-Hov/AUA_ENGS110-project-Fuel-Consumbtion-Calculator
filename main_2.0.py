import functions
functions.load_vehicle_data()

def main():
    print('Welcome to fuel consumption calculator!')
    while True:
        story = functions.choose_story()
        functions.execution_of_choosen_feature(story)
        continue_or_exit = input("\n\nIn case you want to continue press 1 else print 2 to exit > ")
        if continue_or_exit not in ["1", "2"]:
            print("Please try again")
        elif continue_or_exit == "1":
            print("Ok, what would you like to do?")
        elif continue_or_exit == "2":
            print("Thanks for using our app, see you soon!")
            break


main()
