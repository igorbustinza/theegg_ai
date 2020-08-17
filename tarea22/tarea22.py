#tarea 22

#ejemplo1
nvacas1 = 6
pesocamion1 = 700
pesovacas1 = [360,250,400,180,50,90]
litrosleche1 = [40,35,43,28,12,13]

#ejemplo2
nvacas2 = 8
pesocamion2 = 1000
pesovacas2 = [223,243,100,200,200,155,300,150]
litrosleche2 = [30,34,28,45,31,50,29,1]


#ejemplo3
nvacas3 = 10
pesocamion3 = 2000
pesovacas3 = [340,355,223,243,130,240,260,155,302,130]
litrosleche3 = [45,50,34,39,29,40,30,52,31,1]

def  camion_vacas(p,l,C):
	n=len(p)
	pre =[[0 ,[]]  for m in  range(C+1)]
	for i in  range(1,n+1):
		pos =[[0 ,[0  for j in  range(i)]]]
		for m in  range(1,C+1):
			if p[i-1]<=m and l[i-1]+ pre[m-p[i-1]][0] > pre[m][0]:
				pos.append ([l[i-1]+ pre[m-p[i-1]][0] , pre[m-p[i -1]][1][:]+[1]])
			else:
				pos.append ([pre[m][0],pre[m][1][:]+[0]])
		pre=pos
	return  pos[C]

print(camion_vacas(pesovacas1,litrosleche1,pesocamion1)[0])
print(camion_vacas(pesovacas2,litrosleche2,pesocamion2)[0])
print(camion_vacas(pesovacas3,litrosleche3,pesocamion3)[0])


