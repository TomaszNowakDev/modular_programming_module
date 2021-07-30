def get_from_file(file):
    connection = open(file)
    lines = connection.readlines()
    connection.close()
    log = []
    pas = []
    for i in range(len(lines)):
        split_line = lines[i].split()
        log.append(split_line[0])
        pas.append(split_line[1])
    return log, pas


def log_in(log, pas, logs, pwds):
    if log in logs:
        x = logs.index(log)
        if pas == pwds[x]:
            print(f'Welcome {log}!')
        else:
            print('Wrong password')
    else:
        print("Wrong login or password.")


def main():
    logins, passwords = get_from_file("login_details.txt")
    login = input('Login ==> ')
    password = input('Password ==> ')
    log_in(login, password, logins, passwords)


if __name__ == '__main__':
    main()
