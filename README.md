# bitfinex-python

While there are existing python libraries for most cryptocurrency exchanges,
each exchange has a different api. This results on a lot of disparities on how libraries are implemented, and as such each one has a very different usage, and return values. This library attempts to set a standardized way for exchange libraries.

Planned exchanges:

- [ ] Bitfinex
- [ ] Kraken
- [ ] Bitso
- [ ] Gdax/Coinbase
- [ ] Gemini

*Note:* While I attempt to avoid making breaking changes, this library is still 
work in progress (WIP), use under your own risk.


## Instalation
TODO

### Requirements
TODO

## Usage

```py
from bitfinexpy import Bitfinex

b = Bitfinex()

b.ticker('btcusd')
```


## TODO

- [ ]  Add tests WIP
- [X]  Add public endpoints
- [ ]  Add requirements, setup, etc.
- [ ]  Add private endpoints
- [ ]  Unify interface for trading endpoints
= [ ]  Upload to pip

## Contribution

1. Discuss changes by creating a issue.
2. Fork the project.
3. Create a branch with fix, or feature with it's proper tests.
4. Create a PR
