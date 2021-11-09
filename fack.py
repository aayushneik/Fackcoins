import aminofix
import os
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.THISTLE_1 + style.BOLD)
print("""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                       Amino Fack Coins Send 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%""")
print(pyfiglet.figlet_format("Vicious", font="slant"))
client=aminofix.Client()
er=False
while er==False:
	try:
		e=input("\033[1;32m \033[1;33mEmail \033[1;32m:\033[1;0m ")
		p=input("\033[1;32m \033[1;33mPasswrod \033[1;32m:\033[1;0m ")
#login
		client.login(email=e,password=p)
		er=True
	except:
			er=False
			i=input("\n\033[1;32m# \033[1;31maccount is invalid!\n\n\033[1;32m# \033[1;33mcontinue? \033[1;32my\033[1;33m/\033[1;32mn \033[1;33m: \033[1;0m")
			if i =='n' or i =='N' or i =='no' or i =='No':
				os._exit(1)
				
#get transactionId				
tId=client.get_wallet_history(start=0,size=1).transanctionId

#chat url
cht=input("\n\n\033[1;32m#\033[1;33m Give Me The Chat url\033[1;32m : \033[1;0m")
cht=client.get_from_code(cht)
comId=cht.path[1:cht.path.index("/")]

#community join
SUB=aminofix.SubClient(comId=comId,profile=client.profile)

#set chat variable 
cht=cht.objectId

#print the transactionId
print("\n\n\033[1;32m# \033[1;33mThe TransactionId \033[1;32 : \033[1;0m"+tId.pop())

#pick the transactionId
tran=input("\n\n\033[1;32m# \033[1;33mGive Me The TransactionId :\033[1;0m ")

#pick 1 coins!
print("\n\npls first pick 1 coins!")
while True:
#its cool right?
	coins=input("\n\033[1;32m# \033[1;33mHow Much Coins ? :\033[1;0m ")
	rt=int(input("\033[1;32m#\033[1;33m How Many Times?\033[1;32m : \033[1;0m"))
	for srlz in range(rt):
		SUB.send_coins(chatId=cht,coins=coins,transactionId=tran)
		print("\n\033[1;36mDone...")
#first is done [: