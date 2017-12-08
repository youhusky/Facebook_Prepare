from collections import defaultdict


def foodmenu(order, menu):
	res = defaultdict(int)
	queue = [menu[order]]
	while queue:
		menu_list = queue.pop(0)
		while menu_list:
			item = menu_list.pop(0)
			# item.values()-- [1] or ["meat":...]
			if type(item.values()[0]) == type(1):
				res[item.keys()[0]] += item.values()[0]
			else:
				# sub component {water:100}
				for each in item.values()[0]:
					menu_list.append(each)
	return res





menu = {"pizza":[{"floar":100},{"water":100},{"meat":[{"water":100}]}]}
print foodmenu("pizza", menu)