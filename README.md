# Crytocurrency

## Synopsis

This neuron allows you to get cryptocurrency price in other currency. It uses [cryptocompare.com](https://min-api.cryptocompare.com) to get data.

## Installation

```bash
kalliope install --git-url https://github.com/royto/kalliope_neuron_cryptocurrency.git
```

### Options

| parameter   | required | type   | default | choices    | comment                              |
|-------------|----------|--------|---------|------------|--------------------------------------|
| currency    | YES      | String | None    |            | The cryptocurrency to get price      |
| target      | YES      | String | None    |            | The target currency                  |

See [https://min-api.cryptocompare.com/](https://min-api.cryptocompare.com/) to get supported currency

#### Return Values

The return value is dynamic based on source and target currency.

| Name    | Description                                                          | Type   | sample        |
|---------|----------------------------------------------------------------------|--------|---------------|
| currency | a dict containing thethe converted price for the required currency  | dict   | EUR : 5361.82 |

#### Synapses example

``` yml
  - name: "bitcoin-value"
    signals:
      - order: "what is the price of bitcoin"
    neurons:
      - cryptocurrency:
          currency: "BTC"
          target: "EUR"
          file_template: templates/bitcoin_euro.j2

```

The template defined in the templates/bitcoin_euro.j2

```jinja2
The current price of bitcoin is {{ BTC["EUR"] }} euros
```
