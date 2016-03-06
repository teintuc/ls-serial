# lsserial
Small tool to list the serial ports on linux

#### Installing

This script has been devellop with python2. I will work on it to make it python3 accepted.

There is a depedency on ```pyserial```. If you don't use the setup file, you will need to install it manually or install it with pip

	pip install pyserial

Otherwise just run the setup file. Everything will be took care automaticly.

	python2 setup.py install

#### How to use

This script is super easy to use, it is like a ```ls``` or ```lsusb``` command.

	lsserial

All the Com port that ```pyserial``` find will be listed with its description

	> lsserial
	/dev/ttyUSB0 - FT232R USB UART
	etc ...