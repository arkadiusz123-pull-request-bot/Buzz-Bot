
def file_append(file, content):
    if "list" in str(type(content)):
        with open(str(file), mode='a', encoding='utf-8') as myfile:
            for x in content:
                myfile.write(str(x) + "\n")
    else:
        with open(str(file), mode='a', encoding='utf-8') as myfile:
            myfile.write(str(content)+"\n")


def file_overwrite(file, content):
    if "list" in str(type(content)):
        with open(str(file), mode='w', encoding='utf-8') as myfile:
            for x in content:
                myfile.write(str(x) + "\n")
    else:
        with open(str(file), mode='w', encoding='utf-8') as myfile:
            myfile.write(str(content)+"\n")


def error_save(error):
    file_append('saves/error.log', error)


def log(output):
    x = "[Log]: " + str(output).lower()
    print(x)
    file_append('saves/main.log', x)


def file_2_list(file):
    z = []
    x = open(file).readlines()
    for y in x:
        z.append(str(y.replace('\n', '')))
    return z
