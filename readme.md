# 📈 stonky asynchronous version!!! (experimental)

## Blazingly fast! Support for cryptocurrencies! Stock name alias support!
I've tinkered stonky a little bit to improve speed. Gevent modules make it possible for synchronous python codes to execute asynchronously.   

## How to install(for ubuntu)

```
sudo apt install python3.7-dev (or python3.8-dev)
git clone https://github.com/HeavensGold/stonky.git  
cd stonky
python3.7(or python3.8) -m pip install -r requirements.txt --user
```

## How to run(for ubuntu)
```
python3.7 main.py
```

## How to install(for android phone)

You need to install termux(a terminal emulator for android) from GooglePlay or from F-droid.
From termux command line window,

```
pkg install clang python git
git clone https://github.com/HeavensGold/stonky.git
cd stonky
pip install -r requiremnets.txt  ##installing gevent module on the phone takes a looooot of time. be patient:)
```

## How to run(for android phone)
```
python main.py
```
termux installs python3.8 as default.


## How to configure
There is '.stonky.cfg' file on the stonky main directory.
Edit the file with text editors to add or remove tickers and positions.

```
# An example config file for stonky

[watchlist]
# Include this section to show the watchlist report
AAPL
005930.KS: SamsungE
035420.KS: Naver
AMD
INTC
AMZN
NFLX
DIS
GOOGL
NVDA
BTC-USD
ETH-USD
ETC-USD
LTC-USD
XMR-USD
DASH-USD

[positions]
# Used to calculate the balance and profit and loss reports
AMZN=5
#VGRO.TO=1000  ; international exchanges are supported
BTC-USD: 0.1   ; cryptocurrencies are supported

[cash]
# These amounts just get added to the balance report
USD=15000
#AUD=100,000  ; you can seperate large numbers using commas

[preferences]
# You can also set or override these values using command line arguments
currency=  ; if set will convert all amounts using current forex rates
refresh=   ; if set automatically reloads reports for given number of seconds
sort='delta_percent'      ; can use ticket, bid, ask, low, high, close, change, or volume

```



---



![pypi](https://img.shields.io/pypi/v/stonky?style=for-the-badge)
![unittest](https://img.shields.io/github/workflow/status/jkwill87/stocky/unittest?style=for-the-badge)
[![licence](https://img.shields.io/github/license/jkwill87/mnamer.svg?style=for-the-badge)](https://github.com/jkwill87/stonky/blob/master/license.txt)
[![style black](https://img.shields.io/badge/Style-Black-black.svg?style=for-the-badge)](https://github.com/ambv/black)

# 📈 stonky(original)

stonky is a simple command line dashboard for monitoring stocks. It pulls live data from [Yahoo! Finance](https://finance.yahoo.com) so anything it can support, e.g. international exchanges, crypocurrencies, etc., stonky can too.

![screenshot](https://github.com/jkwill87/stonky/raw/master/assets/screenshot.png)

## Install

`$ pip3 install --user stonky`

## Config

stonky is mainly configured through a config file. By default it looks for and loads a file named **`.stonky.cfg`** in your home directory. You can also specify a custom path by passing the `--config=<PATH>` command line argument which can be useful to monitor multiple watchlists. If you run stonky without a config file it will load [the example one](https://github.com/jkwill87/stonky/blob/master/stonky/__example.cfg) by default.

## Arguments

You can also set or override many of stonky's settings via command-line arguments.

```
usage: stonky [-h] [--config PATH] [--currency CODE] [--refresh SECONDS] [--sort FIELD]

optional arguments:
  -h, --help         show this help message and exit
  --config PATH      sets path to config file
  --currency CODE    converts all amounts using current forex rates
  --refresh SECONDS  refreshes output on set interval
  --sort FIELD       orders stocks by field

FIELDS can be one of ticket, bid, ask, low, high, close, change, volume
```

## Contributions

Community contributions are a welcome addition to the project. In order to be merged upsteam any additions will need to be formatted with [black](https://black.readthedocs.io) for consistency with the rest of the project and pass the continuous integration tests run against the PR. Before introducing any major features or changes to the configuration api please consider opening [an issue](https://github.com/jkwill87/stonky/issues) to outline your proposal.

Bug reports are also welcome on the [issue page](https://github.com/jkwill87/stonky/issues). Please include any generated crash reports if applicable. Feature requests are welcome but consider checking out [if it is in the works](https://github.com/jkwill87/stonky/issues?q=label%3Arequest) first to avoid duplication.
