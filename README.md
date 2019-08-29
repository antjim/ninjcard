# ninjcard
Ninjcard is a toolkit that help you to clonate, to read, to write a set of MIFARE cards.  This is a academic project, although this project could use for pentesting.

## Requisites
- You have to use a OS based on Debian (Linux Mint, Ubuntu, Debian, etc).
- It's necessary to use `Python 2.7.15+`.

## Installation
- If you want use a reader RC 522 in a Raspberry pi, you have to execute `sudo bash utils/installRC522.sh`.

- If you want usen a reader ACR122U in a Raspberry pi or other OS (based on Debian), you have to execute `sudo bash utils/installACR122U.sh`.

## Usage
- If you need to use the reader RC 522, you can use this option:
  - `python rc522/ninjcard.py`

- If you need to use *mfoc* or *mfcuk* you can type the option -h for more help.
  - also, you can use `python acr122u/ninjcardACR122U.py`
