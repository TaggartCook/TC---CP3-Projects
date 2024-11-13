#some exceptions are automatic, 
#zero devision, file not found, value error, type error, index error
class NegativeNumberError(Exception):


while True:
    try:
        num = int(input("tell me a number: "))
    except:
        print("That wasn't a while number")
        continue
    else:
        break

while True:        
    try:
        numTwo = int(input("Tell me another number: "))
        if num <= 0 :
            raise NegativeNumberError("Can't be a negative number")
    except (ValueError, NegativeNumberError): 
        print("U Suck")
        continue
    else:
        try:
            print(f'{str(num)} plus {str(numTwo)} equals {num/numTwo}')
            break
        except ValueError:
            print("That wasn't a whole number")
            continue
        except NegativeNumberError as e:
            print(e)
            again = input("Do you want to go again?(Y?N)")
        if again == "Y":
            continue
        elif again == "N":
            break
        else:
            print("Sorry that wasn't an option")

    finally: