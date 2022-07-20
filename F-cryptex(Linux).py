# Загружаем необходимые библиотеки
import simplecrypt
import os
import sys


# Ядро начального меню
def start_menu():
    os.system('clear')
    file_list = os.listdir('Файлы')
    print('')
    print('\033[1;5;38;5;202m F-cryptex \033[0;0m')
    print('')
    print('\033[38;5;82m Файлы: ',file_list)
    print('\033[0;0m')
    print('\033[38;5;226m "n" --- Зашифровать \033[0;0m')
    print('')
    print('\033[38;5;226m "f" --- Расшифровать \033[0;0m')
    print('')
    print('\033[38;5;226m "q" --- Выйти \033[0;0m')
    print('')
    

# Ядро запуска программы
def running():
    try:
        doit = input('\033[38;5;51m Выберите действие: \033[0;0m')
    except EOFError:
    	os.system('clear')
    	exit()
    if doit == 'q':
    	os.system('clear')
    	exit()
    elif doit == 'n':
        crypt()
    elif doit == 'f':
        decrypt()
    else:
        print ('\033[38;5;196m Такой функции нет! Повторите попытку! \033[0;0m')
        running()
    
    
#Ядро процесса шифровки   
def crypt():
    os.chdir('Файлы')
    
    try:
    	fp1 = input('\033[38;5;51m 1.Введите имя файла\n 2.Введите "q" для выхода\n : \033[0;0m')
    except EOFError:
    	os.system('clear')
    	exit()
    
    if fp1 == 'q':
        os.system('clear')
        exit()

    try:
        f1 = open(fp1, 'rb')
    except IOError:
        print ('\033[38;5;196m Файл не найден! Повторите попытку! \033[0;0m')
        os.chdir('..')
        crypt()
    
    text = f1.read()
    	
    try:
    	pas_wr = input('\033[38;5;51m 1.Введите ключ шифрования\n 2.Введите "q" для выхода\n : \033[0;0m')
    except EOFError:
    	os.system('clear')
    	exit()
    
    if pas_wr == 'q':
        os.system('clear')
        exit()
    
    elif pas_wr == '':
        print('\033[38;5;196m Ключ не может быть пустым! Повторите попытку! \033[0;0m')
        os.chdir('..')
        crypt()
    
    passkey = pas_wr
    
    try:
    	sv_pas = input('\033[38;5;51m 1.Введите "f" для сохранения ключа\n 2.Введите "q" для выхода\n 3.Hажмите "Enter" для продолжения\n : \033[0;0m')
    except EOFError:
    	os.system('cls')
    	exit()
    if sv_pas == 'f':
        fkey = open('key.' + fp1, 'wb')
        text_pas = pas_wr
        key_pas = 'Введите любой ключ шифрования на ваш выбор'
        print('\033[38;5;226m Подождите! Идет сохранение ключа! \033[0;0m')
        crypt_pas = simplecrypt.encrypt(key_pas, text_pas)
        fkey.write(crypt_pas)
        fkey.close()
        print("\033[38;5;82m Ключ сохранен! \033[0;0m")
    elif sv_pas == 'q':
        os.system('clear')
        exit()
    	
    print("\033[38;5;226m Подождите! Идет шифровка файла! \033[0;0m")
    cipher = simplecrypt.encrypt(passkey, text)
    print("\033[38;5;82m Файл зашифрован \033[0;0m")
    
    f2 = open('crypt.' + fp1, 'wb')
    f2.write(cipher)

    try:
    	del_in = input('\033[38;5;51m 1.Введите "d" для удаления исходного файла\n 2.Hажмите "Enter" для выхода\n : \033[0;0m')
    except EOFError:	
    	os.system('clear')
    	exit()
    if del_in == 'd' :
        f1.close()
        os.remove(fp1)

    f1.close()
    f2.close()
    os.system('clear')
    exit()
    	
    	
#Ядро процесса расшифровки
def decrypt():
    os.chdir('Файлы')
    try:
        fp1 = input('\033[38;5;51m 1.Введите имя зашифрованного файла\n 2.Введите"q" для выхода\n : \033[0;0m')
    except EOFError:
        os.system('cls')
        exit()
    if fp1 == 'q':
        os.system('clear')
        exit()
    try:
        f1 = open(fp1, 'rb')
    except IOError:
        print ('\033[38;5;196m Файл не найден! Повторите попытку \033[0;0m')
        os.chdir('..')
        decrypt()
    text = f1.read()
    
    def fi_ke():
        global diag
        try:
            diag = input('\033[38;5;51m 1.Введите имя файла с ключом\n 2.Введите "q" для выхода\n : \033[0;0m')
        except EOFError:
        	os.system('clear')
        	exit()
        if diag == 'q':
            os.system('clear')
            exit()
        try:
            fwk = open(diag, 'rb')
        except IOError:
            print ('\033[38;5;196m Файл не найден! Повторите попытку \033[0;0m')
            os.chdir('..')
            decrypt()
        txt_key = fwk.read()
        alg_key = 'Введите любой ключ шифрования на ваш выбор'
        print("\033[38;5;226m Подождите! Идет расшифровка ключа! \033[0;0m")
        global pas_wr_decr
        try:
            pas_wr_decr = simplecrypt.decrypt(alg_key, txt_key)
        except simplecrypt.DecryptionException:
            print ('\033[38;5;196m Ошибка ключа! Повторите попытку \033[0;0m')
            os.chdir('..')
            decrypt()
        fwk.close()
        
        print("\033[38;5;82m Ключ расшифрован! \033[0;0m")
        
    def in_ke():
        global pas_wr_decr
        try:
            pas_wr_decr = input('\033[38;5;51m 1.Введите ключ шифрования\n 2.Введите "q" для выхода\n : \033[0;0m')
        except EOFError:
            	os.system('clear')
            	exit()
        if pas_wr_decr == 'q':
            os.system('clear')
            exit()
        elif pas_wr_decr == '':
            print('\033[38;5;196m Ключ не может быть пустым! Повторите попытку! \033[0;0m')
            os.chdir('..')
            decrypt()

    
    try:
    	dec_key = input('\033[38;5;51m 1.Введите "f" для файла ключа\n 2.Введите "q" для выхода\n 3.Hажмите "Enter" для ввода ключа\n: \033[0;0m')
    except EOFError:
    	os.system('clear')
    	exit()
    if dec_key == 'f':
        fi_ke()
    elif dec_key == 'q':
        os.system('clear')
        exit()
    else:
        in_ke()

    
    passkey = pas_wr_decr

    print("\033[38;5;226m Подождите! Идет расшифровка файла! \033[0;0m")
    
    try:
        cipher = simplecrypt.decrypt (passkey, text)
    except simplecrypt.DecryptionException:
        print ('\033[38;5;196m Ошибка расшифровки! Повторите попытку \033[0;0m')
        os.chdir('..')
        decrypt()
    
    print("\033[38;5;82m Файл расшифрован! \033[0;0m")
    
    	
    f2 = open('uncrypt.' + fp1, 'wb')
    f2.write(cipher)

    try:
        del_in = input('\033[38;5;51m 1.Введите "d" для удаления исходных файлов\n 2.Hажмите "Enter" для выхода\n : \033[0;0m')
    except EOFError:
        os.system('clear')
        exit()
    if del_in == 'd' :
        try:
            f1.close()
            f2.close()
            os.remove(fp1)
            os.remove(diag)
        except NameError:
            	os.system('clear')
            	exit()
            

    f1.close()
    f2.close()
    os.system('clear')
    exit()


# Запуск программы   
start_menu()
running()
