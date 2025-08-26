import socket
import time

target_host = input("Введите хост (например, www.example.com): ")
ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]

print(f"Сканирую {target_host}...\n")
time.sleep(2)

for port in ports:
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    answer = sck.connect_ex((target_host, port))

    if answer == 0:
        print(f"Порт {port} на хосте {target_host} открыт.")
    elif answer == 10061:
        print(f"Порт {port} на хосте {target_host} закрыт.")
    else:
        print(f"Ошибка подключения к {target_host}:{port}. Код ошибки: {answer}")

    sck.close()

print("\nСканирование завершено.")
