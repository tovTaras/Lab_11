import re
from datetime import datetime
import zipfile


def main():
    zip_ref = zipfile.ZipFile("access.log.zip")
    zip_ref.extractall()
    zip_ref.close()
    file_to_read = open("access.log.txt")
    lines = file_to_read.readlines()

    pattern = r'((\S+)\s+[-]+\s+[-]+\s+[\[](\S+)\s\S+]\s["](GET\s\S+style.css\s\S+)["]\s([2][0][0]).+)'
    #  groups:
    # 1 - Match
    # 2 - Scripts
    # 3 - datetime
    # 4 - request
    # 5 - statusCode

    date_start = datetime.strptime('22/Mar/2009:07:40:06', '%d/%b/%Y:%H:%M:%S')
    date_end = datetime.strptime('30/Mar/2009:13:43:28', '%d/%b/%Y:%H:%M:%S')
    my_list = list()

    for line in lines:
        x = re.match(pattern, line)
        if x:
            if date_start < datetime.strptime(x.group(3), '%d/%b/%Y:%H:%M:%S') < date_end:
                my_list.append(x)
            elif datetime.strptime(x.group(3), '%d/%b/%Y:%H:%M:%S') > date_end:
                break
    for i in my_list:
        print(i.group(1))
    print(len(my_list))


if __name__ == "__main__":
    main()
