def parse(xbee_data):
	split_data = xbee_data.split(";")
	data ={x: float(split_data[x - 1]) for x in (1, 2, 3)}
	return data
