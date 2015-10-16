# Imports
# flask
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

# sqlalchemy
from sqlalchemy import Integer, ForeignKey, String, Column, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

# other
import time
import hashlib

# set up app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Finance.db" 

# set up database
db = SQLAlchemy(app)

# set up migration
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('finance', MigrateCommand)

class Tickers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	symbol = db.Column(db.String)
	name = db.Column(db.String)
	ipo = db.Column(db.String)
	sector = db.Column(db.String)
	industry = db.Column(db.String)
	summary = db.Column(db.String)
	details = relationship("Details", backref="tickers", single_parent=True, primaryjoin=("Tickers.id==Details.ticker_id"))

	def __init__(self, symbol, name, ipo, sector, industry, summary):
		self.symbol = symbol 
		self.name = name
		self.ipo = ipo
		self.sector = sector
		self.industry = industry
		self.summary = summary

class Details(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.String)
	open = db.Column(db.String)
	high = db.Column(db.String)
	low = db.Column(db.String)
	close = db.Column(db.String)
	volume = db.Column(db.String)
	adjClose = db.Column(db.String)
	ticker_id = db.Column(db.Integer, ForeignKey('tickers.id'))

	def __init__(self, date, open, high, low, close, volume, adjClose):
		self.date = date
		self.open = open
		self.high = high
		self.low = low
		self.close = close
		self.volume = volume
		self.adjClose = adjClose

if __name__ == '__main__':
	manager.run()
