### Historical Stock Market Data

This is a Python script that grabs a current list of all NASDAQ tickers and retrieves daily 2015 YTD stock data, stored in a SQLite3 database, from Yahoo! Finance.

##### Install requirements.
Execute the following commands:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

##### Set up database.
Execute the following commands:  

```bash
sqlite3 Finance.db

sqlite> .databases
sqlite> .quit
```

After running `sqlite3 Finance.db`, run `.databases` to confirm it was created, followed by `.quit` to exit.

##### Migrate database schema.
Execute the following commands:

```bash
python model.py finance init
python model.py finance migrate
python model.py finance upgrade
```

##### Pull stock data.
Execute `python tickers.py` to query all of the data.

Note: there is a possibility that a ticker may not be retured by Yahoo! Finance, so the tickers are printed with their success/fail status in the Terminal.

##### Use it in your code.
To use this data in your code, create files inside thsi folder and simply import the classes from `model.py` by including the following import statement in your file:

```python
from model import db. Tickers, Details
```

##### When you're done...
Execute the `deactivate` command to turn off your virtual environment.

##### By Jay Ravaliya
