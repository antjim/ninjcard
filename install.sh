#!/bin/bash

sudo apt-get -y update
sudo apt-get -y install python-spidev python3-spidev
git clone https://github.com/lthiery/SPI-Py.git
git checkout 8cce26b9ee6e69eb041e9d5665944b88688fca68
sudo python SPI-Py/setup.py install
