class TrainingSession:
    def __init__(self, officer_name, training_id, date, location, duration, completion_id, scheduled=False, completed=False):
        self.officer_name = officer_name
        self.training_id = training_id
        self.date = date
        self.location = location
        self.duration = duration
        self.completion_id = completion_id
        self.scheduled = scheduled
        self.completed = completed
 
 
class PoliceTrainingScheduler:
    def __init__(self):
        self.file_name = "training_sessions.txt"
        self.training_sessions = []
        self.load_training_sessions()
 
    def add_training_session(self, officer_name, training_id, date, location, duration, completion_id):
        training_session = TrainingSession(officer_name, training_id, date, location, duration, completion_id)
        self.training_sessions.append(training_session)
        self.save_training_sessions()
        print("Training session added successfully.")
 
    def load_training_sessions(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    session_data = line.strip().split(',')
                    officer_name, training_id, date, location, duration, completion_id, scheduled, completed = session_data
                    scheduled = scheduled == 'True'
                    completed = completed == 'True'
                    session = TrainingSession(officer_name, training_id, date, location, duration, completion_id, scheduled, completed)
                    self.training_sessions.append(session)
            print("Training sessions loaded successfully.")
        except FileNotFoundError:
            print("No existing training sessions found.")
 
    def save_training_sessions(self):
        with open(self.file_name, 'w') as file:
            for session in self.training_sessions:
                scheduled = 'True' if session.scheduled else 'False'
                completed = 'True' if session.completed else 'False'
                file.write(f"Officer Name:{session.officer_name}\n trainning ID:{session.training_id}\nDOB:{session.date}\n location:{session.location}\n Duration:{session.duration}\n completion ID:{session.completion_id}\n Sheduler:{scheduled}\n track:{completed}\n")
        print("Training sessions saved successfully.")
 
    def track_training_completion(self, training_id, completion_id, completed):
        for session in self.training_sessions:
            if session.training_id == training_id and session.completion_id == completion_id:
                session.completed = completed
                print(f"Training session with Training ID {training_id} and completion ID {completion_id} marked as {'completed' if completed else 'not completed'} successfully.")
                self.save_training_sessions()
                return
        print("Training session not found.")
 
    def schedule_police_training(self, training_id):
        for session in self.training_sessions:
            if session.training_id == training_id:
                session.scheduled = True
                print(f"Training session with ID {training_id} scheduled successfully.")
                self.save_training_sessions()
                return
        print("Training session not found.")
 
    def update_training_session(self, training_id, officer_name=None, date=None, location=None, duration=None):
        for session in self.training_sessions:
            if session.training_id == training_id:
                session.officer_name = officer_name.strip() if officer_name else session.officer_name
                session.date = date.strip() if date else session.date
                session.location = location.strip() if location else session.location
                session.duration = duration.strip() if duration else session.duration
                self.save_training_sessions()
                return
        print("Training session not found.")
 
    def delete_training_session(self, training_id):
        for session in self.training_sessions:
            if session.training_id == training_id:
                self.training_sessions.remove(session)
                print("Training session deleted successfully.")
                self.save_training_sessions()
                return
        print("Training session not found.")
 
def poc():
    scheduler = PoliceTrainingScheduler()
    while True:
        print("\n\n*********************************************************************")
        print("\nWelcome to the Police Training Program Scheduler...")
        print("1. Add  Training Session")
        print("2. View Training Sessions")
        print("3. Update Training Session")
        print("4. Delete Training Session")
        print("5. Schedule Police Training")
        print("6. Track Training Completion")
        print("7. Exit")
        choice = input("Please enter your choice: ")
        print("\n\n*********************************************************************")
 
        if choice == "1":
            print("\nAdding Training Session")
            officer_name = input("Enter officer's name: ")
            training_id = input("Enter training ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            location = input("Enter location: ")
            duration = input("Enter duration: ")
            completion_id = input("Enter completion ID: ")
            scheduler.add_training_session(officer_name, training_id, date, location, duration, completion_id)
 
        elif choice == "2":
            print("\nViewing Training Sessions")
            if scheduler.training_sessions:
                for session in scheduler.training_sessions:
                    scheduled_status = "Scheduled" if session.scheduled else "Not Scheduled"
                    completion_status = "Completed" if session.completed else "Not Completed"
                    print(f"Officer-Name: {session.officer_name}\nTraining-ID: {session.training_id}\nDate: {session.date}\nLocation: {session.location}\nDuration: {session.duration}\nScheduled: {scheduled_status}\nCompletion ID: {session.completion_id}\nCompletion: {completion_status}\n")
            else:
                print("No training sessions found.")
 
        elif choice == "3":
            print("\nUpdating Training Session")
            training_id = input("Enter training ID to update: ")
            officer_name = input("Enter new officer's name (leave blank to keep unchanged): ")
            date = input("Enter new date (YYYY-MM-DD) (leave blank to keep unchanged): ")
            location = input("Enter new location (leave blank to keep unchanged): ")
            duration = input("Enter new duration (leave blank to keep unchanged): ")
            scheduler.update_training_session(training_id, officer_name, date, location, duration)
 
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
            completion_id = input("Enter completion ID: ")
            completed = input("Has the officer completed the training? (yes/no): ").lower()
            if completed == "yes":
                scheduler.track_training_completion(training_id, completion_id, True)
            elif completed == "no":
                scheduler.track_training_completion(training_id, completion_id, False)
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
 
        elif choice == "7":
            print("Exiting program...")
            break
 
        else:
            print("Invalid choice. Please enter a valid option.")
 
poc()
