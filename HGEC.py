# Changeable values
level = 2
hours = 24
sell_price = 900

# Constant values
buildings = 14
unit_per_hour = level * 2
workers = 100 * level * buildings
unit_worker_cost = 190
admin_overhead = round((workers / 100) * 0.56714, 2)

# Resources prices
price_gold = 6200 / 16
price_chemicals = 14.5 * 3
price_silic = 7.5 * 4

# Unit cost
cost_resources = price_gold + price_chemicals + price_silic
labor_cost = 190 + (190 / 100 * admin_overhead)
unit_cost = (cost_resources + labor_cost)

# Expense
quantity = unit_per_hour * hours * buildings
sum_cost = round(quantity * unit_cost)

# Income
sum_revenue = round(quantity * sell_price)
sum_net = round(sum_revenue - sum_cost)
net_percent = round(sum_net / (sum_cost / 100), 2)
net_hour = round(sum_net / hours)

# Print result
print('\n ', quantity, 'units for', hours, 'h'
      '\n  Admin. overhead is ', admin_overhead, '%')
print('\n| Unit cost $', unit_cost,
      '\n| Resources $', cost_resources,
      '\n| Labor $', labor_cost,
      '\n| Unit Income $', round(sell_price - unit_cost), sep='')
print('\n@ Total expense $', sum_cost,
      '\n@ Total Income $', sum_revenue,
      '\n@ NET income $', sum_net, '(is', net_percent, '%)')
print('\n In hour $', net_hour,
      '\n In day $', net_hour * 24,
      '\n In week $', net_hour * 24 * 7,
      '\n In 4 weeks $', net_hour * 24 * 7 * 4, sep='')
