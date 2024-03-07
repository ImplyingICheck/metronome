# pylint: disable=[missing-module-docstring, missing-class-docstring, protected-access, redefined-outer-name]
import itertools
import math

from numpy.typing import ArrayLike

import pytest
import numpy as np
from metronome_core import audio_engine

SECONDS_PER_MINUTE = 60


@pytest.fixture
def engine_44100_1_channel():
  sample_rate = 44100
  channels = 1
  return (
      audio_engine.AudioEngine(sample_rate=44100, channels=1),
      sample_rate,
      channels,
  )


@pytest.fixture
def engine_44100_2_channel():
  return audio_engine.AudioEngine(sample_rate=44100, channels=2)


@pytest.fixture
def frequency_440():
  return 440


@pytest.fixture
def rhythm_quarter_note_common_time_60_bpm(frequency_440):
  """A quarter note is 1 second long at 60 bpm."""
  bpm = 60
  bottom_number = 4
  sample_length = round(
      bpm * bottom_number / SECONDS_PER_MINUTE
  )  # Resolves to 4
  beat = [
      audio_engine.Wave(frequency_440, 0.25),
      audio_engine.Wave(frequency_440, 0.75),
  ]
  measure = itertools.islice(itertools.cycle(beat), len(beat) * bottom_number)
  return list(measure), sample_length


def test_generate_sine_wave_time_length_one_second(
    engine_44100_1_channel, frequency_440
):
  engine, sample_rate, _ = engine_44100_1_channel  # channels unused
  duration = 1
  output = engine._generate_sine_wave(frequency_440, duration=duration)
  expected_length = sample_rate * duration
  assert len(output) == expected_length


def extract_peak_frequency(waveform: ArrayLike) -> int:
  fourier_transform = np.fft.fft(waveform)
  magnitudes = np.abs(fourier_transform)
  peak_frequency = np.argmax(magnitudes)
  return int(peak_frequency)


def test_generate_sine_wave_frequency_matches(
    engine_44100_1_channel, frequency_440
):
  engine, _, _ = engine_44100_1_channel  # sample_rate, channels unused
  duration = 1
  output = engine._generate_sine_wave(frequency_440, duration=duration)
  peak_frequency = extract_peak_frequency(output)
  expected_frequency = frequency_440
  assert peak_frequency == expected_frequency


def test_generate_silence_length_one_second(engine_44100_1_channel):
  (
      engine,
      sample_rate,
      _,
  ) = engine_44100_1_channel  # sample_rate, channels unused
  duration = 1
  output = engine._generate_silence(duration=duration)
  expected_length = sample_rate * duration
  assert len(output) == expected_length


def test_generate_silence_frequency_zero(engine_44100_1_channel):
  engine, _, _ = engine_44100_1_channel  # sample_rate, channels unused
  duration = 1
  output = engine._generate_silence(duration=duration)
  assert all(frequency == 0 for frequency in output)


def test_create_rhythm_sound_length_4_seconds(
    engine_44100_1_channel, rhythm_quarter_note_common_time_60_bpm
):
  engine, sample_rate, _ = engine_44100_1_channel
  rhythm, expected_length = rhythm_quarter_note_common_time_60_bpm
  waveform = engine.create_rhythm_waveform(rhythm=rhythm)
  actual_length = len(waveform) / sample_rate
  assert math.isclose(actual_length, expected_length)
