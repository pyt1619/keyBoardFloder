import keyboard
import time
import random
BanerStart="""                                                                                
 ▄▄                            ▄▄                                            ▄▄ 
 ██                            ██                                            ██ 
 ██ ▄██▀    ▄████▄   ▀██  ███  ██▄███▄    ▄████▄    ▄█████▄   ██▄████   ▄███▄██ 
 ██▄██     ██▄▄▄▄██   ██▄ ██   ██▀  ▀██  ██▀  ▀██   ▀ ▄▄▄██   ██▀      ██▀  ▀██ 
 ██▀██▄    ██▀▀▀▀▀▀    ████▀   ██    ██  ██    ██  ▄██▀▀▀██   ██       ██    ██ 
 ██  ▀█▄   ▀██▄▄▄▄█     ███    ███▄▄██▀  ▀██▄▄██▀  ██▄▄▄███   ██       ▀██▄▄███ 
 ▀▀   ▀▀▀    ▀▀▀▀▀      ██     ▀▀ ▀▀▀      ▀▀▀▀     ▀▀▀▀ ▀▀   ▀▀         ▀▀▀ ▀▀ 
                      ███                                                       
                                                                                
                                                                                
              ▄▄▄▄   ▄▄▄▄                      ▄▄                               
             ██▀▀▀   ▀▀██                      ██                               
           ███████     ██       ▄████▄    ▄███▄██   ▄████▄    ██▄████           
             ██        ██      ██▀  ▀██  ██▀  ▀██  ██▄▄▄▄██   ██▀               
             ██        ██      ██    ██  ██    ██  ██▀▀▀▀▀▀   ██                
             ██        ██▄▄▄   ▀██▄▄██▀  ▀██▄▄███  ▀██▄▄▄▄█   ██                
             ▀▀         ▀▀▀▀     ▀▀▀▀      ▀▀▀ ▀▀    ▀▀▀▀▀    ▀▀                
                                                                                
                                                                   """
BannerEnd = """ 


▄▄      ▄▄                     ▄▄       
██      ██                     ██       
▀█▄ ██ ▄█▀  ▄████▄    ██▄████  ██ ▄██▀  
 ██ ██ ██  ██▀  ▀██   ██▀      ██▄██    
 ███▀▀███  ██    ██   ██       ██▀██▄   
 ███  ███  ▀██▄▄██▀   ██       ██  ▀█▄  
 ▀▀▀  ▀▀▀    ▀▀▀▀     ▀▀       ▀▀   ▀▀▀  

   ▄▄▄▄      ██                         ▄▄▄▄     
  ██▀▀▀      ▀▀                         ▀▀██     
███████    ████     ██▄████▄   ▄█████▄    ██     
  ██         ██     ██▀   ██   ▀ ▄▄▄██    ██     
  ██         ██     ██    ██  ▄██▀▀▀██    ██     
  ██      ▄▄▄██▄▄▄  ██    ██  ██▄▄▄███    ██▄▄▄  
  ▀▀      ▀▀▀▀▀▀▀▀  ▀▀    ▀▀   ▀▀▀▀ ▀▀     ▀▀▀▀  
                                      

"""
print(BanerStart)                                                                   
syvols=[":",";","<",">","-",",",".","'","/",'"',"`","1","2","3","4","5","6","7","8","9","0"]
len_sym=len(syvols)-1
ar=[]
mes=input("сообщение:\n")
count=int(input("количество:\n"))
random=input("включить рандомизацию доп. символов (y/N):\n")
print("генерация массива")
# print(len(syvols))
if random=="y" or random=="Y" or random=="д" or random=="Д":
	for z in range(count):
		import random
		x=random.randint(0,len_sym)
		new_=syvols[x]
		lenX=int(len(mes)-1)
		place=random.randint(0,lenX)
		mes_ar =list(mes)
		mes_ar[place]=new_
		mes2=""
		for i in range(len(mes_ar)):
			mes2+=mes_ar[i]
		ar.append(mes2)	
else:
	for i in range(count):
		ar.append(mes)
print("Массив сгенерирован!")
input("нажми Enter чтобы начать")
print("у тебя 5 секунд чтобы поставить курсор в нужную позицию")
print(5)
time.sleep(1)
print(4)
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("Go!")
for i in range(count):
	time.sleep(0.005)
	keyboard.write(ar[i])
	keyboard.press_and_release('Enter')
print(BannerEnd)                                                                   