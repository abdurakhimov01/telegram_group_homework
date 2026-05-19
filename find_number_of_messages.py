from read_data import read_datas,json

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    k=json.loads(data)
    f=k["messages"]
    return len(f)
print(find_number_of_messages(read_datas("data/result.json")))