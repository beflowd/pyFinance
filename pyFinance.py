from flask import Flask
import yfinance as yf

msft = yf.Ticker("MSFT")

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>" + str(msft.dividends) + "</p>"
