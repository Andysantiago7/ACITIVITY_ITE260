from 
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




