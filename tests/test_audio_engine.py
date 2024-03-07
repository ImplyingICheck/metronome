# pylint: disable=[missing-module-docstring, missing-class-docstring, protected-access, redefined-outer-name]

from numpy.typing import ArrayLike

import pytest
import numpy as np
from metronome_core import audio_engine


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
