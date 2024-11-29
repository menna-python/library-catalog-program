import os
library_catalog={}
def clear_terminal():
  os.system("cls" if os.name=="nt" else "clear")
def add_books():
  while True:
    clear_terminal()
    isbn=input("Please enter book ISBN: ")
    title=input("Please enter book title: ")
    author=input("Please enter the name of the book author: ")
    library_catalog[isbn]={"Title":title,"Author":author,"Available":True}
    print(f"Book {title} by {author} has added to the library with ISBN {isbn}")
    choice=input("Do you want to add more books?(Y/N)").lower()
    if choice!="y":
      break
def check_out():
  while True:
    clear_terminal()
    isbn=input("Please enter the book ISBN you wish to check out: ")
    if isbn in library_catalog:
      if library_catalog[isbn]["Available"]:
        library_catalog[isbn]["Available"]=False
        print(f"Book with ISBN {isbn} has checked out successfully")
      else:
        print(f"Book with ISBN {isbn} had been checked out by someone")
    else:
      print("This book isn't found in the library")
    choice=input("Do you want to check out more books?(Y/N)").lower()
    if choice!="y":
      break
def check_in():
  while True:
    clear_terminal()
    isbn=input("Please enter the book ISBN you wish to check in: ")
    if isbn in library_catalog:
      if not library_catalog[isbn]["Available"]:
        library_catalog[isbn]["Available"]=True
        print(f"Book with ISBN {isbn} has checked in successfully")
      else:
        print(f"Book with ISBN {isbn} is already present in the library")
    else:
      print("This book isn't found in the library")
    choice=input("Do you want to check in more books?(Y/N)").lower()
    if choice!="y":
      break
def listing_books():
    clear_terminal()
    print("\n Library catalog includes")
    for isbn in library_catalog:
      book_info=library_catalog[isbn]
      print(f"ISBN:{isbn},Title:{book_info['Title']},Author:{book_info['Author']},Available:{book_info['Available']}")
while True:
  print("                         **********Menu**********")
  print("1)Add a book")
  print("2)Check-out a book")
  print("3)Check-in a book")
  print("4)List books")
  print("5)Exit")
  choice=input("Please choose a number from 1 to 5: ")
  if choice=="1":
    add_books()
  elif choice=="2":
    check_out()
  elif choice=="3":
    check_in()
  elif choice=="4":
    listing_books()
  elif choice=="5":
    print("Exiting.....")
    break
  else:
    print("Please choose a valid choice from 1 to 5")
    
      
    
   
    
      
    
       
    
      
        
      
    
    
  