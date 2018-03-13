import os


def print_data(input_path):
    if os.path.exists(input_path):
        for (root, directories, files) in os.walk(input_path):
            for name in files:
                print(os.path.join(root, name))
            for name in directories:
                print(os.path.join(root, name))
    else:
        print("Could not find path")

print_data("E:\Frida\Frida\stick")
