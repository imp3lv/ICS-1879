import module

a = float(input("Введіть сторону квадрата: "))

print("Радіус описаного кола:", module.circumscribed_radius(a))
print("Радіус вписаного кола:", module.inscribed_radius(a))
