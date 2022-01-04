# 1
def list_item(item_dict):
    print('List of all items')
    for item_id, item_list in item_dict.items():
        print(item_id + '\t' + item_list[0])


# 2
def list_item_info(item_dict, item_id):  # only print one items
    print(f'Name: {item_dict[item_id][0]} \nQuantity: {item_dict[item_id][1]} \nGenre: {item_dict[item_id][2]} \n'
          f'Price: {item_dict[item_id][3]} VND')
    print("* " * 10)
