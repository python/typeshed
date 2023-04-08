from periphery.gpio import (
    GPIO as GPIO,
    CdevGPIO as CdevGPIO,
    EdgeEvent as EdgeEvent,
    GPIOError as GPIOError,
    SysfsGPIO as SysfsGPIO,
)
from periphery.i2c import I2C as I2C, I2CError as I2CError
from periphery.led import LED as LED, LEDError as LEDError
from periphery.mmio import MMIO as MMIO, MMIOError as MMIOError
from periphery.pwm import PWM as PWM, PWMError as PWMError
from periphery.serial import Serial as Serial, SerialError as SerialError
from periphery.spi import SPI as SPI, SPIError as SPIError

version: tuple[int, int, int]

def sleep(seconds: float) -> None: ...
def sleep_ms(milliseconds: float) -> None: ...
def sleep_us(microseconds: float) -> None: ...
