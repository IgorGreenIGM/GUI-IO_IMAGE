#coding:utf-8

import tkinter
import pathlib
import subprocess
from ctypes import windll
from tkinter import filedialog, messagebox, scrolledtext, ttk


output_dir = ""
file_names = [] # contain all the slected files names

text_bckgrd_color = "#273136"; text_forgrd_color = "white"
label_bckgrd_color = "#001d26" ; label_forgrd_color = "#00c8ff"
#------------------------------------------------------------------------------------------------------------------------------------------------
def open_files() -> None:
    count_added = 0
    global files_frame; global log_text
    files_list['state'] = 'normal'
    
    files_list.delete('1.0', tkinter.END)
    for name in filedialog.askopenfilenames() :
        if name.lower().endswith('.png'):
            if name not in file_names:
                if not ' ' in name:
                    file_names.append(name)
                else:
                    file_names.append("\"" + name + "\"")
                count_added += 1

    i = 0
    for name in file_names:
        files_list.insert('end', f"{i+1} - {name}\n")
        i += 1

    files_list['state'] = 'disable'

    log_text['state'] = 'normal'
    log_text.insert('1.0', f'succefully added {count_added} png files\n')
    log_text.insert('1.0', f'total number of png files loaded : {len(file_names)}\n')
    log_text['state'] = 'disable'

    """
    Add an updater to logs ie specify the number of files added. it's necessary to add a counter for added files
    """

def selec_out_dir() -> None:
    global output_dir; global log_text
    output_dir = filedialog.askdirectory()
    log_text['state'] = 'normal'
    log_text.insert('1.0', f'Output folder : {output_dir}\n')
    log_text['state'] = 'disable'


def output_paths() -> list[str]:
    global output_dir
    global file_names
    # concat the output directory + file name
    out_paths = []
    for name in file_names:
            if name.endswith('"'):
                out_paths.append(f"\"{output_dir}/{name.split('/')[-1]}") #for paths containing spaces, must be contained in " "
            else:
                out_paths.append(f"{output_dir}/{name.split('/')[-1]}")
    
    return out_paths

def about() -> None:
    
    about = tkinter.Toplevel(app)
    about.title("About Author")
    about.resizable(False, False)

    creator_img = tkinter.PhotoImage(file="./Images/igm.png").subsample(4)
    about_img = tkinter.Label(about)
    about_img['image'] = creator_img
    about_img.grid(row=0, column=0)

    about_text_f = tkinter.LabelFrame(about, text='Contact')
    tkinter.Label(about_text_f, text="igormogou86@gmail.com", font=('Consolas', 8, 'bold')).grid(sticky='nw')
    tkinter.Label(about_text_f, text="license Creative Commons", font=('Consolas', 8, 'bold')).grid(sticky='nw')
    tkinter.Label(about_text_f, text="https://github.com/igorgreenIGM", font=('Consolas', 8, 'bold')).grid(sticky='nw')

    about_text_f.grid(row=0, column=1)
    about.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------
def rgba_to_rgb():
    out = output_paths()

def rgb_to_grayscale():
    out = output_paths()

    settings = tkinter.Toplevel(app, background="#001d26")
    settings.title("RGB to Grayscale")
    settings.resizable(False, False) 
    settings.geometry(f"+{app.winfo_screenmmwidth() // 2}+{app.winfo_screenheight() // 2}")

    tk_graylevel = tkinter.IntVar()
    param_frame = tkinter.LabelFrame(settings, text='Action Parameters', background=label_bckgrd_color, foreground=label_forgrd_color)
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=0, sticky='sw') # Separation
    tkinter.Label(param_frame, text="Gray Level :     ", background=label_bckgrd_color, foreground="white").grid(row=1, column=0, sticky='w')
    tkinter.Scale(param_frame, from_=0, to=3, orient='horizontal', background=label_bckgrd_color, foreground=label_forgrd_color, length=200, variable=tk_graylevel).grid(row=1, column=1, sticky='nw')
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=2, sticky='sw') # Separation    
    
    graylevel = 0
    def valid() -> None:
        global graylevel
        graylevel = tk_graylevel.get()
        settings.destroy()

    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=2, column=0, sticky='sw') # Separation
    tkinter.Button(param_frame, background=text_bckgrd_color, foreground=text_forgrd_color, command=valid, width=20, text="OK").grid(row=3, column=0, columnspan=2, sticky='s')
    param_frame.grid()
    settings.mainloop()

