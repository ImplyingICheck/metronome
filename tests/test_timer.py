# pylint: disable=[missing-module-docstring, missing-class-docstring, protected-access, redefined-outer-name]

import pytest

from metronome import timer
from metronome import notes


@pytest.fixture
def time_signature_4_4():
  return (4, 4)


@pytest.fixture
def time_signature_4_2():
  return (4, 2)


@pytest.fixture
def time_signature_4_1():
  return (4, 1)


@pytest.fixture
def bpm_100():
  return 100


@pytest.fixture
def note_sequence_4_4_whole(bpm_100, time_signature_4_4):
  return (
      notes.NoteSequence(bpm_100, [notes.WholeNote()], time_signature_4_4),
      bpm_100,
  )


@pytest.fixture
def note_sequence_4_4_quarters(bpm_100, time_signature_4_4):
  return (
      notes.NoteSequence(
          bpm_100,
          [
              notes.QuarterNote(),
              notes.QuarterNote(),
              notes.QuarterNote(),
              notes.QuarterNote(),
          ],
          time_signature_4_4,
      ),
      bpm_100,
  )


def test_calculate_time_scale_4_4(time_signature_4_4):
  scale = timer._calculate_time_scale(time_signature_4_4[1])
  assert scale == 1


def test_calculate_time_scale_4_2(time_signature_4_2):
  scale = timer._calculate_time_scale(time_signature_4_2[1])
  assert scale == 1 / 2


def test_calculate_time_scale_4_1(time_signature_4_1):
  scale = timer._calculate_time_scale(time_signature_4_1[1])
  assert scale == 1 / 4


def test_time_subdivision_whole_note(note_sequence_4_4_whole):
  note_sequence, bpm = note_sequence_4_4_whole
  actual = timer.time_subdivision(note_sequence)
  beats_in_a_whole_note = 4
  expected = [(1 / bpm) * beats_in_a_whole_note]
  assert actual == expected


def test_time_subdivision_quarter_notes(note_sequence_4_4_quarters):
  note_sequence, bpm = note_sequence_4_4_quarters
  actual = timer.time_subdivision(note_sequence)
  beats_in_a_quarter_note = 1
  number_quarter_notes = 4
  expected = [
      (1 / bpm) * beats_in_a_quarter_note for _ in range(number_quarter_notes)
  ]
  assert actual == expected
