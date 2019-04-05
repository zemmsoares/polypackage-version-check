# polybar-node-version
![Polybar-node-version Last Version](https://i.imgur.com/tV5dzEI.png)
![Polybar-node-version Outdated](https://i.imgur.com/NgMs5x1.png)
![Polybar-node-version Node not found](https://i.imgur.com/FPpVvql.png)


Polybar python script to scrap latest node version from website and compare it to the installed.

## Module
```ini
[module/nodeversion]
type = custom/script
interval = 30
exec = ~/.config/polybar/node.sh
label = %output:0:75:...%
```

## Icon
Icon from example ( Font Awesome 5 Brands )
```ini
font-1 = Font Awesome 5 Brands:size=10;1
```





