"""Note helper class. Provides note classes with values and NoteSequence, a
class to organize note groups."""
from typing import TypeAlias
from collections.abc import Iterable

from metronome_core import audio_engine

TimeSignature: TypeAlias = tuple[int, int]
NoteValue: TypeAlias = float | int

SECONDS_PER_MINUTE = 60
CONCERT_PITCH = 440
SILENCE_PITCH = 0
BEAT_DIVISOR = 1 / 4
BEAT_DIVISOR_COMPLIMENT = 1 - BEAT_DIVISOR


class Note:

  def __init__(self, value: NoteValue):
    self.value = value


class WholeNote(Note):

  def __init__(self):
    super().__init__(4)


class QuarterNote(Note):

  def __init__(self):
    super().__init__(1)


class NoteSequence:
  """A fully defined series of sounds from which a metronome sound file can
  be generated for the audio_engine.AudioEngine."""

  def __init__(
      self, tempo: int, notes: Iterable[Note], time_signature: TimeSignature
  ):
    self.tempo = tempo
    self.notes = notes
    self.time_signature = time_signature

  def to_waves(self) -> list[audio_engine.Wave]:
    waves: list[audio_engine.Wave] = []
    second_per_value = SECONDS_PER_MINUTE / self.tempo
    for note in self.notes:
      total_duration = note.value * second_per_value
      accent = audio_engine.Wave(CONCERT_PITCH, total_duration * BEAT_DIVISOR)
      waves.append(accent)
      silence = audio_engine.Wave(
          SILENCE_PITCH, total_duration * BEAT_DIVISOR_COMPLIMENT
      )
      waves.append(silence)
    return waves
