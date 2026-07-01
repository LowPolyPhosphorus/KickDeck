"""
KickDeck - HDD Activity LED (PWM, dimmed)
"""
import time

DISK_DEVICE = "mmcblk0"
DISKSTATS_PATH = "/proc/diskstats"
PWM_CHIP = "pwmchip0"
PWM_CHANNEL = "0"
PWM_EXPORT_PATH = f"/sys/class/pwm/{PWM_CHIP}"
DIM_DUTY_NS = 20000
ACTIVE_DUTY_NS = 80000
PERIOD_NS = 1000000
POLL_INTERVAL_SEC = 0.25


def read_write_sectors(device):
    with open(DISKSTATS_PATH) as f:
        for line in f:
            fields = line.split()
            if fields[2] == device:
                return int(fields[9])
    return None


def pwm_set_duty(duty_ns):
    duty_path = f"{PWM_EXPORT_PATH}/pwm{PWM_CHANNEL}/duty_cycle"
    try:
        with open(duty_path, "w") as f:
            f.write(str(duty_ns))
    except FileNotFoundError:
        print(f"[stub] PWM path not found: {duty_path}")


def main():
    last_sectors = read_write_sectors(DISK_DEVICE)
    while True:
        time.sleep(POLL_INTERVAL_SEC)
        current_sectors = read_write_sectors(DISK_DEVICE)
        if current_sectors is None or last_sectors is None:
            print(f"[stub] could not read sectors for '{DISK_DEVICE}'")
            continue
        if current_sectors != last_sectors:
            pwm_set_duty(ACTIVE_DUTY_NS)
        else:
            pwm_set_duty(DIM_DUTY_NS)
        last_sectors = current_sectors


if __name__ == "__main__":
    main()
