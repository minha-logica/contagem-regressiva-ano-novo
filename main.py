import time 
from datetime import datetime, timedelta


def converter_para_HMS(segundos):
    horas,     resto = divmod(segundos,60*60)
    minutos,   resto = divmod(resto, 60)
    segundos = resto
    return horas, minutos, segundos

print("\nContagem Regressiva para o Ano Novo:")

ano_velho = datetime.today().year  

while True:
    h_atual = datetime.now().hour
    m_atual = datetime.now().minute
    s_atual = datetime.now().second
    d_atual = datetime.now().day
    
    tempo_presente = timedelta(    	
    	                days=d_atual,                
    	                hours=h_atual,
    	                minutes=m_atual,
    	                seconds=s_atual
    	            )
    duracao_de_um_ano = timedelta(days=365)
    
    tempo_restante = duracao_de_um_ano - tempo_presente
    
    segundos_restantes = tempo_restante.seconds
    dias_restantes = tempo_restante.days
    
    h, m, s = converter_para_HMS(segundos_restantes)        
    print("\r{} dias e {:02}:{:02}:{:02} horas".format(dias_restantes,h,m,s), end='',flush=True)
        
    if dias_restantes == 0 and segundos_restantes == 0:    
        ano_novo = datetime.today().year
        if ano_novo == ano_velho + 1:
            print(f"\nFeliz Ano Novo!\nFeliz {ano_novo}!")
        break 
        
    time.sleep(1)