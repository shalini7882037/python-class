packet = "T:25.4;H:60;B:78"
fields = packet.split(";")
print(fields)
for field in fields:
    key, value = field.split(":")
    print(key, "->", float(value))
