melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00


def underpaid(filename):
    payment_data = open(filename)

    for line in payment_data:
        order = line.rstrip().split('|')

        fname = order[1].split(' ')[0]
        qty, amt_paid = float(order[2]), float(order[3])
    
        amt_expected = qty * melon_cost
       
        if amt_expected != amt_paid:
            print(f"{fname} paid ${amt_paid:.2f}, expected ${amt_expected:.2f}")

            if amt_expected > amt_paid:
                print(f"Underpaid by ${amt_expected - amt_paid:.2f}")
            elif amt_expected < amt_paid:
                print(f"Overpaid by ${amt_paid - amt_expected:.2f}")

underpaid("customer-orders.txt")
