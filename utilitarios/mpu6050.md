sudo apt-get install python-smbus
sudo apt-get install i2c-tools




raspi-config

#######  MANUAL

Installing Kernel Support (Manually)

If you are using Occidentalis, then your Pi is ready to go with I2C as far as enabling the hardware goes. However, if you are using Raspbian, you will need to open LXTerminal or console or ssh and enter the following command:

    sudo nano /etc/modules

and add these two lines to the end of the file:

    i2c-bcm2708 
    i2c-dev

Agregar lineas para activar en "/boot/config.txt "

	dtparam=i2c1=on
	dtparam=i2c_arm=on
