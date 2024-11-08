from lib.models.destination import Destination
from lib.models.activity import Activity
from lib.models.expense import Expense
from lib.models.user import User

# Example usage for debugging
if __name__ == "__main__":
    # Create a new user
    user_id = User.create("John Doe", "johndoe@example.com")
    print("User created:", User.get_all())

    # Create a new destination linked to the user
    destination_id = Destination.create("Paris", "France", "The city of lights", user_id)
    print("Destinations:", Destination.get_all())

    # Create an activity linked to the destination
    activity_id = Activity.create(destination_id, "Eiffel Tower Tour", "2023-12-01", "10:00", 50.0, "A guided tour")
    print("Activities for destination:", Activity.get_by_destination(destination_id))

    # Add an expense to the activity
    Expense.create(activity_id, 20.0, "Souvenir purchase", "2023-12-01", "Shopping")
    print("Expenses for activity:", Expense.get_by_activity(activity_id))