def grayscale_to_binary():
    out = output_paths()
#------------------------------------------------------------------------------------------------------------------------------------------------ 

def mean_blur():
    out = output_paths()

    settings = tkinter.Toplevel(app, background="#001d26")
    settings.title("Mean Blur")
    settings.resizable(False, False) 
    settings.geometry(f"+{app.winfo_screenmmwidth() // 2}+{app.winfo_screenheight() // 2}")

    tk_neighbours = tkinter.IntVar()
    param_frame = tkinter.LabelFrame(settings, text='Action Parameters', background=label_bckgrd_color, foreground=label_forgrd_color)
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=0, sticky='sw') # Separation
    tkinter.Label(param_frame, text="Neighbours :     ", background=label_bckgrd_color, foreground="white").grid(row=1, column=0, sticky='w')
    tkinter.Scale(param_frame, from_=1, to=100, orient='horizontal', background=label_bckgrd_color, foreground=label_forgrd_color, length=200, variable=tk_neighbours).grid(row=1, column=1, sticky='nw')
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=2, sticky='sw') # Separation    
    
    neighbours = 0
    def valid() -> None:
        global neighbours
        neighbours = tk_neighbours.get()
        settings.destroy()

    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=2, column=0, sticky='sw') # Separation
    tkinter.Button(param_frame, background=text_bckgrd_color, foreground=text_forgrd_color, command=valid, width=20, text="OK").grid(row=3, column=0, columnspan=2, sticky='s')
    param_frame.grid()
    settings.mainloop()

def gaussian_blur():
    out = output_paths()

    settings = tkinter.Toplevel(app, background="#001d26")
    settings.title("Gaussian Blur")
    settings.resizable(False, False) 
    settings.geometry(f"+{app.winfo_screenmmwidth() // 2}+{app.winfo_screenheight() // 2}")

    tk_sigma = tkinter.DoubleVar()
    tk_neighbours = tkinter.IntVar()
    param_frame = tkinter.LabelFrame(settings, text='Action Parameters', background=label_bckgrd_color, foreground=label_forgrd_color)
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=0, sticky='sw') # Separation
    tkinter.Label(param_frame, text="Sigma :     ", background=label_bckgrd_color, foreground="white").grid(row=1, column=0, sticky='w')
    tkinter.Scale(param_frame, from_=0.1, to=20, resolution=0.1, orient='horizontal', background=label_bckgrd_color, foreground=label_forgrd_color, length=200, variable=tk_sigma).grid(row=1, column=1, sticky='nw')
    tkinter.Label(param_frame, text="Neighbours :     ", background=label_bckgrd_color, foreground="white").grid(row=2, column=0, sticky='w')
    tkinter.Scale(param_frame, from_=1, to=100, orient='horizontal', background=label_bckgrd_color, foreground=label_forgrd_color, length=200, variable=tk_neighbours).grid(row=2, column=1, sticky='nw')
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=3, column=2, sticky='sw') # Separation    
    param_frame.grid()

    sigma = 0.0; neighbours = 0; 
    def valid() -> None:
        global sigma; global neighbours
        sigma = tk_sigma.get()
        neighbours = tk_neighbours.get()
        settings.destroy()

    tkinter.Button(param_frame, background=text_bckgrd_color, foreground=text_forgrd_color, command=valid, width=20, text="OK").grid(row=4, column=0, columnspan=2, sticky='s')
    settings.mainloop()
    

