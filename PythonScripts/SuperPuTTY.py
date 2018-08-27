# ---------------------------------------------
# SCRIPT DOES NOT FUNCTION WITHOUT LOGIN INFO
# ---------------------------------------------
import pyautogui
import time

SESSION_COUNT = 6

# Hard-coded coordinates for interactive program elements
# -------------------------------------------------------------------------------
# (Not really any way to make this better currently # as pyautogui has no support
# for in-window references [8/20/18])
host_field_coords = (330, 73)
open_sess_check_coords = (1038, 74)
clr_fields_button_coords = (1064, 74)
first_sess_tab_coords = (89, 137)
change_settings_menu_item_coords = (200, 340)

# Store these coordinates for clicking into session window to type password
sess_window_coords = (110, 240)

settings_change_x_offset = 136

# SENSITIVE LOGIN INFORMATION
'''
logininfo = {
    'hostname': '',
    'user': '',
    'password': '',
}
'''

def main():
    # Allow time for user to abort program if they wish to
    print(">>> Allowing user 3 seconds to kill script with Ctrl-C <<<")
    time.sleep(3)

    open_session(SESSION_COUNT)
    apply_settings(SESSION_COUNT)

def open_session(num_sessions):
    for session in range(num_sessions):
        print("Opening session {}".format(session + 1))
        pyautogui.click(x=host_field_coords[0], y=host_field_coords[1])
        pyautogui.typewrite(logininfo['hostname'] + '\t')
        time.sleep(0.5)

        pyautogui.typewrite(logininfo['user'])
        time.sleep(0.5)

        pyautogui.click(x=open_sess_check_coords[0], y=open_sess_check_coords[1])
        time.sleep(2)

        # Have to double click the 'Clear Fields' button
        pyautogui.click(x=clr_fields_button_coords[0], y=clr_fields_button_coords[1])
        pyautogui.click(x=clr_fields_button_coords[0], y=clr_fields_button_coords[1])
        time.sleep(0.5)

        # Focus the current session to enter the password
        pyautogui.click(x=sess_window_coords[0], y=sess_window_coords[1])

        # Delay since server can be slow to establish connection, especially for 1st session
        time.sleep(2)
        pyautogui.typewrite(logininfo['password'])
        pyautogui.press('enter')
        time.sleep(1)

    print("Done opening all sessions")

def apply_settings(num_sessions):
    tab_y = first_sess_tab_coords[1]
    tab_x = first_sess_tab_coords[0]
    menu_item_x = change_settings_menu_item_coords[0]
    menu_item_y = change_settings_menu_item_coords[1]

    for session in range(num_sessions):
        print("Changing settings for session {}".format(session + 1))
        pyautogui.click(button='right', x=tab_x, y=tab_y)
        time.sleep(1.5)  # The right click menu can take some time to appear
        pyautogui.click(x=menu_item_x, y=menu_item_y)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(0.5)
        tab_x += settings_change_x_offset
        menu_item_x += settings_change_x_offset

    print("Done changing settings for all sessions")

if __name__ == "__main__":
    main()
