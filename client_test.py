import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      datapoint = getDataPoint(quote)
      self.assertEqual(datapoint, (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
      

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      datapoint = getDataPoint(quote)
      self.assertEqual(datapoint, (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  def test_getRatio_calculateRatio(self):
    price_a, price_b = 119.4, 150.04
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, price_a / price_b)
    
  def test_getRatio_calculateRatioWithStockZeroPrice(self):
    price_a, price_b = 119.4, 0
    price_c, price_d = 0, 119.4
    ratio_AB = getRatio(price_a, price_b)
    ratio_CD = getRatio(price_c, price_d)
    
    self.assertEqual(ratio_AB, None)
    self.assertEqual(ratio_CD, 0)



if __name__ == '__main__':
    unittest.main()
