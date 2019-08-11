#!/bin/bash

sudo apt-get -y update
sudo apt-get -y install libnfc-examples libnfc-dev libnfc-bin libusb-dev libpcsclite-dev
tar -xvzf ./utils/libnfc-1.7.0-rc7.tar.gz
./utils/libnfc-1.7.0-rc7/configure
make -C ./utils/libnfc-1.7.0-rc7/
make install -C ./utils/libnfc-1.7.0-rc7/
