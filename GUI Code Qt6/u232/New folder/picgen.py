import os, shutil, json

def lols(file_path_list, processes):
    print(os.path.isdir(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp'))

    if os.path.isdir(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp'):
        shutil.rmtree(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp')
    os.mkdir(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp')
    for folder in range(processes):
        if os.path.isdir(os.getcwd() + os.sep + 'pic2asciitemp' + os.sep + str(int(folder + 1))):
            shutil.rmtree(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp' + os.sep + str(int(folder + 1)))
        os.mkdir(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp' + os.sep + str(int(folder + 1)))
    
    if len(file_path_list) % 2 == 0:
        files_per_json = int(len(file_path_list) / processes)
        file_iterval = files_per_json
        process_iteration = 1
        mk_json = []
        for file in range(len(file_path_list)):
            mk_json.append(file_path_list[file])
            print(process_iteration, file, file_iterval)
            input(mk_json)
            if file + 1 == file_iterval:
                print('should')
                with open(os.getcwd() + os.sep + 'pic2asciitemp' + os.sep + str(process_iteration) + os.sep + str(process_iteration) + '.json', 'w') as the_json_file:
                    json.dump(mk_json, the_json_file)
                process_iteration += 1
                file_iterval += files_per_json
                mk_json = []

    else:
        files_per_json = int(len(file_path_list) // processes)
        ext_files = int(len(file_path_list) % processes)
        process_iteration = 1
        mk_json = []
        for file in range(int(files_per_json * processes))
#lols(['1', '2', '3', '4', '5', '6', '7', '8'], 8)