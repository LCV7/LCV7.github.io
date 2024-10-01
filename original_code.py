import math
import random
import time
import os
import shutil
import smtplib, ssl
from colorama import Fore, Back, Style

def generate_user_profile_html(user_data, template_path='profile_template.html', output_dir='profiles'):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Leer la plantilla HTML
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template = template_file.read()

    # Reemplazar los marcadores de posición con los datos del usuario
    for key, value in user_data.items():
        placeholder = f"{{{{{key}}}}}"
        template = template.replace(placeholder, value)

    # Nombre del archivo basado en el username
    filename = f"{user_data['user_name']}.html"
    file_path = os.path.join(output_dir, filename)

    # Escribir el archivo HTML
    with open(file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(template)
    
    print(f"Perfil generado: {file_path}")
    

original_file = 'C:\\Users\\Reiny\\Desktop\\Cuentas_o\\file.txt' #File.
storage_file = 'C:\\Users\\Reiny\\Desktop\\Cuentas_o\\Storage' #Folder.

port = 465 # For SSL
sender = "b132vp@gmail.com"
g_password = "skrp ytah fjmb qqme"

subject = "Usted ha ganado 1 millon de dolares"
body = "Presione el link que se adjuntara para poder obtener su dinero"
text = f"Subject: {subject}\n\n{body}"

while True:
   try:
      os.system('cls')
      print("\nEnter [1] to Sign in")
      print("Enter [2] to create an account")
      menu = int(input("[1]|[2]: ")) #Input selection.
      if menu == 1 or menu == 2:
         break
      else:
         continue
   except ValueError:
      os.system('cls')
      print("Enter a valid number.")

      time.sleep(1.5)

match menu: #Menu selection.
   case 1: #Sign In.
      os.system('cls')
      print("\nYou are about to Sign In!!\n")

      time.sleep(2) #Waits 2 seconds.

      while True:
         os.system('cls')
         user_name_file = str(input("Enter your Username: ")) #Ask for the Username saved in a file.
         user_name_extension = user_name_file + ".txt" #Username with the extension file.
         user_name_path = os.path.join(storage_file, user_name_extension) #File path (username) it's added to original directory (folder).

         if os.path.exists(user_name_path): #Checks if the path exist.
            break #If the path does exist, then it will exit the loop.
         else: #If it doesn't, it's gonna ask you to write a valid Username.
            os.system('cls')
            print("Enter a valid Username.")

            time.sleep(1.5)

      with open(user_name_path, 'r') as file: #Reads the file with that path/name.
         content = file.readlines() #Because there are multiple lines of information, we need "file.readlines()".

      line_gmail = content[0].strip()
      line_user_name = content[1].strip() 
      line_password = content[2].strip() 
      line_full_name = content[3].strip() 
      line_birthdate = content[4].strip() 
      line_height = content[5].strip() 

      if user_name_file == line_user_name: #Checks if the Username it's the same from the one inside the .txt file.
         while True:
            password = str(input("Enter your password: "))           
            if password == line_password: #Checks if the Password it's the same from the one inside the .txt file.
               break #If the Password is correct (the same from the file) then it will exit the loop.
            else:
               print("\nIncorrect password. Try again.")
         print(f"\nWelcome Back {line_full_name}, A.K.A. '{line_user_name}'")
         print("The current information of your account is...")

         time.sleep(1.5)

         print(f"Gmail: {line_gmail}")
         print(f"Birthdate: {line_birthdate}")
         print(f"Height: {line_height}cm")

         print("Password: " + "*" * len(line_password))
      else:
         print("Username does not match.")
         time.sleep(1.5)

   case 2: #Create an Account.
      os.system('cls')
      print("\nYou are going to create a New Account!!\n")

      time.sleep(2) #Waits 2 seconds.

      shutil.copy(original_file, storage_file) #Copies the file into the folder.

      copied_file = os.path.join(storage_file, os.path.basename(original_file)) #It adds the original file name into the folder path.

      while True:
         os.system('cls')
         new_file_name = input("Enter/Create a new name account: ") #Ask for a name for the new file.

         if new_file_name == "" or new_file_name.isspace():
            os.system('cls')
            print("You aren't allowed to use spaces")
            time.sleep(1.5)
            continue

         extension_file_name = new_file_name + ".txt" #Name with the extension file.

         new_file_path = os.path.join(storage_file, extension_file_name) #New fictional path to the file.

         if not os.path.exists(new_file_path): #Checks if there's already a file/path with the same name.
            break #If it doesn't then it exits the loop.
         else: #Else it's gonna keep asking for a different name.
            os.system('cls')
            print(f"There is already a file/account with the name '{extension_file_name}'. Please try with a different one.")
            time.sleep(1.5)

      os.rename(copied_file, new_file_path) #The copied path it's rename into the fictional path name.
      print(f"File copied and renamed into '{extension_file_name}'")

      while True:
         password = str(input("\nEnter/Create a new password: ")) #Password.

         if password == "" or password.isspace():
            print("You aren't allowed to use spaces")
            time.sleep(1.5)
         else:
            break
            
      #Additional information.
      print("\nYou're almost there, please complete the following requirements.")

      time.sleep(2)

      context = ssl.create_default_context()

      punto_length = 3
      elements_2 = ['.', ' ']

      while True:
         try:
            user_gmail = input("Enter your Gmail acount: ")
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
               server.login(sender, g_password)

               for i in range(punto_length + 1):
                  frame = i % len(elements_2)
                  print(f'\r[{"." * i:<{punto_length}}]', end='')
                  time.sleep(1)

               server.sendmail(sender, user_gmail, text)
               print("\nEmail has been sent!")
            break
         except:
            os.system('cls')
            print("\nInvalid Gmail.")  
            time.sleep(1.5)

      while True:
         try:
            full_name = str(input("Enter your full name: ")) #Full name of the User.
            birth_day = str(int(input("Which day you were born?: ")))
            birth_month = str(int(input("Which month you were born?: ")))
            birth_year = str(int(input("Which year you were born?: ")))

            birth_date = f"{birth_day}/{birth_month}/{birth_year}"

            
            height = float(input("Enter your height (in meters): ")) #Height of the User.
            height = height * 100
            height = str(round(height))
            break
         except:
            os.system('cls')   
            print("Invalid, Try again.")
            time.sleep(1.5)

      with open(new_file_path, 'w') as file: #Open and write into the file.
         file.write(user_gmail + '\n')
         file.write(new_file_name + '\n') #Writes the Username inside the .txt file (this name is also used to name the file that contains it).
         file.write(password + '\n') #Writes the Password inside the .txt file.
         file.write(full_name + '\n') #Writes Fullname inside the .txt file.
         file.write(birth_date + '\n') #Writes Birthdate inside the .txt file.
         file.write(height + '\n') #Writes the Height inside the .txt file.
      print("\nAccount created.\nWe've sent you a message to your Gmail Account.\nGoodbye")
      user_data = {
        'full_name': full_name,
        'user_name': new_file_name,
        'gmail': user_gmail,
        'birth_date': birth_date,
        'height': height
      }
      generate_user_profile_html(user_data)

      
