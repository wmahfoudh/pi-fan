# pi-fan
Turn on Raspberry Pi 3 fan when CPU temperature reaches a certain level

![pi-fan](./pi-fan.png)

- R1 can go up to 1kΩ
- The diode role is to "clamp" the voltage spike that occurs whenever the fan is switched off
- If you have a small fan like those integrated with some cases (200 mA) the diode can be omitted
- Any valid GPIO pin can do

To run th escript with each boot, edit the ``/etc/rc.local`` and add the following line
````bash
python /home/pi/pi-fan.py &
````
Ensure the last line of the file is ``exit 0``
