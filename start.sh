#!/bin/sh
cd /home/$USER/.conky/
python3 ./Scripts/fact.py &
sleep 12
conky -c co_main > log &
conky -c co_weather &
conky -c co_fact &
conky -c co_quote &
