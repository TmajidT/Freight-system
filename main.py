import drivers
import customers
import managers
import orders

def main():
    print("welcome to this program :)")
    while True:
        user = int(input("Who Are You? enter 1 for customer , 2 for driver , 3 for manager or 9 to exit :"))
        if user == 1:
            customers.customers_panel()
        elif user == 2:
            drivers.driver_panel()
        elif user == 3:
            managers.manager_panel()
        elif user == 9:
            break


    #quick access to the code :) just delete # in a section

    #customers.insert_customer(5,"majid sdf")
    #customers.display_all_customers()

    #drivers.insert_driver(2,"not majid akjjkb")
    #drivers.display_all_drivers()

    #managers.insert_manager(13,"probably majid dfghdfgf57")
    #managers.display_all_managers()

    #orders.insert_order(8,"LED lamps",2,5,"esfahan","tehran",55000,"1403-05-26")
    #orders.display_all_orders()
    #orders.display_order_by_id(8)

    #customers.customers_panel()
    #drivers.driver_panel()
    #managers.manager_panel()

if __name__ == '__main__':
    main()