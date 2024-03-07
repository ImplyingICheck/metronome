"""Interface with sounddevice package. Creates a persistent output buffer to
which data representing sound can be written."""
from __future__ import annotations
import numpy as np
import sounddevice
import dataclasses

from collections.abc import Iterable
from types import TracebackType
from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
  Waveform: TypeAlias = np.ndarray[tuple[int], np.dtype[np.float32]]


@dataclasses.dataclass
class Wave:
  frequency: int
  duration: float


class AudioEngine:
  """Can be used in a context manager or using the start() close() methods."""

  def __init__(self, sample_rate: int | None = None, channels: int = 1):
    if not sample_rate:
      sample_rate = sounddevice.query_devices(kind="output")[
          "default_samplerate"
      ]
    self._sample_rate = sample_rate
    self._channels = channels
    self.output_stream = sounddevice.OutputStream(
        sample_rate, channels=channels
    )

  @property
  def sample_rate(self) -> int:
    return self._sample_rate

  @property
  def channels(self) -> int:
    return self._channels

  def __enter__(self):
    self.start()
    return self

  def __exit__(
      self,
      exc_type: BaseException,
      exc_val: BaseException,
      exc_tb: TracebackType,
  ) -> None | bool:
    self.close()
    return True

  def start(self):
    self.output_stream.start()

  def close(self, ignore_errors: bool = True):
    self.output_stream.close(ignore_errors)

  def _generate_sine_wave(self, frequency: float, duration: float) -> Waveform:
    time_array = np.linspace(
        0, duration, int(self.sample_rate * duration), dtype="float32"
    )
    wave = np.sin(2 * np.pi * frequency * time_array)
    return wave

  def _generate_silence(self, duration: float) -> Waveform:
    return np.linspace(0, 0, int(self.sample_rate * duration), dtype="float32")

  def create_rhythm_waveform(self, rhythm: Iterable[Wave]) -> Waveform:
    waveforms: list[Waveform] = []
    for index, note in enumerate(rhythm):
      if index % 2 == 0:
        waveform = self._generate_sine_wave(note.frequency, note.duration)
      else:
        waveform = self._generate_silence(note.duration)
      waveforms.append(waveform)
    axis = 0 if self.channels == 1 else 1
    return np.concatenate(waveforms, axis=axis)

  def play_sound(self, rhythm: Iterable[Wave], volume: float = 0.1) -> None:
    waveform = self.create_rhythm_waveform(rhythm)
    scaled_waveform = volume * waveform
    sounddevice.play(scaled_waveform, self.sample_rate, loop=True)
