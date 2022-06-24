from prettyprinter import pprint

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
        print(file_dict[arrange[0]][1])
        for i in file_dict[arrange[1]]:
            file.write(i)
            file.write('\n')


    #pprint(arrange)
pprint(write_file())

