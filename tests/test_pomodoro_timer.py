import pytest
from src.pomodoro_timer import PomodoroTimer
from datetime import timedelta


def test_pomodoro_timer_start_correctly():
    timer = PomodoroTimer(work_duration=25, break_duration=5)
    assert timer.is_running is False
    timer.start()
    assert timer.is_running is True
    assert timer.end_time > timer.start_time
