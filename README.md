Pycloner: A PoC of Another Site Cloner
======================================


Authors
--------

Félix Brezo (@febrezo)
Yaiza Rubio (@yrubiosec).

License
-------

GPLv3+.

Installation
------------

It can be downloaded from `pip` for the current user:
```
pip install pycloner --user
```

Also as root using:
```
pip install pycloner
```

Usage
-----

The package can be used either as a standalone application or as a library.

```
pycrawler.py -u https://i3visio.com
```
The websites cloned will be collected by default under `./tmp`. This option can be configured as a parameter.


This is a sample of code that uses the `pycloner.crawler.Crawl` class.
```
from pycloner.pycloner import Crawler

cr = Crawler("https://i3visio.com")
cr.crawl()
```
