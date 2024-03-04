"""The top level logic of the metronome app."""
import tkinter
from metronome_gui import counter
from metronome_gui import play_button


if __name__ == "__main__":
  metronome = tkinter.Tk()
  counter_widget = counter.BPMWidget(metronome)
  play_button_widget = play_button.PlayButton(metronome)
  metronome.mainloop()
