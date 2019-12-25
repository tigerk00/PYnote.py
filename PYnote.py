#Made By tigerk00


from tkinter import * # Импортируем всё из библиотеки tkinter
from tkinter import messagebox as mb # Импортируем messagebox для всплывающих дочерних окон 
from tkinter import filedialog as fd # Импортируем filedialog для возможности вывода ошибок и сообщений разного рода для пользователя 
import tkinter.font as font # Импортируем font для роботы со шрифтами (смена шрифта , размера , наклона , и т.д.)
import time as tm # Импортируем данную библиотеку для роботы со временем
import webbrowser # Эта библиотека для роботы с браузером 

# Следущие функции , как видно из названия , отвечают за смену шрифта при нажатии на  определенную команду в каскаде "Шрифты" 
def arial():
    myFont = font.Font(family='Arial ' )  
    text['font'] = myFont #  Обращаемся к виджету text , а именно к его свойству [font] , и меняем его  на значение , указаное в переменной myFont 
    
def comic_sans_ms():
    myFont = font.Font(family='Comic Sans MS')
    text['font'] = myFont

def courier_new():
    myFont = font.Font(family='Courier New')
    text['font'] = myFont
def fixedsys():
    myFont = font.Font(family='Fixedsys')
    text['font'] = myFont

def ms_sans_serif():
    myFont = font.Font(family='MS Sans Serif')
    text['font'] = myFont

def ms_serif():
    myFont = font.Font(family='MS Serif')
    text['font'] = myFont

def symbol():
    myFont = font.Font(family='Symbol')
    text['font'] = myFont

def system():
    myFont = font.Font(family='System')
    text['font'] = myFont

def times_new_roman():
    myFont = font.Font(family='Times New Roman')
    text['font'] = myFont

def verdana():
    myFont = font.Font(family='Verdana')
    text['font'] = myFont
    


# Следущие функции  отвечают за смену размера  шрифта при нажатии на  определенную команду в каскаде "Размер"
def size8():
    myFont = font.Font(size = 8) 
    text['font'] = myFont  # Обращаемся к виджету text , а именно к его свойству [font] , и меняем его  на значение , указаное в переменной myFont

def size10():
    myFont = font.Font(size = 10)
    text['font'] = myFont

def size11():
    myFont = font.Font(size = 11)
    text['font'] = myFont

def size12():
    myFont = font.Font(size = 12)
    text['font'] = myFont

def size14():
    myFont = font.Font(size = 14)
    text['font'] = myFont    

def size16():
    myFont = font.Font(size = 16)
    text['font'] = myFont

def size18():
    myFont = font.Font(size = 18)
    text['font'] = myFont

def size20():
    myFont = font.Font(size = 20)
    text['font'] = myFont

def size22():
    myFont = font.Font(size = 22)
    text['font'] = myFont

def size24():
    myFont = font.Font(size = 24)
    text['font'] = myFont    

def size26():
    myFont = font.Font(size = 26)
    text['font'] = myFont    

def size28():
    myFont = font.Font(size = 28)
    text['font'] = myFont    

def size30():
    myFont = font.Font(size = 30)
    text['font'] = myFont    

 
    
    

# В слудующих 2 переменных будет менятся толщина шрифта (полужирный/нормальный) , по пронципу , что использовался ранее 
def BoldFace():
    myFont = font.Font(weight = "bold")
    text['font'] = myFont

def Normal():
    myFont = font.Font(weight = "normal")
    text['font'] = myFont


# Тут меняем наклон (italic/roman)
def Italic():
    myFont = font.Font(slant = "italic")
    text['font'] = myFont

def Roman():
    myFont = font.Font(slant = 'roman')
    text['font'] = myFont


# Следущая функция отвечает за вывод сообщения пользователю , если он согласится  , будет запущена функция для перечеркивания текста
def overstrike_on():
    answer=mb.askyesno("Подтверждение", message="Вы хотите использовать перечеркивание(это заменит ваш шрифт на стандартный)?")
    if answer==True:
        myFont = font.Font(overstrike = 1) #по умолчанию значение = 0 , если она равно 1 , тогда текст будет перечеркнут
        text['font'] = myFont



#Функции night и day отвечают за активацию ночного и дневного режима соответственно
def night():
    text['bg'] = 'gray16'                   # Тут  меняем background color у  виджета text на gray16
    text['fg']  = "white smoke"             # ... И цвет текста

def day():
    text['bg'] = 'white' 
    text['fg'] = 'black' 


# Следущие функции отвечают за смену размера окна при нажатии на соответственную команду 
def wsize200():
    root.geometry('200x200')

