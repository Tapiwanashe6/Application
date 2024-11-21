from submission_feedback import collect_feedback  # Import feedback collection function
from datetime import datetime  # Import datetime to track feedback submission date

class UserFeedback:
    def __init__(self):
        self.last_feedback_date = None
        self.rewards = 0

    def collect_feedback(self):
        # Collect feedback using the imported function
        feedback = collect_feedback()  # This should only be called once per user input
        if feedback:
            self.save_feedback(feedback)
            print("✅ Feedback submitted successfully! Thank you for your input. 😊")
        else:
            print("❗ No feedback provided. Please try again.")

    def save_feedback(self, feedback):
        # Store the feedback date and increase rewards
        self.last_feedback_date = datetime.now()
        self.rewards += 1

    def display_rewards(self):
        # Display current reward points
        if self.rewards > 0:
            print(f"🎉 You have {self.rewards} reward points!")
        else:
            print("🔄 You currently have 0 reward points. Keep submitting feedback to earn rewards! 🙁")

    def check_reminder(self):
        if self.last_feedback_date is None:
            print("❗ You haven't submitted any feedback yet. Please provide feedback to start receiving reminders. 📝")
        else:
            self.send_reminder(self.last_feedback_date)
            print("🔔 Reminder check completed!")

    def send_reminder(self, last_feedback_date):
        # Placeholder for reminder functionality
        print(f"Reminder: You last submitted feedback on {last_feedback_date}.")

