#!/bin/bash

BRIGHTNESS=`xrandr --verbose | grep -m 1 -i brightness | cut -f2 -d ' '`

A=$(echo "$BRIGHTNESS + .2" | bc -l)

xrandr --output eDP1 --brightness $A
