from datetime import datetime
date = datetime.now()

def generate(uf, year, month, cnpj, model, serie, number, issue_form):
	number_docu = number_doc(number)
	seq = sequence(number)

	key_part = str(uf) + str(year)[2:4] + toStringMonth(month) + str(cnpj) + str(model) + str(serie) + str(number_docu) + str(issue_form) + str(seq)
	
	div = generateDiv(key_part)
	key = key_part + str(div)
	return str(key)
	
def sequence(number):
	list = str(int(number)+1)
	seq = ''
	if len(list) < 8:
		seq = '0'*(8-len(list))
	for ch in list:
		seq += ch

	return seq

def number_doc(number):
	list = str(number)
	seq = ''
	if len(list) < 9:
		seq = '0'*(9-len(list))
	for ch in list:
		seq += ch

	return seq
	
def generateDiv(key):
	div = 0
	count = 2

	for i in range(len(key)-1, -1, -1):
		if count == 10:
			count = 2

		number = int(key[i])

		div += number*count
		count += 1

	res = 11-(div-(int(div/11)*11))
	if res > 9:
		return 0
	return res

def toStringMonth(month):
	if int(month) <= 9:
		return ('0'+str(month))
	else:
		return str(month)
