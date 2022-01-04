def list_cus(customers, customer_id):
    """
    :param customers: dictionary of customer
    :param customer_id: the id of the customer (integer)
    :return: none
    """
    # print customer information
    print("Customer id: {}".format(customer_id))
    print("Customer name: {}".format(customers[str(customer_id)][0]))
    print("Total accumulated budget: {}".format(customers[str(customer_id)][1]))
    print("Promotion: {}".format(customers[str(customer_id)][2]))
    print("Total bills: {}".format(customers[str(customer_id)][3]))
    print("Address: {}".format(customers[str(customer_id)][4]))
