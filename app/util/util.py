def isNull(a):
	a = str(a)
	if not a or not a.strip() or a == 'None':
		return True
	return False