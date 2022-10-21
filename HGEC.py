# It works only for High grade e-comp
# but you can adoptive it for any good.

# Changeable values
levels = 28 # Total levels of all your buildings that used for production Hgec
hours = 24
sell_price = 900

# Constant values
unit_per_hour = 2 # how many one level of building can produce per hour
workers = 100 * levels
admin_overhead = round((workers / 100) * 0.56714, 2) # (0.56714) This found out with experimental way

# Resources prices (averege)
price_gold = 6200 / 16
price_chemicals = 14.5 * 3
price_silic = 7.5 * 4

# Unit cost
cost_resources = price_gold + price_chemicals + price_silic
labor_cost = 190 + (190 / 100 * admin_overhead)
unit_cost = (cost_resources + labor_cost)

quantity = unit_per_hour * hours * levels # Quantity of Hgec
sum_expenses = round(quantity * unit_cost) # Total expenses

# Income
sum_revenue = round(quantity * sell_price)
sum_net = round(sum_revenue - sum_expenses)
net_percent = round(sum_net / (sum_expenses / 100), 2)
net_hour = round(sum_net / hours)

# Print result
print('\n ', quantity, 'units for', hours, 'h'
      '\n  Admin. overhead is ', admin_overhead, '%')
print('\n| Unit cost $', unit_cost,
      '\n| Resources $', cost_resources,
      '\n| Labor $', labor_cost,
      '\n| Unit Income $', round(sell_price - unit_cost), sep='')
print('\n@ Total expense $', sum_expenses,
      '\n@ Total Income $', sum_revenue,
      '\n@ NET income $', sum_net, '(is', net_percent, '%)')
print('\n In hour $', net_hour,
      '\n In day $', net_hour * 24,
      '\n In week $', net_hour * 24 * 7,
      '\n In 4 weeks $', net_hour * 24 * 7 * 4, sep='')