def partial_blur_coord():
    out = output_paths()

    settings = tkinter.Toplevel(app, background="#001d26")
    settings.title("Partial Gaussian Blur")
    settings.resizable(False, False) 
    settings.geometry(f"+{app.winfo_screenmmwidth() // 2}+{app.winfo_screenheight() // 2}")

    tk_sigma = tkinter.DoubleVar()
    tk_neighbours = tkinter.IntVar()
    blur_param_frame = tkinter.LabelFrame(settings, text='Blur Parameters', background=label_bckgrd_color, foreground=label_forgrd_color)
    tkinter.Label(blur_param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=0, sticky='sw') # Separation
    tkinter.Label(blur_param_frame, text="Sigma :     ", background=label_bckgrd_color, foreground="white").grid(row=1, column=0, sticky='w')
    tkinter.Scale(blur_param_frame, from_=0.1, to=20, resolution=0.1, orient='horizontal', background=label_bckgrd_color, foreground=label_forgrd_color, length=200, variable=tk_sigma).grid(row=1, column=1, sticky='nw')
    tkinter.Label(blur_param_frame, text="Neighbours :     ", background=label_bckgrd_color, foreground="white").grid(row=2, column=0, sticky='w')
    tkinter.Scale(blur_param_frame, from_=1, to=100, orient='horizontal', background=label_bckgrd_color, foreground=label_forgrd_color, length=200, variable=tk_neighbours).grid(row=2, column=1, sticky='nw')
    blur_param_frame.grid()

    tk_coords = [tkinter.IntVar() for i in range(4)]
    coord_frame = tkinter.LabelFrame(settings, text="Coordinates", background=label_bckgrd_color, foreground=label_forgrd_color)
    tkinter.Label(coord_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=0, sticky='sw') # Separation
    tkinter.Label(coord_frame, text="X start : ", background=label_bckgrd_color, foreground="white").grid(row=1, column=0)
    tkinter.Spinbox(coord_frame, width=18, background=label_bckgrd_color, foreground=label_forgrd_color, textvariable=tk_coords[0], from_=0, to=99999).grid(row=1, column=1)
    tkinter.Label(coord_frame, text="Y start : ", background=label_bckgrd_color, foreground="white").grid(row=2, column=0)
    tkinter.Spinbox(coord_frame, width=18, background=label_bckgrd_color, foreground=label_forgrd_color, textvariable=tk_coords[1], from_=0, to=99999).grid(row=2, column=1)
    tkinter.Label(coord_frame, text="X end  : ", background=label_bckgrd_color, foreground="white").grid(row=3, column=0)
    tkinter.Spinbox(coord_frame, width=18, background=label_bckgrd_color, foreground=label_forgrd_color, textvariable=tk_coords[2], from_=0, to=99999).grid(row=3, column=1)
    tkinter.Label(coord_frame, text="Y end  : ", background=label_bckgrd_color, foreground="white").grid(row=4, column=0)
    tkinter.Spinbox(coord_frame, width=18, background=label_bckgrd_color, foreground=label_forgrd_color, textvariable=tk_coords[3], from_=0, to=99999).grid(row=4, column=1)
    coord_frame.grid()

    sigma = 0.0; neighbours = 0; coords = []
    def valid() -> None:
        try:
            global sigma; sigma = tk_sigma.get()
            global neighbours; neighbours = tk_neighbours.get()
            global coords; coords = [tk_coords[i].get() for i in range(4)]
        except:
            messagebox.showerror(title="File type error", message="Please assure that all coords fields are completed")
        else:
            settings.destroy()

    tkinter.Label(coord_frame, text=" ", background=label_bckgrd_color).grid(row=5, column=0, sticky='sw') # Separation
    tkinter.Button(coord_frame, background=text_bckgrd_color, foreground=text_forgrd_color, command=valid, width=20, text="OK").grid(row=6, column=0, columnspan=2, sticky='s')
    settings.mainloop()


