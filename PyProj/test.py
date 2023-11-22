from nintendeals import noa
from nintendeals.api import prices

botw = noa.game_info("70010000000025")
print(botw.title)
celeste = noa.game_info("70010000006442")
print(celeste.title)

print()

prices = prices.get_prices([botw, celeste], country="US")
for nsuid, price in prices:
    print(nsuid)
    print(price.value)
    print(price.sale_value)
    print()