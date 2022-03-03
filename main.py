from util.alert_manager import AlertManager

# Pants
# Sweatshirts
# Bags
# Hats
# Shirts
# Accessories
# Shorts
# Skate
# Tops/Sweaters
# T-Shirts
# Jackets
# Shoes

am = AlertManager()
print('Type clothing category')
category = input()
print('Type clothing name')
name = input()
print('Type clothing color')
color = input()
print('Type clothing size')
size = input()
print('Lastly type phone number to be notified')
number = input()
am.add_alert('T-Shirts', 'Classic Logo Tee','White','Large','+19498367866')
am.add_alert(category, name, color, size, number)
print('Alert added successfully')
print('Current alerts are:')
print(am.list_alerts())
am.check_alerts()






