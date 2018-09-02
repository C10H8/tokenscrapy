# token scrapy

This is a Scrapy project to scrape `Token Tracker`  from [https://etherscan.io/tokens?sort=marketcap&order=desc](https://etherscan.io/tokens?sort=marketcap&order=desc).

# require env

`python 3.4.0`


# Running the spiders

```
pip install -r requirement.txt

python run.py

```

# Storage
`mongodb 4.0`

```
MONGO_URI = 'mongodb://zeta:sPWDqjnHdVnaj49b@127.0.0.1:27017/zeta'
MONGODB_DB = 'zeta'
```

# Extracted data
```
{
  "id": 1,
  "price": "$11.2639",
  "volume": "$27,682,595",
  "image_url": "https://etherscan.io/token/images/binance_28.png",
  "name": "BNB",
  "des": "Binance aims to build a world-class crypto exchange, powering the future\nof crypto finance.",
  "change": " -0.31%",
  "market_cap": "$1,075,840,971",
  "example": "BNB "
}
```