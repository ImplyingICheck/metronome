"""Handles requests from the front end."""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from metronome_gui import play_button


def update_bpm(bpm: int):
  raise NotImplementedError


def update_playback_status(state: play_button.PlaybackState):
  raise NotImplementedError
