
clothes = ['T-shirt','Sweater']

print("Anh muon lam gi?")
print("1: Them mat hang")
print("2: Xem danh sach")
print("3: Thay doi mat hang")
print("4: Xoa mat hang")
print("5: Thoat")

loop_continue = True
while loop_continue:
    choice = int(input(">>"))

    def print_its() :
        cloth_no = 1
        for cloth in clothes:
            print("No", end="")
            print(cloth_no, end=". ")
            print(cloth)
            cloth_no += 1
    if choice == 1:
        new_clothes = input("Moi anh them mat hang:")
        clothes.append(new_clothes)

    elif choice == 2:
        print("Moi anh xem danh sach")
        print_its()

    elif choice == 3:
        position = int(input("Anh muon sua mat hang nao? No:"))-1
        new_cloth = input("Anh muon sua thanh mat hang gi?")
        clothes[position]= new_cloth
        print("Danh sach moi:", clothes)
        print_its()

    elif choice ==4:
        vi_tri = int(input("Anh muon xoa mat hang nao? No:"))-1
        clothes.pop (vi_tri)
        print_its()

    elif choice ==5:
        print("Tam biet va hen gap lai")
        loop_continue = False
    else:
        print("Ahihi sai cmnr")
        print("1: Them mat hang")
        print("2: Xem danh sach")
        print("3: Thay doi mat hang")
        print("4: Xoa mat hang")
        print("5: Thoat")
