"""Display, which increments and decrements a value."""
import tkinter as tk


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
    self.count = count

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

  def increment(self):
    self.count += 1
    self.count_label.config(text=str(self.count))

  def decrement(self):
    self.count -= 1
    self.count_label.config(text=str(self.count))