def partial_blur_bin():
    out = output_paths()

    settings = tkinter.Toplevel(app, background="#001d26")
    settings.title("Gaussian Blur")
    settings.resizable(False, False) 
    settings.geometry(f"+{app.winfo_screenmmwidth() // 2}+{app.winfo_screenheight() // 2}")

    binary_img = ""
    def bin_path() -> None:
        global binary_img
        binary_img = filedialog.askopenfilename(defaultextension='.png')

    tk_sigma = tkinter.DoubleVar()
    tk_neighbours = tkinter.IntVar()
    param_frame = tkinter.LabelFrame(settings, text='Action Parameters', background=label_bckgrd_color, foreground=label_forgrd_color)
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=0, sticky='sw') # Separation
    tkinter.Label(param_frame, text="Sigma :     ", background=label_bckgrd_color, foreground="white").grid(row=1, column=0, sticky='w')
    tkinter.Scale(param_frame, from_=0.1, to=20, resolution=0.1, orient='horizontal', background=label_bckgrd_color, foreground=label_forgrd_color, length=200, variable=tk_sigma).grid(row=1, column=1, sticky='nw')
    tkinter.Label(param_frame, text="Neighbours :     ", background=label_bckgrd_color, foreground="white").grid(row=2, column=0, sticky='w')
    tkinter.Scale(param_frame, from_=1, to=100, orient='horizontal', background=label_bckgrd_color, foreground=label_forgrd_color, length=200, variable=tk_neighbours).grid(row=2, column=1, sticky='nw')
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=3, column=0, sticky='sw') # Separation
    tkinter.Button(param_frame, background=text_bckgrd_color, foreground=text_forgrd_color, text="Select Binary File", width=20, command=bin_path).grid(row=4, column=0, columnspan=2)
    param_frame.grid()

    sigma = 0.0; neighbours = 0
    def valid() -> None:
        try:
            global sigma; global neighbours
            global binary_img
            type(binary_img)
        except:
            messagebox.showerror(title='error', message='Please select a PNG file for binary input')
        else:
            sigma = tk_sigma.get()
            neighbours = tk_neighbours.get()
            if binary_img != '':
                if binary_img.endswith('.png'):
                    settings.destroy()
                    print('sigma=', sigma, 'neighbours=', neighbours, 'binary path=', binary_img)
                else:
                    messagebox.showerror(title='error', message='Please select a PNG file for binary input')
            else:
                messagebox.showerror(title='error', message='Please select a file for binary input')

    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=5, column=0, sticky='sw') # Separation
    tkinter.Button(param_frame, background=text_bckgrd_color, foreground=text_forgrd_color, command=valid, width=20, text="OK").grid(row=6, column=0, columnspan=2, sticky='s')
    settings.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------ 
def downscale() -> None:
    out = output_paths()

    settings = tkinter.Toplevel(app, background="#001d26")
    settings.title("Downscale")
    settings.resizable(False, False) 
    settings.geometry(f"+{app.winfo_screenmmwidth() // 2}+{app.winfo_screenheight() // 2}")

    tk_scale = tkinter.IntVar()
    param_frame = tkinter.LabelFrame(settings, text='Action Parameters', background=label_bckgrd_color, foreground=label_forgrd_color)
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=0, sticky='sw') # Separation
    tkinter.Label(param_frame, text="Scale :     ", background=label_bckgrd_color, foreground="white").grid(row=1, column=0, sticky='w')
    tkinter.Spinbox(param_frame, from_=1, to=1000, background=label_bckgrd_color, foreground=label_forgrd_color, textvariable=tk_scale).grid(row=1, column=1, sticky='nw')
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=2, sticky='sw') # Separation    
    
    scale = 0
    def valid() -> None:
        global scale
        scale = tk_scale.get()
        settings.destroy()

    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=2, column=0, sticky='sw') # Separation
    tkinter.Button(param_frame, background=text_bckgrd_color, foreground=text_forgrd_color, command=valid, width=20, text="OK").grid(row=3, column=0, columnspan=2, sticky='s')
    param_frame.grid()
    settings.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------ 
def png_compress() -> None:
    out = output_paths()

    settings = tkinter.Toplevel(app, background="#001d26")
    settings.title("Compress PNG")
    settings.resizable(False, False)
    settings.geometry(f"+{app.winfo_screenmmwidth() // 2}+{app.winfo_screenheight() // 2}")

    tk_complvl = tkinter.IntVar()
    param_frame = tkinter.LabelFrame(settings, text='Action Parameters', background=label_bckgrd_color, foreground=label_forgrd_color)
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=0, sticky='sw') # Separation
    tkinter.Label(param_frame, text="Compress Level :     ", background=label_bckgrd_color, foreground="white").grid(row=1, column=0, sticky='w')
    tkinter.Scale(param_frame, from_=0, to=3, orient='horizontal', background=label_bckgrd_color, foreground=label_forgrd_color, length=200, variable=tk_complvl).grid(row=1, column=1, sticky='nw')
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=2, sticky='sw') # Separation    

    def valid() -> None:
        global log_text
        global file_names 
        global progress_bar

        settings.destroy() # closing the param tab...
        log_text['state'] = 'normal'
        for i in range(len(file_names)):
            try:
                result = subprocess.check_output(f"io.exe -in {file_names[i]} -out {out[i]} -cpng {tk_complvl.get()}")
            except:
                log_text.insert('1.0', f"Error, cannot perform compression on the file {i+1}\n")
            else:
                # log_text.insert('1.0', "File {} succefully compressed. Compress ratio : {:.2f}%\n".format(i+1, (pathlib.Path(out[i]).stat().st_size / (pathlib.Path(file_names[i])).stat().st_size) * 100))
                if (result.decode('utf-8') == "success"):
                    progress_bar['value'] = (i + 1) * 100 / len(file_names)
                    progress_bar.update()
                else:
                    pass # future treatment here
        
        log_text['state'] = 'disable'

                
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=2, column=0, sticky='sw') # Separation
    tkinter.Button(param_frame, background=text_bckgrd_color, foreground=text_forgrd_color, command=valid, width=20, text="OK").grid(row=3, column=0, columnspan=2, sticky='s')
    param_frame.grid()
    settings.mainloop()


