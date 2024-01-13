class NoteManager:
    def __init__(self):
        self.notes = {}

    def add_note(self, id, text, tags):
        self.notes[id] = {'text': text, 'tags': tags}

    def find_note_by_tag(self, tag):
        return [note for id, note in self.notes.items() if tag in note['tags']]
