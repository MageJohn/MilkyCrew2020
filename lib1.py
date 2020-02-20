clean_data = []

with open("f_libraries_of_the_world.txt", "r") as data:
    data = data.readlines()
    for lines in data:
        lines = lines.strip("\n")
        lines = lines.split(" ")
        clean_data.append(lines)

days = int(clean_data[0][2])
lib_sign_up = []
lib_through = []
for i in range(2, len(clean_data) - 1 ,2):
    lib_sign_up.append(int(clean_data[i][1]))
    books = int(clean_data[i][0])
    through = int(clean_data[i][2])
    lib_through.append(int(books/through))

lib_useful = []
for i in range(len(lib_sign_up)):
    days_useful = days - lib_sign_up[i]
    try:
        lib_useful.append((days_useful / lib_through[i]) * 100)
    except:
        lib_useful.append(0)

order_send = []
for i in range(len(lib_useful)):
    high = lib_useful.index(max(lib_useful))
    order_send.append(high)
    del lib_useful[high]

lib_able_to_sign_up = []
time_left = days
count = 0
while time_left >= 0:
    lib = order_send[count]
    lib_able_to_sign_up.append(lib)
    time_left -= lib_sign_up[lib]
    count += 1
print(lib_sign_up[243])
print(lib_able_to_sign_up)

    
