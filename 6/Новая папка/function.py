def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf-8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result
            
def save_data_to_file(name, data_list):
    with open(name, 'w', encoding='utf-8') as datafile:
        for rawdata in data_list:
            datafile.write(','.join(rawdata)+ '\n')
    
    
    
    
    
    
    
    

def print_bus():
    pass
  
def add_bus():
    pass

def search_data():
    return 0

def print_driver():
    return 0

def add_driver():
    return 0
  
def print_route():
    return 0

def add_route():
    return 0
