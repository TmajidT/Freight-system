import drivers
import customers
import managers
import orders

def main():

    #customers.insert_customer(5,"majid sdf")
    #customers.display_all_customers()

    #drivers.insert_driver(2,"not majid akjjkb")
    #drivers.display_all_drivers()

    #managers.insert_manager(13,"probably majid dfghdfgf57")
    #managers.display_all_managers()

    #orders.insert_order(6,5,13,"esfahan","tehran",55000,"1403-05-26")
    #orders.display_all_orders()
    orders.display_order_by_id(6)

if __name__ == '__main__':
    main()