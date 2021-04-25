import time

def start():
  print("I am waiting.")
  inp = input()
  if inp == "hello":
    print("Hello my name is Bob")
    start()
  elif inp == "Hello":
    print("Hello my name is Bob")
    start()
  elif inp == "HELLO":
    print("Hello my name is Bob")
    start()
  elif inp == "hi":
    print("Hello my name is Bob")
    start()
  elif inp == "Hi":
    print("Hello my name is Bob")
    start()
  elif inp == "HI":
    print("Hello my name is Bob")
    start()
  elif inp == "open":
    print("Enter URL and try again")
    start()
  elif inp == "Open":
    print("Enter URL and try again")
    start()
  else:
    print("Sorry, unknown command")
    start()
    
    
    
    
    
    
    
    
    
start()
