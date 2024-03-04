"""Widget displaying status of playback."""
from enum import Enum


class State(Enum):
  PAUSE = 1
  PLAY = 2
