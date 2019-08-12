#!/bin/bash

sudo apt-get -y update
sudo apt-get -y install libnfc-examples libnfc-dev libnfc-bin libusb-dev libpcsclite-dev
tar -xvzf libnfc-1.7.0-rc7.tar.gz
git clone https://github.com/nfc-tools/mfcuk.git
git clone https://github.com/nfc-tools/mfoc.git

cd libnfc-1.7.0-rc7
./configure --prefix=/usr
make && sudo make install

cd ..
cd mfcuk
autoreconf -is
./configure
make && sudo make install

cd ..
cd mfoc
autoreconf -is
./configure
make && sudo make install

echo "[i] Completed."
