from Note import Note

class Notebook:
    """
    The notebook class that manages all the notes
    """

    def __init__(self):
        """The notebook class contains only one property and that is the Notes property which is private because you should only be able to access it through the methods for notes."""
        self._Notes = list()

    def addNote(self, note_to_add):
        """Adds a note to the notebook. The note_to_add argument must be of type Note"""
        if type(note_to_add) != Note:
            raise ValueError("The argument note_to_add must be of type Note. Argument given : {0}".format(note_to_add))
        else:
            # Checking if there are other notes inside the self._Notes list with the same name. All note names must be unique, there are not duplicates allowed.
            note_unique = True

            for note in self._Notes:
                if note.name == note_to_add.name:
                    note_unique = False
                    break
                else:
                    continue

            if note_unique:
                self._Notes.append(note_to_add)
            else:
                raise ValueError("We already have a note with the name {0} inside the notebook. Please choose a new name for the note.".format(note_to_add.name))

        def sort_key_function(note):
            return note.name

        self._Notes.sort(key=sort_key_function, reverse=False)

    def deleteNote_byName(self, note_name_to_delete):
        '''Deletes a note by name inside the notebook'''
        # There's no point in checking the note name to make sure that it is a string since we will check if it matches a note.name property inside the notes list. All note names are strings and that is checked inside the note class so there's no point in checking it again here
        note_found = False
        index_to_delete = 0
        for note in self._Notes:
            if note.name == note_name_to_delete:
                note_found = True
                break
            else:
                index_to_delete += 1
                continue

        if note_found:
            del self._Notes[index_to_delete]
        else:
            raise ValueError("We couldn't find a note with the given name {0}. Make sure you give the method the correct name.".format(note_name_to_delete))

    def deleteNotes_byTags(self, delete_tags):
        '''Delete all the notes that match the given tags perfectly. The tags must be put in a list of strings.'''
        # Check all the notes inside the notes list. If the tags of the notes don't match, add them to the new notes list. In the end swap the self._Notes list with the new list made.
        new_notes_list = list()
        for note in self._Notes:
            if note.getTags() != delete_tags:
                new_notes_list.append(note)

        self._Notes = new_notes_list

    def searchBy_Name(self, note_name):
        '''Return the note that has the given name. If the note with the given name hasn't been found, a ValueError will be returned'''
        for note in self._Notes:
            if note.name == note_name:
                return note

        raise ValueError("The note with the name {0} has not been found. Make sure you give the correct name.".format(note_name))

    def searchBy_Tags(self, note_tags):
        '''Return a list of all the notes that perfectly match all the given tags. The tags must be put in a list of strings.'''
        return_notes = list()

        for note in self._Notes:
            if note.getTags() == note_tags:
                return_notes.append(note)

        return return_notes

if __name__ == "__main__":
    notebook = Notebook()

    global_tags_list = list()
    for i in range(1, 11): global_tags_list.append("tag{0}".format(i))

    Note1 = Note("FirstNote")
    Note1.addToMemo("The memo of my first note.")
    Note1.extendTags(global_tags_list)

    Note2 = Note("SecondNote")
    Note2.addToMemo("The memo of my second note.")
    Note2.extendTags(global_tags_list)

    Note3 = Note("ThirdNote")
    Note3.addToMemo("The memo of my third note.")
    Note3.extendTags(global_tags_list[0:5])

    notebook.addNote(Note1)
    notebook.addNote(Note2)
    notebook.addNote(Note3)

    note_found = notebook.searchBy_Name("ThirdNote")
    # print(note_found.name)
    # print(note_found.getTags())
    # print(note_found.readMemo())

    notes_found_tags = notebook.searchBy_Tags(global_tags_list[0:5])
    """
    for note in notes_found_tags:
        print(note.name)
        print(note.getTags())
        print(note.readMemo())
    """

    # notebook.deleteNote_byName("ThirdNote")
    # print(notebook.searchBy_Name("ThirdNote"))

    # notebook.deleteNotes_byTags(global_tags_list[0:5])
    # print(notebook.searchBy_Tags(global_tags_list[0:5]))