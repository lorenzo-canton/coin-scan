const ccxt = require('ccxt')
const express = require('express')
const path = require('path')
const bodyParser = require("body-parser");

const tracker = require('./bot')
const wallet = require('./wallet')

const app = express()

app.use(express.json())
app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'html/index.html'))
})
app.get('/options', (req, res) => {
    res.sendFile((path.join(__dirname, 'html/options.html')))
})

app.get('/open', (req, res) => {
    res.json(wallet.getOrders())
})
app.get('/history', (req, res) => {
    res.json(wallet.getHistory())
})
app.get('/botoptions', (req, res) => {
    res.json(tracker.getOptions())
})

app.post('/timeframe', (req, res) => {
    console.log(req.body);
    tracker.setTimeFrame(req.body.timeframe)
    res.sendStatus(200)
})
app.post('/number', (req, res) => {
    tracker.setNumber(req.body.number)
    res.sendStatus(200)
})

app.listen(3000)

const exchange = new ccxt.binance()
exchange.loadMarkets()

tracker.startTrack(exchange, ['BTC/USDT'], '15m', 50)