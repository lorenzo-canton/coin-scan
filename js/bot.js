const statistics = require('./statistics')
const wallet = require('./wallet')

ema = null
last_trend = null
options = {
    timeframe : null,
    number : null
}
module.exports = {
    startTrack : async function(exchange, symbols, tf, n) {
        options.timeframe = tf
        options.number = n
        while (true) {
            trackSymbol(exchange, symbols, tf, n).catch()
            await new Promise(resolve => setTimeout(resolve, 10000))
        }
    },
    setTimeFrame : function (tf) {
        options.timeframe = tf
    },
    setNumber : function (n) {
        options.number = n
    },
    getOptions : function () {
        return options
    }
}
async function trackSymbol(exchange, symbols) {
    console.log('-----------------------------------')
    //FETCH API
    exchange.fetchOHLCV(symbols[0], options.timeframe, undefined, options.number)
    .then(candles => {
        prices = candles.map(candle => candle[4])
        price = prices[prices.length - 1]

        wallet.checkOrders(price)

        ema = ema ? statistics.getEma(price, ema, options.number) : statistics.getAvg(prices)
        trend = getTrend(price, ema)
        signal = getSignal(trend)

        //console.log(prices)
        console.log(price)
        //console.log('money ' + wallet.getMoney())
        console.log(ema)
        //console.log('trend\t' + trend)

        if (signal) {
            //console.log('SIGNAL ' + signal)
            wallet.getOrders().forEach(order => {
                if (order.type != signal) wallet.close(order, price)
            })
            wallet.open(signal, price, -10)
        }

        console.log(wallet.getOrders())
        //console.log(wallet.getHistory())
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