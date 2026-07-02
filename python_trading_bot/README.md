# Binance Futures Testnet Trading Bot

## Overview

This project is a command-line Python application that allows users to place Market and Limit orders on the Binance Futures USDT-M Testnet. It is built using the official `python-binance` library and follows a modular architecture with separate components for API interaction, order management, validation, and logging.

The application also provides market information such as the current price and the 24-hour high and low for a trading pair.

---

## Features

- Place Market orders
- Place Limit orders
- Supports both BUY and SELL order types
- Display current market price
- Display 24-hour high and low prices
- Input validation with descriptive error messages
- Logging of API requests, responses, and errors
- Modular and reusable code structure

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
└── bot.log
```

---

## Requirements

- Python 3.x
- Binance Futures Testnet account
- Binance Testnet API credentials

---

## Installation

Clone the repository or download the project folder.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root directory and add your Binance Testnet API credentials:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key
```

---

## Usage

### View Current Price and 24-Hour Statistics

```bash
python cli.py --symbol BTCUSDT --price-info
```

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 62000
```

---

## Example Output

```text
Order Summary
-------------
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001

Submitting order...

Order placed successfully.

Order ID        : 123456789
Status          : FILLED
Executed Qty    : 0.001
Average Price   : 61824.60
```

---

## Logging

The application records all important events in the `bot.log` file, including:

- API requests
- API responses
- Successful order placements
- Validation errors
- Runtime exceptions

These logs can be useful for debugging and monitoring the application's behavior.

---

## Input Validation

The application validates:

- Trading symbol
- Order side (BUY or SELL)
- Order type (MARKET or LIMIT)
- Order quantity
- Limit order price
- Missing or invalid command-line arguments

Meaningful error messages are displayed whenever invalid input is provided.

---

## Technologies Used

- Python 3
- python-binance
- argparse
- python-dotenv
- logging

---

## Assumptions

- The application is intended to work with the Binance Futures USDT-M Testnet.
- API credentials are valid and have trading permissions enabled.
- Users provide valid trading symbols, quantities, and prices.
- An internet connection is available while using the application.

---

## Assignment Requirements Covered

- Place Market and Limit orders on Binance Futures Testnet
- Clean and modular project structure
- Input validation and error handling
- Logging of requests, responses, and errors
- Command-line interface using argparse
- Clear setup and usage instructions

---

## Author

Krishna Verma