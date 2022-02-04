def to_binary(mask):
	splitt = mask.split(".")
	i = 0
	last_string = ""
	while (i < 4):
		bin_split = bin(int(splitt[i]))
		#print(bin_split[2:])
		last_string += bin_split[2:]
		leng = len(bin_split[2:])
		if leng < 8:
			j = 0
			while j < 8:
				last_string += '0'
				j += 1
		i += 1
	return last_string

def first_address(mask, ip_address):
	split_mask = mask.split(".")
	split_ip = ip_address.split(".")
	i = 0
	string_net = ""
	while (i < 4):
		int_m = int(split_mask[i])
		int_ip = int(split_ip[i])
		bitwise = int_m & int_ip
		string_net += str(bitwise) + "."
		i += 1
	return (string_net[:-1])

def or_op(mask, net_add):
	split_mask = mask.split(".")
	split_net = net_add.split(".")
	i = 0
	string_net = ""
	while (i < 4):
		int_m = int(split_mask[i])
		int_net = int(split_net[i])
		or_operation = int_m | int_net
		string_net += str(or_operation) + "."
		i += 1
	return (string_net[:-1])

def inverse(str):
	to_ret = ""
	for i in str:
		if (i == '1'):
			to_ret += "0"
		else:
			to_ret += '1'
	return (to_ret)

def last_address(mask, ip_address):
	net_add = first_address(mask, ip_address)
	mask = inverse(to_binary(mask))
	string_m = ""
	i = 0
	while (i < 32):
		sub_mask = mask[i:i+8]
		sub_mask = int(sub_mask, 2)
		string_m += str(sub_mask) + "."
		i += 8
	#print(string_m[:-1])
	final = or_op(string_m, net_add)
	print("first address: " + net_add)
	print("last address: " + final)




	
# first_address("255.255.255.252", "192.168.35.222")
# last_address("255.255.255.252", "192.168.35.222")


def main_func():
	first = raw_input("enter subnet mask: ")
	second = raw_input("enter ip address: ")
	first_address(second, first)
	last_address(second, first)


main_func()
#"0.0.0.255" | "192.168.000.000"

