import os
import mysql.connector

username = os.environ.get('MYSQL_DB_USERNAME')
password = os.environ.get('MYSQL_DB_PASSWORD')
database = os.environ.get('MYSQL_DB')

account_system = mysql.connector.connect(
    host = "localhost",
    user = username,
    password = password,
    database = database
)

cursor = account_system.cursor()

def signup():
    username = input("Enter Username: ")
    password = input("Create Password: ")
    confirm_password = input("Confirm Password: ")
    SIGNUP_COMMAND = f"INSERT INTO users (username, userpass) VALUES ('{username}', '{password}');"
    try:
        if (confirm_password == password):
            cursor.execute(SIGNUP_COMMAND)
            # Commit changes to the DB.
            account_system.commit()
            print("Successfully created an account!")
            signout()

    except Exception as e: 
        print("An error has occurred!\nRestarting...\n")
        main()

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    LOGIN_COMMAND = "SELECT username, userpass FROM users WHERE username = (%s)"
    try:
        # MySQL .execute() needs an SQL query and tuple as parameters.
        cursor.execute(LOGIN_COMMAND, (username, ))
        records = cursor.fetchall()
        STORED_USERNAME = records[0][0]
        STORED_PASSWORD = records[0][1]
        if (len(records) and (STORED_PASSWORD==password and STORED_USERNAME==username)): 
            print("Successfully logged in!")
            signout()

        else: 
            print("Incorrect username or password!")
            tryagain = input("Try again (Y/N)?")
            if (tryagain.upper() == "Y"):
                login()

    except Exception as e: print(e)

def signout():
    signout_prompt = input("Signout (Y/N)? ")
    if (signout_prompt.upper() == "Y"): main()
    else:
        print("To signout later, enter the command: \signout")
        while(signout_prompt != "Y"):
            signout_prompt = input()
            if (signout_prompt == "\signout"):
                signout_prompt = input("Signout (Y/N)? ")
        main()

def admin(): 
    ADMIN_VIEW = "SELECT * from users"
    cursor.execute(ADMIN_VIEW)
    for values in cursor.fetchall():
        print(values)
    main()

def main():
    questionaire = input("Would you like to login or signup an account (L/S) ? ")
    if (questionaire.upper() == "L"): login()
    elif (questionaire.upper() == "S"): signup()
    elif (questionaire.upper() == "ADMIN"): admin()

if __name__ == "__main__":
    main()

cursor.close()
account_system.close()