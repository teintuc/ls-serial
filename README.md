# lsserial
Small tool to list the serial ports on linux

#### Installing

	pip install install -r requirements.txt
	python -m pip install ./

#### How to use

This script is super easy to use, it is like a ```ls``` or ```lsusb``` command.

	lsserial

All the Com port that ```pyserial``` find will be listed with its description

	> lsserial
	/dev/ttyUSB0 - FT232R USB UART
	etc ...