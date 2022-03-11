const ccxt = require('ccxt')
const express = require('express')
const path = require('path')

const tracker = require('./bot')
const wallet = require('./wallet')

const app = express()

app.use(express.json())

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'))
})

app.get('/open', (req, res) => {
    res.json(wallet.getOrders())
})
app.get('/history', (req, res) => {
    res.json(wallet.getHistory())
})

app.listen(3000)

const exchange = new ccxt.binance()
exchange.loadMarkets()

tracker.startTrack(exchange, ['BTC/USDT'], '1m', 2)