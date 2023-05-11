from pandas import DataFrame

f = open("my_ip.json", "r")
my_ip = DataFrame(f.read())

print(my_ip)
