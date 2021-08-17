class NoteDates:
    '''
        A class that stores the dates of a note. It contains the date when the date has been created and the date when it was last modified
    '''
    def __init__(self, dateCreated, lastDateModified=None):
        '''
            The date is the UTC time in seconds ( e.g. time.time() )
            The last date modified defaults to none since the note hasn't been 'modified' at the start
        '''
        self.dateCreated = dateCreated
        self.lastDateModified = lastDateModified