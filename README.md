# Web API Scripts

Hands-on Python scripts for querying public web APIs and parsing JSON responses from the command line.

## Files

- `steam_price_checker.py`: searches the Steam Store API by game title and displays its current price in MXN (or indicates if it is free), including a retry prompt if no match is found.
- `pokeapi_search.py`: fetches basic Pokémon data from PokeAPI. *(Remove this line if you only upload the Steam script for now)*

## Requirements

- Python 3
- `requests` (`python -m pip install requests`)

## Usage

Run any script from the terminal:

```bash
python steam_price_checker.py
