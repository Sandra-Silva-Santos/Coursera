segundos_str = input("Por favor, entre com o número de segundos que deseja converter:")
total_segs = int(segundos_str)


horas = total_segs // 3600
dias = horas//86400

segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

if (horas >= 24): 

	dias = int(horas / 24)
	horas = int(horas % 24)


print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")