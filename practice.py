"""This program is so we know where camps are overnight
Need to ensure that the quit subroutine is added along with the main function which
needs to be called.
Then create the labels and buttons"""


from tkinter import *

# quit subroutine


def quit():
    main_window.destroy()a

# print details of all the camps


def print_camp_details():
    global j_names, total_entries, name_counta
    name_count = 0
    Label(main_window, font='bold', text="Row").grid(column=0, row=7)
    Label(main_window, font='bold', text="Leader").grid(column=1, row=7)
    Label(main_window, font='bold', text="Location").grid(column=2, row=7)
    Label(main_window, font='bold', text="Number of Campers").grid(column=3, row=7)
    Label(main_window, font='bold', text="Weather").grid(column=4, row=7)

    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][0])).grid(
            column=1, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][1])).grid(
            column=2, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][2])).grid(
            column=3, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][3])).grid(
            column=4, row=name_count+8)
        name_count += 1


# start the program running
def main():
    global main_window
    global camp_details, entry_name, entry_age, entry_gender, total_entries
    camp_details = []
    total_entries = 0
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()


main()
