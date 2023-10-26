from asyncio import TimerHandle
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter
import winsound
from PIL import ImageTk, Image

root= Tk()
canvas = tk.Canvas(root) 
app_width = root.winfo_screenwidth()
app_height = root.winfo_screenheight()
root.geometry(f'{app_width}x{app_height}')

bg_image = Image.open("./image/background/home.png")
bg_image = bg_image.resize((app_width, app_height))
background = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=background)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

progress_bar_width = int(app_width * 0.3)
progress_bar = ttk.Progressbar(root, length=progress_bar_width)
progress_bar.place(relx=0.5, rely=0.5, anchor=CENTER,bordermode='ignore')


def close_window(): 
    root.destroy()

def sound_start():
    winsound.PlaySound("./sound/music.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    
def sound_click():
    winsound.PlaySound('./sound/click.wav', winsound.SND_FILENAME)  

def sound_lost():
    winsound.PlaySound('./sound/lost.wav', winsound.SND_FILENAME)  

def sound_win():
    winsound.PlaySound('./sound/win.wav', winsound.SND_FILENAME)  

def sound_scary():
    winsound.PlaySound('./sound/scary.wav', winsound.SND_ASYNC | winsound.SND_ASYNC) 

def sound_welldone():
    winsound.PlaySound('./sound/welldone.wav', winsound.SND_ASYNC | winsound.SND_ASYNC) 

def sound_bonmd():
    winsound.PlaySound('./sound/bomd.wav', winsound.SND_ASYNC | winsound.SND_ASYNC)

def sound_coin():
    winsound.PlaySound('./sound/coin.wav', winsound.SND_ASYNC | winsound.SND_ASYNC)

def sound_key():
    winsound.PlaySound('./sound/key.wav', winsound.SND_ASYNC | winsound.SND_ASYNC)

def update_progress(value):
    progress_bar['value'] = value
    if value < 100:
        root.after(100, update_progress, value +5)
    else:
        selection_()

def selection_():
    sound_start()
    select_window = Toplevel(root)
    select_window.attributes('-fullscreen', True)

    app_width = select_window.winfo_screenwidth()
    app_height = select_window.winfo_screenheight()
    select_window.geometry(f"{app_width}x{app_height}")

    bg_image = Image.open("./image/background/home.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)

    bg_label = Label(select_window, image=background)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    button_start = tkinter.Button(select_window, text="Start", command=start_game,bg='#AAFF00',border=20,width=20,height=1,font='Impact')
    button_start.place(x=600, y=300)

    button_exit= tkinter.Button(select_window, text="Exit", command=close_window,bg='#FF6347',border=20,width=20,height=1,font='Impact')
    button_exit.place(x=600, y=400)

    select_window.mainloop()


def start_game():
    start_window = Toplevel(root)
    start_window.attributes('-fullscreen', True)

    app_width = start_window.winfo_screenwidth()
    app_height = start_window.winfo_screenheight()
    start_window.geometry(f"{app_width}x{app_height}")

    bg_image = Image.open("./image/background/home.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)

    bg_label = Label(start_window, image=background)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    button_start = tkinter.Button(start_window, text="Easy", command=easy_game,bg='#FFDEAD',border=5,width=20,height=1,font='Impact')
    button_start.place(x=600, y=200)

    button_start = tkinter.Button(start_window, text="Medium", command=medaim_game,bg='#FF69B4',border=5,width=20,height=1,font='Impact')
    button_start.place(x=600, y=300)

    button_start = tkinter.Button(start_window, text="Hard", command=medaim_game,bg='red',border=5,width=20,height=1,font='Impact')
    button_start.place(x=600, y=400)

    button_start = tkinter.Button(start_window, text="back", command=selection_,bg='blue',border=2,width=20,height=1,font='Impact')
    button_start.place(x=10, y=10)

    start_window.mainloop()
def easy_game():
    sound_click()
    sound_scary()
    easy_window = Toplevel(root)
    easy_window.attributes('-fullscreen', True)

    app_width = easy_window.winfo_screenwidth()
    app_height = easy_window.winfo_screenheight()
    easy_window.geometry(f"{app_width}x{app_height}")

    canvas = Canvas(easy_window, width=1920, height=1080)
    canvas.pack()

    image_wall =PhotoImage(file='./image/wall/wall (2).png')
    image_bom =PhotoImage(file='./image/anami/bom.png')
    image_ghost =PhotoImage(file='./image/anami/ghost.png')
    image_tree =PhotoImage(file='./image/plant/tree.png')
    image_beach =PhotoImage(file='./image/plant/beach.png')
    image_door =PhotoImage(file='./image/plant/door.png')
    image_wood =PhotoImage(file='./image/plant/wood.png')
    image_coin =PhotoImage(file='./image/plant/coin.png')
    image_key =PhotoImage(file='./image/plant/key.png')
    image_play =PhotoImage(file='./image/plant/play.png')
    image_heart =PhotoImage(file='./image/plant/heart.png')
    image_clock =PhotoImage(file='./image/plant/clock.png')
    image_grass =PhotoImage(file='./image/plant/grass.png')
    image_vor =PhotoImage(file='./image/plant/vor.png')
    image_wall_grass =PhotoImage(file='./image/plant/wall_grass.png')
    image_home_ghost =PhotoImage(file='./image/anami/home.png')
    # wall3.png
    def delete_button(button):
        canvas.delete(play)
        button.destroy()

    button_start = tkinter.Button(easy_window,text='Start',command=lambda: delete_button(button_start),border=2,bg='orange',width=40,height=5,bd=5)
    button_start.place(x=500, y=300)

    image_enemy1 = ImageTk.PhotoImage(Image.open('./image/anami/zombie.png').resize((50, 50)))
    image_win = ImageTk.PhotoImage(Image.open('./image/background/win.png').resize((700, 700)))
    image_lost = ImageTk.PhotoImage(Image.open('./image/background/lost.png').resize((500, 400)))
    
    canvas.create_image(150, 30, image=image_heart)
    heart2=canvas.create_image(190, 30, image=image_heart)
    heart3=canvas.create_image(240, 30, image=image_heart)
 
    clock=canvas.create_image(900, 50, image=image_clock)
    canvas.create_image(10, 240, image=image_vor) 
    canvas.create_image(150, 590, image=image_wood)
    canvas.create_image(1200, 120, image=image_beach)
    door=canvas.create_image(1250, 220, image=image_door)
    canvas.create_image(1200, 480, image=image_beach)
    canvas.create_image(1050, 220, image=image_wood)
    player=canvas.create_oval(50,450,90,490,fill='pink')
    # -----------time-----------------
    global time
    time = 30
    def settime_():
        global time,process_win
        canvas.itemconfig(timer_text, text= str(time) + "s")
        if time <= 30 and len(process_win)==0:
            time -= 1
        if time <-1 and len(process_win)==0: 
            sound_lost()
            lost_()
        canvas.after(1500,settime_)

    timer_text = canvas.create_text(960, 50, text= str(time) + "s", fill='grey', font='212BabyGirl 20 bold')
    bomd1=canvas.create_image(250, 590, image=image_bom)
    bomd2=canvas.create_image(350, 325, image=image_bom)
    canvas.create_rectangle(0, 620, 1400, 621, fill='green',tags='wall')
    
    bomd3=canvas.create_image(950, 325, image=image_bom)
    canvas.create_image(150, 300, image=image_ghost)
    canvas.create_image(1300, 180, image=image_tree)
    canvas.create_image(400, 700, image=image_wall)
    canvas.create_image(1100, 700, image=image_wall) 

    coin1=canvas.create_image(490, 480, image=image_coin)
    coin2=canvas.create_image(530, 480, image=image_coin)
    bomd4=canvas.create_image(630, 470, image=image_bom)

    coin3=canvas.create_image(630, 330, image=image_coin)
    coin4=canvas.create_image(670, 330, image=image_coin)
    coin5=canvas.create_image(710, 330, image=image_coin)

    coin6=canvas.create_image(1100, 230, image=image_coin)
    coin7=canvas.create_image(1140, 230, image=image_coin)
    coin8=canvas.create_image(1180, 230, image=image_coin)
    
    wall_5=canvas.create_rectangle(400, 170, 798, 210, fill='blue',tags='wall')
    wall_2=canvas.create_rectangle(400, 502, 798, 540, fill='green',tags='wall')
    wall_1=canvas.create_rectangle(100, 352, 495, 390, fill='green',tags='wall')
    wall_3=canvas.create_rectangle(600, 352, 995, 390, fill='green',tags='wall')
    wall_4=canvas.create_rectangle(1000, 252, 1395, 280, fill='green',tags='wall')

    canvas.create_image(800, 372, image=image_wall_grass) 
    canvas.create_image(300, 372, image=image_wall_grass) 
    canvas.create_image(600, 520, image=image_wall_grass) 
    canvas.create_image(600, 190, image=image_wall_grass) 
    canvas.create_image(1200, 270, image=image_wall_grass) 
    play=canvas.create_image(920, 350, image=image_play)
    canvas.create_image(600, 130, image=image_home_ghost) 

    global process_win
    process_win=[]
    def win_():
        canvas.create_image(600, 300, image=image_win)
        button_back = tkinter.Button(easy_window, text='Playe again', command=easy_game,bg='#AAFF00',border=2,width=20,height=1,font='Impact')
        button_back.place(x=300, y=400)
        button_back = tkinter.Button(easy_window, text='Contiue', command=start_game,bg='#AAFF00',border=2,width=20,height=1,font='Impact')
        button_back.place(x=700, y=400)
        button_back = tkinter.Button(easy_window, text='Back', command=start_game,bg='#AAFF00',border=2,width=20,height=1,font='Impact')
        button_back.place(x=500, y=400)
        process_win.append('done')

    def lost_():
        canvas.create_image(600, 300, image=image_lost)
        button_back = tkinter.Button(easy_window, text='Playe again', command=easy_game,bg='#AAFF00',border=2,width=20,height=1,font='Impact')
        button_back.place(x=300, y=400)
        button_back = tkinter.Button(easy_window, text='Back', command=start_game,bg='#AAFF00',border=2,width=20,height=1,font='Impact')
        button_back.place(x=700, y=400)
        process_win.append('done')

    key=canvas.create_image(700, 150, image=image_key)
    global process
    process=[]
    
    global keyPressed
    keyPressed = []
    SPEED = 5
    TIME = 10
    GRAVITY_FORCE=10

    def check_movement(dx=0, dy=0):
        ball_coords = canvas.coords(player)
        new_x1 = ball_coords[0] + dx
        new_y1 = ball_coords[1] + dy
        new_x2 = ball_coords[2] + dx
        new_y2 = ball_coords[3] + dy

        overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)

        for wall_id in canvas.find_withtag("wall"):
            if wall_id in overlapping_objects:
                return False 
        return True

    def start_move(event):
        if event.keysym not in keyPressed:
            print(event.keysym)
            keyPressed.append(event.keysym)
            if len(keyPressed) == 1:
                move()

    def jump(force):
        if force > 0:
            if check_movement(0, -force):
                canvas.move(player, 0, -force)
                easy_window.after(TIME, jump, force-1)
                
    global enemy1_x
    enemy1_x = 400
    global enemy1_dx
    enemy1_dx = 2
    enemy1 = canvas.create_image(400, 90, image=image_enemy1)
    def move_enemy1():
        global enemy1_x,enemy1_dx,process_win
        enemy1_x += enemy1_dx
        canvas.coords(enemy1, enemy1_x, 140)
        if enemy1_x <= 400 or enemy1_x >= 800:
            enemy1_dx = -enemy1_dx
        canvas.after(15, move_enemy1)

    image_enemy2= ImageTk.PhotoImage(Image.open('./image/anami/momi.png').resize((150, 150)))
    enemy2 = canvas.create_image(600, 300, image=image_enemy2)
    global enemy2_x
    enemy2_x = 600
    global enemy2_dx
    enemy2_dx = -2
    enemy2_x += enemy2_dx
    canvas.coords(enemy2, enemy2_x, 300)

    def move_enemy2():
        global enemy2_x, enemy2_dx
        enemy2_x += enemy2_dx
        canvas.coords(enemy2, enemy2_x, 100)
        if enemy2_x <= 300 or enemy2_x >= 900 :
            enemy2_dx = -enemy2_dx

        canvas.after(10, move_enemy2)

    def move():
        door_coord=canvas.coords(door)
        player_coord=canvas.coords(player)
        key_coord=canvas.coords(key)

        coin1_coord=canvas.coords(coin1)
        coin2_coord=canvas.coords(coin2)
        coin3_coord=canvas.coords(coin3)
        coin4_coord=canvas.coords(coin4)
        coin5_coord=canvas.coords(coin5)
        coin6_coord=canvas.coords(coin6)
        coin7_coord=canvas.coords(coin7)
        coin8_coord=canvas.coords(coin8)

        bomd1_coord=canvas.coords(bomd1)
        bomd2_coord=canvas.coords(bomd2)
        bomd3_coord=canvas.coords(bomd3)
        bomd4_coord=canvas.coords(bomd4)

        wall_1_coord=canvas.coords(wall_1)
        wall_2_coord=canvas.coords(wall_2)
        wall_3_coord=canvas.coords(wall_3)
        wall_4_coord=canvas.coords(wall_4)
        wall_5_coord=canvas.coords(wall_5)

        if len(process)==1:
            canvas.delete(heart3)
        if len(process)==2:
            canvas.delete(heart2)
        if len(process)==3:
            sound_lost()
            lost_()
            process.append('1')
        if not keyPressed == []:
            x = 0
            if "Left" in keyPressed and player_coord[0]>10:
                x = -SPEED
                if coin1_coord:
                    if player_coord[0]==coin1_coord[0]+20 and player_coord[1] < wall_2_coord[3]:
                        sound_coin()
                        canvas.delete(coin1)
                if coin2_coord:
                    if player_coord[0]==coin2_coord[0]+20 and player_coord[1] < wall_2_coord[3]:
                        sound_coin()
                        canvas.delete(coin2)
                if coin3_coord:
                    if player_coord[0]==coin3_coord[0]+20 and player_coord[3] < wall_3_coord[1]and player_coord[3]>300:
                        sound_coin()
                        canvas.delete(coin3)
                if coin4_coord:
                    if player_coord[0]==coin4_coord[0]+20 and player_coord[3] < wall_3_coord[1]and player_coord[3]>300:
                        sound_coin()
                        canvas.delete(coin4)
                if coin5_coord:
                    if player_coord[0]==coin4_coord[0]+20 and player_coord[3] < wall_3_coord[1]and player_coord[3]>300:
                        sound_coin()
                        canvas.delete(coin5)
                if coin6_coord:
                    if player_coord[0]==coin6_coord[0]and player_coord[3] < wall_4_coord[1]and player_coord[3]>200:
                        sound_coin()
                        canvas.delete(coin6)
                if coin7_coord:
                    if player_coord[0]==coin7_coord[0]and player_coord[3] < wall_4_coord[1]and player_coord[3]>200:
                        sound_coin()
                        canvas.delete(coin7)
                if coin8_coord:
                    if player_coord[0]==coin8_coord[0]and player_coord[3] < wall_4_coord[1]and player_coord[3]>200:
                        sound_coin()
                        canvas.delete(coin8)
                if key_coord:
                    if (player_coord[0]==key_coord[0] and player_coord[3] < wall_5_coord[1] and player_coord[3]>110):
                        sound_key()
                        canvas.delete(key)
                        
                if bomd1_coord:
                    if player_coord[0]==bomd1_coord[0] and player_coord[1]>wall_2_coord[1] :
                        sound_bonmd()
                        canvas.delete(bomd1)
                        process.append('1')
                if bomd2_coord :
                    if (player_coord[0]==bomd2_coord[0] and player_coord[3] < wall_1_coord[1] and player_coord[3]>300):
                        sound_bonmd()
                        canvas.delete(bomd2)
                        process.append('1')
                if bomd3_coord:
                    if player_coord[0]==bomd3_coord[0] and player_coord[3] < wall_3_coord[1]and player_coord[3]>300:
                        sound_bonmd()
                        canvas.delete(bomd3)
                        process.append('1')
                if bomd4_coord:
                    if player_coord[2]==bomd4_coord[0]+10 and player_coord [1]< wall_2_coord[3] and player_coord [1]> wall_3_coord[3]:
                        sound_bonmd()
                        canvas.delete(bomd4)
                        process.append('1')
            if "Right" in keyPressed and player_coord[0]<1330:
                x = SPEED
                if door_coord:
                    if player_coord[2]==door_coord[0] and not key_coord and player_coord[3]<wall_4_coord[1]:
                        win_(),sound_win()
                if coin1_coord:
                    if player_coord[2]==coin1_coord[0]-20 and player_coord[1] < wall_2_coord[3]:
                        sound_coin()
                        canvas.delete(coin1)
                if coin2_coord:
                    if player_coord[2]==coin2_coord[0]-20 and player_coord[1] < wall_2_coord[3]:
                        sound_coin()
                        canvas.delete(coin2)
                if coin3_coord:
                    if player_coord[2]==coin3_coord[0]-20 and player_coord[3] < wall_3_coord[1]and player_coord[3]>300:
                        sound_coin()
                        canvas.delete(coin3)
                if coin4_coord:
                    if player_coord[2]==coin4_coord[0]-20 and player_coord[3] < wall_3_coord[1]and player_coord[3]>300:
                        sound_coin()
                        canvas.delete(coin4)
                if coin5_coord:
                    if player_coord[2]==coin5_coord[0]-20 and player_coord[3] < wall_3_coord[1]and player_coord[3]>300:
                        sound_coin()
                        canvas.delete(coin5)
                if coin6_coord:
                    if player_coord[0]==coin6_coord[0]-50 and player_coord[3] < wall_4_coord[1]and player_coord[3]>200:
                        sound_coin()
                        canvas.delete(coin6)
                if coin7_coord:
                    if player_coord[0]==coin7_coord[0]-50 and player_coord[3] < wall_4_coord[1]and player_coord[3]>200:
                        sound_coin()
                        canvas.delete(coin7)
                if coin8_coord:
                    if player_coord[0]==coin8_coord[0]-50 and player_coord[3] < wall_4_coord[1]and player_coord[3]>200:
                        sound_coin()
                        canvas.delete(coin8)
                if key_coord:
                    if player_coord[2]==key_coord[0]-10 and player_coord[3] < wall_5_coord[1]and player_coord[3]>110:
                        sound_key()
                        canvas.delete(key)
                if bomd1_coord:
                    if player_coord[2]==bomd1_coord[0]-10 and player_coord[1]>wall_2_coord[1] :
                        sound_bonmd()
                        canvas.delete(bomd1)
                        process.append('1')
                if bomd2_coord:
                    if player_coord[2]==bomd2_coord[0]-10 and player_coord[3] < wall_1_coord[1]and player_coord[3]>300:
                        sound_bonmd()
                        canvas.delete(bomd2)
                        process.append('1')
                if bomd3_coord:
                    if player_coord[2]==bomd3_coord[0]-10 and player_coord[3] < wall_3_coord[1] and player_coord[3]>300:
                        sound_bonmd()
                        canvas.delete(bomd3)
                        process.append('1')
                if bomd4_coord:
                    if player_coord[2]==bomd4_coord[0]-10 and player_coord [1]< wall_2_coord[3] and player_coord [1]> wall_3_coord[3]:
                        sound_bonmd()
                        canvas.delete(bomd4)
                        process.append('1')
            if check_movement(x,0):
                canvas.move(player, x, 0)
            if "space" in keyPressed and not check_movement(0,GRAVITY_FORCE):
                jump(30)
            easy_window.after(TIME, move)

    def stop_move(event):
        global keyPressed
        if event.keysym in keyPressed:
            keyPressed.remove(event.keysym)

    def gravity():
        if check_movement(0, GRAVITY_FORCE):
            canvas.move(player,0, GRAVITY_FORCE)
        easy_window.after(TIME, gravity)

    move_enemy1() 
    move_enemy2()  

    settime_()
    gravity()

    easy_window.bind("<Key>", start_move)
    easy_window.bind("<KeyRelease>", stop_move)
    easy_window.mainloop()
# ..................................madiam........................
def medaim_game():
    sound_click()
    medaim_window = Toplevel(root)
    medaim_window.attributes('-fullscreen', True)

    app_width =medaim_window.winfo_screenwidth()
    app_height =medaim_window.winfo_screenheight()
    medaim_window.geometry(f"{app_width}x{app_height}")


    button_easy = tkinter.Button(medaim_window, text="back", command=start_game,bg='blue',border=2,width=20,height=1,font='Impact')
    button_easy.place(x=500, y=500)

    canvas = Canvas(medaim_window, width=1920, height=1080)
    canvas.pack()

    background_image = tk.PhotoImage(file='./image/background/ice3.png')
    canvas.create_image(0,0, anchor=tk.NW, image=background_image)
 # -----------time-----------------
    global times
    times = 30
    def settimes_():
        global times,process_win
        canvas.itemconfig(timer_text, text= str(times) + "s")
        if times <= 30 and len(process_win)==0 :
            times -= 1
        if times <-1 and len(process_win)==0: 
            sound_lost()
            lost_()
        canvas.after(1500,settimes_)
# -------------------------------------------------------------------------
    image_win = ImageTk.PhotoImage(Image.open('./image/background/win.png').resize((700, 700)))
    global process_win
    process_win=[]
    def win_():
        canvas.create_image(600, 300, image=image_win)
        button_back = tkinter.Button(medaim_window, text='Playe again', command=medaim_game,bg='#AAFF00',border=2,width=20,height=1,font='Impact')
        button_back.place(x=300, y=400)
        button_back = tkinter.Button(medaim_window, text='Contiue', command=start_game,bg='#AAFF00',border=2,width=20,height=1,font='Impact')
        button_back.place(x=700, y=400)
        button_back = tkinter.Button(medaim_window, text='Back', command=start_game,bg='#AAFF00',border=2,width=20,height=1,font='Impact')
        button_back.place(x=500, y=400)
        process_win.append('done')

    image_lost = ImageTk.PhotoImage(Image.open('./image/background/lost.png').resize((500, 400)))
    def lost_():
        canvas.create_image(600, 300, image=image_lost)
        button_back = tkinter.Button(medaim_window, text='Playe again', command=medaim_game,bg='#AAFF00',border=2,width=20,height=1,font='Impact')
        button_back.place(x=300, y=400)
        button_back = tkinter.Button(medaim_window, text='Back', command=start_game,bg='#AAFF00',border=2,width=20,height=1,font='Impact')
        button_back.place(x=700, y=400)
        process_win.append('done')

    image_wall = tk.PhotoImage(file='./image/wall/wall (2).png')
    image_wall3 = tk.PhotoImage(file='./image/wall/wall3.png')
    image_key = tk.PhotoImage(file='./image/plant/key.png')
    image_grass2 = tk.PhotoImage(file='./image/wall/grass2.png')
    image_wall4 = tk.PhotoImage(file='./image/wall/wall4.png')
    image_coin = tk.PhotoImage(file='./image/plant/coin.png')
    image_bomRed= tk.PhotoImage(file='./image/anami/bomRed.png')
    image_wave = tk.PhotoImage(file='./image/anami/wave.png')
    image_tree2 = tk.PhotoImage(file='./image/plant/tree2.png')
    image_clock =PhotoImage(file='./image/plant/clock.png')
    image_play =PhotoImage(file='./image/plant/play.png')
    
    image_plant3 = tk.PhotoImage(file='./image/anami/plant3.png')
    image_beach = tk.PhotoImage(file='./image/plant/beachs.png')
    image_door = tk.PhotoImage(file='./image/plant/door.png')
    image_wood = tk.PhotoImage(file='./image/plant/wood.png')
    image_heart =PhotoImage(file='./image/plant/heart.png')

    canvas.create_rectangle(0, 637, 800, 650, fill='white',tags='wall')
    bomR1=canvas.create_image(350, 610, image=image_bomRed)
    bomR2=canvas.create_image(400, 300, image=image_bomRed)
    bomR3=canvas.create_image(700, 315, image=image_bomRed)
    bomR4=canvas.create_image(1100, 220, image=image_bomRed)

    timer_text = canvas.create_text(960, 50, text= str(times) + "s", fill='grey', font='212BabyGirl 20 bold')
    canvas.create_image(150, 600, image=image_wood)
    canvas.create_image(1300, 180, image=image_tree2)

    clock=canvas.create_image(900, 50, image=image_clock)

    door=canvas.create_image(400, 145, image=image_door)

    canvas.create_image(1200, 480, image=image_beach)
    canvas.create_image(400, 720, image=image_wall)

    coin9=canvas.create_image(550, 480, image=image_coin)
    coin10=canvas.create_image(600, 480, image=image_coin)
    coin11=canvas.create_image(650, 480, image=image_coin)

    coin4=canvas.create_image(1200, 230, image=image_coin)
    coin5=canvas.create_image(1250, 230, image=image_coin)

    coin1=canvas.create_image(250, 330, image=image_coin)
    coin2=canvas.create_image(300, 330, image=image_coin)

    coin6=canvas.create_image(750, 325, image=image_coin)
    coin7=canvas.create_image(800, 325, image=image_coin)
    coin8=canvas.create_image(850, 325, image=image_coin)

    canvas.create_image(955, 670, image=image_wave)                
    canvas.create_image(1250, 670, image=image_wave)                              
    canvas.create_image(700, 455, image=image_plant3)

    wall_door=canvas.create_rectangle(350, 210, 450, 220, fill='red',tags='wall')
    canvas.create_image(400, 200, image=image_wall3)

    canvas.create_rectangle(1150, 80, 1250, 120, fill='grey',tags='wall')
    canvas.create_image(1200, 100, image=image_wall3)

    wall_key=canvas.create_rectangle(670, 170, 728, 200, fill='pink',tags='wall')
    key=canvas.create_image(700, 150, image=image_key)
    canvas.create_image(700, 200, image=image_wall4)
    canvas.create_rectangle(870, 170, 928, 200, fill='black',tags='wall')
    player=canvas.create_oval(100,150,150,200,fill='pink')
    canvas.create_image(900, 200, image=image_wall4)

    canvas.create_image(150, 30, image=image_heart)
    heart2=canvas.create_image(190, 30, image=image_heart)
    heart3=canvas.create_image(240, 30, image=image_heart)
    def delete_button(button):
        canvas.delete(play)
        button.destroy()

    button_start = tkinter.Button(medaim_window,text='Start',command=lambda: delete_button(button_start),border=2,bg='orange',width=40,height=5,bd=5)
    button_start.place(x=500, y=300)

    wall1=canvas.create_rectangle(400, 500, 750, 550, fill='blue',tags='wall')
    canvas.create_image(580, 528, image=image_grass2)
    wall2=canvas.create_rectangle(100, 350, 470, 400, fill='grey',tags='wall')
    canvas.create_image(280, 378, image=image_grass2)
    wall3=canvas.create_rectangle(600, 350, 970, 400, fill='green',tags='wall')
    canvas.create_image(790, 370, image=image_grass2)
    wall4=canvas.create_rectangle(1000, 250, 1400, 300, fill='pink',tags='wall')
    canvas.create_image(1190, 275, image=image_grass2)
    play=canvas.create_image(920, 350, image=image_play)

    global processe
    processe=[]
    global keyPressed
    keyPressed = []
    SPEED = 5
    TIME = 10
    GRAVITY_FORCE=10

    def check_movement(dx=0, dy=0):
        ball_coords = canvas.coords(player)

        new_x1 = ball_coords[0] + dx
        new_y1 = ball_coords[1] + dy
        new_x2 = ball_coords[2] + dx
        new_y2 = ball_coords[3] + dy

        overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)

        for wall_id in canvas.find_withtag("wall"):
            if wall_id in overlapping_objects:
                return False 

        return True 
    def start_move(event):
        if event.keysym not in keyPressed:
            print(event.keysym)
            keyPressed.append(event.keysym)
            if len(keyPressed) == 1:
                move()

    def jump(force):
        if force > 0:
            if check_movement(0, -force):
                canvas.move(player, 0, -force)
            medaim_window.after(TIME, jump, force-1)

    def move():
        door_coord=canvas.coords(door)
        wall_door_coord=canvas.coords(wall_door)

        coin1_coord=canvas.coords(coin1)
        coin2_coord=canvas.coords(coin2)
        coin4_coord=canvas.coords(coin4)
        coin5_coord=canvas.coords(coin5)
        coin6_coord=canvas.coords(coin6)
        coin7_coord=canvas.coords(coin7)
        coin8_coord=canvas.coords(coin8)
        coin9_coord=canvas.coords(coin9)
        coin10_coord=canvas.coords(coin10)
        coin11_coord=canvas.coords(coin11)
        key_coord=canvas.coords(key)
        bomR1_coord=canvas.coords(bomR1)
        bomR2_coord=canvas.coords(bomR2)
        bomR3_coord=canvas.coords(bomR3)
        bomR4_coord=canvas.coords(bomR4)

        wall1_coord=canvas.coords(wall1)
        wall2_coord=canvas.coords(wall2)
        wall3_coord=canvas.coords(wall3)
        wall4_coord=canvas.coords(wall4)
        wall_key_coord=canvas.coords(wall_key)
    
        player_coord=canvas.coords(player)

        if len(processe)==1:
            canvas.delete(heart3)
        if len(processe)==2:
            canvas.delete(heart2)
        if len(processe)==3:
            sound_lost()
            lost_()
            processe.append('1')
        if not keyPressed == []:
            x = 0
            if "Left" in keyPressed:
                x = -SPEED
                if not key_coord:
                    if player_coord[2]==door_coord[0]+50 and player_coord[3]<wall_door_coord[1] and player_coord[1]>140 :
                        sound_win()
                        win_()
                if key_coord:
                    if player_coord[2]==key_coord[0]+50 and player_coord[3]<wall_key_coord[1] and player_coord[1]>70:
                        canvas.delete(key)
                        sound_key()
                if coin9_coord:
                    if player_coord[2]==coin9_coord[0]+50 and player_coord[3]<wall1_coord[1]and player_coord[3]>wall3_coord[1]:
                        canvas.delete(coin9)
                        sound_coin()
                if coin10_coord:
                    if player_coord[2]==coin10_coord[0]+50 and player_coord[3]<wall1_coord[1]and player_coord[3]>wall3_coord[1]:
                        canvas.delete(coin10)
                        sound_coin()
                if coin11_coord:
                    if player_coord[2]==coin11_coord[0]+50 and player_coord[3]<wall1_coord[1]and player_coord[3]>wall3_coord[1]:
                        canvas.delete(coin11)
                        sound_coin()
                if coin6_coord:
                    if player_coord[2]==coin6_coord[0]+50 and player_coord[3]<wall3_coord[1] and player_coord[3]>200:
                        canvas.delete(coin6)
                        sound_coin()
                if coin7_coord:
                    if player_coord[2]==coin7_coord[0]+50 and player_coord[3]<wall3_coord[1] and player_coord[3]>200:
                        canvas.delete(coin7)
                        sound_coin()
                if coin8_coord:
                    if player_coord[2]==coin8_coord[0]+50 and player_coord[3]<wall3_coord[1] and player_coord[3]>200:
                        canvas.delete(coin8)
                        sound_coin()
                if bomR2_coord:
                    if player_coord[2]==bomR2_coord[0]+50 and player_coord[3]<wall2_coord[1] and player_coord[3]>200:
                        canvas.delete(bomR2)
                        sound_bonmd()
                        processe.append('1')
                if coin1_coord:
                    if player_coord[2]==coin1_coord[0]+50 and player_coord[3]<wall2_coord[1] and player_coord[3]>200:
                        canvas.delete(coin1)
                        sound_coin()
                if coin2_coord:
                    if player_coord[2]==coin2_coord[0]+50 and player_coord[3]<wall2_coord[1] and player_coord[3]>200:
                        canvas.delete(coin2)
                        sound_coin()
                if bomR3_coord:
                    if player_coord[2]==bomR3_coord[0]+50 and player_coord[3]<wall3_coord[1] and player_coord[3]>200:
                        canvas.delete(bomR3)
                        processe.append('1')
                if bomR4_coord:
                    if player_coord[2]==bomR4_coord[0]+50 and player_coord[3]<wall4_coord[1] and player_coord[3]>100:
                        canvas.delete(bomR4)
                        processe.append('1')
                if coin4_coord:
                    if player_coord[2]==coin4_coord[0]+50 and player_coord[3]<wall4_coord[1] and player_coord[3]>100:
                        canvas.delete(coin4)
                        sound_coin()
                if coin5_coord:
                    if player_coord[2]==coin5_coord[0]+50 and player_coord[3]<wall4_coord[1] and player_coord[3]>100:
                        canvas.delete(coin5)
                        sound_coin()
            if "Right" in keyPressed:
                x = SPEED
                if not key_coord:
                    if player_coord[2]==door_coord[0]-10 and player_coord[3]<wall_door_coord[1] and player_coord[1]:
                        sound_win()
                        win_()
                if key_coord:
                    if player_coord[2]==key_coord[0]-10 and player_coord[3]<wall_key_coord[1] and player_coord[1]>70:
                        canvas.delete(key)
                        sound_bonmd()
                if bomR1_coord:
                    if player_coord[2]==bomR1_coord[0]-10 and player_coord[3]>wall1_coord[1]:
                        canvas.delete(bomR1)
                        sound_bonmd()
                        processe.append('1')
                if coin9_coord:
                    if player_coord[2]==coin9_coord[0]-10 and player_coord[3]<wall1_coord[1]and player_coord[3]>wall3_coord[1]:
                        canvas.delete(coin9)
                        sound_coin()
                if coin10_coord:
                    if player_coord[2]==coin10_coord[0]-10 and player_coord[3]<wall1_coord[1]and player_coord[3]>wall3_coord[1]:
                        canvas.delete(coin10)
                        sound_coin()
                if coin11_coord:
                    if player_coord[2]==coin11_coord[0]-10 and player_coord[3]<wall1_coord[1]and player_coord[3]>wall3_coord[1]:
                        canvas.delete(coin11)
                        sound_coin()
                if coin6_coord:
                    if player_coord[2]==coin6_coord[0]-10 and player_coord[3]<wall3_coord[1] and player_coord[3]>200:
                        canvas.delete(coin6)
                        sound_coin()
                if coin7_coord:
                    if player_coord[2]==coin7_coord[0]-10 and player_coord[3]<wall3_coord[1] and player_coord[3]>200:
                        canvas.delete(coin7)
                        sound_coin()
                if coin8_coord:
                    if player_coord[2]==coin8_coord[0]-10 and player_coord[3]<wall3_coord[1] and player_coord[3]>200:
                        canvas.delete(coin8)
                        sound_coin()
                if bomR2_coord:
                    if player_coord[2]==bomR2_coord[0]-10 and player_coord[3]<wall2_coord[1] and player_coord[3]>200:
                        canvas.delete(bomR2)
                        sound_bonmd()
                        processe.append('1')
                if coin1_coord:
                    if player_coord[2]==coin1_coord[0]-10 and player_coord[3]<wall2_coord[1] and player_coord[3]>200:
                        canvas.delete(coin1)
                        sound_coin()
                if coin2_coord:
                    if player_coord[2]==coin2_coord[0]-10 and player_coord[3]<wall2_coord[1] and player_coord[3]>200:
                        canvas.delete(coin2)
                        sound_coin()
                if bomR3_coord:
                    if player_coord[2]==bomR3_coord[0]-10 and player_coord[3]<wall3_coord[1] and player_coord[3]>200:
                        canvas.delete(bomR3)
                        sound_bonmd()
                        processe.append('1')
                if bomR4_coord:
                    if player_coord[2]==bomR4_coord[0]-10 and player_coord[3]<wall4_coord[1] and player_coord[3]>100:
                        canvas.delete(bomR4)
                        sound_bonmd()
                        processe.append('1')
                if coin4_coord:
                    if player_coord[2]==coin4_coord[0]-10 and player_coord[3]<wall4_coord[1] and player_coord[3]>100:
                        canvas.delete(coin4)
                        sound_coin()
                if coin5_coord:
                    if player_coord[2]==coin5_coord[0] -10 and player_coord[3]<wall4_coord[1] and player_coord[3]>100:
                        canvas.delete(coin5)
                        sound_coin()
            if check_movement(x,0):
                canvas.move(player, x, 0)
            if "space" in keyPressed and not check_movement(0,GRAVITY_FORCE):
                jump(30)
            medaim_window.after(TIME, move)

    def stop_move(event):
        global keyPressed
        if event.keysym in keyPressed:
            keyPressed.remove(event.keysym)

    def gravity():
        if check_movement(0, GRAVITY_FORCE):
            canvas.move(player,0, GRAVITY_FORCE)
        medaim_window.after(TIME, gravity)

    gravity()
    settimes_()
    medaim_window.bind("<Key>", start_move)
    medaim_window.bind("<KeyRelease>", stop_move)
    medaim_window.mainloop()
root.after(100, update_progress, 0)

root.mainloop()