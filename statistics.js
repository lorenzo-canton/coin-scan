long_ema = null
short_ema = null
last_ema = null
module.exports = {
    getEmaTrend : function (prices, long_n, short_n) {
        if (long_ema) long_ema = ema(prices[prices.length - 1], long_ema, long_n)
        else long_ema = avg(prices)
        if (short_ema) short_ema = ema(prices[prices.length - 1], short_ema, short_n)
        else short_ema = avg(prices.slice(prices.length - short_n, prices.length))
    
        //console.log('EMA (' + long_n + ')\t' + long_ema)
        //console.log('EMA (' + short_n + ')   \t' + short_ema)
    
        if (short_ema > long_ema) return 'BUY'
        return 'SELL'
    }
}

function avg(arr) {
    out = 0
    arr.forEach(n => out += n)
    return out / arr.length
}
function ema(price, last, n) {
    const alpha = 2 / (n + 1)
    return last + alpha * (price - last)
}