from sys import argv

_, hour, output_hours, prize = argv

print(int((int(hour)*int(output_hours))+int(prize)))
