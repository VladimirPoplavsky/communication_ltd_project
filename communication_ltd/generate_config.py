# import configparser
#
# # CREATE OBJECT
# config_file = configparser.ConfigParser()
#
#
# # ADD NEW SECTIONS AND SETTINGS
# config_file["Password Management"] = {
#         "# Enter the minimal required length of a password\n"
#         "Password Length": "10",
#         "\n# Options for password complexity:uppercase,lowercase,numbers,specialcharacters\n"
#         "Password Complexity": "upperCase,lowerCase,numbers,specialCharacters",
# #        "Allow Upper-case Letters in Password (y/n)": "y",
# #        "Allow Lower-case Letters in Password (y/n)": "y",
# #        "Allow numbers in Password (y/n)": "y",
# #        "Allow Special Characters in Password (y/n)": "y",
#         "\n# How many passwords need a user change before reusing one? \n"
#         "# For example he may not use the same password as the last 3 ones\n"
#         "# Passwords out of range are deleted.\n"
#         "Password History": "3",
#         "\n# Are there any forbidden passwords? \n"
#         "Password Black List": "123456789,HelloWorld,ForbiddenPassword",
#         "\n# How many time may a user enter a password incorrectly? \n"
#         "Max Try to Login": "3"
#         }
#
# # SAVE CONFIG FILE
# with open(r"configurations.ini", 'w') as configfileObj:
#     config_file.write(configfileObj)
#     configfileObj.flush()
#     configfileObj.close()
#
# print("Config file 'configurations.ini' created")
#
# # PRINT FILE CONTENT
# read_file = open("configurations.ini", "r")
# content = read_file.read()
# print("Content of the config file are:\n")
# print(content)
# read_file.flush()
# read_file.close()