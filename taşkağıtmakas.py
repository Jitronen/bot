import random

exit= False
user_points = 0
computer_points = 0


while exit == False:
    options = ["TAŞ", "KAĞIT","MAKAS"]
    user_input = input("Seç; TAŞ, KAĞIT, MAKAS ya da ÇIK:")
    computer_input = random.choice(options)
    if user_input == "ÇIK":
        print("Oyun bitti")
        exit=True
    
    if user_input == "TAŞ":
        if computer_input == "TAŞ":
            print("TAŞ girdin")
            print("TAŞ girildi(pc)")
            print("Berabere!")
        elif computer_input == "KAĞIT":
            print("TAŞ girdin")
            print("KAĞIT girildi(pc)")
            print("PC kazandı!")
            computer_points += 1
        elif computer_input == "MAKAS":
            print("TAŞ girdin")
            print("MAKAS girildi(pc)")
            print("Kazandın!")
            user_points += 1        
    
    elif user_input == "KAĞIT":
        if computer_input == "KAĞIT":
            print("KAĞIT girdin")
            print("KAĞIT girildi(pc)")
            print("Berabere!")
       
            print("KAĞIT girdin")
            print("TAŞ girildi(pc)")
            print("Kazandın!")
            user_points += 1
        elif computer_input == "MAKAS":
            print("Kağıt girdin")
            print("Makas girildi(pc)")
            print("PC kazandı!")
            computer_points += 1     
    
    elif user_input == "MAKAS":
        if computer_input == "MAKAS":
            print("MAKAS girdin")
            print("MAKAS girildi(pc)")
            print("Berabere!")
       
            print("MAKAS girdin")
            print("KAĞIT girildi(pc)")
            print("Kazandın!")
            user_points += 1
        elif computer_input == "MAKAS":
            print("MAKAS girdin")
            print("TAŞ girildi(pc)")
            print("PC kazandı!")   
            computer_points += 1 

    elif user_input != "TAŞ" or user_input != "KAĞIT" or user_input != "MAKAS" or user_input != "ÇIK" :
        print("geçersiz")
        