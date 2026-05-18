from read_data import read_data,json

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    data=json.loads(data)
    o=[]
    for i in data["messages"]:
        if "from" in i:
            o.append(i["from"])
    return o
print(find_all_users_name(read_data("data/result.json")))