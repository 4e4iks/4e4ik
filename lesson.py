import json
from datetime import datetime

class Note:
    def init(self, id, title, message, timestamp):
        self.id = id
        self.title = title
        self.message = message
        self.timestamp = timestamp

class NoteApp:
    def init(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open("notes.json", "r") as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(**note_data)
                    self.notes.append(note)
        except FileNotFoundError:
            pass

    def save_notes(self):
        with open("notes.json", "w") as file:
            data = [{"id": note.id, "title": note.title, "message": note.message, "timestamp": note.timestamp}
                    for note in self.notes]
            json.dump(data, file, indent=2)

    def add_note(self, title, message):
        note_id = len(self.notes) + 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, title, message, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        print("Note successfully saved.")

    def read_notes(self, date_filter=None):
        if date_filter:
            filtered_notes = [note for note in self.notes if note.timestamp.startswith(date_filter)]
            for note in filtered_notes:
                print(f"ID: {note.id}, Title: {note.title}, Body: {note.message}, Date/Time: {note.timestamp}")
        else:
            for note in self.notes:
                print(f"ID: {note.id}, Title: {note.title}, Body: {note.message}, Date/Time: {note.timestamp}")

    def edit_note(self, note_id, title, message):
        for note in self.notes:
            if note.id == note_id:
                note.title = title
                note.message = message
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print("Note successfully edited.")
                return
        print("Note with the specified ID not found.")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()
        print("Note successfully deleted.")

if name == "main":
    note_app = NoteApp()

    while True:
        command = input("Enter command (add/read/edit/delete/exit): ")

        if command == "add":
            title = input("Enter note title: ")
            message = input("Enter note body: ")
            note_app.add_note(title, message)

        elif command == "read":
            date_filter = input("Enter date for filtering (yyyy-mm-dd): ")
            note_app.read_notes(date_filter)

        elif command == "edit":
            note_id = int(input("Enter note ID for editing: "))
            title = input("Enter new note title: ")
            message = input("Enter new note body: ")
            note_app.edit_note(note_id, title, message)

        elif command == "delete":
            note_id = int(input("Enter note ID for deletion: "))
            note_app.delete_note(note_id)

        elif command == "exit":
            break

        else:
            print("Invalid command. Please try again.")