import pyautogui
import time
import sys

# SESSION_COUNT defaults to 5 if not otherwise specified as command line argument
SESSION_COUNT = 5
USER_DELAY = 5

# Hard-coded coordinates for interactive program elements
# -------------------------------------------------------------------------------
# (Not really any way to make this better currently as pyautogui has no support
# for in-window references [8/20/18])
host_field_coords = (330, 73)
# TODO: I think this could be replaced by appending newline to end of username input
open_sess_check_coords = (1038, 74)
clr_fields_button_coords = (1064, 74)
first_sess_tab_coords = (89, 140)
change_settings_menu_item_coords = (200, 340)

# Store these coordinates for clicking into session window to type password
sess_window_coords = (110, 240)

settings_change_x_offset = 136

# SENSITIVE LOGIN INFORMATION
login_info = {}

def main():

    if len(sys.argv) >= 2:
        read_login_info(sys.argv[1])
        if len(sys.argv) == 3:
            print("\nSetting SESSION_COUNT to {}\n".format(sys.argv[2]))
            SESSION_COUNT = int(sys.argv[2])
    else:
        print("Usage: SuperPuTTY.py [login_file] [session_count]")
        sys.exit()

    # Allow time for user to abort program if they wish to
    print(">>> Allowing user {} seconds to kill script with Ctrl-C <<<".format(USER_DELAY))
    time.sleep(USER_DELAY)
    open_session(SESSION_COUNT)

def read_login_info(config_name):
    try:
        with open(config_name, 'r') as config_file:
            print("\nlogin_file found as {}".format(config_name))
            for line in config_file:
                values = [datum.strip() for datum in line.split('=')]
                if values[0] == 'hostname':
                    login_info['hostname'] = values[1]
                elif values[0] == 'user':
                    login_info['user'] = values[1]
                elif values[0] == 'password':
                    login_info['password'] = values[1]
    except FileNotFoundError:
        print("\nUnable to read file for login info.  Exiting.")
        sys.exit()


def open_session(num_sessions):
    for session in range(num_sessions):
        print("Opening session {}".format(session + 1))
        pyautogui.click(x=host_field_coords[0], y=host_field_coords[1])
        pyautogui.typewrite(login_info['hostname'] + '\t')
        pyautogui.typewrite(login_info['user'])

        pyautogui.click(x=open_sess_check_coords[0], y=open_sess_check_coords[1])
        time.sleep(2)

        # Have to double click the 'Clear Fields' button to clear things
        pyautogui.click(x=clr_fields_button_coords[0], y=clr_fields_button_coords[1])
        pyautogui.click(x=clr_fields_button_coords[0], y=clr_fields_button_coords[1])
        time.sleep(0.5)

        # Focus the current session to enter the password
        pyautogui.click(x=sess_window_coords[0], y=sess_window_coords[1])

        # Delay since server can be slow to establish connection, especially for 1st session
        time.sleep(2)
        pyautogui.typewrite(login_info['password'])
        pyautogui.press('enter')
        time.sleep(1)

    print("Done opening all sessions")

if __name__ == "__main__":
    main()
