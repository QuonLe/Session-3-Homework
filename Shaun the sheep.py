sheep_size = [5,7,300,90,24,50,75]
Hello = ("Hello, my name is Quon and these are my sheep sizes")

while True:
    choice = int(input("What do you want to know?"))

    def shear_sheep():
        shear = max(sheep_size)
        sheep_size.index(shear)
        no_shear = sheep_size.index(shear)
        sheep_size[no_shear] = 8

    if choice == 1:
        print(Hello)
        print(sheep_size)

    elif choice == 2:
        shear = max(sheep_size)
        print("Now my biggest sheep has size {0} let's shear it".format(shear))

    elif choice == 3:
        shear_sheep()
        print("After shearing, here is my flock")
        print(sheep_size)

    elif choice == 4:
        shear_sheep()
        newsheep_size = [size + 50 for size in sheep_size]
        print("One month has passed, now here is my flock")
        print(newsheep_size)

    elif choice ==5:
        month = int(input("How is your flock after?(month)"))
        for m in range(month):
            sheep_size = [size + 50 for size in sheep_size]
            shear = max(sheep_size)
            print("Month", m + 1)
            print("One month has passed, now here is my flock")
            print(sheep_size)
            shear_sheep()
            print("Now my biggest sheep has size {0} let's shear it".format(shear))
            print("After shearing, here is my flock")
            print(sheep_size)
            print()

    else:
        month = int(input("How is your flock after?(month)"))
        for m in range(month):
            sheep_size = [size + 50 for size in sheep_size]
            shear = max(sheep_size)
        shear_sheep()
        total_size = sum(sheep_size)
        print(total_size)