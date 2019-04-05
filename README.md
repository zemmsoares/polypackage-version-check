# polybar-node-version
![Polynews Example](https://i.imgur.com/rPo7kIE.png)

Polybar python script to scrap latest node version from website and compare it to the installed.

## Module
```ini
[module/nodeversion]
type = custom/script
exec = ~/.config/polybar/nodeversion.py
interval = 30
format-prefix = " "
```

## Icon
Icon from example ( Font Awesome 5 Brands )
```ini
font-1 = Font Awesome 5 Brands:size=10;1
```
