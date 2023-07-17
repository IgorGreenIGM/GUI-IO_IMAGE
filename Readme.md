## Graphical User Interface wrapper for IO_IMAGE Framework

the purpose of this Gui is to wrap up the IO Image Image treatment Framework for automate task such as :
    - Raw Pixels Visualisation 
    - Converter :
        * RGBA to RGB
        * RGB to Grayscale
        * binarisation
    - Histogram ploting (using Ploter-flag- C module)
    - Pixels Buffer Analysis algorithms
    - Blur(Mean and Gaussian versions)
    - Edge detection
    - PNG compression
    - image Downscale

## todo, revesions and behavior :

function to downscale an image

fixes : 
added comment to tell that it's the user responsability to free the get_rawpixels() method result

fixes : 
added changed output of edge_detection method : the result is now a grayscale buffer instead of rgb buffer

Train a model that analysis conversations and give the common use of emojis vs their real signification

tkinter how to add space between frames

Add info bulle to explain each menu option (eg sigma, neigbours, iters, etc)
tkinter autoscroll a Scrolled text when text is added

## useful code for later
neighbours = simpledialog.askinteger(title="Neighbours radius", prompt="Please, \nSpecify the Number of neighbours Pixels radius\nNote :\n Bigger Neighbours = More blurred output")
if (neighbours == None):
    messagebox.showinfo(title='Error', message='Please,\n Enter the neighbours pixels radius')    

sigma = simpledialog.askfloat(title="Neighbours radius", prompt="Please, \nSpecify sigma param\nNote :\n smaller sigma = more neighbours pixels influence")
if (sigma == None):
    messagebox.showinfo(title='Error', message='Please,\n Enter the sigma value')    

## to do tomorrow : 
-> Arrange the menues popup settings
-> Set image inside the Gui windows after all the input images are selected
-> add an image info parser and displayer
-> add a scrollable images previews on the main window frame
-> set all images preview selectable
-> Add a select input folder option
-> directly open only png files instead of all get and exclude does that endswith ".png"
-> Add a better structure to source code
-> Add a Poo Approach for the source code 
