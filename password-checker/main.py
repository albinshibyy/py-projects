import os

def main():
    while True:
        print("PASSWORD STRENGTH CHECKER MAIN FILE")
        print("--------------------")

        print("--------------------")
        print("1) simple = 1 \n 2) advanced = 2")
        whii = input("Which strength test: (sinple / advanced)")
        if whii == "1":
          # Execute file1
          os.system("python simple.py")
        elif whii == "2":
          os.system("python adva.py")
        else:
            print("wrong choice")
        print("----------------")
        checkk = input("Do you want to continue in main file: ")
        if checkk  in ("n","no","exit","N","NO","No"):
            print("Program exiting")
            break
        else:
            continue



if __name__ == "__main__":
    main()
