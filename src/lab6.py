from src.simple_timer.display import display_countdown
from src.simple_timer.timer import start_timer

def main():
    try:
        time_left = float(input("Введіть час для таймеру"))
        if time_left <= 0:
            raise ValueError("Час таймеру не може бути меншим за або дорівнювати 0")
        print(f"Таймер закінчив свою роботу: {start_timer(time_left, display_countdown)}")
    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()