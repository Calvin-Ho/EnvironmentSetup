import pyautogui
import time
import sys

SESSION_COUNT = 10
USER_DELAY = 5

# Hard-coded coordinates for interactive program elements
# -------------------------------------------------------------------------------
# (Not really any way to make this better currently as pyautogui has no support
# for in-window references [8/20/18])
host_field_coords = (330, 73)
# TODO: I think this could be replaced by appending newline to end of username input
open_sess_check_coords = (1038, 74)
clr_fields_button_coords = (1064, 74)

# Store these coordinates for clicking into session window to type password
sess_window_coords = (110, 240)
rename_window_coords=(900, 500)

# Amount of horizontal distance to adjust for subsequent tabs
menu_x_offset = 100

login_info = {}

# Dictionary of tab names to commands that should be entered into the session
# to navigate them to correct directory
# (As of Python 3.6, dict insertion order is presevered so don't worry about ordering)
name_to_path_map = {
    'infra' : ['srg_diags', 'cd infra'],
    'inventory' : ['srg_diags', 'cd inventory'],
    'configs' : ['srg_diags', 'cd configs'],
    'scripts' : ['srg_diags', 'cd scripts'],
    'platforms/ASR1K' : ['srg_diags', 'cd platforms/ASR1K'],
    'platforms/ISR' : ['srg_diags', 'cd platforms/ISR'],
    '13RU-ESP200-1' : ['logs', 'cd ASR1K-13RU-ESP',  'cd 13RU-ESP200-1'],
    '13RU-ESP100-1' : ['logs', 'cd ASR1K-13RU-ESP',  'cd 13RU-ESP100-1'],
    '6RUX-ArgusX-1' : ['logs', 'cd ASR1K-6RUX-ArgusX',  'cd 6RUX-ArgusX-1'],
    'Fugazi-1' : ['logs', 'cd ASR1K-Fugazi',  'cd Fugazi-1'],
    'Gladius-1' : ['logs', 'cd ASR1K-Gladius',  'cd Gladius-1'],
    'GreenDay' : ['logs', 'cd ASR1K-Greenday',  'cd Greenday'],
    'Kahuna-1' : ['logs', 'cd ASR1K-Kahuna',  'cd Kahuna-1'],
    'Kahuna-2' : ['logs', 'cd ASR1K-Kahuna',  'cd Kahuna-2'],
    'Kingpin-1' : ['logs', 'cd ASR1K-Kingpin',  'cd Kingpin-1'],
    'Nightster-1' : ['logs', 'cd ASR1K-Nightster',  'cd Nightster-1'],
    'Ramones' : ['logs', 'cd ASR1K-Ramones',  'cd Ramones'],
    'SpeedRacer-1' : ['logs', 'cd ASR1K-SpeedRacer',  'cd SpeedRacer-1'],
    'SpeedRacer-2' : ['logs', 'cd ASR1K-SpeedRacer',  'cd SpeedRacer-2'],
    'Neptune-1' : ['logs', 'cd ISR-Neptune',  'cd Neptune-1'],
    'Neptune-2' : ['logs', 'cd ISR-Neptune',  'cd Neptune-2'],
    'Neptune-3' : ['logs', 'cd ISR-Neptune',  'cd Neptune-3'],
    'misc1' : ['srg_diags'],
    'misc2' : ['srg_diags'],
    'misc3' : ['srg_diags'],
    'misc4' : ['srg_diags'],
    'misc5' : ['srg_diags'],
    'srg-vm-2: 1' : ['srg_diags'],
    'srg-vm-2: 2' : ['srg_diags'],
    }

def main():
    SESSION_COUNT = len(name_to_path_map)

    print("\nUsing SESSION_COUNT of {}...\n".format(SESSION_COUNT))

    # Allow time for user to abort program if they wish to
    print(">>> Allowing user {} seconds to kill script with Ctrl-C <<<".format(USER_DELAY))
    time.sleep(USER_DELAY)
    open_sessions(SESSION_COUNT)
    setup_tabs(SESSION_COUNT)

def read_login_info(config_name):
    try:
        with open(config_name, 'r') as config_file:
            print("\nlogin_file found as {}".format(config_name))
            for line in config_file:
                values = [datum.strip() for datum in line.split('=')]
                if values[0] == 'hostname':
                    login_info['hostname'] = values[1]
                    print("-- Hostname is: {}".format(values[1]))
                elif values[0] == 'user':
                    login_info['user'] = values[1]
                    print("-- User is: {}".format(values[1]))
                elif values[0] == 'password':
                    login_info['password'] = values[1]
    except FileNotFoundError:
        print("\nUnable to read file for login info.  Exiting.")
        sys.exit()

def open_sessions(num_sessions):
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

def setup_tabs(num_sessions):
    session_num = 1 # Start this at 1 for easier printing

    for tab_name, tab_cmds in name_to_path_map.items():
        print("Renaming session tab {} with name {}".format(session_num, tab_name))
        # Focus connection bar and switch to next tab
        pyautogui.press('f12')
        pyautogui.hotkey('ctrl', 'tab')

        # Rename the tab
        pyautogui.press('f2')
        time.sleep(0.5)
        pyautogui.click(x=rename_window_coords[0], y=rename_window_coords[1])
        pyautogui.typewrite(tab_name)
        pyautogui.press('enter')
        time.sleep(0.5)

        # Focus the current session to begin entering commands
        pyautogui.click(x=sess_window_coords[0], y=sess_window_coords[1])

        # Changing directory of current session tab
        for cmd in tab_cmds:
            print("-- Sending command '{}'".format(cmd))
            pyautogui.typewrite(cmd)
            pyautogui.press('enter')
            time.sleep(0.5)
        
        # Clear screen after changing directories
        pyautogui.typewrite('clear')
        pyautogui.press('enter')
        time.sleep(0.25)

        session_num += 1

    print("Done setting up all session tabs")

if __name__ == "__main__":
    main()
