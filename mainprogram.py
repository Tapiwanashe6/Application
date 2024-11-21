from user_feedback import UserFeedback

def main():
    user = UserFeedback()  # Create a UserFeedback object
    
    while True:
        print("Main Menu 🌟:")
        print("1. Submit Feedback")
        print("2. Check Rewards")
        print("3. Receive Reminders")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            user.collect_feedback()  # Collect feedback from the user
        elif choice == '2':
            user.display_rewards()  # Show current reward points
        elif choice == '3':
            user.check_reminder()  # Check if reminders are due
        elif choice == '4':
            print("Goodbye! 👋")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid input. Please enter a number from 1 to 4.")  # Invalid option handler

if __name__ == "__main__":
    print("Welcome to the Feedback System! 😊")
    print("We value your feedback, and you'll earn rewards as you submit them.")
    main()  # Start the main program loop

