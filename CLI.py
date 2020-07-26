import youtube
import os
import time
from os import path

help_file_path = os.path.abspath("help.txt")


def main():
    start_time = time.time()
    main_banner()
    while True:
        command = cmd_input()

        if eic(command, "exit"):
            exit_time = time.time() - start_time
            print("Program has run for %d seconds" % exit_time)
            quit()

        elif eic(command, "help"):
            help_list = read_from_file()
            print_help(help_list)

        elif eic(command, "download"):
            print("Please enter target link")
            link = input(">>> ")

            download_start = time.time()
            YouTube = youtube.youtube_parse_link(link)
            result = youtube.download_progressive(YouTube)
            download_end = time.time-download_start

            print("That download took %s" % download_end)
            print("You can access the video at %s" % result)



def main_banner():
    seperator()
    justify("Welcome to")
    justify("Fwibisono87's Viddownloader")
    justify("Version 2 Mark VI 'Austin'")
    seperator()


def cmd_input():
    seperator("-")
    justify("Input commands below")
    justify("To exit, enter 'exit', for a list of commands, enter 'help'")
    seperator("-")
    command = input(">>> ")
    return command


def seperator(char="=", multiplier=80):
    print(char*multiplier)


def justify(string, length=80):
    print(("{:^%s}" % length).format(string))


def eic(string1, string2):
    if string1.casefold() == string2.casefold():
        return True
    else:
        return False


def read_from_file(help_file = help_file_path):
    if os.path.exists(help_file):
        with open(help_file) as file:
            line_list = file.readlines()
        return line_list


def print_help(help_list):
    seperator("-")
    justify("Help File")
    seperator("-")
    help_number = 0
    for helps in help_list:
        help = helps.replace("\n", ".")
        help_number += 1
        print("|{:<3}|{:<74}|".format(help_number, help))


if __name__ == "__main__":
    main()