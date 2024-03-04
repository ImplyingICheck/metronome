# pylint: disable=[missing-module-docstring, missing-class-docstring, protected-access, redefined-outer-name]

from metronome_gui import play_button


def test_state_pause_value_is_1():
  assert play_button.State.PAUSE.value == 1


def test_state_play_value_is_2():
  assert play_button.State.PLAY.value == 2
