names = ['Leo','Sam','Jim']
message1 = f"I wanna invite {names[0]} to my party"
message2 = f"I wanna invite {names[1]} to my party"
message3 = f"I wanna invite {names[2]} to my party"

print(f"{message1}\n{message2}\n{message3}")
print(f"{names.pop().title()} can't come to the party")
names.append('Frank')
message4 = f"I wanna invite {names[2]} to my party"
print(f"{message1}\n{message2}\n{message4}")