"""
KickDeck - Rotary Encoder (EC11) -> Volume Control
"""
import subprocess
import time

CLK_PIN = 14
DT_PIN = 3
SW_PIN = 5
GPIO_SYSFS_BASE = "/sys/class/gpio"
POLL_INTERVAL_SEC = 0.005
DEBOUNCE_SEC = 0.05
VOLUME_STEP_PERCENT = 5


def read_gpio(pin):
    value_path = f"{GPIO_SYSFS_BASE}/gpio{pin}/value"
    try:
        with open(value_path) as f:
            return int(f.read().strip())
    except FileNotFoundError:
        print(f"[stub] GPIO path not found: {value_path}")
        return None


def volume_up():
    subprocess.run(["amixer", "set", "Master", f"{VOLUME_STEP_PERCENT}%+"], check=False)


def volume_down():
    subprocess.run(["amixer", "set", "Master", f"{VOLUME_STEP_PERCENT}%-"], check=False)


def toggle_mute():
    subprocess.run(["amixer", "set", "Master", "toggle"], check=False)


def main():
    last_clk = read_gpio(CLK_PIN)
    last_sw = read_gpio(SW_PIN)

    while True:
        time.sleep(POLL_INTERVAL_SEC)
        clk = read_gpio(CLK_PIN)
        dt = read_gpio(DT_PIN)
        sw = read_gpio(SW_PIN)

        if clk is None or dt is None or sw is None:
            time.sleep(1)
            continue

        if clk != last_clk:
            time.sleep(DEBOUNCE_SEC)
            if dt != clk:
                volume_up()
            else:
                volume_down()
            last_clk = clk

        if sw == 0 and last_sw == 1:
            toggle_mute()
        last_sw = sw


if __name__ == "__main__":
    main()
