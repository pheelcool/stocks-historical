# Import statements
import csv
import sys
import urllib2
from datetime import date, timedelta
from model import db, Tickers, Details

# Start by deleting all current rows
Tickers.query.delete()
Details.query.delete()

# Pull all tickers in CSV
tickerlist = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
tickerresponse = urllib2.urlopen(tickerlist)
tickerarray = csv.reader(tickerresponse)
added = [0, 0]

def generateUrl(ticker):
	return "http://real-chart.finance.yahoo.com/table.csv?s=" + ticker + "&d=9&e=16&f=2015&g=d&a=1&b=1&c=2015&ignore=.csv"

# Loop through all tickers and add to database
for tick in tickerarray:
	ticker = Tickers(tick[0], tick[1], tick[4], tick[5], tick[6], tick[7])

	try:
		history = urllib2.urlopen(generateUrl(tick[0]))
		historycsv = csv.reader(history)

		for hist in historycsv:
			detail = Details(hist[0], hist[1], hist[2], hist[3], hist[4], hist[5], hist[6])
			ticker.details.append(detail)	

		db.session.add(ticker)
		db.session.commit()
		added[0] += 1
		print tick[0] + " added."
	except:
		added[1] += 1
		print tick[0] + " failed."

# Commit, print success.
print "Successfully added " + str(added[0]) + " of " + str(added[0] + added[1]) + " tickers."
