import os, shutil, json

def lols(file_path_list, processes):
    #Check and create temp files
    if os.path.isdir(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp'):
        shutil.rmtree(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp')
    os.mkdir(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp')
    for folder in range(processes):
        if os.path.isdir(os.getcwd() + os.sep + 'pic2asciitemp' + os.sep + str(int(folder + 1))):
            shutil.rmtree(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp' + os.sep + str(int(folder + 1)))
        os.mkdir(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp' + os.sep + str(int(folder + 1)))
    
######################################################
#separate the file_path_list into the processes:
    if len(file_path_list) % processes == 0:
        files_per_json = int(len(file_path_list) / processes)
        file_iterval = files_per_json
        process_iteration = 1
        mk_json = []
        for file in range(len(file_path_list)):
            mk_json.append(file_path_list[file])
            if file + 1 == file_iterval:
                with open(os.getcwd() + os.sep + 'pic2asciitemp' + os.sep + str(process_iteration) + os.sep + 'tmp.json', 'w') as the_json_file:
                    json.dump(mk_json, the_json_file)
                process_iteration += 1
                file_iterval += files_per_json
                mk_json = []

    else:
        files_per_json = int(len(file_path_list) // processes)
        file_interval = files_per_json
        ext_files = int(len(file_path_list) % processes)
        process_iteration = 1
        mk_json = []
        for file in range(int(files_per_json * processes)):
            mk_json.append(file_path_list[file])
            if file + 1 == file_interval:
                with open(os.getcwd() + os.sep + 'pic2asciitemp' + os.sep + str(process_iteration) + os.sep + 'tmp.json', 'w') as the_json_file:
                    json.dump(mk_json, the_json_file)
                process_iteration += 1
                file_interval += files_per_json
                mk_json = []
        with open(os.getcwd() + os.sep + 'pic2asciitemp' + os.sep + str(processes) + os.sep + 'tmp.json', 'r') as the_json_file:
            the_json_file.seek(0)
            mk_json = json.load(the_json_file).copy()
            mk_json += file_path_list[int(-1 * ext_files):]
        with open(os.getcwd() + os.sep + 'pic2asciitemp' + os.sep + str(processes) + os.sep + 'tmp.json', 'w') as the_json_file:
            json.dump(mk_json, the_json_file)