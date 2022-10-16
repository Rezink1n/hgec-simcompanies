level = 2
buildings = 14
unit_worker_cost = 190
hours = 48
sell_price = 900
admin_overhead = 20

price_gold = 6100 / 16
price_chemicals = 14.5 * 3
price_sillicon = 7.5 * 4

cost_resources = price_gold + price_chemicals + price_sillicon
labor_cost = 190 + (190 / 100 * admin_overhead)
unit_cost = (cost_resources + labor_cost)

per_hour = level * 2

quantity = per_hour * hours * buildings
sum_cost = quantity * unit_cost
sum_revenue = quantity * sell_price
sum_net = sum_revenue - sum_cost
net_percent = round(sum_net / (sum_cost / 100), 2)
net_hour = sum_net / hours
print()
print('For', hours, 'hours you can produce', quantity, 'units of HGEC.')
print()
print('Unit cost $', unit_cost, ' which:', sep='')
print('1) Resources $', cost_resources, sep='')
print('2) Labor cost $', labor_cost, sep='')
print()
print('It will cost you $', sum_cost, 'and you get on selling $', sum_revenue,
      'with NET income $', sum_net, '(is', net_percent, '%)')
print()
print('In hour $', (net_hour),
      ' | In day $', net_hour * 24,
      ' | In week $', net_hour * 24 * 7,
      ' | In 4 weeks $', net_hour * 24 * 7 * 4, sep='')
