names = ['Leo','Sam','Jim']
message1 = f"I wanna invite {names[0]} to my party"
message2 = f"I wanna invite {names[1]} to my party"
message3 = f"I wanna invite {names[2]} to my party"

print(f"{message1}\n{message2}\n{message3}")
print(f"{names.pop().title()} can't come to the party")
names.append('Frank')
message4 = f"I wanna invite {names[2]} to my party"
print(f"{message1}\n{message2}\n{message4}")

names.insert(0, 'Ryan')
names.insert(2, 'Karen')
names.append('Uooka')

print(f'Dear {names[0]}, {names[1]}, {names[2]}, {names[3]}, {names[4]}, {names[5]}, please come to my party')

