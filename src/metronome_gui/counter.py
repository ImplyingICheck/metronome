"""Display, which increments and decrements a value."""
import tkinter as tk

from metronome_core import metronome_interface

BPM_MIN = 1
BPM_MAX = 200


class CounterWidget:
  """Tracks a value "count" and allows user input to decrease and increase the
  value."""

  def __init__(
      self,
      master: tk.Tk,
      count: int = 0,
      increment_text: str = "Increment",
      decrement_text: str = "Decrement",
  ):
    self.master = master
    self._count = count

    self.count_label = tk.Label(master, text=str(self.count))
    self.count_label.pack()

    self.increment_button = tk.Button(
        master, text=increment_text, command=self.increment
    )
    self.increment_button.pack()

    self.decrement_button = tk.Button(
        master, text=decrement_text, command=self.decrement
    )
    self.decrement_button.pack()

  @property
  def count(self):
    return self._count

  def update_label(self):
    self.count_label.config(text=str(self.count))

  def update_count(self, delta: int, absolute: bool = False):
    """This function should always be called using super() as update_count()
    handles updating the view after updating the count property."""
    if absolute:
      self._count = delta
    else:
      self._count += delta
    self.update_label()

  def increment(self):
    self.update_count(1)

  def decrement(self):
    self.update_count(-1)


class BPMWidget(CounterWidget):
  """Adds callbacks to the metronome model."""

  def __init__(
      self,
      master: tk.Tk,
      count: int = 1,
      increment_text: str = "Increment",
      decrement_text: str = "Decrement",
  ):
    super().__init__(master, count, increment_text, decrement_text)
    self.slider = tk.Scale(
        master,
        from_=BPM_MIN,
        to=BPM_MAX,
        orient="horizontal",
        command=self.on_slider_change,
        showvalue=False,
    )
    self.slider.pack()

  def update_count(self, delta: int, absolute: bool = False):
    super().update_count(delta=delta, absolute=absolute)
    self.slider.set(self.count)

  def on_slider_change(self, value: str):
    self.update_count(int(value), absolute=True)

  def increment(self):
    super().increment()
    metronome_interface.update_bpm(self.count)

  def decrement(self):
    if self.count > 1:
      self.update_count(-1)
    else:
      self.update_count(1, absolute=True)
      return
    metronome_interface.update_bpm(self.count)
