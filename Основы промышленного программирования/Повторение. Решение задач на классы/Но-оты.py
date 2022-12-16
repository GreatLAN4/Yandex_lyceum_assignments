class Note:
    notes = {"до": "до-о", "ре": "ре-э", "ми": "ми-и",
             "фа": "фа-а", "соль": "со-оль", "ля": "ля-а",
             "си": "си-и"}

    def __init__(self, note, length=False):

        self.length = length

        if self.length:
            self.note = Note.notes[note]
        else:
            self.note = note

    def __str__(self):
        return self.note
