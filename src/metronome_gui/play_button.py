"""Widget displaying status of playback."""
import tkinter as tk
from enum import Enum
from metronome_core import metronome_interface

_PAUSE_TEXT = "Paused"
_PLAY_TEXT = "Playing"


class PlaybackState(Enum):
  PAUSE = 1
  PLAY = 2


class PlayButton:
  """View for displaying playback status of the metronome."""

  def __init__(self, master: tk.Tk):
    self._state = PlaybackState.PAUSE
    self.button = tk.Button(master, text=_PAUSE_TEXT, command=self.toggle_state)
    self.button.pack()

  @property
  def state(self) -> PlaybackState:
    return self._state

  def toggle_state(self):
    if self.state == PlaybackState.PAUSE:
      self._state = PlaybackState.PLAY
      self.button.config(text=_PLAY_TEXT)
    elif self.state == PlaybackState.PLAY:
      self._state = PlaybackState.PAUSE
      self.button.config(text=_PAUSE_TEXT)
    metronome_interface.update_playback_status(self.state)
