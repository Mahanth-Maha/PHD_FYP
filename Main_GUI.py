import tkinter
import customtkinter
import os
from PIL import Image
import sys
from PIL import Image
import cv2
import phd_api


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.image_input_path = None
        self.img_out = None
        self.title("PHD_FYP")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Project.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Pothole_Detection_Banner.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "running.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "running_fill.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        # self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
        #                                              dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
                
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Pothole Detection", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="About",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        # self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
        #                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
        #                                               image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        # self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
        #                                                         command=self.change_appearance_mode_event)
        # self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Select Image", command=self.browse_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Run Model", image=self.image_icon_image, compound="right", command=self.run_button_event)
        self.home_frame_button_2.grid(row=3, column=0, padx=20, pady=10)
        # self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        # self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        # self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        # self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.second_frame, width= 480,height=450)
        self.textbox.grid(row=0, column=1, sticky="nsew")
        self.textbox.insert("0.0", "ABOUT\n\n" + " test text here "*200)
        # create third frame
        # self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        # self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        # if name == "frame_3":
        #     self.third_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    # def frame_3_button_event(self):
    #     self.select_frame_by_name("frame_3")
    
    def run_button_event(self):
        print("Run button click")
        
        # import model_runner
        # open the image and display it
        # self.img_out = model_runner.run_main(self.image_input_path)
        self.selected_image = customtkinter.CTkImage(Image.open(self.image_input_path), size=(300, 200))
        self.home_frame_selected_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.selected_image)
        self.home_frame_selected_image_label.grid(row=2, column=0, padx=20, pady=10)
        # DISPLAYS OUTPUT IMAGE
        # cv2.imshow("TEST",self.img_out)
        # cv2.waitKey(0)
        # CLOSES WINDOW ONCE KEY IS PRESSED
    
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        
    def browse_image(self):
        # Ask the user to select an image file
        self.image_input_path = customtkinter.filedialog.askopenfilename()
        self.selected_image = customtkinter.CTkImage(Image.open(self.image_input_path), size=(300, 200))
        self.home_frame_selected_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.selected_image)
        self.home_frame_selected_image_label.grid(row=2, column=0, padx=20, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()