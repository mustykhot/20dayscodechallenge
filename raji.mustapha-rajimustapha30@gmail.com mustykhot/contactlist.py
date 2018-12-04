print('WELCOME TO YOUR CONTACT LIST')
l=[]
def new_function():  
    while True:
          s=input('enter continue to proceed or stop to stop')
          if s=='continue':
             z=input('enter the contact')
             w=input('enter the name')
             l.append(w+":"+z)
             continue
          elif s=='stop':break
def  search():
    p=input('enter d name you want to search: ')
    for i in l:
      if p in i:
        print(i)
      else:
        print('not found')
    

def start():
    print ("Hi ")
    while True:
        print ("To make new contacts type in 'New' \nTo check current contacts type in 'Contacts'\n to search for contacts type search")
               
        print( "Go to: ")
        choose = (input()).lower()
        if choose == "new":
            new_function()
        elif choose == "contacts":
            print (l)
        elif choose == "search":
              search() 
start()