#------------------------------------------------------------------------------------------------------------------------------------------------ 
def edge_detect() -> None:
    out = output_paths()

    settings = tkinter.Toplevel(app, background="#001d26")
    settings.title("Edge Detection")
    settings.resizable(False, False) 
    settings.geometry(f"+{app.winfo_screenmmwidth() // 2}+{app.winfo_screenheight() // 2}")

    tk_iters = tkinter.IntVar()
    param_frame = tkinter.LabelFrame(settings, text='Action Parameters', background=label_bckgrd_color, foreground=label_forgrd_color)
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=0, sticky='sw') # Separation
    tkinter.Label(param_frame, text="Iterations :     ", background=label_bckgrd_color, foreground="white").grid(row=1, column=0, sticky='w')
    tkinter.Spinbox(param_frame, from_=1, to=100, background=label_bckgrd_color, foreground=label_forgrd_color, textvariable=tk_iters).grid(row=1, column=1, sticky='nw')
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=2, sticky='sw') # Separation    
    
    iters = 0
    def valid() -> None:
        global iters
        iters = tk_iters.get()
        settings.destroy()

    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=2, column=0, sticky='sw') # Separation
    tkinter.Button(param_frame, background=text_bckgrd_color, foreground=text_forgrd_color, command=valid, width=20, text="OK").grid(row=3, column=0, columnspan=2, sticky='s')
    param_frame.grid()
    settings.mainloop()


def histogram() -> None:
    out = output_paths()

def files_info() -> None:
    global file_names
    global analyse_text
    global log_text

    files = ",".join(file_names)

    log_text['state'] = 'normal'
    analyse_text['state'] = 'normal'

    try:
        analyse_text.insert('1.0', f"{subprocess.check_output(f'io.exe -in {files} -out {files} -infos').decode('utf-8')}")
    except:
        log_text.insert('1.0', "Error, cannot perform information retrievment... maybe the files list is empty or thre's a non-compatible image ?\n")
    else:
        log_text.insert('1.0', "Informations have been succefully parsed\n")

    log_text['state'] = 'disable'
    analyse_text['state'] = 'disable'

def colors_nb() -> None:
    out = output_paths()

def redundant_colors() -> None:
    out = output_paths()

    settings = tkinter.Toplevel(app, background="#001d26")
    settings.title("Redundant Colors")
    settings.resizable(False, False) 
    settings.geometry(f"+{app.winfo_screenmmwidth() // 2}+{app.winfo_screenheight() // 2}")

    tk_occ = tkinter.IntVar()
    param_frame = tkinter.LabelFrame(settings, text='Action Parameters', background=label_bckgrd_color, foreground=label_forgrd_color)
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=0, sticky='sw') # Separation
    tkinter.Label(param_frame, text="Colors Number :     ", background=label_bckgrd_color, foreground="white").grid(row=1, column=0, sticky='w')
    tkinter.Spinbox(param_frame, from_=1, to=99999, background=label_bckgrd_color, foreground=label_forgrd_color, textvariable=tk_occ).grid(row=1, column=1, sticky='nw')
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=2, sticky='sw') # Separation    
    
    occ = 0
    def valid() -> None:
        global occ
        occ = tk_occ.get()
        print("occs=", occ)
        settings.destroy()

    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=2, column=0, sticky='sw') # Separation
    tkinter.Button(param_frame, background=text_bckgrd_color, foreground=text_forgrd_color, command=valid, width=20, text="OK").grid(row=3, column=0, columnspan=2, sticky='s')
    param_frame.grid()
    settings.mainloop()

