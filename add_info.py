def add_items(item_dict):
    """
    This function is used to add items info to the database
    :param item_dict: A dictionary of items in the store
    """
    infos = ['Name', 'Quantity', 'Genre', 'Price']
    detail = []
    key = input('Enter ID: ')
    # Increase the quantity if ID already in the dictionary
    if key in item_dict:
        quantity = int(input('Enter the quantity: '))
        item_dict[key][1] += quantity
    # Add item to dict if key isn't in the dictionary
    else:
        for info in infos:
            detail.append(input(f'{info}: '))
        item_dict[key] = [detail[i] for i in range(len(detail))]
        item_dict[key][1] = int(item_dict[key][1])


def add_customers(customer_dict, customer_id):
    """
    This function is used to add customer infos to the database
    :param customer_dict: A dictionary of customers
    :param customer_id: A customer ID
    :return:
    """
    key = customer_id
    # Asking for user to input their information
    name = input('Enter name: ')
    address = input('Enter 1 for (in HCM city) and 2 for (outside HCM city): ')
    total_money = 0
    total_order = 0
    rank = 'Bronze'
    customer_dict[key] = [name, total_money, rank, total_order, address]
