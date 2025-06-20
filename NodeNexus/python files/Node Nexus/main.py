from currency import Dollar
from bst import BST
import random

def printToBoth(message, file = None):
    print(message)

    if file:
        file.write(message + "\n")

def getValidCurrencyInput():
    while True:
        try:
            amount_str = input("Please enter your currency amount (E.G., 12.34): ").strip()

            if not amount_str:
                return None
            
            amount = float(amount_str)
            if amount < 0:
                print("Your currency amount cannot be a negative number. Please try again.")
                continue

            return Dollar(amount)
        
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            continue

def interactiveMenu(bst, output_file):
    while True:
        print("\n" + "="*35)
        print("BST Interactive Menu")
        print("="*35)
        print("1.) Add Currency")
        print("2.) Search Currency")
        print("3.) Delete Currency")
        print("4.) Print Currency")
        print("5.) Exit The Program")

        choice = input("\nEnter your choice please (1-5): ").strip()

        if choice == "1":
            printToBoth("\n=== Add Currency ===", output_file)
            currency = getValidCurrencyInput()

            if currency is None:
                printToBoth("The Operation is cancelled.", output_file)
                continue

            if bst.insert(currency):
                message = f"Currency was successfully added: {currency}"
                printToBoth(message, output_file)
            
            else:
                message = f"The duplicate currency was ignored: {currency}"
        
        elif choice == "2":
            printToBoth("\n=== Search Currency ===", output_file)
            currency = getValidCurrencyInput()

            if currency is None:
                printToBoth("The Operation is cancelled.", output_file)
                continue

            if bst.search(currency):
                message = f"Currency was successfully found: {currency}"
                printToBoth(message, output_file)

            else:
                message = f"The currency was not found: {currency}"
                printToBoth(message, output_file)

        elif choice == "3":
            printToBoth("\n=== Delete Currency ===", output_file)
            currency = getValidCurrencyInput()

            if currency is None:
                printToBoth("The Operation is cancelled.", output_file)
                continue

            if bst.delete(currency):
                message = f"Currency was successfully deleted: {currency}"
                printToBoth(message, output_file)
            else:
                message = f"The currency was not found: {currency}"
                printToBoth(message, output_file)

        elif choice == "4":
            printToBoth("\n=== All Traversals ===", output_file)
            bst.printTree(output_file)

        elif choice == "5":
            printToBoth("\n=== Final Tree State ===", output_file)
            bst.printTree(output_file)
            printToBoth("\nThank you for using my BST/AVL Demo!", output_file)
            break

        else:
            print("That is an invalid choice. Please enter 1-5.")

def main():

    try:
        output_file = open("output.txt", "w", encoding="utf-8")
        printToBoth("="*35, output_file)
        printToBoth("NodeNexus - BST/AVL Tree Demo", output_file)
        printToBoth("Author: Enrico Jeroense", output_file)
        printToBoth("="*35, output_file)

        bst = BST()

        seed_values = [round(random.uniform(0, 500), 2) for _ in range(20)]

        printToBoth("\n=== Seeding The Tree With Initial Data ===", output_file)

        for value in seed_values:
            currency = Dollar(value)
            if bst.insert(currency):
                message = f"Inserted currency: {currency}"
                printToBoth(message, output_file)

            else:
                message = f"Duplicate currency found. Ignored: {currency}"
                printToBoth(message, output_file)

        printToBoth(f"\nTotal nodes in Tree: {bst.count()}", output_file)
        printToBoth("\n=== Initial Traversals(After Seeding) ===", output_file)
        bst.printASCIITree(output_file)

        interactiveMenu(bst, output_file)

    except IOError as e:
        print(f"There was a error opening the output file: {e}")
        return
    
    finally:
        if "output_file" in locals():
            output_file.close()
            print("Output is being written into output.txt")

if __name__ == "__main__":
    main()
