"""Internal time keeping mechanism of the metronome. All time signatures are
compared to common time and scaled appropriately."""
import math

COMMON_TIME = 4


def calculate_time_scale(bottom_number: int) -> float | int:
  scale = math.log(bottom_number, COMMON_TIME)
  return 1 / 4 if scale == 0 else scale
