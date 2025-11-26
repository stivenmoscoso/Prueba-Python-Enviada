# Registration Module 
inventory = [{'title': 'el principito', 'author': 'Stiven', 'category': 'fabula', 'price': 2000, 'stock': 50,},
             {'title': 'don quijote', 'author': 'Stiven', 'category':'clasico', 'price': 4000, 'stock': 30,},
             {'title': '1983', 'author': 'Carlos', 'category':'novela', 'price' : 1000, 'stock': 20,},
             {'title': 'python', 'author': 'Juan', 'category': 'programacion', 'price': 2500, 'stock': 100,},
             {'title': 'poemas', 'author': 'Stiven', 'category': 'fabula','price' :800, 'stock': 15,},
             ]

            


def register_product(title, author, category,price, stock):

    title = input("Book Title: ")
    author = input("Author Name: ")
    category = input("Book Category: ")
    price = input("Book Price: ")
    stock = input("Stock:  ")
    register_product(title, author, category, price, stock)

    inventory.append(book)


    book = {
        'title': title,
        'author': author,
        'category': category,
        'price': price,
        'stock': stock
    }

    
    print (f"Book: '{title}' registered successfully.")

# funtion to consult books
def consult_book(inventory, name_search):
    for book in inventory:
     if book["title"] == name_search.lower():
        return book
    return None
# function to update book information
    
def update_product(inventory, title, new_author, new_category, new_price, new_stock):

    book = consult_book(inventory,title)
    if book is None:
        print("Book not found.")
        return
    else:
        if new_author != "":
            book['author'] = new_author
        if new_category != "":
            book['category'] = new_category
        if new_stock != "":
           try:
             book['stock'] = int(new_stock)
           except ValueError:
               print("Stock invalid, Not Update")
        if new_price != "":
           try:
             book['price'] = float(new_price)
           except ValueError:
               print("Price invalid, Not Update")
        print(f"{title} Update successfully")
        

# function to delete a book from inventory
def delete_product(inventory, title):
    book = consult_book(inventory, title)
    if book == None:
        print("Book not found.")
        return
    else:
        inventory.remove(book)
        print(f"Book '{title}' deleted successfully.")


# Sales Module
sales = []
def register_sales(inventory):
    print("-----Register Sale-----")
    customer_name = input("Enter Customer Name: ")
    type_client = input("Enter Type of Client (Regular o VIP): ")
    book_title_sale = input("Enter The Book Title sold: ").lower()

    book = consult_book(inventory, book_title_sale)

    if book is None:
        print("Book not found in inventory.")
        return
    quantity = int(input("Enter Quantity sold: "))   

    if quantity > book['stock']:
        print("Insufficient stock for the sale.")
        return 
    
    #time of sale
    from datetime import datetime
    time = datetime.now().strftime("%Y-%m-%d %H:%M")

    #descount 
    descuento = float(input("Ingrese el Descuento aplicado:"))
    #final price
    final_price = (book['price'] * quantity) - descuento

#register sale
    sale = {
        'customer_name': customer_name,
        'type_client': type_client,
        'book_title_sale': book_title_sale,
        'quantity': quantity,
        'time': time,
        'descuento': descuento,
        'final_price': final_price
    }
    sales.append(sale)


    #update stock
    book['stock'] -= quantity

    print(f"Sale registered successfully for '{book_title_sale}'.") 
    print(f"Final Price after discount: ${final_price}")

def mostrar_ventas():
    if not sales:
        print("No hay ventas registradas.")
        return  
    print("\n----- LISTA DE VENTAS -----")
    for venta in sales:
        print(f"""
Cliente: {venta['customer_name']}
Tipo de Cliente: {venta['type_client']}
Libro vendido: {venta['book_title_sale']}
Cantidad: {venta['quantity']}
Fecha y hora: {venta['time']}
Descuento: {venta['descuento']}
Precio final: {venta['final_price']}
------------------------------""")
    


from collections import defaultdict

#top 3 of sales
def top_3_sales():
    sales_count = defaultdict(int)

    for sale in sales:
        sales_count[sale['book_title_sale']] += sale['quantity']
    
    top_sales = sorted(sales_count.items(), key=lambda x: x[1], reverse=True)[:3]
    print("---The 3 best-selling books---")
    for sale, quantity in top_sales: 
        print(f"Book:{sale}, Quantity: {quantity} unidades vendidas")


#sales report for Author
def sales_author():
    if  not sales:
        print("No hay ventas registradas")
        return
    
    sold_authors = defaultdict(int) 

    for sale in sales:
     book = consult_book(inventory, sale['book_title_sale'])
     if book:
         sold_authors[book['author']] += sale['quantity']
    print("---Ventas por Autor---")

    for author, quantity in sold_authors.items():
        print(f"Autor {author}, Cantidad Vendida {quantity} units sold")
    
  





 

 