class TrainingSession:
    def __init__(self, officer_name, training_id, date, location, duration, scheduled=False, completed=False):
        self.officer_name = officer_name
        self.training_id = training_id
        self.date = date
        self.location = location
        self.duration = duration
        self.scheduled = scheduled
        self.completed = completed
 
class PoliceTrainingScheduler:
    def __init__(self):
        self.training_sessions = []
 
    def add_training_session(self, officer_name, training_id, date, location, duration):
        training_session = TrainingSession(officer_name, training_id, date, location, duration)
        self.training_sessions.append(training_session)
        print("Training session added successfully.")
 
    def track_training_completion(self, training_id, completed):
        for session in self.training_sessions:
            if session.training_id == training_id:
                session.completed = completed
                print(f"Training session with ID {training_id} marked as {'completed' if completed else 'not completed'} successfully.")
                return
        print("Training session not found.")
 
    def schedule_police_training(self, training_id):
        for session in self.training_sessions:
            if session.training_id == training_id:
                session.scheduled = True
                print(f"Training session with ID {training_id} scheduled successfully.")
                return
        print("Training session not found.")
 
    def update_training_session(self, training_id,officer_name=None,date=None, location=None, duration=None):
        for session in self.training_sessions:
            #actualTraining_id=session.training_id
 
            if session.training_id == training_id:
                session.officer_name=officer_name.strip() if officer_name else session.officer_name
                #officer_name = input("Enter new officer's name: ").strip()
                session.date = date.strip() if date else session.date
                #date = input("Enter new date (YYYY-MM-DD): ").strip()
                session.location = location.strip() if location else session.location
                #location = input("Enter new location: ").strip()
                session.duration = duration.strip() if duration else session.duration
                #duration = input("Enter new duration: ").strip() 
                return
        print("Training session not found.")
 
    def delete_training_session(self, training_id):
        for session in self.training_sessions:
            if session.training_id == training_id:
                self.training_sessions.remove(session)
                print("Training session deleted successfully.")
                return
        print("Training session not found.")
 
def poc():
    scheduler = PoliceTrainingScheduler()
    while True:
        print("\nWelcome to the Police Training Program Scheduler...")
        print("1. Add Training Session")
        print("2. View Training Sessions")
        print("3. Update Training Session")
        print("4. Delete Training Session")
        print("5. Schedule Police Training")
        print("6. Track Training Completion")
        print("7. Exit")
        choice = input("Please enter your choice: ")
 
        if choice == "1":
            print("\nAdding Training Session")
            officer_name = input("Enter officer's name: ")
            training_id = input("Enter training ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            location = input("Enter location: ")
            duration = input("Enter duration: ")
            scheduler.add_training_session(officer_name, training_id, date, location, duration)
 
        elif choice == "2":
            print("\nViewing Training Sessions")
            if scheduler.training_sessions:
                for session in scheduler.training_sessions:
                    scheduled_status = "Scheduled" if session.scheduled else "Not Scheduled"
                    completion_status = "Completed" if session.completed else "Not Completed"
                    print(f"Officer-Name: {session.officer_name}\nTraining-ID: {session.training_id}\nDate: {session.date}\nLocation: {session.location}\nDuration: {session.duration}\nScheduled: {scheduled_status}\nCompletion: {completion_status}\n")
            else:
                print("No training sessions found.")
 
        elif choice == "3":
            print("\nUpdating Training Session")
            training_id = input("Enter training ID to update: ")
 
            for session in scheduler.training_sessions:
                if session.training_id == training_id:
                    print("Enter the new values for the following parameters (leave blank to keep unchanged):")
                    officer_name = input("Enter new officer's name: ").strip()
                    date = input("Enter new date (YYYY-MM-DD): ").strip()
                    location = input("Enter new location: ").strip()
                    duration = input("Enter new duration: ").strip()
                    scheduler.update_training_session(training_id, officer_name=officer_name or None, date=date or None, location=location or None, duration=duration or None)
                    print("Updated successfully")
                    break
 
                print("Training session not found.")
 
        elif choice == "4":
            print("\nDeleting Training Session")
            training_id = input("Enter training ID to delete: ")
            scheduler.delete_training_session(training_id)
 
        elif choice == "5":
            print("\nScheduling Police Training")
            training_id = input("Enter training ID to schedule: ")
 
            scheduler.schedule_police_training(training_id)
 
        elif choice == "6":
            print("\nTracking Training Completion")
            training_id = input("Enter training ID: ")
            completed = input("Has the officer completed the training? (yes/no): ").lower()
            if completed == "yes":
                scheduler.track_training_completion(training_id, True)
            elif completed == "no":
                scheduler.track_training_completion(training_id, False)
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
 
        elif choice == "7":
            print("Exiting program...")
            break
 
        else:
            print("Invalid choice. Please enter a valid option.")
 
poc()
