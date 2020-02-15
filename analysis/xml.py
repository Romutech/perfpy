import os

def launch_analysis(data_file):
    directory = os.path.dirname(__file__) # we get the right path.
    path_to_file = os.path.join(os.path.dirname(directory), "data", data_file) # with this path, we go inside the folder `data` and get the file.

    with open(path_to_file,"r") as f:
        preview = f.readline()

    print("oh oh Yeah! We managed to read the file. Here is a preview: {}".format(preview))


if __name__ == "__main__":
    launch_analysis('SyceronBrut.xml')