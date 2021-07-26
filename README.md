# KEL103
supporting software / resources for the Korad KEL103 electronic load

# factory-provided software
the KEL103 comes with accessories including a CD with some windows software. Korad has [hosted these files here](http://www.koradtechnology.com/companyfile/19.html).

another copy of these files is available at [cdn.subluminal.li/third-party/korad/kel103/factory/cd.zip](https://cdn.subluminal.li/third-party/korad/kel103/factory/cd.zip)

noteworthy components of the software package

name | filepath
-----|---------
Kel 103 Assistant | ```Test Command/KEL103.exe```
USB-K-R-Com Port 2.0.inf | ```Software/USB driver/USB-K-R-Com Port 2.0.inf```


# python driver
a good python driver for ethernet control of the KEL103:
[Mango-kid/py-korad](https://github.com/Mango-kid/py-korad)

# ethernet notes
ethernet is not enabled by default on the device. there's a [good amazon review](https://www.amazon.com/gp/customer-reviews/R2X1A7FTF0PBPM?ref%5F=cm%5Fcr%5Fdp%5Fd%5Frvw%5Fttl&ASIN=B07GVNQZQF&sa-no-redirect=1&pldnSite=1) that explains how to set up the ethernet interface. gist repeated below:

## configuring the KEL103 for ethernet control

### connect
configuration of the ethernet interface must be done using the supplied desktop software, either through the network or usb.

*note*: the network interface may not work by default. in this case use usb to try to configure the interface

#### connecting without usb
* run **Kel 103 Assistant**
* switch to 'Network Debuger' (sic) tab
* click 'Scan Devices'
* wait for device to be listed
  * if it never shows up you may need to install usb drivers and connect that way. see below

#### connect with usb
* install usb drivers
  * connect usb cable
  * turn on KEL103
  * right click on **USB-K-R-Com Port 2.0.inf** and select 'isntall'
* run **Kel 103 Assistant**
* switch to 'USB Debuger' tab
* click 'Scan Devices'
* wait for the device to be listed (likely as a COMX port)
* select the device listing
* click 'Open USB'

### configuring ethernet
once connected to the device through the assistant software you can configure the network (ethernet / LAN) interface. power cycle the device for changes to take effect on the interface

#### dhcp (dynamic ip address allocation)
* select 'DHCP' uner 'IP Settings'

#### static ip
* select 'Static IP' uner 'IP Settings'
* provide desired settings
  * 'IP addres', 'NetMask' and 'GateWay' are all **required**
  * **IP Addres**: desired static ip address
  * **NetMask**: ??? - try entering the network mask that the router uses
  * **GateWay**: ??? - try entering the ip address of the router/gateway

# tools

name | filepath | description
-----|----------|------------
ping.py | ```tools/ping.py``` | utility to quickly ping a range of addresses on the network
