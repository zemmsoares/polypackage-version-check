#!/bin/bash

output=$(python ~/.config/polybar/nodeversion.py)

icon=""

if [[ $output = *Latest* ]]; then
    echo "%{F#4F8F57}$icon  ${output//"Latest"}"
elif [[ $output = *Outdated* ]]; then
    echo "%{F#bc1a1a}$icon  ${output//"Outdated"}" 
else
    echo "%{F#65737E}$icon  ${output//"Error"}"               
fi


