# Загружаем необходимые библиотеки
import simplecrypt
import os
import sys
import getpass

# Ядро начального меню
def start_menu():
    os.system('clear')
    file_list = os.listdir('../files')
    print('')
    print('\033[1;5;38;5;202m F-cryptex \033[0;0m')
    print('')
    print('\033[38;5;82m Файлы: ', file_list)
    print('\033[0;0m')
    print('\033[38;5;226m "1" --- Зашифровать \033[0;0m')
    print('')
    print('\033[38;5;226m "2" --- Расшифровать \033[0;0m')
    print('')
    print('\033[38;5;226m "3" --- Обновить \033[0;0m')
    print('')
    print('\033[38;5;226m "4" --- Выйти \033[0;0m')
    print('')
    running()

# Ядро запуска программы
def running():
    try:
        doit = input('\033[38;5;51m Выберите действие: \033[0;0m')
    except:
    	os.system('clear')
    	exit()
    if doit == '4':
    	os.system('clear')
    	exit()
    elif doit == '1':
        crypt()
    elif doit == '2':
        decrypt()
    elif doit == '3':
        start_menu()
    else:
        print ('\033[38;5;196m Такой функции нет! Повторите попытку! \033[0;0m')
        running()
    
    
#Ядро процесса шифровки   
def crypt():
    os.chdir('../files')
    try:
    	fp1 = input("\033[38;5;82m Введите имя файла\033[38;5;226m\n '1' --- Для выхода\n '2' --- Вернуться в меню\033[38;5;51m\n Ввод: \033[0;0m")
    except:
    	os.system('clear')
    	exit()
    if fp1 == '1':
        os.system('clear')
        exit()
    elif fp1 == '2':
        os.chdir('../bin')
        start_menu()
    try:
        f1 = open(fp1, 'rb')
    except:
        print ('\033[38;5;196m Файл не найден! Повторите попытку! \033[0;0m')
        crypt()
    
    text = f1.read()
    	
    print("\033[38;5;82m Введите ключ шифрования\033[38;5;226m\n '1'---Для выхода\n '2'---Вернуться в меню\033[0;0m")
    try:
        pas_wr = getpass.getpass("\033[38;5;51m Ввод: \033[0;0m")
    except:
        f1.close()
        os.system('clear')
        exit()
    
    if pas_wr == '1':
        f1.close()
        os.system('clear')
        exit()
    
    elif pas_wr == '2':
        f1.close()        
        os.chdir('../bin')
        start_menu()
    
    elif pas_wr == '':
        print('\033[38;5;196m Ключ не может быть пустым! Повторите попытку! \033[0;0m')
        f1.close()
        crypt()
    
    passkey = pas_wr
    
    print("\033[38;5;226m Подождите! Идет шифровка файла! \033[0;0m")
    cipher = simplecrypt.encrypt(passkey, text)
    print("\033[38;5;82m Файл зашифрован \033[0;0m")
    
    f2 = open('crypt.' + fp1, 'wb')
    f2.write(cipher)
    f1.close()
    f2.close()
    try:
    	del_in = input("\033[38;5;226m '1'---Для удаления исходного файла\n '2'---Для выхода\n 'Enter'---Для продолжения\n\033[38;5;51m Ввод: \033[0;0m")
    except:	
    	os.system('clear')
    	exit()
    if del_in == '1' :
        os.remove(fp1)
        os.chdir('../bin')
        start_menu()
    elif del_in == '2' :
        os.system('clear')
        exit()
    else:
        os.chdir('../bin')
        start_menu()
    	
    	
#Ядро процесса расшифровки
def decrypt():
    os.chdir('../files')
    try:
        fp1 = input("\033[38;5;82m Введите имя зашифрованного файла\n\033[38;5;226m '1'---Для выхода\n '2'---Вернуться в меню\n\033[38;5;51m Ввод: \033[0;0m")
    except:
        os.system('cls')
        exit()
    if fp1 == '1':
        os.system('clear')
        exit()
    elif fp1 == '2':
        os.chdir('../bin')
        start_menu()
    try:
        f1 = open(fp1, 'rb')
    except:
        print ('\033[38;5;196m Файл не найден! Повторите попытку \033[0;0m')
        decrypt()
    text = f1.read()
        
    def in_ke():
        global pas_wr_decr
        try:
            print("\033[38;5;82m Введите ключ шифрования\n\033[38;5;226m '1'---Для выхода\n '2'---Вернуться в меню")
            pas_wr_decr = getpass.getpass("\033[38;5;51m Ввод: \033[0;0m")
        except:
                f1.close()
                os.system('clear')
                exit()
        if pas_wr_decr == '1':
            os.system('clear')
            exit()
        elif pas_wr_decr == '2':
            f1.close()        
            os.chdir('../bin')
            start_menu()
        elif pas_wr_decr == '':
            print('\033[38;5;196m Ключ не может быть пустым! Повторите попытку! \033[0;0m')
            f1.close()
            decrypt()

    in_ke()
    passkey = pas_wr_decr

    print("\033[38;5;226m Подождите! Идет расшифровка файла! \033[0;0m")
    
    try:
        cipher = simplecrypt.decrypt (passkey, text)
    except simplecrypt.DecryptionException:
        print ('\033[38;5;196m Ошибка расшифровки! Повторите попытку \033[0;0m')
        f1.close()
        decrypt()
    
    print("\033[38;5;82m Файл расшифрован! \033[0;0m")
    
    	
    f2 = open('uncrypt.' + fp1, 'wb')
    f2.write(cipher)
    f1.close()
    f2.close()
    try:
        del_in = input("\033[38;5;226m '1'---Для удаления исходных файлов\n '2'---Для выхода\n 'Enter'---Для продолжения\n\033[38;5;51m Ввод: \033[0;0m")
    except:
        os.system('clear')
        exit()
    if del_in == '1' :
        os.remove(fp1)
        os.chdir('../bin')
        start_menu()
            
    elif del_in == '2' :
        os.system('clear')
        exit()
    else:
        os.chdir('../bin')
        start_menu()


# Запуск программы   
start_menu()
