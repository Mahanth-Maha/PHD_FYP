import customtkinter
import os
from PIL import Image
import phd_api


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.Model = phd_api.PHD_API()
        self.image_input_path = None
        self.image_output_path, self.detect_Scores, self.detect_status = None, None, None
        self.title("PHD_FYP")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "img")
        self.logo_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "Project.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "Pothole_Detection_Banner.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "running.png")),
                                                       dark_image=Image.open(os.path.join(image_path, "running_fill.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))

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

        # create home frame
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(
            row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(
            self.home_frame, text="Select Image", command=self.browse_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(
            self.home_frame, text="Run Model", image=self.image_icon_image, compound="right", command=self.run_button_event)
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(
            self.second_frame, width=1000, height=700, font=("Courier", 16))
        self.textbox.grid(row=0, column=1, sticky="nsew")
        self.textbox.insert("0.0", "ABOUT\n\n" + """
╔═╗╔═╗╔╦╗╦ ╦╔═╗╦  ╔═╗  ╔╦╗╔═╗╔╦╗╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
╠═╝║ ║ ║ ╠═╣║ ║║  ║╣    ║║║╣  ║ ║╣ ║   ║ ║║ ║║║║
╩  ╚═╝ ╩ ╩ ╩╚═╝╩═╝╚═╝  ═╩╝╚═╝ ╩ ╚═╝╚═╝ ╩ ╩╚═╝╝╚╝
\nA web app for The Pot Hole Detection on images and open CV and TensorFlow.\n\nThe web app would include a way to upload the image that the user took of the pothole at certain location and our model would predict if there exist any pothole  and then updates the database. So, that whenever Other person logs into the webpage, he will be notified that there is a pothole day by showing the marker over the location that the picture was taken.\n\nBy using this markers on the location one could easily find out that the road that they are taking Contains a pothole, so They can slow down the vehicle or if they really want to avoid such potholes and don't, Make any damage to the vehicle, They could take another path which has the less potholes.\n\nGovernment bodies can use this app to locate the potholes that there exist in the roads and try to fix it. Or any citizens near the locations could try to fix it by covering it is something that it would make it gone. **Thus making the world a better place.**\n\n Developed by \n\t
 __     __      _      _                 __  __          _    _          _   _ _______ _    _ 
 \ \   / //\   | |    | |        /\     |  \/  |   /\   | |  | |   /\   | \ | |__   __| |  | |
  \ \_/ //  \  | |    | |       /  \    | \  / |  /  \  | |__| |  /  \  |  \| |  | |  | |__| |
   \   // /\ \ | |    | |      / /\ \   | |\/| | / /\ \ |  __  | / /\ \ | . ` |  | |  |  __  |
    | |/ ____ \| |____| |____ / ____ \  | |  | |/ ____ \| |  | |/ ____ \| |\  |  | |  | |  | |
    |_/_/    \_\______|______/_/    \_\ |_|  |_/_/    \_\_|  |_/_/    \_\_| \_|  |_|  |_|  |_|
                                                                                              
                                                                                              """)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def run_button_event(self):
        if self.image_input_path == None:
            from tkinter import messagebox
            messagebox.showerror("Error", "Select the image first !")
            return
        self.image_output_path, self.detect_Scores, self.detect_status = self.Model.run_phd_and_save_img(
            self.image_input_path)
        self.selected_image = customtkinter.CTkImage(
            Image.open(self.image_output_path), size=(300, 200))
        self.home_frame_selected_image_label = customtkinter.CTkLabel(
            self.home_frame, text="", image=self.selected_image)
        self.home_frame_selected_image_label.grid(
            row=4, column=0, padx=20, pady=10)

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def browse_image(self):
        # Ask the user to select an image file
        self.image_input_path = customtkinter.filedialog.askopenfilename()
        self.selected_image = customtkinter.CTkImage(
            Image.open(self.image_input_path), size=(300, 200))
        self.home_frame_selected_image_label = customtkinter.CTkLabel(
            self.home_frame, text="", image=self.selected_image)
        self.home_frame_selected_image_label.grid(
            row=3, column=0, padx=20, pady=10)


if __name__ == "__main__":
    print("Please Wait while loading... \nHang on tight... \nit typically takes 30 seconds to 2 minutes <ONE TIME LOAD>")
    app = App()
    app.mainloop()
