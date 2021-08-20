from NoteDates import NoteDates
import time

class Note:
    '''
    The note class.
    '''

    def __init__(self, name):
        '''
            Each note has a unique name that can't be repeated inside the notebook.
            It has a private memo. The memo is private since it should only be edited by using the addToMemo and rewriteMemo methods.
            The dates property is a NoteDates object which contains the date when it was created and the last date modified
            It also contains a list with tags so that we can find notes faster by filtering them by tags inside the notebook.
            The tags are not allowed to repeat themselves and they should also be private and can only be accessed through methods.
        '''
        if type(name) != str:
            raise ValueError("The name of the note must be a string. Argument given : {0}".format(name))

        self.name = name
        self._memo = ""
        self._dates = NoteDates()
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

        # Change the lastDateModified of the memo
        self._dates.lastDateModified = time.time()

    def rewriteMemo(self, new_memo):
        '''Rewrites the entire memo with the new_memo given '''
        if type(new_memo) != str:
            raise ValueError("The new memo must be a string. Argument given: {0}".format(new_memo))

        self._memo = ""
        self.addToMemo(new_memo)

        # Change the lastDateModified of the memo
        self._dates.lastDateModified = time.time()

    def readMemo(self):
        '''Returns the memo of the note'''
        return self._memo

    def extendTags(self, tags_to_add):
        '''Extends the tags list with the tags_to_add list'''
        self.checkTagsList(tags_to_add)
        self._tags.extend(tags_to_add)

    def deleteTags(self, tags_to_delete):
        '''Delete all tags from the tags list that are inside the tags_to_delete list'''
        self.checkTagsList(tags_to_delete)
        for tag_to_delete in tags_to_delete:
            try:
                self._tags.remove(tag_to_delete)
            except ValueError:
                raise ValueError("We couldn't find the following tag : {0}".format(tag_to_delete))

    def rewriteTags(self, new_tags):
        '''Replace the current tags with the new given new_tags list'''
        self.checkTagsList(new_tags)
        self._tags = new_tags

    def getTags(self):
        '''Get the tags of the note'''
        return self._tags

    def getDates(self):
        '''Get the NoteDates object of the Note object that contains the date when it was created and the last date modified'''
        return self._dates

    def checkTagsList(self, tags_list):
        # Check the list itself
        if type(tags_list) != list:
            raise ValueError("The tags list must be a list. The argument given : {0}".format(tags_list))

        # Check every value in the list
        for tag in tags_list:
            if type(tag) != str:
                raise ValueError(
                    "All tags must be strings. We found {0} inside the tags list which is not a string.".format(tag))


# Testing the note object
if __name__ == "__main__":
    from NoteDates import NoteDates
    import time

    note = Note(
        "myNewNote",  # NOTE NAME
    )

    # print(note.readMemo())
    note.addToMemo("This is my memo")
    note.addToMemo("This is my new memo")
    # print(note.readMemo())
    note.rewriteMemo("I rewrote everything")
    # print(note.readMemo())

    extendTagList = list()
    for i in range(1, 6):
        extendTagList.append("tag{0}".format(i))

    note.extendTags(extendTagList)
    # print(note.getTags())
    note.deleteTags(["tag2", "tag3"])
    # print(note.getTags())
    note.rewriteTags(["tag88", "tag89"])
    # print(note.getTags())