"""The top level logic of the metronome app."""
import tkinter
from metronome_gui import counter

if __name__ == "__main__":
  metronome = tkinter.Tk()
  counter_widget = counter.BPMWidget(metronome)
  metronome.mainloop()
