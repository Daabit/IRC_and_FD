from tkinter import *
from tkinter import messagebox


#Clases
class App(Tk):
    
    def __init__(self):
        super().__init__()
        
        #Ventana de programa
        self.title("Igneous Rock Classifier & Formal Description")
        
        #MENUBAR
        self.menubar = Menu(self)
        self.config(menu = self.menubar)

        self.file_menu = Menu(self.menubar, tearoff = 0) #tearoff = 0 quita unas líneas que salen al principio del menu desplegable.
        self.menubar.add_cascade(label = "Archivo", menu = self.file_menu)
        self.file_menu.add_separator() #Añade una linea horizontal para separar opciones.
        self.file_menu.add_command(label = "Nuevo")
        self.file_menu.add_command(label = "Abrir")
        self.file_menu.add_command(label = "Guardar")
        self.file_menu.add_separator() #Añade una linea horizontal para separar opciones.
        self.file_menu.add_command(label = "Salir", command = quit)

        self.edit_menu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "Editar", menu = self.edit_menu)
        self.edit_menu.add_separator() #Añade una linea horizontal para separar opciones.
        self.edit_menu.add_command(label = "Deshacer")
        self.edit_menu.add_command(label = "Rehacer")
        self.edit_menu.add_separator() #Añade una linea horizontal para separar opciones.
        self.edit_menu.add_command(label = "Cortar")
        self.edit_menu.add_command(label = "Copiar")
        self.edit_menu.add_command(label = "Pegar")

        self.help_menu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "Ayuda", menu = self.help_menu)
        self.help_menu.add_command(label = "Sobre Rocas2", command = self.create_window_IRC)
                
        #WIDGETS
        
        #1. General data
        self.gral_data_frame = Frame(self)
        self.gral_data_frame.grid(row = 0, column = 0, sticky = "n", padx = 5, pady = 5)
        self.gral_data_label = Label(self.gral_data_frame, text = "1. GENERAL DATA", font = ("Helvetica", 10, "bold"))
        self.gral_data_label.grid(row = 0, column = 0, columnspan = 2, sticky = "n")
        
        #Sample code
        self.sample_code_label = Label(self.gral_data_frame, text = "Sample code:")
        self.sample_code_label.grid(row = 1, column = 0, sticky = "w")
        
        self.sample_code_entry = Entry(self.gral_data_frame)
        self.sample_code_entry.grid(row = 1, column = 1)
        
        #Sample location
        self.sample_location_label = Label(self.gral_data_frame, text = "Sample location:")
        self.sample_location_label.grid(row = 2, column = 0, sticky = "w")
        
        self.sample_location_entry = Entry(self.gral_data_frame)
        self.sample_location_entry.grid(row = 2, column = 1)
        
        #Analyst name
        self.analyst_name_label = Label(self.gral_data_frame, text = "Analyst:")
        self.analyst_name_label.grid(row = 3, column = 0, sticky = "w")
        
        self.analyst_name_entry = Entry(self.gral_data_frame)
        self.analyst_name_entry.grid(row = 3, column = 1)
        
        #Sample coordinates
        self.coordinates_label = Label(self.gral_data_frame, text = "Sample coordinates", font = ("Helvetica", 10, "bold"))
        self.coordinates_label.grid(row = 4, column = 0, columnspan = 2)
        
        self.sample_e_coord_label = Label(self.gral_data_frame, text = "East coordinate:")
        self.sample_e_coord_label.grid(row = 5, column = 0, sticky = "w")
        
        self.sample_e_coord_entry = Entry(self.gral_data_frame)
        self.sample_e_coord_entry.grid(row = 5, column = 1)
        
        self.sample_n_coord_label = Label(self.gral_data_frame, text = "North coordinate:")
        self.sample_n_coord_label.grid(row = 6, column = 0, sticky = "w")
        
        self.sample_n_coord_entry = Entry(self.gral_data_frame)
        self.sample_n_coord_entry.grid(row = 6, column = 1)
        
        #Thin secton available
        self.thin_section_avail = Label(self.gral_data_frame, text = "Thin section available", font = ("Helvetica", 10, "bold"))
        self.thin_section_avail.grid(row = 7, column = 0, columnspan = 2)
        
        self.thin_section_IV = IntVar()
        self.thin_section_selection = ["Yes", "No"]
        
        for index in range(len(self.thin_section_selection)):
            self.thin_section_rb = Radiobutton(
                self.gral_data_frame,
                text = self.thin_section_selection[index],
                variable = self.thin_section_IV,
                value = index,
                command = self.choose_thin_section)
            self.thin_section_rb.grid(row = 8, column = 0 + index)

        #Intrusive vs Effusive
        self.intr_vs_effu = Label(self.gral_data_frame, text = "Your rock is intrusive or effusive?")
        self.intr_vs_effu.grid(row = 11, column = 0, columnspan = 2)
        
        self.intr_vs_effu_IV = IntVar()
        self.intr_vs_effu_selection = ["Intrusive", "Effusive"]
        
        self.rock_type = None
        
        for index in range(len(self.intr_vs_effu_selection)):
            self.intr_vs_effu_rb = Radiobutton(
                self.gral_data_frame,
                text = self.intr_vs_effu_selection[index],
                variable = self.intr_vs_effu_IV,
                value = index,
                command = self.choose_intr_vs_effu)
            self.intr_vs_effu_rb.grid(row = 12, column = 0 + index)
            
            self.intr_vs_effu_IV.set(0)
            self.choose_intr_vs_effu()  # Asigna self.rock_type con base en la opción por defecto, para que no aparezca None o [""] al procesar los datos.
            
        #2. Rock General Constitution
        self.gral_rock_constn_frame = Frame(self)
        self.gral_rock_constn_frame.grid(row = 1, column = 0, sticky = "n", padx = 5, pady = 5)
        
        self.gral_rock_constn = Label(self.gral_rock_constn_frame, text = "2. ROCK GENERAL CONSTITUTION", font = ("Helvetica", 10, "bold"))
        self.gral_rock_constn.grid(row = 0, column = 0, columnspan = 2) 
        
        self.gral_rock_constn_IV = IntVar()
        self.gral_rock_constn_selection = ["Holocristalina de grano grueso", "Holocristalina de grano medio",
                          "Holocristalina de grano fino", "Hipocristalina", "Hipohialina"]

        self.rock_constn = None

        for index in range(len(self.gral_rock_constn_selection)):
            self.gral_rock_constn_rb = Radiobutton(self.gral_rock_constn_frame, 
                                           text = self.gral_rock_constn_selection[index],
                                           variable = self.gral_rock_constn_IV,
                                           value = index,
                                           command = self.choose_general_rock_constn)
            self.gral_rock_constn_rb.grid(row = 1 + index + 1, column=0, columnspan = 2, sticky = "w") # "index + 1" para que las opcines salgan verticales y no se solape con su respectivo label
        
            self.gral_rock_constn_IV.set(0)
            self.choose_general_rock_constn()  # Asigna self.rock_constn con base en la opción por defecto, para que no aparezca None o [""] al procesar los datos.
        
        #3. Main texture and structures
        self.textr_struc_frame = Frame(self)
        self.textr_struc_frame.grid(row = 0, column = 1, sticky = "n", padx = 5, pady = 5)
        self.textr_struc = Label(self.textr_struc_frame, text = "3. MAIN TEXTURES AND \nSTRUCTURES", font = ("Helvetica", 10, "bold")).grid(row = 0, column = 0)
        
        self.list_textr_struc = Listbox(self.textr_struc_frame, selectmode = MULTIPLE)
        self.list_textr_struc.grid(row = 1, column = 0)

        self.list_textr_struc.insert(1, "Porfírica")
        self.list_textr_struc.insert(2, "Glomeroporfírica")
        self.list_textr_struc.insert(3, "Miarolítica")
        self.list_textr_struc.insert(4, "Amigdalar")
        self.list_textr_struc.insert(5, "Bandeada")
        self.list_textr_struc.insert(6, "Laminar")
        self.list_textr_struc.insert(7, "Masiva")
        self.list_textr_struc.insert(8, "Pegmatítica")
        self.list_textr_struc.insert(9, "Estratificada-foliada")

        self.list_textr_struc.config(height=self.list_textr_struc.size()) #El tamaño de la caja se ajustará a la cantidad de items

        self.add_textr_struc = Entry(self.textr_struc_frame)
        self.add_textr_struc.grid(row = 2, column = 0)
        
        self.add_option_textr = Label(self.textr_struc_frame, text = "Añadir otra opción a la lista:").grid(row = 3, column = 0)

        self.add_textr_struc_bt = Button(self.textr_struc_frame, text = "Añadir", command = self.new_textr_struc)
        self.add_textr_struc_bt.grid(row = 4, column = 0)
        
        #4. Quartz or Feldspathoids
        self.qz_vs_fd_frame = Frame(self)
        self.qz_vs_fd_frame.grid(row = 1, column = 1, sticky = "n", padx = 5, pady = 5)
        self.toggle_frame_state(self.qz_vs_fd_frame, 'disabled')
        
        self.qz_vs_fd_label = Label(self.qz_vs_fd_frame, text = "4. DOES YOUR SAMPLE HAVE \nQUARTZ OR FELDSPATHOIDS?", font = ("Helvetica", 10, "bold"))
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
        self.req_minerals_thin_frame = Frame(self)
        self.req_minerals_thin_frame.grid(row = 0, column = 2, sticky = "n", padx = 5, pady = 5)

        self.req_minerals_thin = Label(self.req_minerals_thin_frame, text = "5. REQUIRED MINERALS", font = ("Helvetica", 10, "bold"))
        self.req_minerals_thin.grid(row = 0, column = 0, columnspan = 2, sticky = "n")
        
        self.qz_thin = Label(self.req_minerals_thin_frame, text = "Quartz:")
        self.qz_thin.grid(row = 1, column = 0)
        self.qz_thin_entry = Entry(self.req_minerals_thin_frame, width = 2)
        self.qz_thin_entry.grid(row = 1, column = 1)
        
        self.af_thin = Label(self.req_minerals_thin_frame, text = "Alkali feldspar:")
        self.af_thin.grid(row = 2, column = 0)
        self.af_thin_entry = Entry(self.req_minerals_thin_frame, width = 2)
        self.af_thin_entry.grid(row = 2, column = 1)
        
        self.pl_thin = Label(self.req_minerals_thin_frame, text = "Plagioclase:")
        self.pl_thin.grid(row = 3, column = 0)
        self.pl_thin_entry = Entry(self.req_minerals_thin_frame, width = 2)
        self.pl_thin_entry.grid(row = 3, column = 1)
        
        self.ol_thin = Label(self.req_minerals_thin_frame, text = "Olivine:")
        self.ol_thin.grid(row = 4, column = 0)
        self.ol_thin_entry = Entry(self.req_minerals_thin_frame, width = 2)
        self.ol_thin_entry.grid(row = 4, column = 1)
        
        self.clpx_thin = Label(self.req_minerals_thin_frame, text = "Clinopyroxene:")
        self.clpx_thin.grid(row = 5, column = 0)
        self.clpx_thin_entry = Entry(self.req_minerals_thin_frame, width = 2)
        self.clpx_thin_entry.grid(row = 5, column = 1)
        
        self.orpx_thin = Label(self.req_minerals_thin_frame, text = "Orthopyroxene:")
        self.orpx_thin.grid(row = 6, column = 0)
        self.orpx_thin_entry = Entry(self.req_minerals_thin_frame, width = 2)
        self.orpx_thin_entry.grid(row = 6, column = 1)
        
        self.amph_thin = Label(self.req_minerals_thin_frame, text = "Amphibole:")
        self.amph_thin.grid(row = 7, column = 0)
        self.amph_thin_entry = Entry(self.req_minerals_thin_frame, width = 2)
        self.amph_thin_entry.grid(row = 7, column = 1)
        
        self.bt_thin = Label(self.req_minerals_thin_frame, text = "Biotite:")
        self.bt_thin.grid(row = 8, column = 0)
        self.bt_thin_entry = Entry(self.req_minerals_thin_frame, width = 2)
        self.bt_thin_entry.grid(row = 8, column = 1)
        
        self.mzv_thin = Label(self.req_minerals_thin_frame, text = "Muscovite:")
        self.mzv_thin.grid(row = 9, column = 0)
        self.mzv_thin_entry = Entry(self.req_minerals_thin_frame, width = 2)
        self.mzv_thin_entry.grid(row = 9, column = 1)
        
        self.ox_feti_thin = Label(self.req_minerals_thin_frame, text = "Fe-Ti oxides:")
        self.ox_feti_thin.grid(row = 10, column = 0)
        self.ox_feti_thin_entry = Entry(self.req_minerals_thin_frame, width = 2)
        self.ox_feti_thin_entry.grid(row = 10, column = 1)
        
        #Thin section Feldspathoids
        self.req_minerals_thin_frame_fd = Frame(self)
        self.req_minerals_thin_frame_fd.grid(row = 0, column = 2, sticky = "n", padx = 5, pady = 5)

        self.req_minerals_thin = Label(self.req_minerals_thin_frame_fd, text = "5. REQUIRED MINERALS", font = ("Helvetica", 10, "bold"))
        self.req_minerals_thin.grid(row = 0, column = 0, columnspan = 2, sticky = "n")
        
        self.fd_thin_fd = Label(self.req_minerals_thin_frame_fd, text = "Feldspathoid:")
        self.fd_thin_fd.grid(row = 1, column = 0)
        self.fd_thin_entry = Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.fd_thin_entry.grid(row = 1, column = 1)
        
        self.af_thin = Label(self.req_minerals_thin_frame_fd, text = "Alkali feldspar:")
        self.af_thin.grid(row = 2, column = 0)
        self.af_thin_entry = Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.af_thin_entry.grid(row = 2, column = 1)
        
        self.pl_thin = Label(self.req_minerals_thin_frame_fd, text = "Plagioclase:")
        self.pl_thin.grid(row = 3, column = 0)
        self.pl_thin_entry = Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.pl_thin_entry.grid(row = 3, column = 1)
        
        self.ol_thin = Label(self.req_minerals_thin_frame_fd, text = "Olivine:")
        self.ol_thin.grid(row = 4, column = 0)
        self.ol_thin_entry = Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.ol_thin_entry.grid(row = 4, column = 1)
        
        self.clpx_thin = Label(self.req_minerals_thin_frame_fd, text = "Clinopyroxene:")
        self.clpx_thin.grid(row = 5, column = 0)
        self.clpx_thin_entry = Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.clpx_thin_entry.grid(row = 5, column = 1)
        
        self.orpx_thin = Label(self.req_minerals_thin_frame_fd, text = "Orthopyroxene:")
        self.orpx_thin.grid(row = 6, column = 0)
        self.orpx_thin_entry = Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.orpx_thin_entry.grid(row = 6, column = 1)
        
        self.amph_thin = Label(self.req_minerals_thin_frame_fd, text = "Amphibole:")
        self.amph_thin.grid(row = 7, column = 0)
        self.amph_thin_entry = Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.amph_thin_entry.grid(row = 7, column = 1)
        
        self.bt_thin = Label(self.req_minerals_thin_frame_fd, text = "Biotite:")
        self.bt_thin.grid(row = 8, column = 0)
        self.bt_thin_entry = Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.bt_thin_entry.grid(row = 8, column = 1)
        
        self.mzv_thin = Label(self.req_minerals_thin_frame_fd, text = "Muscovite:")
        self.mzv_thin.grid(row = 9, column = 0)
        self.mzv_thin_entry = Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.mzv_thin_entry.grid(row = 9, column = 1)
        
        self.ox_feti_thin = Label(self.req_minerals_thin_frame_fd, text = "Fe-Ti oxides:")
        self.ox_feti_thin.grid(row = 10, column = 0)
        self.ox_feti_thin_entry = Entry(self.req_minerals_thin_frame_fd, width = 2)
        self.ox_feti_thin_entry.grid(row = 10, column = 1)
        
        #No thin section
        self.req_minerals_no_thin_frame = Frame(self)
        self.req_minerals_no_thin_frame.grid(row = 0, column = 2, sticky = "n", padx = 5, pady = 5)
        
        self.req_minerals_no_thin = Label(self.req_minerals_no_thin_frame, text = "5. REQUIRED MINERALS", font = ("Helvetica", 10, "bold"))
        self.req_minerals_no_thin.grid(row = 0, column = 0, columnspan = 2, sticky = "n")
        
        self.qz_no_thin = Label(self.req_minerals_no_thin_frame, text = "Quartz:")
        self.qz_no_thin.grid(row = 1, column = 0)
        self.qz_no_thin_entry = Entry(self.req_minerals_no_thin_frame, width = 2)
        self.qz_no_thin_entry.grid(row = 1, column = 1)
        
        self.af_no_thin = Label(self.req_minerals_no_thin_frame, text = "Alkali feldspar:")
        self.af_no_thin.grid(row = 2, column = 0)
        self.af_no_thin_entry = Entry(self.req_minerals_no_thin_frame, width = 2)
        self.af_no_thin_entry.grid(row = 2, column = 1)
        
        self.pl_no_thin = Label(self.req_minerals_no_thin_frame, text = "Plagioclase:")
        self.pl_no_thin.grid(row = 3, column = 0)
        self.pl_no_thin_entry = Entry(self.req_minerals_no_thin_frame, width = 2)
        self.pl_no_thin_entry.grid(row = 3, column = 1)
        
        self.m_no_thin = Label(self.req_minerals_no_thin_frame, text = "M:")
        self.m_no_thin.grid(row = 4, column = 0)
        self.m_no_thin_entry = Entry(self.req_minerals_no_thin_frame, width = 2)
        self.m_no_thin_entry.grid(row = 4, column = 1)
        
        #Estas dos funciones deben ir aquí porque deben esperar a que se creen los frames necesarios para actuar correctamente y permitan tener una opción seleccionada por default, a comparación de los otros radiobutton donde las funciones están dentro de la misma sección.
        self.choose_qz_vs_fd_frame()
        self.choose_qz_vs_fd()
        
        #6. Emplacement level
        self.emplacement_level_frame = Frame(self)
        self.emplacement_level_frame.grid(row = 1, column = 2, sticky = "n", padx = 5, pady = 5)
        
        self.emplacement_level = Label(self.emplacement_level_frame, text = "6. EMPLACEMENT LEVEL", font = ("Helvetica", 10, "bold"))
        self.emplacement_level.grid(row = 0, column = 0, columnspan = 2)
        
        self.emplacement_level_IV = IntVar()
        self.emplacement_level_selection = ["Plutónico profundo", "Hipabisal",
                          "Hipovolcánico"]

        self.emp_level = None
        
        for index in range(len(self.emplacement_level_selection)):
            radiobutton_emplacement = Radiobutton(self.emplacement_level_frame, 
                                           text = self.emplacement_level_selection[index],
                                           variable = self.emplacement_level_IV,
                                           value = index,
                                           command = self.choose_emplacement_level)
            radiobutton_emplacement.grid(row = index + 1, column=0, sticky = "w") # "index + 1" para que las opcines salgan verticales y no se solape con su respectivo label

            self.emplacement_level_IV.set(0)
            self.choose_emplacement_level()  # Asigna self.emp_level con base en la opción por defecto, para que no aparezca None o [""] al procesar los datos.

        #7. Alteration
        self.alteration_frame = Frame(self)
        self.alteration_frame.grid(row = 0, column = 3, sticky = "n", padx = 5, pady = 5)
        
        self.alteration = Label(self.alteration_frame, text = "7. ALTERATION", font = ("Helvetica", 10, "bold"))
        self.alteration.grid(row = 0, column = 0)
        
        self.list_alteration = Listbox(self.alteration_frame, selectmode = MULTIPLE)
        self.list_alteration.grid(row = 1, column = 0, sticky = "ew")

        self.list_alteration.insert(1, "Silicificación")
        self.list_alteration.insert(2, "Oxidación")
        self.list_alteration.insert(3, "Propilítica")
        self.list_alteration.insert(4, "Arcillosa")
        self.list_alteration.insert(5, "Calcárea")

        self.list_alteration.config(height=self.list_alteration.size()) #El tamaño de la caja se ajustará a la cantidad de items

        self.new_alteration = Entry(self.alteration_frame)
        self.new_alteration.grid(row = 3, column = 0, sticky = "ew")

        add_new_alteration = Button(self.alteration_frame, text = "Añadir", command = self.add_alteration)
        add_new_alteration.grid(row = 4, column = 0, sticky = "ew")
        
        #8. Alteration level
        self.alteration_level_frame = Frame(self)
        self.alteration_level_frame.grid(row = 1, column = 3, sticky = "n", padx = 5, pady = 5)
        
        self.alteration_level = Label(self.alteration_level_frame, text = "8. ALTERATION LEVEL", font = ("Helvetica", 10, "bold"))
        self.alteration_level.grid(row = 0, column = 0, sticky = "n")
        
        self.alteration_level_IV = IntVar()
        self.alteration_level_selection = ["Débil", "Moderada",
                          "Fuerte"]

        self.alt_lvl = None

        for index in range(len(self.alteration_level_selection)):
            radiobutton_alteration_lvl = Radiobutton(self.alteration_level_frame, 
                                           text = self.alteration_level_selection[index],
                                           variable = self.alteration_level_IV,
                                           value = index,
                                           command = self.choose_alteration_level)
            radiobutton_alteration_lvl.grid(row = index + 1, column = 0, sticky = "w") # "index + 1" para que las opcines salgan verticales y no se solape con su respectivo label
        
            self.alteration_level_IV.set(0)
            self.choose_alteration_level()  # Asigna self.alt_lvl con base en la opción por defecto, para que no aparezca None o [""] al procesar los datos.
        
        #9. Observations
        self.observations_results_frame = Frame(self)
        self.observations_results_frame.grid(row = 2, column = 0, columnspan = 4, sticky = "new", padx = 5, pady = 5)
        
        self.observations = Label(self.observations_results_frame, text = "9. OBSERVATIONS", font = ("Helvetica", 10, "bold"))
        self.observations.grid(row = 0, column = 0)
        
        self.observations_text = Text(self.observations_results_frame)
        self.observations_text.config(width = 25, height = 10)
        self.observations_text.grid(row = 1, column = 0)
        
        #Submit button
        self.submit_button = Button(self.observations_results_frame, text = "Process all data", command = self.submit_data)
        self.submit_button.grid(row = 2, column = 0, sticky = "n", pady = 5)
        
        #10. Results
        
        self.results = Label(self.observations_results_frame, text = "10. RESULTS", font = ("Helvetica", 10, "bold"))
        self.results.grid(row = 0, column = 1, sticky = "n")
        
        #Sample Info
        self.info_box = Text(self.observations_results_frame, width = 70, height = 10)
        self.info_box.grid(row = 1, column = 1, sticky = "n")
        
    #FUNCIONES
    def create_window_IRC(self):
        pass
    
    def choose_thin_section(self):
        if self.thin_section_IV.get() == 0:
            self.toggle_frame_state(self.qz_vs_fd_frame, 'normal')
            self.hide_all_mineral_frames()
        elif self.thin_section_IV.get() == 1:
            self.toggle_frame_state(self.qz_vs_fd_frame, 'disabled')
            self.hide_all_mineral_frames()
            self.req_minerals_no_thin_frame.grid(row = 0, column = 2, sticky = "n")
    
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
            self.rock_constn = "Holocristalina de grano grueso"
        elif(self.gral_rock_constn_IV.get() == 1):
            self.rock_constn = "Holocristalina de grano medio"
        elif(self.gral_rock_constn_IV.get() == 2):
            self.rock_constn = "Holocristalina de grano fino"
        elif(self.gral_rock_constn_IV.get() == 3):
            self.rock_constn = "Hipocristalina"
        elif(self.gral_rock_constn_IV.get() == 4):
            self.rock_constn = "Hipohialina"
    
    def qapf_intrusive(self):
        pass
    
    def qapf_effusive(self):
        pass
    
    def choose_emplacement_level(self):
        if(self.emplacement_level_IV.get() == 0):
            self.emp_level = "Plutónico profundo"
        elif(self.emplacement_level_IV.get() == 1):
            self.emp_level = "Hipabisal"
        elif(self.emplacement_level_IV.get() == 2):
            self.emp_level = "Hipovolcánico"
    
    def add_alteration(self):
        self.list_alteration.insert(END, self.new_alteration.get())
        self.list_alteration.config(height=self.list_alteration.size())
        self.new_alteration.delete(0, END)
    
    def choose_alteration_level(self):
        if(self.alteration_level_IV.get() == 0):
            self.alt_lvl = "Débil"
        elif(self.alteration_level_IV.get() == 1):
            self.alt_lvl = "Moderada"
        elif(self.alteration_level_IV.get() == 2):
            self.alt_lvl = "Fuerte"
    
    def new_textr_struc(self):
        self.list_textr_struc.insert(END, self.add_textr_struc.get())
        self.list_textr_struc.config(height=self.list_textr_struc.size())
        self.add_textr_struc.delete(0, END)

    def submit_data(self):
        import tkinter as tk    #NO SE PORQUE TUVE QUE IMPORTAR ASI PERO SI NO LO HACIA NO FUNCIONABA EL insert()
        sample_code = self.sample_code_entry.get()
        sample_location = self.sample_location_entry.get()
        analyst = self.analyst_name_entry.get()
        east_coordinate = self.sample_e_coord_entry.get()
        north_coordinate = self.sample_n_coord_entry.get()
        rock_type = self.rock_type
        rock_constn = self.rock_constn
        qz_vs_fd = self.qz_vs_fd
        alt_lvl = self.alt_lvl
        emp_level = self.emp_level
        observations = self.observations_text.get("1.0", tk.END) #Esto permite copiar todo el texto del cuadro
        
        
        sample_info = f"Sample code: {sample_code}\nSample location: {sample_location}\nAnalyst: {analyst}\nCoordinates: {east_coordinate}; {north_coordinate}\nRock type: {rock_type}\nRock general constitution: {rock_constn}\nHave Qz or Fd: {qz_vs_fd}\nAlteration level: {alt_lvl}\nEmplacement level: {emp_level}\nObservations: {observations}"
        
        self.info_box.insert(tk.END, sample_info)
        self.info_box.config(state = tk.DISABLED) #EVITA QUE SE PUEDA EDITAR EL TEXTO
    
app = App()
app.mainloop()