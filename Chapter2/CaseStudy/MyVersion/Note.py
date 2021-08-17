class Note:
    '''
    The note class.
    '''
    def __init__(self, name, dates):
        '''
            Each note has a unique name that can't be repeated inside the notebook.
            It has a private memo. The memo is private since it should only be edited by using the addToMemo and rewriteMemo methods.
            The dates property is a NoteDates object which contains the date when it was created and the last date modified
            It also contains a list with tags so that we can find notes faster by filtering them by tags inside the notebook.
            The tags are not allowed to repeat themselves and they should also be private and can only be accessed through methods.
        '''
        self.name = name
        self._memo = ""
        self.dates = dates
        self._tags = list()

    def addToMemo(self, memo_add_string):
        '''
            Adds a new string to the memo. It adds the string plus a period if not found at the end, and a newline at the start of the memo
            I added a new line at the start of the memo and not at the end because I don't want to waste a new line for the last note.
            If the last note will have a >\n< at the end then it will create a new line that I don't need.
            I'll only add a new line for new memos
        '''
        if type(memo_add_string) != str:
            raise ValueError("The given argument must be a ")

        if self._memo == "":
            if memo_add_string.endswith("."):
                self._memo += memo_add_string
            else:
                self._memo += "{0}.".format(memo_add_string)
        elif memo_add_string.endswith("."):
            self._memo += "\n{0}".format(memo_add_string)
        else:
            self._memo += "\n{0}.".format(memo_add_string)

    def rewriteMemo(self, new_memo):
        '''Rewrites the entire memo with the new_memo given '''
        if type(new_memo) != str:
            raise ValueError("The new memo must be a string. Argument given: {0}".format(new_memo))

        self._memo = ""
        self.addToMemo(new_memo)

    def readMemo(self):
        '''Returns the memo of the note'''
        return self._memo

    def extendTags(self, tags_to_add):
        '''Extends the tags list with the tags_to_add list'''
        if type(tags_to_add) != list:
            raise ValueError("The argument tags_to_add must be a list. Argument given : {0}".format(tags_to_add))

        self._tags.extend(tags_to_add)

    def deleteTags(self, tags_to_delete):
        '''Delete all tags from the tags list that are inside the tags_to_delete list'''
        for tag_to_delete in tags_to_delete:
            try:
                self._tags.remove(tag_to_delete)
            except ValueError:
                raise ValueError("We couldn't find the following tag : {0}".format(tag_to_delete))

    def rewriteTags(self, new_tags):
        '''Replace the current tags with the new given new_tags list'''
        if type(new_tags) != list:
            raise ValueError("The tags must be a list. Argument given : {0}".format(new_tags))

        self._tags = new_tags

    def getTags(self):
        '''Get the tags of the note'''
        return self._tags

    def changeName(self, newName):
        '''Change the name of the note'''
        if type(newName) != str:
            raise ValueError("The new name of the note must be a string. Argument given : {0}".format(newName))

        self.name = newName


# Testing the note object
if __name__ == "__main__":
    from NoteDates import NoteDates
    import time

    note_dates = NoteDates(time.time(), None)
    note = Note(
        "myNewNote", # NOTE NAME
        note_dates, # NOTE DATES
    )

    # print(note.readMemo())
    note.addToMemo("This is my memo")
    note.addToMemo("This is my new memo")
    # print(note.readMemo())
    note.rewriteMemo("I rewrote everything")
    # print(note.readMemo())

    note.extendTags(["tag1", "tag2", "tag3", "tag4", "tag5"])
    print(note.getTags())
    note.deleteTags(["tag2", "tag3"])