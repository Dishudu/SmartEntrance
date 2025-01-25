# import RPi.GPIO as GPIO


# class GPIOController:
#     def __init__(self, pin: int):
#         self.pin = pin
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(self.pin, GPIO.OUT)

#     def set_high(self):
#         GPIO.output(self.pin, GPIO.HIGH)

#     def set_low(self):
#         GPIO.output(self.pin, GPIO.LOW)

#     def cleanup(self):
#         GPIO.cleanup()

# заглушка для Windows
class GPIOController:
    def __init__(self, pin: int):
        self.pin = pin

    def set_high(self):
        print(f"GPIO {self.pin}: Включен")

    def set_low(self):
        print(f"GPIO {self.pin}: Выключен")

    def cleanup(self):
        print("GPIO: Очистка")
