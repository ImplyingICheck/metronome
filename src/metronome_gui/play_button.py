"""Widget displaying status of playback."""
import tkinter as tk
from enum import Enum


class State(Enum):
  PAUSE = 1
  PLAY = 2


class PlayButton:
  """View for displaying playback status of the metronome."""

  def __init__(self, master: tk.Tk):
    self._state = State.PAUSE
    self.button = tk.Button(master, command=self.toggle_state)
    self.button.pack()

  @property
  def state(self) -> State:
    return self._state

  def toggle_state(self):
    if self._state == State.PAUSE:
      self._state = State.PLAY
      self.button.config(text="PLAY")
    elif self._state == State.PLAY:
      self._state = State.PAUSE
      self.button.config(text="PAUSE")
