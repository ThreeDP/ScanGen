from manageFiles import create_table, insert_data
from compress import compress

if __name__ == '__main__':
    
    name_index = 0
    table = create_table()

    while name_index < len(table):
        name_index = insert_data(name_index, table)

    compress('./')