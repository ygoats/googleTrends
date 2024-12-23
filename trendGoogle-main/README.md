# trendGoogle
This scanner will post the fastest searched cryptocurrencies on Google over the last 6 hours.
It uses a propietary moving average calculation.

pip3 install telegram-send

pip3 install pytrends

pip3 install plotly

Run trendOnce.py to run the scanner once
Run trendRun1.py to run on specific intervals

Change masterList.py to the cryptocurrencies or words you would like to use in your scanner.

SETTING UP TELEGRAM

Go to @BotFather on telegram and setup an Bot with the easy to follow instructions.

Alternatively please use in the cli

telegram-send --configure

remove the conf = "user1.conf" from the telegram-send() portion of the code
