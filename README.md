# pi-fan
Turn on Raspberry Pi 3 fan when CPU temperature reaches a certain level

![pi-fan](./pi-fan.png)

- R1 can range from 220Ω up to 1kΩ
- The 2N2222 transistor can feed up to 600 mA fan
- If you see a yellow *lightning bolt* in the top right corner of the screen, that means that you don't have enough power going to the Raspberry Pi, a 5V / 2500 mA will generally do
- The diode role is to "clamp" the voltage spike that occurs whenever the fan is switched off, and so protect the Raspberry Pi
- If you have a small fan like those integrated with some cases (200 mA or less) the diode can be omitted
- Any valid GPIO pin can do
- The program will tun on the fan when CPU temperature reaches ``fanOnTemperature``, the fan will turn off only when the temperature goes below ``fanOffTemperature``
- Values of 60 degrees for ``fanOnTemperature`` and 45 for ``fanOnffTemperature`` showed during tests good compromize between cooling and between intermittent on/off of the fan, adjust them as per your *taste*

# Allow the script to run at startup
Supposing the script is saved in the ``/home/pi/progs/`` folder:
## */etc/rc.local* method
Edit the ``/etc/rc.local`` script and add the following line:
````bash
/home/pi/progs/pi-fan.py &
````
- It is not necessary to add ``sudo`` to the command as the ``rc.local`` is run by the ``root`` user
- Ensure the last line of the script is ``exit 0``

## *as a service* (preferred method)
Create a service file: ``sudo nano /etc/systemd/system/pi-fan.service`` and paste the following:
````bash
[Unit]
Description=pi-fan

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/progs/pi-fan.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
````
Enable the service at startup with ``sudo systemctl enable pi-fan.service``
