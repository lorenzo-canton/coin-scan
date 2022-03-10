const statistics = require('./statistics')
const wallet = require('./wallet')

exchange = null
symbols = null
timeframe = '15m'
long_n = 50
short_n = 20
ema_signal = null

module.exports = {
    startTrack : function(exc, sym, tf, nl, ns) {
        exchange = exc
        symbol = sym
        timeframe = tf
        long_n = nl
        short_n = ns
        trackSymbol().catch()
    }
}
async function trackSymbol() {
    console.log('-----------------------------------')
    //FETCH API
    exchange.fetchOHLCV(symbol, timeframe, undefined, long_n).then(data => {
        prices = data.map(candle => candle[4])
        wallet.checkOrders(prices[prices.length - 1])
        new_ema_signal = statistics.getEmaTrend(prices, long_n, short_n)
        
        //CAMBIO DIREZIONE TREND GENERA SEGNALE
        if (ema_signal && new_ema_signal != ema_signal) {        
            ema_signal = new_ema_signal

            //APRI POSIZIONI

            //chiude le posizioni di tipo contrario al segnale
            //se il segnale e' BUY chiude gli ordini SELL
            wallet.getOrders().forEach(order => {
                if (order.type != ema_signal) wallet.close(order, prices[prices.length - 1])
            })
            //apre un nuovo ordine
            wallet.open(ema_signal, prices[prices.length - 1], 10)

        } else if (!ema_signal) ema_signal = new_ema_signal
        
        console.log('price\t\t' + prices[prices.length - 1]);
        console.log('trend  ' + new_ema_signal)
        console.log('wallet ' + wallet.getMoney())
        console.log(wallet.getOrders())      
        //console.log(wallet.getHistory())
    })
    //LOOP
    await new Promise(resolve => setTimeout(resolve, 10000))
    trackSymbol().catch()
}
