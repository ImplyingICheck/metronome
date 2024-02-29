"""Internal time keeping mechanism of the metronome. All time signatures are
compared to common time and scaled appropriately."""
import math

from metronome_core import notes

COMMON_TIME = 4


def _calculate_time_scale(bottom_number: int) -> float | int:
  scale = math.log(bottom_number, COMMON_TIME)
  return 1 / 4 if scale == 0 else scale


def time_subdivision(note_sequence: notes.NoteSequence):
  seconds_per_beat = 1 / note_sequence.tempo
  time_scale = _calculate_time_scale(note_sequence.time_signature[1])
  return [
      seconds_per_beat * time_scale * note.value for note in note_sequence.notes
  ]
