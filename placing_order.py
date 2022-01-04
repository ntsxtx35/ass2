import os
import add_info
from list_customer_info import list_cus
from list_item_info import list_item_info,list_item

# Create a dictionary of order using the order list
def get_order_dict(order_lst):
    """
    This function is used to create a dictionary of customer order
    :param order_lst: A list of customer order
    :return: A dictionary of customer order
    """
    order_dict = {}
    # Loop through each order in the order list
    for sub_order in order_lst:
        if sub_order[0] in order_dict:
            order_dict[sub_order[0]] += sub_order[1]
        else:
            order_dict[sub_order[0]] = sub_order[1]
    return order_dict


# Calculate total cost for an order
def cal_total_cost(order_dict, store_dict):
    """
    This function is used to calculate the total cost of customer order
    :param order_dict: A dictionary of customer order
    :param store_dict: A dictionary of items in the store
    :return: Total cost of customer order (int)
    """
    total_cost = 0
    # Loop through the order dictionary to calculate the total cost
    for k, v in order_dict.items():
        total_cost += (v * store_dict[k][3])
    return int(total_cost)


def placing_order(store_dict, customer_dict):
    """
    This function is used to place order, calculate total cost and update the data of items and customers
    :param store_dict: A dictionary of items in the store
    :param customer_dict: A dictionary of customer
    :return: final_order(dict), total_cost(int), customer_id(str)
    """
    orders_list = []
    total_cost = 0

    # Ask for user ID
    customer_id = input('Enter your customer ID: ')

    # If the customer id is not in dict, let the customer register
    if customer_id not in customer_dict:
        print('Your ID is not in the database. PLease register')
        add_info.add_customers(customer_dict, customer_id)

    list_item(store_dict)
    # Loop to let the customers to enter the items ID that they want to buy
    while True:
        item_id = input('Enter item ID to order and N to stop: ')
        if item_id == 'N' or item_id == 'n':
            break
        else:
            item_quantity = int(input('Enter quantity: '))
            orders_list.append([item_id, item_quantity])

    # Create the dictionary of order
    orders_dict = get_order_dict(orders_list)

    # Update the store dictionary
    for k, v in orders_dict.items():
        if v <= store_dict[k][1]:
            store_dict[k][1] -= v
        else:
            # Loop to check for the remaining item in the store and ask for valid input again
            while True:
                print(f'Sorry we only have {store_dict[k][1]} items {k} ')
                quantity = int(input('Please input the quantity again: '))
                if quantity <= store_dict[k][1]:
                    store_dict[k][1] -= quantity
                    break
            orders_dict[k] = quantity

        # Update number of orders
        customer_dict[customer_id][3] += 1

        # Update number of total_money
        total_cost = cal_total_cost(orders_dict, store_dict)
        customer_dict[customer_id][1] += total_cost

    return orders_dict, int(total_cost), customer_id


def bill( orders,ls_cus,items, total,cus_id ):
    """
    :param ls_cus: list customer (list)
    :param cus_id: customer id (string)
    :param orders: list product customer order include product id, product price (list)
    :param total: total of money to pay the books (integer)
    :param items: list all item (dictionary)
    :return: none
    """
    os.system("clear")
    list_cus(ls_cus,cus_id)
    [list_item_info(items,key) for key in orders.keys()]
    print("ship: {}\ntotal price: {}".format(int(ls_cus[cus_id][-1]) * 15000, total + int(ls_cus[cus_id][-1]) * 15000))
    discount = 0 if ls_cus[cus_id][2] == "Bronze" else (total * 0.2 if ls_cus[cus_id][2] == "Gold" else total * 0.1)
    print("discount: {}\npay: {}".format(discount, total - discount + int(ls_cus[cus_id][-1]) * 15000))


