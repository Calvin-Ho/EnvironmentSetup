# ---------------------------------------------
# SCRIPT DOES NOT FUNCTION WITHOUT LOGIN INFO
# ---------------------------------------------
import pyautogui
import time

SESSION_COUNT = 6

# Hard-coded coordinates for interactive program elements
# (Not really any way to make this better currently # as pyautogui has no support
# for in-window references [8/20/18])
host_field_coords = (330, 73)
open_sess_check_coords = (1038, 74)
clear_fields_coords = (1064, 74)

# Hard-coded offsets for session tabs
# --------------------------------------
# Distance from center of one session tab to next tab
sess_tab_offset = (110, 140)
# Vertical distance from tab to actual session
sess_tab_vert_offset = 100

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

def open_session(num_sessions):
    # Add 1 to end of range as I need counter to begin at 1 for calculations
    for session in range(1, num_sessions + 1):
        print("Opening session {}".format(session))
        pyautogui.click(x=host_field_coords[0], y=host_field_coords[1])
        pyautogui.typewrite(logininfo['hostname'] + '\t')
        time.sleep(0.5)

        pyautogui.typewrite(logininfo['user'] + '\t')
        time.sleep(0.5)

        pyautogui.click(x=open_sess_check_coords[0], y=open_sess_check_coords[1])
        time.sleep(2)

        # Have to double click for some reason
        pyautogui.click(x=clear_fields_coords[0], y=clear_fields_coords[1])
        pyautogui.click(x=clear_fields_coords[0], y=clear_fields_coords[1])
        time.sleep(0.5)

        select_session(session)

        # Delay since server can be slow to establish connection, especially for 1st session
        time.sleep(2)
        pyautogui.typewrite(logininfo['password'])
        pyautogui.press('enter')

        time.sleep(2)

    print("Done opening all sessions")

def select_session(sess_num):
    # X, Y coordinates of current tab
    tab_position = (sess_num * sess_tab_offset[0], sess_num * sess_tab_offset[1])

    # Select the session tab and click into the session window
    pyautogui.click(tab_position[0], tab_position[1])
    time.sleep(0.5)
    pyautogui.click(tab_position[0], tab_position[1] + sess_tab_vert_offset)
    time.sleep(0.5)

if __name__ == "__main__":
    main()
