class Bug:
    def __init__(self, title, description, assigned_to=None):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.status = "Open"

class BugTracker:
    def __init__(self):
        self.bugs = []

    def log_bug(self, title, description, assigned_to=None):
        new_bug = Bug(title, description, assigned_to)
        self.bugs.append(new_bug)
        print("Bug logged successfully!")

    def assign_bug(self, bug_index, assigned_to):
        if 0 <= bug_index < len(self.bugs):
            self.bugs[bug_index].assigned_to = assigned_to
            print("Bug assigned successfully!")
        else:
            print("Invalid bug index!")

    def prioritize_and_test(self):
        for bug in self.bugs:
            if bug.status == "Open":
                # Implement prioritization logic here
                bug.status = "Testing"
                print(f"Bug '{bug.title}' is now in testing.")

    def deploy_fixes(self):
        for bug in self.bugs:
            if bug.status == "Testing":
                # Implement deployment logic here
                bug.status = "Closed"
                print(f"Bug '{bug.title}' has been fixed and closed.")

# Creating an instance of the BugTracker
tracker = BugTracker()

# Step 1: Log errors and assign them
tracker.log_bug("UI Glitch", "Button colors are incorrect.")
tracker.log_bug("Function Crash", "App crashes when user does X.", assigned_to="John")

# Step 2: Prioritize and test
tracker.prioritize_and_test()

# Step 3: Deploy the fixes
tracker.deploy_fixes()

# Step 1: Log another bug
tracker.log_bug("Performance Issue", "App is slow when loading large files.")

# Display current bugs
print("Current bugs:")
for idx, bug in enumerate(tracker.bugs):
    print(f"{idx + 1}. {bug.title} - Assigned to: {bug.assigned_to}, Status: {bug.status}")