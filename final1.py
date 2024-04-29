     
class TrainingSession:
    def __init__(self, training_id, date, location, duration):
        self.training_id = training_id
        self.date = date
        self.location = location
        self.duration = duration
 
class TrainingCompletion:
    def __init__(self, completion_id, training_id, outcome):
        self.completion_id = completion_id
        self.training_id = training_id
        self.outcome = outcome
 
class PoliceTrainingScheduler:
    def __init__(self):
        self.training_sessions = []
        self.completion_records = []
 
    def add_training_session(self, training_id, date, location, duration):
        training_session = TrainingSession(training_id, date, location, duration)
        self.training_sessions.append(training_session)
        print("Training session added successfully.")
 
    def track_training_completion(self, completion_id, training_id, outcome):
        completion_record = TrainingCompletion(completion_id, training_id, outcome)
        self.completion_records.append(completion_record)
        print("Training completion tracked successfully.")
 
    def schedule_police_training(self, training_id):
        for session in self.training_sessions:
            if session.training_id == training_id:
                session.scheduled = True
                print(f"Training session with ID {training_id} scheduled successfully.")
                return
        print("Training session not found.")

    def update_training_session(self, training_id, date, location, duration):
        for session in self.training_sessions:
            if session.training_id == training_id:
                session.date = date
                session.location = location
                session.duration = duration
                print("Training session updated successfully.")
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
        print("\nWelcome to the Police Training Program Scheduler!")
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
            training_id = input("Enter training ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            location = input("Enter location: ")
            duration = input("Enter duration: ")
            scheduler.add_training_session(training_id, date, location, duration)
 
        elif choice == "6":
            print("\nTracking Training Completion")
            completion_id = input("Enter completion ID: ")
            training_id = input("Enter training ID: ")
            outcome = input("Enter outcome (Completed/Not Completed): ")
            scheduler.track_training_completion(completion_id, training_id, outcome)
 
        elif choice == "5":
            print("\nScheduling Police Training")
            training_id = input("Enter training ID to schedule: ")
            scheduler.schedule_police_training(training_id)
 
        elif choice == "3":
            print("\nUpdating Training Session")
            training_id = input("Enter training ID to update: ")
            date = input("Enter new date (YYYY-MM-DD): ")
            location = input("Enter new location: ")
            duration = input("Enter new duration: ")
            scheduler.update_training_session(training_id, date, location, duration)
 
        elif choice == "4":
            print("\nDeleting Training Session")
            training_id = input("Enter training ID to delete: ")
            scheduler.delete_training_session(training_id)
 
        elif choice == "2":
            print("\nTraining Sessions:")
            if scheduler.training_sessions:
                for session in scheduler.training_sessions:
                    print(f"Training ID: {session.training_id}, Date: {session.date}, Location: {session.location}, Duration: {session.duration}")
            else:
                print("No training sessions found.")
 
        elif choice == "7":
            print("Exiting program...")
            break
 
        else:
            print("Invalid choice. Please enter a valid option.")
 

poc()
