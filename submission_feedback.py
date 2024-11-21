def collect_feedback():
    # Collect feedback from user
    try:
        food_quality = int(input("Rate the food quality (1-5): "))
        service_efficiency = int(input("Rate service efficiency (1-5): "))
        menu_variety = int(input("Rate menu variety (1-5): "))
        comments = input("Additional comments (optional): ")

        # Return feedback as a dictionary or any other data structure
        feedback = {
            'food_quality': food_quality,
            'service_efficiency': service_efficiency,
            'menu_variety': menu_variety,
            'comments': comments
        }
        return feedback
    except ValueError:
        print("❗ Invalid input. Please enter numbers between 1 and 5 for ratings.")
        return None

