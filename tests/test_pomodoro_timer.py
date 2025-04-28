import pytest
from src.pomodoro_timer import PomodoroTimer
from datetime import timedelta


def test_pomodoro_timer_start_correctly():
    timer = PomodoroTimer(work_duration=25, break_duration=5)
    assert timer.is_running is False
    timer.start()
    assert timer.is_running is True
    assert timer.end_time > timer.start_time


def test_pomodoro_timer_reset():
    timer = PomodoroTimer()
    timer.start()
    timer.reset()
    assert timer.start_time is None
    assert timer.end_time is None
    assert timer.is_running is False


def test_pomodoro_timer_check_status_not_running():
    timer = PomodoroTimer()
    status = timer.check_status()
    assert status == "Timer is not running."


def test_pomodoro_timer_check_status_running():
    timer = PomodoroTimer(work_duration=0.1)  # Short duration for testing
    timer.start()
    assert timer.is_running is True
    status = timer.check_status()
    assert "Still running..." in status


def test_pomodoro_timer_check_status_finished(monkeypatch):
    timer = PomodoroTimer(work_duration=0)
    timer.start()

    class FakeDatetime:
        @classmethod
        def now(cls):
            return timer.end_time + timedelta(seconds=1)

    monkeypatch.setattr("src.pomodoro_timer.datetime", FakeDatetime)

    assert timer.check_status() == "Pomodoro finished!"