def wsize300():
    root.geometry('300x200')

def wsize403():
    root.geometry('400x300')

def wsize503():
    root.geometry('500x300')


def wsize504():
    root.geometry('500x400')

def wsize505():
    root.geometry('500x500')

def wsize806():
    root.geometry('800x600')

def wsizestandart():
    root.geometry('600x400')

def wsize1006():
    root.geometry('1000x600')


# С помощью уже извесной нам библиотеки данная функция просто открывает нам поисковую систему Google
def search():
    webbrowser.open("www.google.com")






def insert_text():
    try:
        file_name=fd.askopenfilename() # С помощью "askopenfilename" вызываем всплывающее окно с запросом на открытые файла , который вы выберете
        f=open(file_name) # Открываем файл , который вы выбрали
        s=f.read() # Читаем его ...
        text.insert(1.0,s) # И после этого "вставляем его в наш текстовый редактор"
        f.close()
    except FileNotFoundError:
        mb.showinfo("Внимание", "Файл не загружен") # Если же вы не выбрали файл для открытия ,"перехватчик событий" покажет нам с помощью ".showinfo"   
                                                    # предупреждение о том , что файл не был загружен 

# Всплывающее окно для отображения времени
def messageWindow():
    
    win = Toplevel()
    win.resizable(height = False , width = False) # Размер окна невозможно изменить
    win.title(" Текущее время")  # название окна
    current_time = tm.strftime('%H:%M:%S ' + ' %d.%m.%Y' )  # Формат времени , в каком оно будет отображаться  
    clock_label = Label(win , font = 'system 15' , bg = 'black' , fg = 'red' , text = current_time) # Цвет текста(цифр) , Шрифт , Цвет фона , и присваивание ...
    clock_label.pack()                                                                              # ... тексту значения из предущей строки
    
   
    
    Button(win, text='OK', command=win.destroy).pack() # Кнопка "ОК" , при нажатии на которую , наше всплывающее окно из датою буддет уничтожено
    win.grab_set() # "Перехватчик" событий ( на клавиатуре , на мышке , и т.д.) , чтобы без закрытия дочернего окна , работать с текстовым редактором было нельзя
    win.focus_set() # Фокусировка на дочернем окне , опять-таки , чтобы без закрытия дочернего окна , работать с текстовым редактором было нельзя

# Функция , которая отвечает за сохранение файла 
def extract_text():
    try:
        file_name=fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),          # В скобках указываются возможные форматы для сохранения
                                              ("HTML files", "*.html; *.htm"),
                                              ("All files", "*.*")))
        f=open(file_name, 'w')
        s=text.get(1.0, END)
        f.write(s)
        f.close()
    except FileNotFoundError:
        mb.showinfo("Внимание", "Файл не сохранён")

# Функция для удаления всего текста у виджете text 
def delete_text():
    answer=mb.askyesno("Подтверждение", message="Вы хотите удалить текст?") 
    if answer==True:
        text.delete(0.0, END)    # При подтверждении своего действия текст удалится с начала вашего документа , с позиции 0.0 , до конца (END) .        

# Функция для выхода из прилжения 
def quit_text():
    q_answer = mb.askyesno("Подтверждение" , message = 'Вы уверенны , что хотите выйти?' )
    if q_answer==True:
        global root
        root.destroy()




root=Tk() # Создаём окно 
root.iconbitmap('D:\images\icons8.ico') # Тут идет присваивание окну картинки (которая находится за заданой директорией , у вас будет она другой)
root.title('PYnote') # Название окна
root.geometry('600x400') # Размер окна
root.resizable(height = False , width = False)
frame=Frame() # создаем фрейм 
frame.pack(fill='both',expand=True)
        
text=Text(frame, font='Arial 14', wrap='word') 
scrollbar=Scrollbar(frame) # вызываем  полосу прокрутки
scrollbar['command'] = text.yview # по оси у
text['yscrollcommand'] = scrollbar.set 
text.pack(side='left', fill='both', expand=True) # expand=True отвечает за распределение пространства между виджетами в случае увеличения род. окна
scrollbar.pack(side='right', fill='y')
frame.grid_columnconfigure(0,weight=1)  #привязывает ширину фрейма к размеру окна
frame.grid_rowconfigure(0,weight=1)  #привязывает высоту фрейма к размеру окна

mainmenu=Menu(root) # Создаем меню , родителем которого есть root
root.config(menu=mainmenu) # Утверждаем  данное действие  , присваиваем menu значение mainmenu
mainmenu.add_command(label="Открыть", command=insert_text ) #Создаем комманду , вписываем ее название , и функцию , которую она будет выполнять при нажатии на нее.
mainmenu.add_command(label="Сохранить", command=extract_text)



