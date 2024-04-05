 ### 22.เขียนโปรแกรมเพื่อช่วยร้านอาหารคํานวณราคา โดย Japanese buffet ราคา 1000 บาท 
 ### และ Korean buffet ราคา 1500 บาท ถ้าวันนี้เป็นวันพุธจะได้รับส่วนลด 15% 

buffet = input("Enter your buffet choice: ")
pay = 0
if buffet == "Korean" or buffet == "Japanese":
    day = input("Is to day Wednesday(yes/no): ")
    if buffet == "Korean":
        if day == "yes":
            pay = 1500 - (1500 * 0.15)
        elif day == "no":
            pay = 1500
    elif buffet == "Japanese":
        if day == "yes":
            pay = 1000 - (1000 * 0.15)
        elif day == "no":
            pay = 1000
    print("Your payment is %.2f baht" % pay)
else:
    print("Sorry,there is no %s buffet" % buffet)
