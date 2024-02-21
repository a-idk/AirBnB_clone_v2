#!/bin/bash
cd ..;
python3 -m web_flask.$1 > /dev/null 2>&1 &
echo $! > web_flask/$1.pid

sleep 5;
