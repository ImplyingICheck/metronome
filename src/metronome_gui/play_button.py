"""Widget displaying status of playback."""
import tkinter as tk
from enum import Enum


class State(Enum):
  PAUSE = 1
  PLAY = 2


class PlayButton:

  def __init__(self, master: tk.Tk):
    self._state = State.PAUSE
    self.button = tk.Button(master)
