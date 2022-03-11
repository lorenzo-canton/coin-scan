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
        doOpen(type, position, stop)  
    },
    close : doClose,
    checkOrders : function (price) {
        orders.forEach(order => {
            if (order.type == 'BUY') order.balance = price - order.openPosition
            else order.balance = order.openPosition - price

            if (order.balance < order.stop) doClose(order, price)
        })
    }
}

function doOpen(type, position, stop) {
    orders.push({
        type : type,
        balance : 0,
        stop : stop,
        openPosition : position
    })
}

function doClose(order, position) {
    order = orders.find(e => e == order)
    if (order) {
        if (order.type == 'BUY') order.balance = position - order.openPosition
        else order.balance = order.openPosition - position

        orders = orders.filter(e => e != order)
        money += order.balance

        order.closePosition = position

        order_history.push(order)
    }        
}