money = 0
orders = []
order_history = []
module.exports = {
    getHistory : function() {
        return order_history
    },
    getOrders : function () {
        return orders
    },
    getMoney : function () {
        return money
    },
    open : function (type, position, stop) {
        orders.push({
            type : type,
            stop : stop,
            openPosition : position
        })
    },
    close : doClose,
    checkOrders : function (price) {
        orders.forEach(order => {
            if ((order.type == 'BUY' && order.open - price < order.stop) 
                || (order.type == "SELL" && price - order.open < order.stop)) {
                console.log('hit stop loss');
                doClose(order, price)
            }
        })
    }
}
function doClose(order, position) {
    order = orders.find(e => e == order)
    if (order) {
        balance = 0

        if (order.type == 'BUY') balance += position - order.openPosition
        else balance -= order.openPosition - position

        orders = orders.filter(e => e != order)
        money += balance

        order_history.push({
            type: order.type,
            stop : order.stop,
            openPosition: order.openPosition,
            closePosition: position,
            balance: balance
        })
    }        
}