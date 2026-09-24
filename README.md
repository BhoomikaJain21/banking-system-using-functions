# Mini Project: Banking System

A menu-driven Python application that simulates basic banking operations using
core Python fundamentals — no OOP, just variables, functions, loops,
conditionals, lists, dictionaries, and string operations.

## Features

- **Create Account** — generates a unique 6-digit account number, collects a
  4-digit PIN and an opening deposit.
- **Login** — authenticate with account number and PIN (3 attempts allowed).
- **Check Balance** — view current account balance.
- **Deposit** — add funds to your account.
- **Withdraw** — remove funds, blocked if the amount exceeds your balance.
- **Transfer** — send funds to another existing account.
- **Transaction History** — view a timestamped log of every deposit,
  withdrawal, and transfer on the account.
- **Change PIN** — update your PIN after verifying the current one.

## Tech Used

- `random` — generates unique account numbers.
- `datetime` — timestamps every transaction.
- Dictionaries — each account is stored as a dictionary (name, pin, balance,
  transaction history) inside a master `accounts` dictionary keyed by account
  number.
- Lists — each account's transaction history is a list of timestamped strings.
- Loops & conditionals — input validation and retry logic throughout
  (e.g. rejecting non-numeric input, negative amounts, over-limit withdrawals).

## How to Run

Requires Python 3.10+ (uses `match`/`case`).

```bash
python banking_system.py
```

You'll be greeted with the main menu:

```
MAIN MENU
1. Create account
2. Login
3. Exit
```

After logging in, you'll get access to the full account menu:

```
ACCOUNT MENU
1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Transaction History
6. Change PIN
7. Logout
```

## Notes

- All data is stored **in memory** — accounts are lost when the program exits.
  There is no persistent storage (file or database) in this version.
- Account numbers are randomly generated 6-digit integers and guaranteed
  unique within a single run.
- PINs must be exactly 4 digits.

## Project Structure

```
.
├── banking_system.py   # Full application (all functions + menu loop)
└── README.md
```
