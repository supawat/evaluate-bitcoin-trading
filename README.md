# Evaluate Bitcoin Trading
#### Video Demo:  https://youtu.be/CqDeAMuCXMI
#### Description:

Python program for Evaluate Bitcoin Trading in USD and THB currency

Source code  : https://github.com/supawat/evaluate-bitcoin-trading

Project Version 0.0.1

Main feature

    1. See current price of Bitcoin

    2. Evaluate Bitcoin selling with fee exchange rate

    3. Evaluate Bitcoin buying with fee exchange rate


API

    - API for currency exchange rates data https://apilayer.com/

    - API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json


Prerequisite Installation

Install Python interpreter

    Windows:

    1. Download the latest version of Python from the official website: https://www.python.org/downloads/windows/
    2. Run the installer and follow the instructions to complete the installation process.
    3. Open Command Prompt and type "python" to launch the Python interpreter.

    Linux:

    1. Open Terminal
    2. Check if Python is already installed by typing "python3"
    3. If Python is not installed, type "sudo apt-get install python3" to install Python
    4. Type "python3" to launch the Python interpreter.

    macOS:

    1. Check if Python is already installed by typing "python3" in Terminal.
    2. If Python is not installed, download the latest version of Python from the official website: https://www.python.org/downloads/mac-osx/
    3. Run the installer and follow the instructions to complete the installation process.
    4. Open Terminal and type "python3" to launch the Python interpreter.


Install requirements packages

    $ pip install -r requirements.txt


How to run program

    $ python project.py

    if can not run try

    $ python3 project.py


Main menu after run program

    Current price [C], SELL [S], BUY [B], Exit [Q] :

    - Type 'C' if you want to see current price of Bitcoin in USD and THB currency

    - Type 'S' if you want to evaluate Bitcoin selling

    - Type 'B' if you want to evaluate Bitcoin buying

    - Type 'Q' if you want to exit program

How to test program
    
    $ pytest test_project.py
