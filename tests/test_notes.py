# pylint: disable=[missing-module-docstring, missing-class-docstring, protected-access, redefined-outer-name]

import pytest

from metronome_core import notes
from metronome_core import audio_engine


@pytest.fixture
def bpm_60():
  return 60


@pytest.fixture
def quarter_note_measure():
  return [notes.QuarterNote()] * 4


@pytest.fixture
def common_time():
  return (4, 4)


@pytest.fixture
def quarter_note_60_bpm_note_sequence(
    bpm_60, quarter_note_measure, common_time
):
  return notes.NoteSequence(bpm_60, quarter_note_measure, common_time)


def test_to_waves_common_time_quarter_notes(quarter_note_60_bpm_note_sequence):
  expected = [audio_engine.Wave(440, 0.25), audio_engine.Wave(0, 0.75)] * 4
  note_sequence = quarter_note_60_bpm_note_sequence
  actual = note_sequence.to_waves()
  assert actual == expected
