def read_files():
    files_list = ['1.txt', '2.txt', '3.txt']
    file_dict = {}
    for item in files_list:
        text = [item]
        with open(item, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                text.append(line)
            file_dict.update({len(text) - 1:text})
    return file_dict


def write_file():
    file_dict = read_files()
    arrange = sorted(file_dict.keys())
    with open('final.txt', 'w', encoding='utf-8') as file:
        file.write(file_dict[arrange[0]][0])
        file.write('\n')
        file.write(str(arrange[0]))
        file.write('\n')
        for i in file_dict[arrange[0]]:
            if file_dict[arrange[0]].index(i) == 0:
                continue
            else:
                file.write(i)
        file.write('\n')
        file.write(file_dict[arrange[1]][0])
        file.write('\n')
        file.write(str(arrange[1]))
        file.write('\n')
        for i in file_dict[arrange[1]]:
            if file_dict[arrange[1]].index(i) == 0:
                continue
            else:
                file.write(i)
        file.write('\n')
        file.write(file_dict[arrange[2]][0])
        file.write('\n')
        file.write(str(arrange[2]))
        file.write('\n')
        for i in file_dict[arrange[2]]:
            if file_dict[arrange[2]].index(i) == 0:
                continue
            else:
                file.write(i)


if __name__ == '__main__':
    write_file()