import tkinter as tk

root = tk.Tk()
root.title("Project GUI")
root.geometry("900x720")

root.configure(bg = '#856ff8')

head = tk.Label(root,
                text = "Rock Paper Scissor",
                fg = "#A66FD1",
                bg = '#6FF7F3',
                font = ("Times New Roman",24,'bold','italic'))
head.place(x = 320, y = 30)

computer_score = 0
user_score = 0

score1 = tk.Label(root,
                  text = f'{computer_score}\nComputer',
                  bg = '#856ff8',
                  fg = '#302d45',
                  font = ("Times New Roman", 13, 'bold')).place(x = 280, y = 90)

score2 = tk.Label(root,
                  text = f'{user_score}\nUser',
                  bg = '#856ff8',
                  fg = '#302d45',
                  font = ("Times New Roman", 13, 'bold')).place(x = 510, y = 90)

rock_button1 = tk.Button(root,
                    text = 'Rock\n0',
                    bg = '#6f6f6f',
                    fg = 'white',
                    height = 5,
                    width = 10).place(x =195, y = 210)

paper_button2 = tk.Button(root,
                    text = 'Paper\n1',
                    bg = '#6f6f6f',
                    fg = 'white',
                    height = 5,
                    width = 10).place(x = 395, y = 210)

scissor_button3 = tk.Button(root,
                    text = 'Scissor\n2',
                    bg = '#6f6f6f',
                    fg = 'white',
                    height = 5,
                    width = 10).place(x = 595, y = 210)

playername = ""

player = tk.Entry(root,
                  text = playername) .pack()## type: ignore



root.mainloop()