import os
clear = lambda: os.system('cls')

money = 500
item={"Diaomond": 100, "Sword":30, "Armor":15} 
print("""                     
            OO
            ()
            )(
         o======o
            ||  
   ===Iron Smith Shop===
            ||
            ||
        888888888
      8888888888888
      8888888888888
,,;,,;;"Y888888Y",,,,,,,;;,;    

                             """)

def Diskon(x,y):
 if x >= 150:
    if y == "1":#Premium 
        return (x - (x * (50/100)))

    elif y == "2":#Gold
        return (x - (x * (30/100)))

    elif y =="3":#Silver
        return x - (x * (10/100))   

for item_name in item:
    print("-----------------------------")
    print("Uang anda adalah " + str(money))
    print("Anda akan membeli " + item_name + ' dengan harga ' + str(item[item_name]))

    input_count=input("Mau berapa " + item_name + " ?: ")

    total_price=item[item_name]*int(input_count)

    if total_price >= 150:
        clear()
        print("===Pembelian " + item_name + "===")
        print("UwU ================== UwU")
        print("Anda Mendapatkan Diskon")
        print("Karena pembelian lebih dari 150")
        print("UwU ================== UwU")

        y=input('''Pilih member:
1.Premium
2.Gold
3.Silver
ketik jenis member : ''')

        money=money-Diskon(total_price,y)
        print("anda membeli " + input_count + ' ' + item_name)
        
        if money == 0:
            clear()
            print("dompet anda kosong")
            break

    elif money >= total_price:
        print("anda membeli " + input_count + ' ' + item_name)
        money=money-total_price
    elif money == 0:
        clear()
        print("dompet anda kosong")
        break
    else:
        print("Uang anda tidak cukup")
        print("Anda tidak dapat membeli " + item_name + " sebanyak itu")


print("/////////////////////////////")
print("===Sisa Uang anda adalah " + str(money) + "===")
print("/////////////////////////////")



 