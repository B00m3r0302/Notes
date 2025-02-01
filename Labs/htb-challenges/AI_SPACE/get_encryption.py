def read_file_header(filename, length=1028):
    with open(filename, 'rb') as f:
        return f.read(length)
    return

filename = 'distance_matrix.npy'
header = read_file_header(filename)
print(header)