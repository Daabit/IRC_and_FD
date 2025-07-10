from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import webbrowser

#Clases
class App(Tk):
    
    def __init__(self):
        super().__init__()
        
        style = ttk.Style()
        style.theme_use("vista")
        
        #Ventana de programa
        self.title("Igneous Rock Classifier & Formal Description")
        
        #MENUBAR
        self.menubar = Menu(self)
        self.config(menu = self.menubar)

        self.file_menu = Menu(self.menubar, tearoff = 0) #tearoff = 0 quita unas líneas que salen al principio del menu desplegable.
        self.menubar.add_cascade(label = "File", menu = self.file_menu)
        self.file_menu.add_separator() #Añade una linea horizontal para separar opciones.
        self.file_menu.add_command(label = "New", command = self.new_window_IRC)
        self.file_menu.add_command(label = "Save", command = self.save_analysis)
        self.file_menu.add_separator() #Añade una linea horizontal para separar opciones.
        self.file_menu.add_command(label = "Exit", command = self.destroy)

        self.edit_menu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "Edit", menu = self.edit_menu)
        self.edit_menu.add_separator() #Añade una linea horizontal para separar opciones.
        self.edit_menu.add_command(label = "Undo", command = self.undo_text)
        self.edit_menu.add_command(label = "Redo", command = self.redo_text)
        self.edit_menu.add_separator() #Añade una linea horizontal para separar opciones.
        self.edit_menu.add_command(label = "Cut", command = self.cut_text)
        self.edit_menu.add_command(label = "Copy", command = self.copy_text)
        self.edit_menu.add_command(label = "Paste", command = self.paste_text)

        self.help_menu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "Help", menu = self.help_menu)
        self.help_menu.add_command(label = "About IRC & FD", command = self.create_window_about_IRC)
                
        #WIDGETS
        
        #1. General data
        self.gral_data_frame = ttk.Frame(self)
        self.gral_data_frame.grid(row = 0, column = 0, sticky = "n", padx = 5, pady = 5)
        self.gral_data_label = ttk.Label(self.gral_data_frame, text = "1. GENERAL DATA", font = ("Helvetica", 10, "bold"))
        self.gral_data_label.grid(row = 0, column = 0, columnspan = 2, sticky = "n")
        
        #Sample code
        self.sample_code_label = ttk.Label(self.gral_data_frame, text = "Sample code:")
        self.sample_code_label.grid(row = 1, column = 0, sticky = "w")
        
        self.sample_code_entry = ttk.Entry(self.gral_data_frame)
        self.sample_code_entry.grid(row = 1, column = 1)
        
        #Sample location
        self.sample_location_label = Label(self.gral_data_frame, text = "Sample location:")
        self.sample_location_label.grid(row = 2, column = 0, sticky = "w")
        
        self.sample_location_entry = ttk.Entry(self.gral_data_frame)
        self.sample_location_entry.grid(row = 2, column = 1)
        
        #Analyst name
        self.analyst_name_label = ttk.Label(self.gral_data_frame, text = "Analyst:")
        self.analyst_name_label.grid(row = 3, column = 0, sticky = "w")
        
        self.analyst_name_entry = ttk.Entry(self.gral_data_frame)
        self.analyst_name_entry.grid(row = 3, column = 1)
        
        #Sample coordinates
        self.coordinates_label = Label(self.gral_data_frame, text = "Sample coordinates", font = ("Helvetica", 10, "bold"))
        self.coordinates_label.grid(row = 4, column = 0, columnspan = 2)
        
        self.sample_e_coord_label = ttk.Label(self.gral_data_frame, text = "East coordinate:")
        self.sample_e_coord_label.grid(row = 5, column = 0, sticky = "w")
        
        self.sample_e_coord_entry = ttk.Entry(self.gral_data_frame)
        self.sample_e_coord_entry.grid(row = 5, column = 1)
        
        self.sample_n_coord_label = ttk.Label(self.gral_data_frame, text = "North coordinate:")
        self.sample_n_coord_label.grid(row = 6, column = 0, sticky = "w")
        
        self.sample_n_coord_entry = ttk.Entry(self.gral_data_frame)
        self.sample_n_coord_entry.grid(row = 6, column = 1)
        
        #Thin secton available
        self.thin_section_avail = ttk.Label(self.gral_data_frame, text = "Thin section available", font = ("Helvetica", 10, "bold"))
        self.thin_section_avail.grid(row = 7, column = 0, columnspan = 2)
        
        self.thin_section_IV = IntVar()
        self.thin_section_selection = ["Yes", "No"]
        
        self.thin_section = None
        
        for index in range(len(self.thin_section_selection)):
            self.thin_section_rb = ttk.Radiobutton(
                self.gral_data_frame,
                text = self.thin_section_selection[index],
                variable = self.thin_section_IV,
                value = index,
                command = lambda: [self.choose_thin_section_b(), self.choose_thin_section(), self.quartz_forced()])
            self.thin_section_rb.grid(row = 8, column = 0 + index)

        self.thin_section_IV.set(0)
        self.choose_thin_section_b() # Asigna self.intr_vs_effu con base en la opción por defecto, para que no aparezca None o [""] al procesar los datos.
        self.choose_thin_section

        #Intrusive vs Effusive
        self.intr_vs_effu = ttk.Label(self.gral_data_frame, text = "Your rock is intrusive or effusive?", font = ("Helvetica", 10, "bold"))
        self.intr_vs_effu.grid(row = 11, column = 0, columnspan = 2)
        
        self.intr_vs_effu_IV = IntVar()
        self.intr_vs_effu_selection = ["Intrusive", "Effusive"]
        
        self.rock_type = None
        
        for index in range(len(self.intr_vs_effu_selection)):
            self.intr_vs_effu_rb = ttk.Radiobutton(
                self.gral_data_frame,
                text = self.intr_vs_effu_selection[index],
                variable = self.intr_vs_effu_IV,
                value = index,
                command = self.choose_intr_vs_effu)
            self.intr_vs_effu_rb.grid(row = 12, column = 0 + index)
            
        self.intr_vs_effu_IV.set(0)
        self.choose_intr_vs_effu()  # Asigna self.intr_vs_effu con base en la opción por defecto, para que no aparezca None o [""] al procesar los datos.
            
        #2. Rock General Constitution
        self.gral_rock_constn_frame = ttk.Frame(self)
        self.gral_rock_constn_frame.grid(row = 1, column = 0, sticky = "n", padx = 5, pady = 5)
        
        self.gral_rock_constn = ttk.Label(self.gral_rock_constn_frame, text = "2. ROCK GENERAL CONSTITUTION", font = ("Helvetica", 10, "bold"))
        self.gral_rock_constn.grid(row = 0, column = 0, columnspan = 2) 
        
        self.gral_rock_constn_IV = IntVar()
        self.gral_rock_constn_selection = ["Coarse grain holocrystalline", "Medium grain holocrystalline",
                          "Fine grain holocrystalline", "Hypocrystalline", "Hypohialline"]

        self.rock_constn = None

        for index in range(len(self.gral_rock_constn_selection)):
            self.gral_rock_constn_rb = ttk.Radiobutton(self.gral_rock_constn_frame, 
                                           text = self.gral_rock_constn_selection[index],
                                           variable = self.gral_rock_constn_IV,
                                           value = index,
                                           command = self.choose_general_rock_constn)
            self.gral_rock_constn_rb.grid(row = 1 + index + 1, column=0, columnspan = 2, sticky = "w") # "index + 1" para que las opcines salgan verticales y no se solape con su respectivo label
        
        self.gral_rock_constn_IV.set(0)
        self.choose_general_rock_constn()  # Asigna self.rock_constn con base en la opción por defecto, para que no aparezca None o [""] al procesar los datos.
        
        #3. Main texture and structures
        self.textr_struc_frame = ttk.Frame(self)
        self.textr_struc_frame.grid(row = 0, column = 1, sticky = "n", padx = 5, pady = 5)
        
        self.textr_struc = ttk.Label(self.textr_struc_frame, text = "3. MAIN TEXTURES AND \nSTRUCTURES", font = ("Helvetica", 10, "bold")).grid(row = 0, column = 0)
        
        self.list_textr_struc = Listbox(self.textr_struc_frame, selectmode = MULTIPLE, exportselection = False)#exportselection = False permite que no se deseleccionen elementos de otros checkbuttons
        self.list_textr_struc.grid(row = 1, column = 0)

        self.list_textr_struc.insert(1, "Porphyritic")
        self.list_textr_struc.insert(2, "Glomerophyric")
        self.list_textr_struc.insert(3, "Miarolitic")
        self.list_textr_struc.insert(4, "Amigdalar")
        self.list_textr_struc.insert(5, "Banded")
        self.list_textr_struc.insert(6, "Laminar")
        self.list_textr_struc.insert(7, "Masive")
        self.list_textr_struc.insert(8, "Pegmatitic")
        self.list_textr_struc.insert(9, "Stratified-foliated")

        self.list_textr_struc.config(height=self.list_textr_struc.size()) #El tamaño de la caja se ajustará a la cantidad de items
        
        self.textr_struc_selected = None
        
        self.add_textr_struc = ttk.Entry(self.textr_struc_frame)
        self.add_textr_struc.grid(row = 2, column = 0)
        
        self.add_option_textr = ttk.Label(self.textr_struc_frame, text = "Add another option:").grid(row = 3, column = 0)

        self.add_textr_struc_bt = ttk.Button(self.textr_struc_frame, text = "Add", command = lambda: [self.get_textr_struc(),self.new_textr_struc()])
        self.add_textr_struc_bt.grid(row = 4, column = 0)
                
        #4. Quartz or Feldspathoids
        self.qz_vs_fd_frame = ttk.Frame(self)
        self.qz_vs_fd_frame.grid(row = 1, column = 1, sticky = "n", padx = 5, pady = 5)
        self.toggle_frame_state(self.qz_vs_fd_frame, 'disabled')
        
        self.qz_vs_fd_label = ttk.Label(self.qz_vs_fd_frame, text = "4. DOES YOUR SAMPLE HAVE \nQUARTZ OR FELDSPATHOIDS?", font = ("Helvetica", 10, "bold"))
        self.qz_vs_fd_label.grid(row = 0, column = 0, columnspan = 2)
        
        self.qz_vs_fd_IV = IntVar()
        self.qz_vs_fd_selection = ["Quartz", "Feldspathoids"]
        
        self.qz_vs_fd = None
        
        for index in range(len(self.qz_vs_fd_selection)):
            self.qz_vs_fd_rb = Radiobutton(
                self.qz_vs_fd_frame,
                text = self.qz_vs_fd_selection[index],
                variable = self.qz_vs_fd_IV,
                value = index,
                command = lambda: [self.choose_qz_vs_fd_frame(), self.choose_qz_vs_fd()])
            self.qz_vs_fd_rb.grid(row = 10, column = 0 + index)

        self.qz_vs_fd_IV.set(0)
        
        #5. Required minerals
        
        #Thin section Quartz
        self.req_minerals_thin_frame = ttk.Frame(self)
        self.req_minerals_thin_frame.grid(row = 0, column = 2, sticky = "n", padx = 5, pady = 5)

        self.req_minerals_thin = ttk.Label(self.req_minerals_thin_frame, text = "5. REQUIRED MINERALS", font = ("Helvetica", 10, "bold"))
        self.req_minerals_thin.grid(row = 0, column = 0, columnspan = 2, sticky = "n")
        
        self.qz_thin = ttk.Label(self.req_minerals_thin_frame, text = "Quartz:")
        self.qz_thin.grid(row = 1, column = 0)
        self.qz_thin_entry = ttk.Entry(self.req_minerals_thin_frame, width = 2)
        self.qz_thin_entry.grid(row = 1, column = 1)
        
        self.af_thin = ttk.Label(self.req_minerals_thin_frame, text = "Alkali feldspar:")
        self.af_thin.grid(row = 2, column = 0)
        self.af_thin_entry = ttk.Entry(self.req_minerals_thin_frame, width = 2)
        self.af_thin_entry.grid(row = 2, column = 1)
        
        self.pl_thin = ttk.Label(self.req_minerals_thin_frame, text = "Plagioclase:")
        self.pl_thin.grid(row = 3, column = 0)
        self.pl_thin_entry = ttk.Entry(self.req_minerals_thin_frame, width = 2)
        self.pl_thin_entry.grid(row = 3, column = 1)
        
        self.ol_thin = ttk.Label(self.req_minerals_thin_frame, text = "Olivine:")
        self.ol_thin.grid(row = 4, column = 0)
        self.ol_thin_entry = ttk.Entry(self.req_minerals_thin_frame, width = 2)
        self.ol_thin_entry.grid(row = 4, column = 1)
        
        self.clpx_thin = ttk.Label(self.req_minerals_thin_frame, text = "Clinopyroxene:")
        self.clpx_thin.grid(row = 5, column = 0)
        self.clpx_thin_entry = ttk.Entry(self.req_minerals_thin_frame, width = 2)
        self.clpx_thin_entry.grid(row = 5, column = 1)
        
        self.orpx_thin = ttk.Label(self.req_minerals_thin_frame, text = "Orthopyroxene:")
        self.orpx_thin.grid(row = 6, column = 0)
        self.orpx_thin_entry = ttk.Entry(self.req_minerals_thin_frame, width = 2)
        self.orpx_thin_entry.grid(row = 6, column = 1)
        
        self.amph_thin = ttk.Label(self.req_minerals_thin_frame, text = "Amphibole:")
        self.amph_thin.grid(row = 7, column = 0)
        self.amph_thin_entry = ttk.Entry(self.req_minerals_thin_frame, width = 2)
        self.amph_thin_entry.grid(row = 7, column = 1)
        
        self.bt_thin = ttk.Label(self.req_minerals_thin_frame, text = "Biotite:")
        self.bt_thin.grid(row = 8, column = 0)
        self.bt_thin_entry = ttk.Entry(self.req_minerals_thin_frame, width = 2)
        self.bt_thin_entry.grid(row = 8, column = 1)
        
        self.mzv_thin = ttk.Label(self.req_minerals_thin_frame, text = "Muscovite:")
        self.mzv_thin.grid(row = 9, column = 0)
        self.mzv_thin_entry = ttk.Entry(self.req_minerals_thin_frame, width = 2)
        self.mzv_thin_entry.grid(row = 9, column = 1)
        
        self.ox_feti_thin = ttk.Label(self.req_minerals_thin_frame, text = "Fe-Ti oxides:")
        self.ox_feti_thin.grid(row = 10, column = 0)
        self.ox_feti_thin_entry = ttk.Entry(self.req_minerals_thin_frame, width = 2)
        self.ox_feti_thin_entry.grid(row = 10, column = 1)
        
        #Thin section Feldspathoids
        self.req_minerals_thin_frame_fd = ttk.Frame(self)
        self.req_minerals_thin_frame_fd.grid(row = 0, column = 2, sticky = "n", padx = 5, pady = 5)

        self.req_minerals_thin = ttk.Label(self.req_minerals_thin_frame_fd, text = "5. REQUIRED MINERALS", font = ("Helvetica", 10, "bold"))
        self.req_minerals_thin.grid(row = 0, column = 0, columnspan = 2, sticky = "n")
        
        self.fd_thin_fd = ttk.Label(self.req_minerals_thin_frame_fd, text = "Feldspathoid:")
        self.fd_thin_fd.grid(row = 1, column = 0)
        self.fd_thin_entry = ttk.Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.fd_thin_entry.grid(row = 1, column = 1)
        
        self.af_thin = ttk.Label(self.req_minerals_thin_frame_fd, text = "Alkali feldspar:")
        self.af_thin.grid(row = 2, column = 0)
        self.af_thin_entry_fd = ttk.Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.af_thin_entry_fd.grid(row = 2, column = 1)
        
        self.pl_thin = ttk.Label(self.req_minerals_thin_frame_fd, text = "Plagioclase:")
        self.pl_thin.grid(row = 3, column = 0)
        self.pl_thin_entry_fd = ttk.Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.pl_thin_entry_fd.grid(row = 3, column = 1)
        
        self.ol_thin = ttk.Label(self.req_minerals_thin_frame_fd, text = "Olivine:")
        self.ol_thin.grid(row = 4, column = 0)
        self.ol_thin_entry_fd = ttk.Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.ol_thin_entry_fd.grid(row = 4, column = 1)
        
        self.clpx_thin = ttk.Label(self.req_minerals_thin_frame_fd, text = "Clinopyroxene:")
        self.clpx_thin.grid(row = 5, column = 0)
        self.clpx_thin_entry_fd = ttk.Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.clpx_thin_entry_fd.grid(row = 5, column = 1)
        
        self.orpx_thin = ttk.Label(self.req_minerals_thin_frame_fd, text = "Orthopyroxene:")
        self.orpx_thin.grid(row = 6, column = 0)
        self.orpx_thin_entry_fd = ttk.Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.orpx_thin_entry_fd.grid(row = 6, column = 1)
        
        self.amph_thin = ttk.Label(self.req_minerals_thin_frame_fd, text = "Amphibole:")
        self.amph_thin.grid(row = 7, column = 0)
        self.amph_thin_entry_fd = ttk.Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.amph_thin_entry_fd.grid(row = 7, column = 1)
        
        self.bt_thin = ttk.Label(self.req_minerals_thin_frame_fd, text = "Biotite:")
        self.bt_thin.grid(row = 8, column = 0)
        self.bt_thin_entry_fd = ttk.Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.bt_thin_entry_fd.grid(row = 8, column = 1)
        
        self.mzv_thin = ttk.Label(self.req_minerals_thin_frame_fd, text = "Muscovite:")
        self.mzv_thin.grid(row = 9, column = 0)
        self.mzv_thin_entry_fd = ttk.Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.mzv_thin_entry_fd.grid(row = 9, column = 1)
        
        self.ox_feti_thin = ttk.Label(self.req_minerals_thin_frame_fd, text = "Fe-Ti oxides:")
        self.ox_feti_thin.grid(row = 10, column = 0)
        self.ox_feti_thin_entry_fd = ttk.Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.ox_feti_thin_entry_fd.grid(row = 10, column = 1)
        
        #No thin section
        self.req_minerals_no_thin_frame = ttk.Frame(self)
        self.req_minerals_no_thin_frame.grid(row = 0, column = 2, sticky = "n", padx = 5, pady = 5)
        
        self.req_minerals_no_thin = ttk.Label(self.req_minerals_no_thin_frame, text = "5. REQUIRED MINERALS", font = ("Helvetica", 10, "bold"))
        self.req_minerals_no_thin.grid(row = 0, column = 0, columnspan = 2, sticky = "n")
        
        self.qz_no_thin = ttk.Label(self.req_minerals_no_thin_frame, text = "Quartz:")
        self.qz_no_thin.grid(row = 1, column = 0)
        self.qz_no_thin_entry = ttk.Entry(self.req_minerals_no_thin_frame, width = 2)
        self.qz_no_thin_entry.grid(row = 1, column = 1)
        
        self.af_no_thin = ttk.Label(self.req_minerals_no_thin_frame, text = "Alkali feldspar:")
        self.af_no_thin.grid(row = 2, column = 0)
        self.af_no_thin_entry = ttk.Entry(self.req_minerals_no_thin_frame, width = 2)
        self.af_no_thin_entry.grid(row = 2, column = 1)
        
        self.pl_no_thin = ttk.Label(self.req_minerals_no_thin_frame, text = "Plagioclase:")
        self.pl_no_thin.grid(row = 3, column = 0)
        self.pl_no_thin_entry = ttk.Entry(self.req_minerals_no_thin_frame, width = 2)
        self.pl_no_thin_entry.grid(row = 3, column = 1)
        
        self.m_no_thin = ttk.Label(self.req_minerals_no_thin_frame, text = "M:")
        self.m_no_thin.grid(row = 4, column = 0)
        self.m_no_thin_entry = ttk.Entry(self.req_minerals_no_thin_frame, width = 2)
        self.m_no_thin_entry.grid(row = 4, column = 1)
        
        #Estas dos funciones deben ir aquí porque deben esperar a que se creen los frames necesarios para actuar correctamente y permitan tener una opción seleccionada por default, a comparación de los otros radiobutton donde las funciones están dentro de la misma sección.
        self.choose_qz_vs_fd_frame()
        self.choose_qz_vs_fd()
        
        #6. Emplacement level
        self.emplacement_level_frame = ttk.Frame(self)
        self.emplacement_level_frame.grid(row = 1, column = 2, sticky = "n", padx = 5, pady = 5)
        
        self.emplacement_level = ttk.Label(self.emplacement_level_frame, text = "6. EMPLACEMENT LEVEL", font = ("Helvetica", 10, "bold"))
        self.emplacement_level.grid(row = 0, column = 0, columnspan = 2)
        
        self.emplacement_level_IV = IntVar()
        self.emplacement_level_selection = ["Plutonic", "Hypabyssal",
                          "Hypovolcanic"]

        self.emp_level = None
        
        for index in range(len(self.emplacement_level_selection)):
            radiobutton_emplacement = ttk.Radiobutton(self.emplacement_level_frame, 
                                           text = self.emplacement_level_selection[index],
                                           variable = self.emplacement_level_IV,
                                           value = index,
                                           command = self.choose_emplacement_level)
            radiobutton_emplacement.grid(row = index + 1, column=0, sticky = "w") # "index + 1" para que las opcines salgan verticales y no se solape con su respectivo label

        self.emplacement_level_IV.set(0)
        self.choose_emplacement_level()  # Asigna self.emp_level con base en la opción por defecto, para que no aparezca None o [""] al procesar los datos.

        #7. Alteration
        self.alteration_frame = ttk.Frame(self)
        self.alteration_frame.grid(row = 0, column = 3, sticky = "n", padx = 5, pady = 5)
        
        self.alteration = ttk.Label(self.alteration_frame, text = "7. ALTERATION", font = ("Helvetica", 10, "bold"))
        self.alteration.grid(row = 0, column = 0)
        
        self.list_alteration = Listbox(self.alteration_frame, selectmode = MULTIPLE, exportselection = False)#exportselection = False permite que no se deseleccionen elementos de otros checkbuttons
        self.list_alteration.grid(row = 1, column = 0, sticky = "ew")

        self.list_alteration.insert(1, "Silicification")
        self.list_alteration.insert(2, "Oxidation")
        self.list_alteration.insert(3, "Propylite")
        self.list_alteration.insert(4, "Clayey")
        self.list_alteration.insert(5, "Calcareous")

        self.list_alteration.config(height=self.list_alteration.size()) #El tamaño de la caja se ajustará a la cantidad de items

        self.alteration_selected = None
        
        self.new_alteration = ttk.Entry(self.alteration_frame)
        self.new_alteration.grid(row = 3, column = 0, sticky = "ew")

        add_new_alteration = ttk.Button(self.alteration_frame, text = "Add", command = lambda: [self.get_alteration(), self.add_alteration()])
        add_new_alteration.grid(row = 4, column = 0, sticky = "ew")
        
        #8. Alteration level
        self.alteration_level_frame = ttk.Frame(self)
        self.alteration_level_frame.grid(row = 1, column = 3, sticky = "n", padx = 5, pady = 5)
        
        self.alteration_level = ttk.Label(self.alteration_level_frame, text = "8. ALTERATION LEVEL", font = ("Helvetica", 10, "bold"))
        self.alteration_level.grid(row = 0, column = 0, sticky = "n")
        
        self.alteration_level_IV = IntVar()
        self.alteration_level_selection = ["Weak", "Moderate",
                          "Strongly"]

        self.alt_lvl = None

        for index in range(len(self.alteration_level_selection)):
            radiobutton_alteration_lvl = ttk.Radiobutton(self.alteration_level_frame, 
                                           text = self.alteration_level_selection[index],
                                           variable = self.alteration_level_IV,
                                           value = index,
                                           command = self.choose_alteration_level)
            radiobutton_alteration_lvl.grid(row = index + 1, column = 0, sticky = "w") # "index + 1" para que las opcines salgan verticales y no se solape con su respectivo label
        
        self.alteration_level_IV.set(0)
        self.choose_alteration_level()  # Asigna self.alt_lvl con base en la opción por defecto, para que no aparezca None o [""] al procesar los datos.
        
        #9. Observations
        self.observations_results_frame = ttk.Frame(self)
        self.observations_results_frame.grid(row = 2, column = 0, columnspan = 4, sticky = "new", padx = 5, pady = 5)
        
        self.observations = ttk.Label(self.observations_results_frame, text = "9. OBSERVATIONS", font = ("Helvetica", 10, "bold"))
        self.observations.grid(row = 0, column = 0)
        
        self.observations_text = Text(self.observations_results_frame, undo = True)
        self.observations_text.config(width = 25, height = 10)
        self.observations_text.grid(row = 1, column = 0)
        
        #Submit button
        self.submit_button = ttk.Button(self.observations_results_frame, text = "Process all data", command = self.submit_data)
        self.submit_button.grid(row = 2, column = 0, sticky = "n", pady = 5)
        
        #10. Results
        
        self.results = ttk.Label(self.observations_results_frame, text = "10. RESULTS", font = ("Helvetica", 10, "bold"))
        self.results.grid(row = 0, column = 1, sticky = "n")
        
        self.save_analysis_button = ttk.Button(self.observations_results_frame, text = "Save analysis", command = self.save_analysis)
        self.save_analysis_button.grid(row= 2, column = 1)
        
        #Sample Info
        self.info_box = Text(self.observations_results_frame, width = 70, height = 10)
        self.info_box.grid(row = 1, column = 1, sticky = "n")
        
        #Creación de los atajos del teclado después de la creación de todos los widgets que lo utilicen
        self.bind_all("<Control-z>", lambda event: self.undo_text())
        self.bind_all("<Control-y>", lambda event: self.redo_text())
        self.bind_all("<Control-x>", lambda event: self.cut_text())
        self.bind_all("<Control-c>", lambda event: self.copy_text())
        self.bind_all("<Control-v>", lambda event: self.paste_text())
        
    #FUNCIONES
    def new_window_IRC(self):
        self.new_window = App()
    
    def create_window_about_IRC(self):
        import tkinter as tk
        from tkinter import ttk
        url = "https://www.linkedin.com/in/daabluac/"
        def open_linkedin():
            webbrowser.open(url)
        self.window_about_IRC = Toplevel()
        self.window_about_IRC.title("About IRC & FD")
        self.window_about_IRC.config(width = 500, height = 500)
        ttk.Label(self.window_about_IRC, text = "Contact", font = ("Arial", 10, "bold")).grid(row = 0, column = 0)
        ttk.Label(self.window_about_IRC, text = "Author: David Lucero").grid(row = 1, column = 0)
        ttk.Label(self.window_about_IRC, text = "Email: daabluac@gmail.com").grid(row = 2, column = 0, sticky = "nsew")
        ttk.Button(self.window_about_IRC, text = "LinkedIn", command = open_linkedin).grid(row = 3, column = 0)
        ttk.Button(self.window_about_IRC, text = "Ok", command = self.window_about_IRC.destroy).grid(row = 4, column = 0)
    
    def choose_thin_section_b(self):
        if(self.thin_section_IV.get() == 0):
            self.thin_section = "Yes"
        elif(self.thin_section_IV.get() == 1):
            self.thin_section = "No"
        
    def choose_thin_section(self):
        if self.thin_section_IV.get() == 0:
            self.toggle_frame_state(self.qz_vs_fd_frame, 'normal')
            self.hide_all_mineral_frames()
        elif self.thin_section_IV.get() == 1:
            self.toggle_frame_state(self.qz_vs_fd_frame, 'disabled')
            self.hide_all_mineral_frames()
            self.req_minerals_no_thin_frame.grid(row = 0, column = 2, sticky = "n")
    
    def quartz_forced(self):
        if self.thin_section_IV.get() == 0:
            self.qz_vs_fd_IV.set(0)  # Fuerza la selección a "Quartz" para que el frame de Required Minerals no desaparezca si se selecciona No en lamina delgada y luego se selecciona que si.
            self.choose_qz_vs_fd()   # Asigna la variable self.qz_vs_fd
            self.choose_qz_vs_fd_frame()  # Muestra el frame de minerales adecuado
    
    def toggle_frame_state(self, frame, state):
        for child in frame.winfo_children():
            widget_type = child.winfo_class()
            if widget_type in ('Button', 'Entry', 'Radiobutton', 'Checkbutton', 'Spinbox', 'Text', 'Listbox'):
                    child.configure(state=state)
            elif widget_type == 'Label':
                    child.configure(fg='gray' if state == 'disabled' else 'black')
    
    def hide_all_mineral_frames(self):
        self.req_minerals_no_thin_frame.grid_forget()
        self.req_minerals_thin_frame.grid_forget()
        self.req_minerals_thin_frame_fd.grid_forget()
    
    def get_textr_struc(self):
        self.selected_indices = self.list_textr_struc.curselection()  # obtiene los índices seleccionados
        self.selected_textures = [self.list_textr_struc.get(i) for i in self.selected_indices]  # obtiene los textos seleccionados
        self.textr_struc_selected = self.selected_textures  # los guarda en la variable de instancia
    
    def new_textr_struc(self):
        self.list_textr_struc.insert(END, self.add_textr_struc.get())
        self.list_textr_struc.config(height=self.list_textr_struc.size())
        self.add_textr_struc.delete(0, END)
    
    def choose_qz_vs_fd_frame(self):
        self.hide_all_mineral_frames()
        if self.qz_vs_fd_IV.get() == 0:
            self.req_minerals_thin_frame.grid(row = 0, column = 2, sticky = "n")
        elif self.qz_vs_fd_IV.get() == 1:
            self.req_minerals_thin_frame_fd.grid(row = 0, column = 2, sticky = "n")   
    
    def choose_qz_vs_fd(self):
        if(self.qz_vs_fd_IV.get() == 0):
            self.qz_vs_fd = "Quartz"
        elif(self.qz_vs_fd_IV.get() == 1):
            self.qz_vs_fd = "Feldspathoids" 
    
    def choose_intr_vs_effu(self):
        if(self.intr_vs_effu_IV.get() == 0):
            self.rock_type = "Intrusive"
        elif(self.intr_vs_effu_IV.get() == 1):
            self.rock_type = "Effusive"
    
    def choose_general_rock_constn(self):
        if(self.gral_rock_constn_IV.get() == 0):
            self.rock_constn = "Coarse grain holocrystalline"
        elif(self.gral_rock_constn_IV.get() == 1):
            self.rock_constn = "Medium grain holocrystalline"
        elif(self.gral_rock_constn_IV.get() == 2):
            self.rock_constn = "Fine grain holocrystalline"
        elif(self.gral_rock_constn_IV.get() == 3):
            self.rock_constn = "Hypocrystalline"
        elif(self.gral_rock_constn_IV.get() == 4):
            self.rock_constn = "Hypohialine"
    
    def choose_emplacement_level(self):
        if(self.emplacement_level_IV.get() == 0):
            self.emp_level = "Plutonic"
        elif(self.emplacement_level_IV.get() == 1):
            self.emp_level = "Hypabyssal"
        elif(self.emplacement_level_IV.get() == 2):
            self.emp_level = "Hipovolcanic"
    
    def get_alteration(self):
        selected_indices_alt = self.list_alteration.curselection()
        self.alteration_selected = [self.list_alteration.get(i) for i in selected_indices_alt]
    
    def add_alteration(self):
        self.list_alteration.insert(END, self.new_alteration.get())
        self.list_alteration.config(height=self.list_alteration.size())
        self.new_alteration.delete(0, END)
    
    def choose_alteration_level(self):
        if(self.alteration_level_IV.get() == 0):
            self.alt_lvl = "Weak"
        elif(self.alteration_level_IV.get() == 1):
            self.alt_lvl = "Moderate"
        elif(self.alteration_level_IV.get() == 2):
            self.alt_lvl = "Strongly"

    def qapf_thin_intr_qz(self):
        try:
            qz_n_thin = (int(self.qz_thin_entry.get()) * 100) / (int(self.af_thin_entry.get()) + int(self.pl_thin_entry.get()) + int(self.qz_thin_entry.get()))
        except KeyError:
            qz_n_thin = 0 # Valor por defecto si la clave no existe
        try:
            af_vs_pl = (int(self.af_thin_entry.get()) * 100) / (int(self.af_thin_entry.get()) + int(self.pl_thin_entry.get()))
        except KeyError:
            af_vs_pl = 0 # Valor por defecto si la clave no existe
            
        self.rock_name = "Undefined"  # Default value to avoid unbound error
        if qz_n_thin >= 90:
            self.rock_name = "Quarzolite"
        elif qz_n_thin >= 60 and qz_n_thin < 90:
            self.rock_name = "Quartz-rich granitoid"
        elif qz_n_thin >= 20 and qz_n_thin < 60:
            if af_vs_pl >= 90:
                self.rock_name = "Alkali feldspar granite"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Syenogranite"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Monzogranite"
            elif af_vs_pl >= 10 and af_vs_pl < 35:
                self.rock_name = "Granodiorite"
            elif af_vs_pl < 10:
                self.rock_name = "Tonalite"
        elif qz_n_thin >= 5 and qz_n_thin < 20:
            if af_vs_pl >= 90:
                self.rock_name = "Quartz alkali feldspar syenite"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Quartz syenite"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Quartz monzonite" 
            elif af_vs_pl >= 10 and af_vs_pl < 35:
                self.rock_name = "Quartz monzodiorite/Quartz monzogabbro"
            elif af_vs_pl < 10:
                self.rock_name = "Quartz diorite/Quartz gabbro/Quartz anorthosite"
        elif qz_n_thin < 5 and qz_n_thin >= 0:
            if af_vs_pl >= 90:
                self.rock_name = "Alkali feldspar syenite"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Syenite"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Monzonite"
            elif af_vs_pl >= 10 and af_vs_pl < 35:
                self.rock_name = "Monzogabbro/Monzodiorite"
            elif af_vs_pl < 10:
                self.rock_name = "Diorite/Gabbro/Anorthosite"
    
    def qapf_thin_effu_qz(self):
        try:
            qz_n_thin = (int(self.qz_thin_entry.get()) * 100) / (int(self.af_thin_entry.get()) + int(self.pl_thin_entry.get()) + int(self.qz_thin_entry.get()))
        except KeyError:
            qz_n_thin = 0 # Valor por defecto si la clave no existe
        try:
            af_vs_pl = (int(self.af_thin_entry.get()) * 100) / (int(self.af_thin_entry.get()) + int(self.pl_thin_entry.get()))
        except KeyError:
            af_vs_pl = 0 # Valor por defecto si la clave no existe

        self.rock_name = "Undefined"  # Default value to avoid unbound error
        if qz_n_thin >= 90:
            self.rock_name = "Undefined"
        elif qz_n_thin >= 60 and qz_n_thin < 90:
            self.rock_name = "Undefined"
        elif qz_n_thin >= 20 and qz_n_thin < 60:
            if af_vs_pl >= 90:
                self.rock_name = "Alkali feldspar rhyolite"
            elif af_vs_pl >= 35 and af_vs_pl < 90:
                self.rock_name = "Rhyolite"
            elif af_vs_pl < 35:
                self.rock_name = "Dacite"
        elif qz_n_thin >= 5 and qz_n_thin < 20:
            if af_vs_pl >= 90:
                self.rock_name = "Quartz alkali feldspar trachyte"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Quartz trachyte"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Quartz latite"
            elif af_vs_pl < 35:
                self.rock_name= "Basalt/Andesite"
        elif qz_n_thin < 5:
            if af_vs_pl >= 90:
                self.rock_name = "Alkali feldspar trachyte"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Trachyte"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Latite"
            elif af_vs_pl < 35:
                self.rock_name = "Basalt/Andesite"
        
    def qapf_thin_intr_fd(self):
        try:
            fd_n_thin = (int(self.fd_thin_entry.get()) * 100) / (int(self.af_thin_entry.get()) + int(self.pl_thin_entry.get()) + int(self.fd_thin_entry.get()))
        except KeyError:
            fd_n_thin = 0 # Valor por defecto si la clave no existe
        try:
            af_vs_pl = (int(self.af_thin_entry_fd.get()) * 100) / (int(self.af_thin_entry_fd.get()) + int(self.pl_thin_entry_fd.get()))
        except KeyError:
            af_vs_pl = 0 # Valor por defecto si la clave no existe
        
        self.rock_name = "Undefined"
        if fd_n_thin >= 90:
            self.rock_name = "Foidolite"
        elif fd_n_thin >= 60 and fd_n_thin < 90:
            self.rock_name = "Foidolite"
        elif fd_n_thin >= 10 and fd_n_thin < 60:
            if af_vs_pl >= 90:
                self.rock_name = "Foid syenite"
            elif af_vs_pl >= 50 and af_vs_pl < 90:
                self.rock_name = "Foid monzosyenite"
            elif af_vs_pl >= 10 and af_vs_pl < 50:
                self.rock_name = "Foid monzodiorite/Foid monzogabbro"
            elif af_vs_pl < 10:
                self.rock_name = "Foid diorite/Foid gabbro"
        elif fd_n_thin < 10:
            if af_vs_pl >= 90:
                self.rock_name = "Foid-bearing alkali feldspar syenite"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Foid-bearing syenite"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Foid-bearing monzonite"
            elif af_vs_pl >= 10 and af_vs_pl < 35:
                self.rock_name = "Foid-bearing monzodiorite/Foid-bearing monzogabbro"
            elif af_vs_pl < 10:
                self.rock_name = "Foid-bearing diorite/Foid-bearing gabbro/Foid-bearing anorthosite"
    
    def qapf_thin_effu_fd(self):
        try:
            fd_n_thin = (int(self.fd_thin_entry.get()) * 100) / (int(self.af_thin_entry_fd.get()) + int(self.pl_thin_entry_fd.get()) + int(self.fd_thin_entry.get()))
        except KeyError:
            fd_n_thin = 0 # Valor por defecto si la clave no existe
        try:
            af_vs_pl = (int(self.af_thin_entry_fd.get()) * 100) / (int(self.af_thin_entry_fd.get()) + int(self.pl_thin_entry_fd.get()))
        except KeyError:
            af_vs_pl = 0 # Valor por defecto si la clave no existe
            
        self.rock_name = "Undefined"    
        if fd_n_thin >= 90:
            self.rock_name = "Foidite"
        elif fd_n_thin >= 60 and fd_n_thin < 90:
            if af_vs_pl >= 50:
                self.rock_name = "Phonolitic foidite"
            elif af_vs_pl <= 49:
                self.rock_name = "Tephritic foidite"
        elif fd_n_thin >= 10 and fd_n_thin < 60:
            if af_vs_pl >= 90:
                self.rock_name = "Phonolite"
            elif af_vs_pl >= 50 and af_vs_pl < 90:
                self.rock_name = "Tephritic phonolite"
            elif af_vs_pl >= 10 and af_vs_pl < 50:
                if int(self.ol_thin_entry_fd.get()) <= 10:
                    self.rock_name = "Phonolitic tephrite"
                elif int(self.ol_thin_entry_fd.get()) > 10:
                    self.rock_name = "Phonolitic basanite"
            elif af_vs_pl < 10:
                if int(self.ol_thin_entry_fd.get()) <= 10:
                    self.rock_name = "Tephrite"
                elif int(self.ol_thin_entry_fd.get()) > 10:
                    self.rock_name = "Basanite"
        elif fd_n_thin < 10:
            if af_vs_pl >= 90:
                self.rock_name = "Foid-bearing alkali feldspar tachyte"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Foid-bearing trachyte"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Foid-bearing latite"
            elif af_vs_pl < 35:
                self.rock_name = "Basalt/Andesite"  
    
    def qapf_no_thin_intr_qz(self):
        try:
            qz_n_thin = (int(self.qz_no_thin_entry.get()) * 100) / (int(self.af_no_thin_entry.get()) + int(self.pl_no_thin_entry.get()) + int(self.qz_no_thin_entry.get()))
        except KeyError:
            qz_n_thin = 0 # Valor por defecto si la clave no existe
        try:
            af_vs_pl = (int(self.af_no_thin_entry.get()) * 100) / (int(self.af_no_thin_entry.get()) + int(self.pl_no_thin_entry.get()))
        except KeyError:
            af_vs_pl = 0 # Valor por defecto si la clave no existe
    
        self.rock_name = "Undefined"  # Default value to avoid unbound error
        if qz_n_thin >= 90:
            self.rock_name = "Quarzolite"
        elif qz_n_thin >= 60 and qz_n_thin < 90:
            self.rock_name = "Quarzolite"
        elif qz_n_thin >= 20 and qz_n_thin < 60:
            if af_vs_pl >= 90:
                self.rock_name = "Alkali feldspar granite"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Syenogranite"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Monzogranite"
            elif af_vs_pl >= 10 and af_vs_pl < 35:
                self.rock_name = "Granodiorite"
            elif af_vs_pl < 10:
                self.rock_name = "Tonalite"
        elif qz_n_thin >= 5 and qz_n_thin < 20:
            if af_vs_pl >= 90:
                self.rock_name = "Quartz alkali feldspar syenite"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Quartz syenite"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Quartz monzonite"
            elif af_vs_pl >= 10 and af_vs_pl < 35:
                self.rock_name = "Quartz monzodiorite/Quartz monzogabbro"
            elif af_vs_pl < 10:
                self.rock_name = "Quartz diorite/Quartz gabbro/Quartz anorthosite"
        elif qz_n_thin < 5 and qz_n_thin >= 0:
            if af_vs_pl >= 90:
                self.rock_name = "Alkali feldspar syenite"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Syenite"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Monzonite"
            elif af_vs_pl >= 10 and af_vs_pl < 35:
                self.rock_name = "Monzogabbro/Monzodiorite"
            elif af_vs_pl < 10:
                self.rock_name = "Diorite/Gabbro/Anorthosite"    
    
    def qapf_no_thin_effu_qz(self):
        try:
            qz_n_thin = (int(self.qz_no_thin_entry.get()) * 100) / (int(self.af_no_thin_entry.get()) + int(self.pl_no_thin_entry.get()) + int(self.qz_no_thin_entry.get()))
        except KeyError:
            qz_n_thin = 0 # Valor por defecto si la clave no existe
        try:
            af_vs_pl = (int(self.af_no_thin_entry.get()) * 100) / (int(self.af_no_thin_entry.get()) + int(self.pl_no_thin_entry.get()))
        except KeyError:
            af_vs_pl = 0 # Valor por defecto si la clave no existe

        self.rock_name = "Undefined"  # Default value to avoid unbound error
        if qz_n_thin >= 90:
            self.rock_name = "Undefined"
        elif qz_n_thin >= 60 and qz_n_thin < 90:
            self.rock_name = "Undefined"
        elif qz_n_thin >= 20 and qz_n_thin < 60:
            if af_vs_pl >= 90:
                self.rock_name = "Alkali feldspar rhyolite"
            elif af_vs_pl >= 35 and af_vs_pl < 90:
                self.rock_name = "Rhyolite"
            elif af_vs_pl < 35:
                self.rock_name = "Dacite"
        elif qz_n_thin >= 5 and qz_n_thin < 20:
            if af_vs_pl >= 90:
                self.rock_name = "Quartz alkali feldspar trachyte"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Quartz trachyte"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Quartz latite"
            elif af_vs_pl < 35:
                self.rock_name= "Basalt/Andesite"
        elif qz_n_thin < 5:
            if af_vs_pl >= 90:
                self.rock_name = "Alkali feldspar trachyte"
            elif af_vs_pl >= 65 and af_vs_pl < 90:
                self.rock_name = "Trachyte"
            elif af_vs_pl >= 35 and af_vs_pl < 65:
                self.rock_name = "Latite"
            elif af_vs_pl < 35:
                self.rock_name = "Basalt/Andesite"            

    def submit_data(self):
        import tkinter as tk    #NO SE PORQUE TUVE QUE IMPORTAR ASI PERO SI NO LO HACIA NO FUNCIONABA EL insert()
        
        self.get_textr_struc() #Para obtener los datos de los Listbox() se tiene que volver a llamar la función aquí, para actualizarla
        self.get_alteration()
        
        sample_code = self.sample_code_entry.get()
        sample_location = self.sample_location_entry.get()
        analyst = self.analyst_name_entry.get()
        east_coordinate = self.sample_e_coord_entry.get()
        north_coordinate = self.sample_n_coord_entry.get()
        thin_section = self.thin_section
        rock_type = self.rock_type
        rock_constn = self.rock_constn
        textr_struc = ", ".join(self.textr_struc_selected) if self.textr_struc_selected else "None selected" #Hace que aparezca en string en vez de "[Textura]"
        qz_vs_fd = self.qz_vs_fd
        alteration = ", ".join(self.alteration_selected) if self.alteration_selected else "None selected" #Hace que aparezca en string en vez de "[Alteration]"
        alt_lvl = self.alt_lvl
        emp_level = self.emp_level
        observations = self.observations_text.get("1.0", tk.END) #Esto permite copiar todo el texto del cuadro

        if self.thin_section == "Yes" and self.rock_type == "Intrusive" and self.qz_vs_fd == "Quartz":
            self.qapf_thin_intr_qz()
        elif self.thin_section == "Yes" and self.rock_type == "Effusive" and self.qz_vs_fd == "Quartz":
            self.qapf_thin_effu_qz()
        elif self.thin_section == "Yes" and self.rock_type == "Intrusive" and self.qz_vs_fd == "Feldspathoids":
            self.qapf_thin_intr_fd()
        elif self.thin_section == "Yes" and self.rock_type == "Effusive" and self.qz_vs_fd == "Feldspathoids":
            self.qapf_thin_effu_fd()
        elif self.thin_section == "No" and self.rock_type == "Intrusive" and self.qz_vs_fd == "Quartz":
            self.qapf_no_thin_intr_qz()
        elif self.thin_section == "No" and self.rock_type == "Effusive" and self.qz_vs_fd == "Quartz":
            self.qapf_no_thin_effu_qz()
            
        rock_name = self.rock_name
        
        sample_info = f"Sample code: {sample_code}\nRock name: {rock_name}\nFormal description: {rock_constn} {rock_name} with {textr_struc} texture, {alt_lvl} {alteration} alteration, from a probable {emp_level} enviroment and the following observations: {observations}\n\nAll data\nSample location: {sample_location}\nAnalyst: {analyst}\nCoordinates: {east_coordinate}; {north_coordinate}\nThin section: {thin_section}\nRock type: {rock_type}\nRock general constitution: {rock_constn}\nTextures and structures: {textr_struc}\nHave Qz or Fd: {qz_vs_fd}\nEmplacement level: {emp_level}\nAlteration: {alteration}\nAlteration level: {alt_lvl}"
        
        self.info_box.insert(tk.END, sample_info)
        self.info_box.config(state = tk.DISABLED) #EVITA QUE SE PUEDA EDITAR EL TEXTO
    
    def save_analysis(self):
        file = filedialog.asksaveasfile(
                                    defaultextension = ".txt",
                                    filetypes = [
                                        ("Text file", ".txt"),
                                        ("HTML File", ".html"),
                                        ("All files", "*.*")
                                    ])
    
        if file is None:  # Evita lanzar una excepción cuando cerramos la ventana de guardado sin guardar nada
            return
        file_text = str(self.info_box.get(1.0, END))
        file.write(file_text)
        file.close()
    
    #FUNCIONES PARA LAS HERRAMIENTAS DEL MENU EDIT
    def get_focus_widget(self):
        widget = self.focus_get()
        return widget if isinstance(widget, (Entry, Text)) else None

    def undo_text(self):
        widget = self.get_focus_widget()
        if isinstance(widget, Text):  # Sólo Text soporta undo/redo
            try:
                widget.edit_undo()
            except Exception:
                pass

    def redo_text(self):
        widget = self.get_focus_widget()
        if isinstance(widget, Text):
            try:
                widget.edit_redo()
            except Exception:
                pass

    def cut_text(self):
        widget = self.get_focus_widget()
        try:
            widget.event_generate("<<Cut>>")
        except Exception:
            pass

    def copy_text(self):
        widget = self.get_focus_widget()
        try:
            widget.event_generate("<<Copy>>")
        except Exception:
            pass

    def paste_text(self):
        widget = self.get_focus_widget()
        try:
            widget.event_generate("<<Paste>>")
        except Exception:
            pass
    
app = App()
app.mainloop()
