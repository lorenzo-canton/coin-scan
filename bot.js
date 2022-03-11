const statistics = require('./statistics')
const wallet = require('./wallet')

ema = null
last_trend = null

module.exports = {
    startTrack : async function(exchange, symbols, timeframe, n) {
        while (true) {
            trackSymbol(exchange, symbols, timeframe, n).catch()
            await new Promise(resolve => setTimeout(resolve, 10000))
        }
    }
}
async function trackSymbol(exchange, symbols, timeframe, ema_n) {
    console.log('-----------------------------------')
    //FETCH API
    exchange.fetchOHLCV(symbols[0], timeframe, undefined, ema_n)
    .then(candles => {
        prices = candles.map(candle => candle[4])
        price = prices[prices.length - 1]

        ema = ema ? statistics.getEma(price, ema, ema_n) : statistics.getAvg(prices)
        trend = getTrend(price, ema)
        signal = getSignal(trend)

        console.log(prices)
        console.log(price)
        console.log('ema(' + ema_n + ')\t' + ema)
        console.log('trend\t' + trend)
        if (signal) {
            console.log('SIGNAL ' + signal)
            
        }

        last_trend = trend
    })
}

function getTrend(price, ema) {
    if (price > ema) return true
    return false

}
function getSignal(trend) {
    if (last_trend != null && trend != last_trend) {
        return trend ? 'BUY' : 'SELL'
    }
    return null
}