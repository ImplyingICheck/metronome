# pylint: disable=[missing-module-docstring, missing-class-docstring, protected-access, redefined-outer-name]

import pytest

from metronome import timer


@pytest.fixture
def time_signature_4_4():
  return (4, 4)


@pytest.fixture
def time_signature_4_2():
  return (4, 2)


@pytest.fixture
def time_signature_4_1():
  return (4, 1)


def test_calculate_time_scale_4_4(time_signature_4_4):
  scale = timer.calculate_time_scale(time_signature_4_4[1])
  assert scale == 1


def test_calculate_time_scale_4_2(time_signature_4_2):
  scale = timer.calculate_time_scale(time_signature_4_2[1])
  assert scale == 1 / 2


def test_calculate_time_scale_4_1(time_signature_4_1):
  scale = timer.calculate_time_scale(time_signature_4_1[1])
  assert scale == 1 / 4
