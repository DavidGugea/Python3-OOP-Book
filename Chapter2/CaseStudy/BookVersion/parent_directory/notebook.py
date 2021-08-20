import datetime

# Store the next available id for all new notes
last_id = 0

class Note:
    '''Represent a note in hte notebook. Match against a string in searches and store tags for each note.'''

    def __init__(self, memo, tags=''):
        '''initialize a note with memo and optional space-separated tags. Automatically set the note's creating date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        global last_id
        last_id += 1
        self.id = last_id

    def match(self, givenFilter):
        '''
            Determine if this note matches the filter text. Return Ture if it matches, flase otherwise

            Search is case sensitive and matches both text and tags.
        '''

        return givenFilter in self.memo or givenFilter in self.tags

class Notebook:
    '''Represent a collection of notes that can be tagged, modified, and searched.'''

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = list()
    
    def new_note(self, memo, tags=''):
        '''Create a new note and addd it to the list.'''
        self.notes.append(Note(memo, tags))
    
    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note

        return None

    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and cahnge its memo to the given value.'''
        note = self._find_note(note_di)
        if note:
            note.memo = memo
            return True

        return False

    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its tags to the given value.'''
        self._find_note(note_id).tags = tags
        
    def search(self, filter):
        '''Find all notes that match the given filter string.'''
        return [note for note in self.notes if note.match(filter)]