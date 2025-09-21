




## Directly interacting with the GPIO addresses
When you are using Raspberry Pi you have some CLI / terminal tools

```bash
# Install the latest GPIOD tooling
sudo apt install gpiod

gpiodetect # list available GPIO chips
gpioinfo # list available GPIO lines (pins)
gpioset # set GPIO pin HIGH/LOW
gpioget # read GPIO pin value
```