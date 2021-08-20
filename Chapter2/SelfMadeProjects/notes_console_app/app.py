from Notebook import Notebook
import time
from Note import Note
from NoteDates import NoteDates

class App:
    def __init__(self):
        '''The app class contains a notebook that is private since it should only be changed based on user input from the asked questions'''
        self._notebook = Notebook()

    def errorMessage(self, msg):
        '''Special error message for the user. It doesn't raise any errors, it's just an error message'''
        for i in range(3):
            print()

        print(msg)
        print("Try again.")

        for i in range(3):
            print()

    def run(self):
        """Run the app"""
        """
            1. Add a note
            2. Delete a note by name
            3. Delete notes by tags
            4. Search a note by name
            5. Search notes by tags
            6. Exit
        """
        while True:
            main_question_choice = self.runMainQuestions()

            if main_question_choice == 1:
                self.addToNotebook()
            elif main_question_choice == 2:
                self.deleteFromNotebook_byName()
            elif  main_question_choice == 3:
                self.deleteFromNotebook_byTags()
            elif main_question_choice == 4:
                self.searchInNotebook_byName()
            elif main_question_choice == 5:
                self.searchInNotebook_byTags()
            elif main_question_choice == 6:
                break

    def runMainQuestions(self):
        '''This method will ask the user the main questions, presenting to him, how he can manage the notebook'''
        while True:
            print("What do you want to do ?")
            print("1. Add a note")
            print("2. Delete a note by name")
            print("3. Delete notes by tags")
            print("4. Search a note by name")
            print("5. Search notes by tags")
            print("6. Exit")

            # Check the user input
            user_main_questions_input = input("Choice ( 1 -- 6 ) -- > ")
            try:
                user_main_questions_input = int(user_main_questions_input)
                return user_main_questions_input
            except ValueError:
                self.errorMessage("The input that you give must be a number between 1 and 6")

    def getTags(self):
        while True:
            tags = input("Tags of the note ( input as a table with strings ) -- > ")
            try:
                tags = eval(tags)
                if type(tags) != list:
                    raise ValueError

                for tag in tags:
                    if type(tag) != str:
                        raise ValueError

                return tags
            except:
                self.errorMessage("The tags must be in a list type that only has strings ( e.g. : ['tag1', 'tag2'] ). Your input -- > {0}".format(tags))

    def displayNote(self, note):
        print("Note name -- > {0}".format(note.name))
        print("Note memo -- > {0}".format(note.readMemo()))
        print("Note tags -- > {0}".format(note.getTags()))

        note_dates_date_created = time.asctime(note.getDates().dateCreated)
        note_dates_last_date_modified = time.asctime(note.getDates().lastDateModified)
        print("Note date created -- > {0} || Note last date modified -- > {1}".format(note_dates_date_created, note_dates_last_date_modified))

    def addToNotebook_questions(self):
        """Get the list back with all the information needed for the new notebook inside a dictionary"""
        return_dictionary = {}

        note_name = input("Name of the note -- > ")
        note_memo = input("Memo of the note -- > ")
        note_tags = self.getTags()

        return_dictionary["name"] =  note_name
        return_dictionary["memo"] = note_memo
        return_dictionary["tags"] = note_tags

        return return_dictionary

    def addToNotebook(self):
        note_info = self.addToNotebook_questions()

        note_to_add = Note(note_info.get("name"))
        note_to_add.addToMemo(note_info["memo"])
        note_to_add.extendTags(note_info["tags"])

        self._notebook.addNote(note_to_add)

    def deleteFromNotebook_byName(self):
        note_name = input("Name of the note -- > ")
        self._notebook.deleteNote_byName(note_name)

    def deleteFromNotebook_byTags(self):
        note_tags = self.getTags()
        self._notebook.deleteNotes_byTags(note_tags)

    def searchInNotebook_byName(self):
        note_name = input("Name of the note -- > ")
        note_found = self._notebook.searchBy_Name(note_name)
        self.displayNote(note_found)

    def searchInNotebook_byTags(self):
        note_tags = self.getTags()
        notes_found = self._notebook.searchBy_Tags(note_tags)
        for note in notes_found:
            print()
            self.displayNote(note)
            print()

if __name__ == "__main__":
    app = App()
    app.run()