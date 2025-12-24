import requests
import hashlib
import sys


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error Fetching: {response.status_code}, check the API and try again")
    return response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for hsh, count in hashes:
        if hsh == hash_to_check:
            return int(count)
    return 0


def pwned_api_check(password):
    # check if password exists in the api response
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5char)
    return get_password_leaks_count(response, tail)


def main(passwords):
    for password in passwords:
        count = pwned_api_check(password)
        if count > 0:
            print(f"Oh no! the password {password}, has been leaked {count} times!")
        else:
            print(f"{password} is all good! go ahead.")
    return "Program Done! All the passwords are Checked"


if __name__ == "__main__":
    try:
        passwords_file = sys.argv[1]
        try:
            with open(passwords_file, "r") as my_file:
                passwords = my_file.read().splitlines()
            sys.exit(main(passwords))
        except FileNotFoundError:
            print(f"File does not exist. Kindly check if {passwords_file} exists.")
    except IndexError:
        print(f"Kindly specify the file name when running this program from the command line.")
    sys.exit("Exited without Checking Passwords")

# sample how to run this code: python checkmypassword.py file1.txt
