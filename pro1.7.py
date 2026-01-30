def display_menu():
    print("\n--- List Operations Menu ---")
    print("1. Add element")
    print("2. Remove element")
    print("3. Display list")
    print("4. Search for an element")
    print("5. Sort the list")
    print("6. Reverse the list")
    print("7. Exit")

def list_operations():
    my_list = []
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            item = input("Enter the element to add: ")
            my_list.append(item)
            print(f"'{item}' added to the list.")

        elif choice == '2':
            item = input("Enter the element to remove: ")
            if item in my_list:
                my_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print("Error: Element not found.")

        elif choice == '3':
            print("Current List:", my_list)

        elif choice == '4':
            item = input("Enter element to search: ")
            if item in my_list:
                index = my_list.index(item)
                print(f"'{item}' found at index {index}.")
            else:
                print("Element not found.")

        elif choice == '5':
            my_list.sort()
            print("List sorted successfully.")

        elif choice == '6':
            my_list.reverse()
            print("List reversed.")

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    list_operations()
