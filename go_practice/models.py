from django.db import models


class Exercise(models.Model):
    TYPES = (
        ("scale", "Scale"),
        ("arpeggio", "Arpeggio"),
        ("chord", "Chord"),
    )
    NOTES = (
        ("C", "C"),
        ("C", "C#"),
        ("D", "D"),
        ("D#", "D#"),
        ("E", "E"),
        ("F", "F"),
        ("F#", "F#"),
        ("G", "G"),
        ("G#", "G#"),
        ("A", "A"),
        ("A#", "A#"),
        ("B", "B"),
    )

    QUALITIES = (
        ("major", "Major Triad"),
        ("minor", "Minor Triad"),
        ("diminished_triad", "Diminished Triad"),
        ("major7", "Major 7th"),
        ("dominant", "Dominant 7th"),
        ("minor7", "Minor 7th"),
        ("half-diminished", "Half-diminished 7th"),
        ("diminished7", "Diminished 7th"),
    )

    type = models.CharField(max_length=25, choices=TYPES)
    note = models.CharField(max_length=2, choices=NOTES)
    quality = models.CharField(max_length=25, choices=QUALITIES)

    class Meta:
        unique_together = ("type", "note", "quality")

    def __str__(self):
        return f"{self.type} - {self.note} - {self.quality}"
