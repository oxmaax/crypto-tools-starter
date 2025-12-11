
---

### `price_checker.py`

```python
import requests


def get_btc_price_usd() -> float:
    """
    fetch the current bitcoin price in usd using coingecko's public api.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data["bitcoin"]["usd"]


if __name__ == "__main__":
    try:
        price = get_btc_price_usd()
        print(f"current bitcoin price: ${price:,.2f} usd")
    except Exception as e:
        print("error fetching price:", e)
