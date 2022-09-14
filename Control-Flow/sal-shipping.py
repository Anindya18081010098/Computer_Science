ground_shipping = [[1.5, 20.0], [3.0, 20.0], [4.0, 20.0], [4.75, 20.0]]
ground_shipping_pr = 125.00
drone_shipping = [[4.50, 0.00], [9.00, 0.00], [12.00, 0.00], [14.25, 0.00]]
weight = float(input('Weight?'))

def ground(weight):
  if weight <= 2:
    price = weight*ground_shipping[0][0] + ground_shipping[0][1]
    return price
  elif weight >2 or weight<= 6:
    price = weight*ground_shipping[1][0] + ground_shipping[1][1]
    return price
  elif weight >6 or weight<= 10:
    price = weight*ground_shipping[2][0] + ground_shipping[2][1]
    return price
  else:
    price = weight*ground_shipping[3][0] + ground_shipping[3][1]
    return price

def ground_pr(weight):
  price_w = ground(weight)
  price = price_w + ground_shipping_pr
  return price

def drone(weight):
  if weight <= 2:
    price = weight*drone_shipping[0][0] + drone_shipping[0][1]
    return price
  elif weight >2 or weight<= 6:
    price = weight*drone_shipping[1][0] + drone_shipping[1][1]
    return price
  elif weight >6 or weight<= 10:
    price = weight*drone_shipping[2][0] + drone_shipping[2][1]
    return price
  else:
    price = weight*drone_shipping[3][0] + drone_shipping[3][1]
    return price
    
print("The cost of Ground Shipping: " + str(ground(weight)))
print("The cost of Premium Ground Shipping: " + str(ground_pr(weight)))
print("The cost of Drone Shipping: " + str(drone(weight)))

if ground(weight) < ground_pr(weight) and ground(weight) < drone(weight):
  print("Ground Shipping is the cheapest option.")
elif ground_pr(weight) < ground(weight) and ground_pr(weight) < drone(weight): 
  print("Premium Shipping is the cheapest option.")
elif drone(weight) < ground(weight) and drone(weight) < ground_pr(weight):
  print("Drone Shipping is the cheapest option.")
else:
  print("It is your choice to make.")

