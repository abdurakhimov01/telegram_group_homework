from read_data import read_data,json

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    data=json.loads(data)
    o=[]
    for i in data["messages"]:
        if "from" in i:
            o.append(i["from_id"])
    return o
print(find_number_of_messages(read_data("data/result.json")))