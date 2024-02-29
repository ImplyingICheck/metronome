"""Note helper class. Provides note classes with values and NoteSequence, a
class to organize note groups."""
import decimal
from typing import TypeAlias
from collections.abc import Iterable


TimeSignature: TypeAlias = tuple[int, int]
NoteValue: TypeAlias = decimal.Decimal


class Note:

  def __init__(self, value: NoteValue):
    self.value = value


class WholeNote(Note):

  def __init__(self):
    super().__init__(decimal.Decimal(4))


class QuarterNote(Note):

  def __init__(self):
    super().__init__(decimal.Decimal(1))


class NoteSequence:

  def __init__(
      self, tempo: int, notes: Iterable[Note], time_signature: TimeSignature
  ):
    self.tempo = tempo
    self.notes = notes
    self.time_signature = time_signature
