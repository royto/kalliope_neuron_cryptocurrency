# Crytocurrency

## Synopsis

This neuron allows you to get cryptocurrency price in other currency

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

| Name    | Description                                    | Type   | sample      |
|---------|------------------------------------------------|--------|-------------|
| target  | the converted price for the required currency  | Float  | 5361.82     |

#### Synapses example

``` yml
  - name: "bitcoin-value"
    signals:
      - order: "what is the price of bitcoin"
    neurons:
      - cryptocurrency:
          currency: "BTC"
          target: "EUR"

```

The template defined in the templates/diagral.j2

```jinja2
Ouverture du portail
```
