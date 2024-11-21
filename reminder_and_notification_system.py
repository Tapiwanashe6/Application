from datetime import datetime, timedelta

def send_reminder(last_feedback_date):
    if datetime.now() - last_feedback_date > timedelta(days=1):  # Reminder after 1 day
        print("🔄 Reminder: It's been a while since you gave feedback. Please share your thoughts! 📝")
    else:
        print("📝 Thank you for submitting your feedback recently!")

