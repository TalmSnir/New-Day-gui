from tkinter import *
import daily_calendar_agenda
import inbox_check
import youtube_songs
import quote_of_the_day


def start_the_day():
    youtube_songs.play_song()


root = Tk()
root.iconbitmap('favicon.ico')


q_of_the_day = quote_of_the_day.get_quote()
quote_text_label = Label(root, text=q_of_the_day[1],
                         bd=0, pady=10, padx=20, fg='blue')
quote_author_label = Label(root, text=q_of_the_day[0],
                           bd=0, padx=20, fg='blue')

quote_text_label.pack()
quote_author_label.pack()

btn_frame = LabelFrame(root, pady=5, padx=5)
btn_frame.pack(padx=10, pady=20)
start_btn = Button(btn_frame, text='press to start your day',
                   activebackground='cyan', command=start_the_day, border=4)
start_btn.pack()

root.mainloop()
