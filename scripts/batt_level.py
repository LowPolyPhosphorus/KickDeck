"""
KickDeck - Battery Level / Low Battery LED
"""
import time

I2C_BUS = 1
UPS_I2C_ADDRESS = 0x36
BATTERY_PERCENT_REGISTER = 0x04
GPIO_PIN = 12
GPIO_SYSFS_PATH = f"/sys/class/gpio/gpio{GPIO_PIN}"
LOW_BATTERY_THRESHOLD = 20
POLL_INTERVAL_SEC = 10


def read_battery_percent():
    try:
        from smbus2 import SMBus
        with SMBus(I2C_BUS) as bus:
            return bus.read_byte_data(UPS_I2C_ADDRESS, BATTERY_PERCENT_REGISTER)
    except Exception as e:
        print(f"[stub] I2C read failed: {e}")
        return None


def set_led(on: bool):
    value_path = f"{GPIO_SYSFS_PATH}/value"
    try:
        with open(value_path, "w") as f:
            f.write("1" if on else "0")
    except FileNotFoundError:
        print(f"[stub] GPIO path not found: {value_path}")


def main():
    while True:
        percent = read_battery_percent()
        if percent is None:
            print("[stub] no battery reading available")
        else:
            print(f"[stub] Battery: {percent}%")
            set_led(percent <= LOW_BATTERY_THRESHOLD)
        time.sleep(POLL_INTERVAL_SEC)


if __name__ == "__main__":
    main()
