import os

def get_files(curr_dir):
    result = [f for f in os.listdir(curr_dir) if os.path.isfile(os.path.join(curr_dir,f))]
    return result
