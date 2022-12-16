PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    long = {"до": "до-о", "ре": "ре-э", "ми": "ми-и",
            "фа": "фа-а", "соль": "со-оль", "ля": "ля-а",
            "си": "си-и"}

    def __init__(self, note, is_long=False):
        self.is_long = is_long
        self.note = note

    def __str__(self):
        return self.note if not self.is_long else Note.long[self.note]


class LoudNote(Note):
    def __str__(self):
        return super().__str__().upper()


class DefaultNote(Note):
    def __init__(self, pitch=PITCHES[0], is_long=False):
        super().__init__(pitch, is_long)


class NoteWithOctave(Note):
    def __init__(self, pitch, octave, is_long=False):
        self.octave = octave
        super().__init__(pitch, is_long)

    def __str__(self):
        return "{} ({})".format(super().__str__(), self.octave)
