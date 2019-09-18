

def simplify_graph(graph):
	people_accnt = [0 for x in range(len(graph))]
	for i in range(len(graph)):
		for j in range(len(graph[i])):
			people_accnt[i] = people_accnt[i] - graph[i][j]
			people_accnt[j] = people_accnt[j] + graph[i][j]
	print(people_accnt)
	return people_accnt

def print_transacs(givers, receivers,  givers_iden, receivers_iden):
	i,j = 0,0
	while(i<len(givers)):
		if givers[i] == receivers[j]:
			print('person {} pays to person {} amount {}'.format(givers_iden[i],receivers_iden[j],givers[i]))
			givers[i] = 0
			receivers[j] = 0
			j = j+1
			i = i+1
		elif givers[i] > receivers[j]:
			print('person {} pays to person {} amount {}'.format(givers_iden[i],receivers_iden[j],receivers[j]))
			givers[i] = givers[i] - receivers[j]
			receivers[j] = 0
			j = j+1
		else:
			print('person {} pays to person {} amount {}'.format(givers_iden[i],receivers_iden[j],givers[i]))
			receivers[j] = receivers[j] - givers[i]
			givers[i] = 0
			i = i+1

def min_cash_flow(graph):
	simple_graph = simplify_graph(graph)
	receivers = [x for x in simple_graph if x > 0]
	receivers_iden = [x+1 for x in range(len(simple_graph)) if simple_graph[x] > 0]
	givers = [abs(x) for x in simple_graph if x < 0]
	givers_iden = [x+1 for x in range(len(simple_graph)) if simple_graph[x] < 0]
	receivers.sort()
	givers.sort()
	print_transacs(givers, receivers, givers_iden, receivers_iden)

graph_owe = [[0, 1000, 2000], 
          [0, 0, 5000], 
          [0, 0, 0]] 
  
min_cash_flow(graph_owe)