menu=Menu(tearoff=0) # tearoff=0  - по умолчании стоит 1 , если поставим 0 , тогда будет возможность  вызвать плавующее окно
menu.add_command(label="Очистить", command=delete_text)
text.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))


# Дальше идёт всё тоже самое , только меняются функции , которые вызываются при нажатии на команды и привязка Menu к другим  меню .
otherfile = Menu(mainmenu)
mainmenu.add_cascade(label = 'Другое..' , menu = otherfile)
otherfile.add_command(label= 'Ночная тема'  , command = night)
otherfile.add_command(label= 'Дневная тема'  , command = day)
otherfile.add_command(label = 'Текущее время' , command = messageWindow)
otherfile.add_command(label = 'Поиск с помощью поисковой системы Google' , command = search)
textfile = Menu(mainmenu)
mainmenu.add_cascade(label = 'Текст' , menu = textfile)

# Будьте внимательны -  несколько меню тут привязывается  к textfile , это говорит о том , что  при нажатии на Вкладку "Текст" , 
# мы увидим множество других подконтрольных меню , с которых сможем переходить и использовать другие команды.
file = Menu(textfile)
textfile.add_cascade(label = "Шрифты" , menu = file )
file.add_command(label = "Comic Sans MS" , command = comic_sans_ms)
file.add_command(label = "Arial" , command = arial)
file.add_command(label = "Courier New" , command = courier_new)
file.add_command(label = "Fixedsys" , command = fixedsys)
file.add_command(label = "MS Sans Serif" , command = ms_sans_serif)
file.add_command(label = "MS Serif" , command = ms_serif)
file.add_command(label = "Symbol" , command = symbol)
file.add_command(label = "System" , command = system)
file.add_command(label = "Times New Roman" , command = times_new_roman)
file.add_command(label = "Verdana" , command = verdana)



sizefile = Menu(textfile)
textfile.add_cascade(label = "Размер" , menu = sizefile)
sizefile.add_command(label = " 8 " , command = size8)
sizefile.add_command(label = " 10 " , command = size10)
sizefile.add_command(label = " 11 " , command = size11)
sizefile.add_command(label = " 12 " , command = size12)
sizefile.add_command(label = " 14 " , command = size14)
sizefile.add_command(label = " 16 " , command = size16)
sizefile.add_command(label = " 18 " , command = size18)
sizefile.add_command(label = " 20 " , command = size20)
sizefile.add_command(label = " 22 " , command = size22)
sizefile.add_command(label = " 24 " , command = size24)
sizefile.add_command(label = " 26 " , command = size26)
sizefile.add_command(label = " 28 " , command = size28)
sizefile.add_command(label = " 30 " , command = size30)


weightfile = Menu(textfile)
textfile.add_cascade(label = 'Начертание' , menu = weightfile)
weightfile.add_command(label = "Полужирный" , command = BoldFace)
weightfile.add_command(label = "Обычный" , command = Normal)

slantfile = Menu(textfile)
textfile.add_cascade(label = 'Наклон' , menu = slantfile)
slantfile.add_command(label = 'italic' , command = Italic)
slantfile.add_command(label = 'roman' , command= Roman)

underlinefile = Menu(textfile)
textfile.add_cascade(label = 'Перечеркивание' , menu = underlinefile)
underlinefile.add_command(label = 'Есть перечеркивание' , command = overstrike_on)


# Тут опять идёт привязка к  mainmenu , это значит , что меню "Размер окна" вы увидете сразу , не переходя по других меню 
windowfile = Menu(mainmenu)
mainmenu.add_cascade(label = "Размер окна" , menu = windowfile )
windowfile.add_command(label = "200х200" , command = wsize200)
windowfile.add_command(label = "300x250" , command = wsize300)
windowfile.add_command(label = "400x300" , command = wsize403)
windowfile.add_command(label = "500x300" , command = wsize503)
windowfile.add_command(label = "500x400" , command = wsize504)
windowfile.add_command(label = "500х500" , command = wsize505)
windowfile.add_command(label = "800x600" , command = wsize806)
windowfile.add_command(label = "1000x600" , command = wsize1006)
windowfile.add_command(label = "стандартный" , command = wsizestandart)




mainmenu.add_command(label = "Выход" , command = quit_text ) # Команда для выхода из приложения , находится в конце в списку всех меню для удобства пользователя
root.mainloop() # Ключовая строка , без нее ваше приложение попросту не будет работать(не отобразится)
