from susu import SusuGroup


group = SusuGroup("50.00")

group.add_member("Ama")
group.add_member("Kofi")
group.add_member("Esi")

print(group.members)
print(group.weekly_amount)
print(group.current_week)
print(group.payments)
group.add_member("Ama")