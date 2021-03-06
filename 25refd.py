def search_string_in_file(file_name, string_to_search):
    line_number = 0
    list_of_results = []
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                list_of_results.append((line_number, line.rstrip()))
    return list_of_results


count = 0
while count <= 3:
    matched_lines = search_string_in_file('/home/jogubaba/Downloads/servervmname', 'WLN4PADC001')
    print('Total Matched lines : ', len(matched_lines))
    for elem in matched_lines:
        print('Line Number = ', elem[0],': ', elem[1])
    else:
        print("Not in file")
    count += 1
    break
