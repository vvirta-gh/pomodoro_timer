from datetime import datetime, timedelta


class PomodoroTimer:
    def __init__(self, work_duration=25, break_duration=5):
        self.work_duration = timedelta(minutes=work_duration)
        self.break_duration = timedelta(minutes=break_duration)
        self.start_time = None
        self.end_time = None
        self.is_running = False

    def start(self):
        if self.is_running:
            raise RuntimeError("Timer is already running!")
        self.start_time = datetime.now()
        self.end_time = self.start_time + self.work_duration
        self.is_running = True
        print(f"Pomodoro started! Ends at {self.end_time.strftime('%H:%M:%S')}")

    def check_status(self):
        if not self.is_running:
            return "Timer is not running."
        if datetime.now() >= self.end_time:
            self.is_running = False
            return "Pomodoro finished!"
        remaining = (self.end_time - datetime.now()).total_seconds()
        return f"Still running... {int(remaining)} seconds left."

    def reset(self):
        self.start_time = None
        self.end_time = None
        self.is_running = False
        print("Timer has been reset.")


if __name__ == "__main__":
    pass
