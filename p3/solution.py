
def compute_average(input_file):
    try:
        with open(input_file, 'r') as f:
            numbers_list = [line.strip() for line in f]
        print(input_file, ":")
        for i in range(len(numbers_list)):
            numbers_list[i] = int(numbers_list[i])
            print(numbers_list[i])
        result = int(sum(numbers_list) / len(numbers_list))
        print("Output: ", result)
    except (ValueError,IOError) as e:
        print('Could not compute average.')
        print(str(e))

compute_average('input.txt')
