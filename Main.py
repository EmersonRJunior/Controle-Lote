#python .\setup.py build

from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import Pagina_1

app = Tk()
app.geometry('370x550')
app.title('Fechamento')

frames_master = ttk.Notebook(app)
frames_master.pack(fill='both', expand=1)

frame_romaneio = ttk.Frame(frames_master)
frame_romaneio.pack(fill='both', expand=1)

frame_codigos = ttk.Frame(frames_master)
frame_codigos.pack(fill='both', expand=1)

frames_master.add(frame_romaneio, text='Romaneios')
frames_master.add(frame_codigos, text='Códigos')

pag_1 = Pagina_1.Pagina_1(frame_romaneio)
pag_1.top_frames()
pag_1.mid_frames()
pag_1.bot_frames()

app.mainloop()
