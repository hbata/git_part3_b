import os
from test2 import get_files

def list_files(curr_dir):
    all_files = get_giles(curr_dir)
    
    for m_file in all_files():
        print(m_file)



if __name__ == '__main__':
    curr_dir = os.getcwd()
    list_files(curr_dir)
