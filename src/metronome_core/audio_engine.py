"""Interface with sounddevice package. Creates a persistent output buffer to
which data representing sound can be written."""
from types import TracebackType

import numpy as np
import sounddevice


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

  def _generate_sine_wave(self, frequency: float, duration: float):
    time_array = np.linspace(
        0, duration, int(self.sample_rate * duration), dtype="float32"
    )
    wave = np.sin(2 * np.pi * frequency * time_array)
    return wave

  def _generate_silence(self, duration: float):
    return np.linspace(0, 0, int(self.sample_rate * duration), dtype="float32")

  def play_sound(
      self, frequency: float, duration: float = 1, volume: float = 0.1
  ):
    waveform = self._generate_sine_wave(frequency, duration)
    scaled_waveform = volume * waveform
    try:
      self.output_stream.write(scaled_waveform)
    except sounddevice.PortAudioError as e:
      if e.args[1] == -9983:
        raise AttributeError(
            f"{self.__class__} output_stream was not initialized. Use a"
            f" context manager or the start() and close() methods."
        ) from None
      else:
        raise e from None
