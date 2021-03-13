import tkinter as tk
from PIL import Image, ImageTk
import math
from preset import Preset
from boss import Boss

class Menu:

    # init

    def __init__(self, menu = None, preset = None):

        # read preset
        self.current_preset_line = int(open('data/config.txt', 'r').read().split('\n')[0].split(', ')[1])
        if self.current_preset_line >= len(Preset.preset_list):
            self.current_preset_line = 0

        # main menu
        self.change_menu('main')

    # general functions

    def clear_menu(self):
        for widget in root.winfo_children():
            widget.destroy()

    def change_menu(self, menu):

        self.clear_menu()

        if menu == 'main':
            self.construct_main_menu()
        
        if menu == 'presets':
            self.construct_presets_menu()

        if menu == 'newpreset':
            self.construct_new_preset_menu()
        
        if menu == 'editpreset':
            self.construct_edit_preset_menu()

    # main menu

    def construct_main_menu(self):
        # frames
        self.top_frame = tk.Frame(root, bg='white', height=100, width=600)
        self.mid_frame = tk.Frame(root, bg='white', height=400, width=600)
        self.bot_frame = tk.Frame(root, bg='white', height=100, width=600)
        self.top_frame.pack_propagate(0)
        self.mid_frame.pack_propagate(0)
        self.bot_frame.pack_propagate(0)
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

        # title text
        self.title_text = tk.Label(self.top_frame, text=Preset.preset_list[self.current_preset_line].name, font=('bold', '25'), height=100, bg='white')
        self.title_text.pack()

        # choose boss button
        self.choose_boss = tk.Button(self.bot_frame, text="Choose Boss", command=self.choose_boss_command, font=('bold', '20'))
        self.choose_boss.place(x=66.67, y=17.5, width=200, height=65)

        # select bosses button
        self.select_presets = tk.Button(self.bot_frame, text="Select Preset", command=self.select_presets_command, font=('bold', '20'))
        self.select_presets.place(x=333.33, y=17.5, width=200, height=65)

    def choose_boss_command(self):

        boss = Preset.get_boss(self.current_preset_line)

        for widget in self.mid_frame.winfo_children():
            widget.destroy()

        image = Image.open(boss.dir)
        image = image.resize((math.floor(image.width * 300 / image.height), 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)

        img_label = tk.Label(self.mid_frame, image=img, bg='white')
        img_label.photo = img
        img_label.winfo_width()
        img_label.place(x=300-img_label.winfo_reqwidth()/2,y=20)

        img_text = tk.Label(self.mid_frame, text=boss.name, font=('bold', '20'), bg='white')
        img_text.place(x=300-img_text.winfo_reqwidth()/2, y=320+img_text.winfo_reqheight()/2)

    def select_presets_command(self):
        self.change_menu('presets')

    # preset menu

    def construct_presets_menu(self):
        # frames
        self.top_frame = tk.Frame(root, bg='white', height=500, width=600)
        self.bot_frame = tk.Frame(root, bg='white', height=100, width=600)
        self.top_frame.pack_propagate(0)
        self.bot_frame.pack_propagate(0)
        self.top_frame.pack()
        self.bot_frame.pack()
        
        # listbox
        self.presets_box = tk.Listbox(self.top_frame, selectmode="single", font=('bold', '20'))
        self.presets_box.place(x=30, y=30, width=520, height=440)
        self.update_presets()

        # scrollbar
        self.presets_scrollbar = tk.Scrollbar(self.top_frame)
        self.presets_scrollbar.place(x=550, y=30, width=20, height=440)

        self.presets_box.configure(yscrollcommand=self.presets_scrollbar.set)
        self.presets_scrollbar.configure(command=self.presets_box.yview)

        # select button
        self.select_button = tk.Button(self.bot_frame, text="Select", command=self.select_button_command, font=('bold', '18'))
        self.select_button.place(x=16.67, y=17.5, width=100, height=65)

        # new button
        self.new_button = tk.Button(self.bot_frame, text="New", command=self.new_button_command, font=('bold', '18'))
        self.new_button.place(x=133.34, y=17.5, width=100, height=65)

        # edit button
        self.edit_button = tk.Button(self.bot_frame, text="Edit", command=self.edit_button_command, font=('bold', '18'))
        self.edit_button.place(x=250.01, y=17.5, width=100, height=65)

        # delete button
        self.delete_button = tk.Button(self.bot_frame, text="Delete", command=self.delete_button_command, font=('bold', '18'))
        self.delete_button.place(x=366.68, y=17.5, width=100, height=65)

        # back button
        self.back_button = tk.Button(self.bot_frame, text="Back", command=self.back_button_command, font=('bold', '18'))
        self.back_button.place(x=483.35, y=17.5, width=100, height=65)

        self.update_presets()
    
    def select_button_command(self):
        self.current_preset_line = self.presets_box.curselection()[0]
        self.change_menu('main')

    def new_button_command(self):
        self.change_menu('newpreset')

    def edit_button_command(self):
        self.current_preset_id = self.presets_box.curselection()[0]
        self.change_menu('editpreset')

    def delete_button_command(self):
        deleted_id = self.presets_box.curselection()[0]
        if deleted_id <= self.current_preset_line:
            self.current_preset_line -= 1
        if self.current_preset_line < 1:
            self.current_preset_line = 1
        Preset.delete_preset(deleted_id)
        self.update_presets()

    def back_button_command(self):
        self.change_menu('main')

    def update_presets(self):
        self.presets_box.delete(0, self.presets_box.size())
        Preset.create_presets_list()
        for preset in Preset.preset_list:
            self.presets_box.insert('end', preset.name)
    
    # preset menu

    def construct_general_preset_menu(self):
        # frames
        self.top_frame = tk.Frame(root, bg='white', height=100, width=600)
        self.mid_frame = tk.Frame(root, bg='white', height=400, width=600)
        self.bot_frame = tk.Frame(root, bg='white', height=100, width=600)
        self.top_frame.pack_propagate(0)
        self.mid_frame.pack_propagate(0)
        self.bot_frame.pack_propagate(0)
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

        # tickboxes
        self.tickboxes = []
        self.intvars = []
        boss_list = Boss.all_bosses
        
        for x in range(0, len(boss_list)):
            self.intvars.append(tk.IntVar())
            self.tickboxes.append(tk.Checkbutton(self.mid_frame, text=boss_list[x].name, bg='#cccccc', variable=self.intvars[x]))

        max_width = 0
        max_height = 0
        for x in range(0, len(boss_list)):
            width = self.tickboxes[x].winfo_reqwidth()
            if width > max_width:
                max_width = width
            height = self.tickboxes[x].winfo_reqheight()
            if height > max_height:
                max_height = height

        xcount = 4
        xgap = round(600-(xcount * max_width))/(xcount+1)
        ycount = math.ceil(len(boss_list) / xcount)
        ygap = round(((400 - max_height * ycount)/(ycount+1)))
        
        for x in range(0, len(boss_list)):
            gridx = x%xcount
            gridy = math.floor(x/xcount)
            xpos = xgap + gridx * (max_width + xgap)
            ypos = ygap + gridy * (max_height + ygap)
            self.tickboxes[x].place(x=xpos, y=ypos, width=max_width)

        # back button
        self.back_to_preset = tk.Button(self.bot_frame, text="Back", command=self.back_to_preset_button_command, font=('bold', '20'))
        self.back_to_preset.place(x=333.33, y=17.5, width=200, height=65)

    def back_to_preset_button_command(self):
        self.change_menu('presets')

    # new preset menu

    def construct_new_preset_menu(self):
        self.construct_general_preset_menu()

        # preset name entry
        self.preset_name_entry = tk.Entry(self.top_frame, font=('bold', '20'))
        self.preset_name_entry.place(x=30, y=30, width=540, height=40)
        self.preset_name_entry.insert(0, 'Preset Name')

        # save preset button
        self.save_preset_button = tk.Button(self.bot_frame, text="Save Preset", command=self.save_preset_button_command, font=('bold', '20'))
        self.save_preset_button.place(x=66.67, y=17.5, width=200, height=65)

    def save_preset_button_command(self):
        idlist = ''
        for x in range(0, len(Boss.all_bosses)):
            if self.intvars[x].get() == 1:
                idlist += Boss.all_bosses[x].id
        name = self.preset_name_entry.get()
        Preset.create_preset(name, idlist)
        self.back_to_preset_button_command()

    # edit preset menu

    def construct_edit_preset_menu(self):
        self.construct_general_preset_menu()
        current_preset_boss_list = Preset.preset_list[self.current_preset_id].boss_list

        # preset name entry
        self.preset_name_entry = tk.Entry(self.top_frame, font=('bold', '20'))
        self.preset_name_entry.place(x=30, y=30, width=540, height=40)
        self.preset_name_entry.insert(0, Preset.preset_list[self.current_preset_id].name)

        # save preset button
        self.save_preset_button = tk.Button(self.bot_frame, text="Save Preset", command=self.save_preset_changes_button_command, font=('bold', '20'))
        self.save_preset_button.place(x=66.67, y=17.5, width=200, height=65)

        for x in range(0, len(current_preset_boss_list)):
            self.intvars[int(current_preset_boss_list[x].id)].set(1)

    def save_preset_changes_button_command(self):
        idlist = ''
        for x in range(0, len(Boss.all_bosses)):
            if self.intvars[x].get() == 1:
                idlist += Boss.all_bosses[x].id
        name = self.preset_name_entry.get()
        Preset.update_preset(name, self.current_preset_id, idlist)
        self.back_to_preset_button_command()

if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(0,0)
    
    m = Menu()

    root.title('Runescape Boss Selector')
    root.mainloop()
    f = open('data/config.txt', 'w').write('previous_preset, ' + str(m.current_preset_line))