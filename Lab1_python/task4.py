
group1 = [14, 27, 35, 14, 48, 62, 27, 73]
group2 = [27, 35, 41, 48, 56, 73, 41, 89]
group3 = [27, 35]

a = set(group1)
b = set(group2)
c = set(group3)

print("Початковий список 1:", group1)
print("Початковий список 2:", group2)

print("\nУнікальні елементи:")
print("Множина A:", sorted(a))
print("Множина B:", sorted(b))
print("Множина C:", sorted(c))

print("\nОперації над множинами:")
print("Перетин A і B:", sorted(a & b))
print("Об'єднання A і B:", sorted(a | b))
print("Симетрична різниця A і B:", sorted(a ^ b))

print("\nПеревірка підмножин:")
print("C є підмножиною A:", c <= a)
print("A є підмножиною B:", a <= b)