def kmean_domiant() -> None:
    out = output_paths()

    settings = tkinter.Toplevel(app, background="#001d26")
    settings.title("Dominant Colors")
    settings.resizable(False, False) 
    settings.geometry(f"+{app.winfo_screenmmwidth() // 2}+{app.winfo_screenheight() // 2}")

    tk_occ = tkinter.IntVar()
    tk_iters = tkinter.IntVar()
    param_frame = tkinter.LabelFrame(settings, text='Action Parameters', background=label_bckgrd_color, foreground=label_forgrd_color)
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=0, column=0, sticky='sw') # Separation
    tkinter.Label(param_frame, text="Colors Number :     ", background=label_bckgrd_color, foreground="white").grid(row=1, column=0, sticky='w')
    tkinter.Spinbox(param_frame, from_=1, to=9999, background=label_bckgrd_color, foreground=label_forgrd_color, textvariable=tk_occ).grid(row=1, column=1, sticky='nw')
    tkinter.Label(param_frame, text="Iterations :     ", background=label_bckgrd_color, foreground="white").grid(row=2, column=0, sticky='w')
    tkinter.Spinbox(param_frame, from_=1, to=100, background=label_bckgrd_color, foreground=label_forgrd_color, textvariable=tk_iters).grid(row=2, column=1, sticky='nw')
    tkinter.Label(param_frame, text=" ", background=label_bckgrd_color).grid(row=3, column=2, sticky='sw') # Separation    
    param_frame.grid()

    occ = 0; iters = 0
    def valid() -> None:
        global occ; global iters
        occ = tk_occ.get()
        iters = tk_iters.get()
        print("occ=", occ, ' iters=', iters)
        settings.destroy()

    tkinter.Button(param_frame, background=text_bckgrd_color, foreground=text_forgrd_color, command=valid, width=20, text="OK").grid(row=4, column=0, columnspan=2, sticky='s')
    settings.mainloop()


# setting windows parameters
windll.shcore.SetProcessDpiAwareness(1) #define HD 4k mode for high res screen

app = tkinter.Tk("IO IMAGE")
app.title("IO IMAGE")

"""
    _summary_ setting opening windows, for initialising settings in the back-end
"""
opening_frame = tkinter.Label(app)
back_img = tkinter.PhotoImage(file="./Images/Startup/g.png")
app.geometry(f"{back_img.width()}x{back_img.height()}+{(app.winfo_screenwidth() - back_img.width()) // 2}+{(app.winfo_screenheight() - back_img.height()) // 2}")
opening_frame['image'] = back_img
opening_frame.place(x=-2, y=-2) #centering the background image a little bit
app.resizable(False, False)

"""
    _summary_ Menu Define
"""
main_menu = tkinter.Menu(app)
menu_bckgrd = "#001d26"; menu_foregrd = "white"

file_menu = tkinter.Menu(main_menu, background=menu_bckgrd, foreground=menu_foregrd, tearoff=False)
#------------------------------------------------------------------------------------------------------------
file_menu.add_command(label="Open", background=menu_bckgrd, foreground=menu_foregrd, command=open_files)
file_menu.add_command(label="Select Output Folder", background=menu_bckgrd, foreground=menu_foregrd, command=selec_out_dir)
file_menu.add_separator()
file_menu.add_command(label="About", background=menu_bckgrd, foreground=menu_foregrd, command=about)
file_menu.add_separator()
file_menu.add_command(label="Quit", background=menu_bckgrd, foreground=menu_foregrd, command=app.destroy)

action_menu = tkinter.Menu(main_menu, background=menu_bckgrd, foreground=menu_foregrd, tearoff=False)
# ------------------------------------------------------------------------------------------------------------
# Blur Section
blur_submenu = tkinter.Menu(action_menu, background=menu_bckgrd, foreground=menu_foregrd, tearoff=False)
action_menu.add_cascade(label="Blur", menu=blur_submenu, foreground=menu_foregrd)
blur_submenu.add_command(label="Mean Blur", background=menu_bckgrd, foreground=menu_foregrd, command=mean_blur)
blur_submenu.add_command(label="Guassian Blur", background=menu_bckgrd, foreground=menu_foregrd, command=gaussian_blur)
blur_submenu.add_separator()
blur_submenu.add_command(label="Partial Gaussian Blur (Binary)", background=menu_bckgrd, foreground=menu_foregrd, command=partial_blur_bin)
blur_submenu.add_command(label="Partial Gaussian Blur (Coords)", background=menu_bckgrd, foreground=menu_foregrd, command=partial_blur_coord)

