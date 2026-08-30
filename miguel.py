def print_complete_receipt(Name,Contact,Address,Products,Subtotal,Total,Discount):
    print_receipt_customer_info_part(Name,Contact,Address)
    for product in Products:
        print_receipt_products_part(product["Name"],product["Price"],product["Quantity"])
    print_receipt_pricing_part(Subtotal,Total,Discount)

def print_receipt_customer_info_part(Name,Contact,Address):
    print("        ", "OFFICIAL STORE RECEIPT" ,"    ")
    print("========================================")
    print("Customer Name:" , Name)
    print("Contact Number:" , Contact)
    print("Address:" , Address)

def print_receipt_products_part(Product,Price,Quantity):
    print("----------------------------------------")
    print(  "PRODUCT" , "       " ,    "PRICE" ,  "               "       "QTY")
    print("----------------------------------------")
    print( Product ,"          ",    Price , "              ",    Quantity )
    print("----------------------------------------")

def print_receipt_pricing_part(Subtotal,Total,Discount):
    print("Subtotal:" , Subtotal)
    print("Discounted:" , Discount)
    print("----------------------------------------")
    print("Total of purchased:" ,Total)
    print("========================================")
    print("       ", "THANK YOU FOR PURCHASING!" "     ")
    print("          ", "PLEASE COME AGAIN!!")
    print()

def get_discount():
    Discount = int(input("Enter Discount(%): "))
    return Discount

def compute_subtotal(amount1 , amount2, amount3):
    Subtotal = amount1 + amount2 + amount3 
    return Subtotal

def compute_amount(Price,Quantity):
    amount = float(Price * Quantity)
    return amount

def compute_total(Subtotal, Discount):
    return  Subtotal - Discount

def get_info_for_product():
    Product  = input("Product name: ")
    Price = float(input("Enter Price: "))
    Quantity = int(input("Enter Quantity: "))
    Product_total = compute_amount(Price,Quantity)
    product = {"Name": Product,
               "Price": Price,
               "Quantity": Quantity,
               "Product_total": Product_total}
    return product


def get_customer():
   Name = input("Enter Customer Name: ")
   Contact = input("Enter Contact Number: ")
   Address = input("Enter Customer Address: ")
   Customer = {
           "Name": Name,
           "Address": Address,
           "Contact":Contact,
           }
   return Customer



def main():
    Customer = get_customer()

    P1 = get_info_for_product()
    P2 = get_info_for_product()
    P3 = get_info_for_product()

    products = [P1, P2, P3]

    subtotal = compute_subtotal(P1["Product_total"], P2["Product_total"], P3["Product_total"])
    discount = get_discount()
    total = compute_total(subtotal,discount)

    print_complete_receipt(Customer["Name"],Customer["Contact"],Customer["Address"],products,subtotal,total,discount)

main()






