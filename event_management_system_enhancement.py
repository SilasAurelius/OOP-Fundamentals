# Task 2: Event Management System Enhancement

# - Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

# - Code Example: Basic Event class without participant tracking.

class Event:
    def __init__(self, name, date, participants=0):
        self.name = name
        self.date = date    
        self.participants = participants
    
    def add_participant(self):
        self.participants += 1
    
    def get_participants(self):
        return self.participants

new_participant1 = Event("Kevin's Retirement Party", "10-20-2024", 50)
new_participant2 = Event("Cindy's Wedding", "11-24-2025", 100)

new_participant1.add_participant()
new_participant2.add_participant()

print(f"{new_participant1.name} event has {new_participant1.get_participants()} participants.")
print(f"{new_participant2.name} event has {new_participant2.get_participants()} participants.")