# Convert Section
convert_submenu = tkinter.Menu(action_menu, background=menu_bckgrd, foreground=menu_foregrd, tearoff=False)
action_menu.add_cascade(label="Convert", menu=convert_submenu, foreground=menu_foregrd)
convert_submenu.add_command(label="RGBA -> RGB", background=menu_bckgrd, foreground=menu_foregrd, command=rgba_to_rgb)
convert_submenu.add_command(label="RGB -> Grayscale", background=menu_bckgrd, foreground=menu_foregrd, command=rgb_to_grayscale) # when implementing, detect if the image is RGB or RGBA
convert_submenu.add_command(label="Grayscale -> Binary", background=menu_bckgrd, foreground=menu_foregrd, command=grayscale_to_binary)

action_menu.add_command(label="Downscale", background=menu_bckgrd, foreground=menu_foregrd, command=downscale)
action_menu.add_command(label="Edge Detection", background=menu_bckgrd, foreground=menu_foregrd, command=edge_detect)
action_menu.add_command(label="Compress PNG", background=menu_bckgrd, foreground=menu_foregrd, command=png_compress)

analyse_menu = tkinter.Menu(main_menu, background=menu_bckgrd, foreground=menu_foregrd, tearoff=False)
#------------------------------------------------------------------------------------------------------------
analyse_menu.add_command(label="Histogram", background=menu_bckgrd, foreground=menu_foregrd, command=histogram); analyse_menu.add_separator()
analyse_menu.add_command(label="Files Infos", background=menu_bckgrd, foreground=menu_foregrd, command=files_info); analyse_menu.add_separator()
analyse_menu.add_command(label="Colors Number", background=menu_bckgrd, foreground=menu_foregrd, command=colors_nb)
analyse_menu.add_command(label="Redundant Colors", background=menu_bckgrd, foreground=menu_foregrd, command=redundant_colors)
analyse_menu.add_command(label="Dominant Colors : K-mean", background=menu_bckgrd, foreground=menu_foregrd, command=kmean_domiant)

main_menu.add_cascade(label="File", menu=file_menu, background=menu_bckgrd, foreground=menu_foregrd)
main_menu.add_cascade(label="Action", menu=action_menu, background=menu_bckgrd, foreground=menu_foregrd)
main_menu.add_cascade(label="Analysis", menu=analyse_menu, background=menu_bckgrd, foreground=menu_foregrd)
app.config(menu=main_menu)


files_frame = tkinter.LabelFrame(app, text="Input Images", background=text_bckgrd_color, foreground=text_forgrd_color)
ttk.Label(files_frame, text=" ", background=text_bckgrd_color).grid(sticky='nw') # Separation
files_list = scrolledtext.ScrolledText(files_frame, background=menu_bckgrd, foreground=menu_foregrd, state='disable')
files_list.grid()
files_frame.grid(row=0, column=0)


progress_frame = tkinter.LabelFrame(app, text="Progression Status", background=text_bckgrd_color, foreground=text_forgrd_color)
ttk.Label(progress_frame, text=" ", background=text_bckgrd_color).grid(sticky='nw') # Separation
progress_bar = ttk.Progressbar(progress_frame, length=1325, variable=0)
progress_bar.grid(sticky='nw')
progress_frame.grid(row=1, column=0, sticky='nw')

logs_frame = tkinter.LabelFrame(app, text="Logs", background=text_bckgrd_color, foreground=text_forgrd_color)
log_text = scrolledtext.ScrolledText(logs_frame, background=menu_bckgrd, foreground=menu_foregrd, state='disable', height=1)
log_text.grid(row=0, column=0, sticky='nw')
logs_frame.grid(row=2, column=0)

analyse_frame = tkinter.LabelFrame(app, text="Analyses", background=text_bckgrd_color, foreground=text_forgrd_color)
analyse_text = scrolledtext.ScrolledText(analyse_frame, background=menu_bckgrd, foreground=menu_foregrd, state='disable', width=29, height=33, )
analyse_text.grid(row=0, column=0, sticky='nw')
analyse_frame.grid(row=0, column=1, sticky='nw', rowspan=3)

app.mainloop()