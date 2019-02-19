# pi-fan
Turn on Raspberry Pi 3 fan when CPU temperature reaches a certain level

![pi-fan](./pi-fan.png)

- R1 can range from 220Ω up to 1kΩ
- The 2N2222 transistor can feed up to 600 mA fan
- If you see a yellow *lightning bolt* in the top right corner of the screen, that means that you don't have enough power going to the Raspberry Pi, a 5V / 2500 mA will generally do
- The diode role is to "clamp" the voltage spike that occurs whenever the fan is switched off
- If you have a small fan like those integrated with some cases (200 mA) the diode can be omitted
- Any valid GPIO pin can do
- The program will tun on the fan when CPU temperature reaches ``fanOnTemperature``, the fan will turn off only when the temperature goes below ``fanOffTemperature``
- Values of 55 degrees for ``fanOnTemperature`` and 45 for ``fanOnffTemperature`` showed during tests good compromize between cooling and intermittent on/off of the fan. To maintain the CPU temperature within those limits under normal use (browsing, system update, etc.) an average of 5 minutes off and 1 minute on for the fan was observed
- Tests were carried out with a small 200 mA fan that comes with the case

To run the script at startup, and supposing it is saved in the ``/home/pi`` folder, edit the ``/etc/rc.local`` and add the following line
````bash
/home/pi/pi-fan.py &
````
- It is not necessary to add ``sudo`` to the command as the ``rc.local`` is run by the ``root`` user
- Ensure the last line of the file is ``exit 0``
