from servicios import (register_product, consult_book,update_product,delete_product, register_sales, top_3_sales, sales_author,mostrar_ventas, inventory)


def main():

    while True:
        print("----SISTEMA------")
        print("____________________")
        print("1. Add New Book")
        print("2. Search Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Register Sale")
        print("6. Report: Top 3 of Sale")
        print("7. Report: Sale by Author")
        print ("8. Report: View sales")
        print("0. Salir")
        print("_____________________")

        opcion = input("Select one of the following options: ")
        
        if opcion == "1":
            register_product()
            
            

        elif opcion == "2":
            title = input("Write the title of the book: ")
            libro = consult_book(inventory, title)
            print(libro if libro else "Not Found")

        elif opcion == "3":
            title = input("book title to update: ")
            new_author = input("Enter New Author: ")
            new_category = input("Enter New Category: ")
            new_price = input("Enter New Price: ")
            new_stock = input("Enter New Stock: ")
            update_product(inventory,title,new_author,new_category,new_price, new_stock)
        elif opcion == "4":
            title = input("Book title for delete: ")
            delete_product(inventory, title)

        elif opcion == "5":
            register_sales(inventory)

        elif opcion == "6":
            top_3_sales()

        elif opcion == "7":
            sales_author()
            
        elif opcion == "8":
            mostrar_ventas()    

        elif opcion == "0":
             print("Exit, Thanks")
             break
             
        else: print("Invalid option, please correct")

main()