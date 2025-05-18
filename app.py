from tkinter import *

# CybersecurityRiskAssessment class is a single page GUI Cybersecurity Risk Assessment calculator to evaluate 
# the probability of Cybersecurity incidents using the Single Loss Expectancy (SLE) and Annual Loss Expectancy (ALE) fomulas.
# The SLE is caculated by multiplying the asset value (AV) with the exposure value (EV), and the ALE is calcualted by
# multiplying the SLE with the annualised rated of occurrence (AR)
class CybersecurityRiskAssessment():

    # Constructor to initialise GUI components
    def __init__(self):
        row_index = 0

        # Instantiate window object
        self.window = Tk()

        # Set the title of window and size
        self.window.title("Cybersecurity Risk Assessment")
        self.window.geometry("800x400")

        # Add asset name to the layout
        self.asset_name_label = Label(self.window, text="Enter the asset name:", anchor='w', width=30)
        self.asset_name_label.grid(row=row_index, column=0, padx=10, pady=10)
        self.asset_name_input = Entry(self.window, width=10)
        self.asset_name_input.grid(row=row_index, column=1, padx=10, pady=10)
        
        # Increment row_index
        row_index += 1

        # Add asset value to the layout
        self.asset_value_label = Label(self.window, text="Enter the asset value:", anchor='w', width=30)
        self.asset_value_label.grid(row=row_index, column=0, padx=10, pady=10)
        self.asset_value_input = Entry(self.window, width=10)
        self.asset_value_input.grid(row=row_index, column=1, padx=10, pady=10)

        # Increment row_index
        row_index += 1

        # Add exposure value to the layout
        self.exp_label = Label(self.window, text="Enter the exposure value:", anchor='w', width=30)
        self.exp_label.grid(row=row_index, column=0, padx=10, pady=10)
        self.exp_input = Entry(self.window, width=10)
        self.exp_input.grid(row=row_index, column=1, padx=10, pady=10)

        # Increment row_index
        row_index += 1

        # Add annularised rate to the layout
        self.annualarised_rate_label = Label(self.window, text="Enter the annualarised rate of occurance:", anchor='w', width=30)
        self.annualarised_rate_label.grid(row=row_index, column=0, padx=10, pady=10)
        self.annualarised_rate_input = Entry(self.window, width=10)
        self.annualarised_rate_input.grid(row=row_index, column=1, padx=10, pady=10)

        # Increment row_index
        row_index += 1
        
        # Add the calculate button to the layout
        self.calculate_button = Button(self.window, text="Calculate", anchor='center', width=5)
        self.calculate_button.grid(row=row_index, column=0, padx=5, pady=10)

        # Add the clear button to the layout
        self.clear_button = Button(self.window, text="Clear", anchor='center', width=5)
        self.clear_button.grid(row=row_index, column=1, padx=5, pady=10)

        # Add the close button to the layout
        self.close_button = Button(self.window, text="Exit", anchor='center', width=5)
        self.close_button.grid(row=row_index, column=2, padx=5, pady=10)

        # Increment row_index
        row_index += 1
        
        # Add asset name label for the output to the layout
        self.asset_name_output_label = Label(self.window, text="Asset name is:", anchor='w', width=40)
        self.asset_name_output_label.grid(row=row_index, column=1, padx=10, pady=10)

        # Add SLE value label for the output to the layout
        self.sle_output_label = Label(self.window, text="SLE result is:", anchor='w', width=40)
        self.sle_output_label.grid(row=row_index, column=1, padx=10, pady=10)

        # Add ALE value label for the output to the layout
        self.ale_output_label = Label(self.window, text="ALE result is:", anchor='w', width=40)
        self.ale_output_label.grid(row=row_index, column=1, padx=10, pady=10)

        # Bind the calculate button to the function
        self.calculate_button.bind("<Button-1>", self.calculate_button_is_clicked)

        # Bind the clear button to the function
        self.clear_button.bind("<Button-1>", self.clear_button_is_clicked)

        # Bind the close button to the function
        self.close_button.bind("<Button-1>", self.close_button_is_clicked)

    # Function get the value of asset name from user input
    # If the asset name is empty, raise an error
    def get_asset_name(self):
        an = self.asset_name_input.get()
        if not an:
            raise ValueError("Invalid asset name")
        return an
    
    # Function get the value of asset value from user input
    # If the asset value is empty or not an interger, raise an error
    def get_asset_value(self):
        av = self.asset_value_input.get()
        try:
            av = int(av)
        except ValueError as e:
            raise e
        return int(av)
    
    # Function get the value of exposure value from user input
    # If the exposure value is empty or not an integer, raise an error
    def get_exposure_value(self):
        ev = self.exp_input.get()
        try:
            ev = int(ev)
        except ValueError as e:
            print("Exposure value error:", e)
            raise e
        return int(ev)
    
    # Function get the value of annualised rate from user input
    # If the annualised rate is empty or not a float, raise an error

    def get_annualised_rate(self):
        ar = self.annualarised_rate_input.get()
        try:
            ar = float(ar)
        except ValueError as e:
            print("Annualised rate error:", e)
            raise e
        return ar
    
    def clear_asset_name(self):
        self.asset_name_input.delete(0, 'end')

    def clear_asset_value(self):
        self.asset_value_input.delete(0, 'end')

    def clear_exposure_value(self):
        self.exp_input.delete(0, 'end')

    def clear_annualised_rate(self):
        self.annualarised_rate_input.delete(0, 'end')

    # Function to calculate SLE and ALE
    def calculate(self):
        av = self.get_asset_value()
        ev = self.get_exposure_value()
        ar = self.get_annualised_rate()

        SLE = av * ev / 100
        ALE = SLE * ar

        return (SLE, ALE)

    # Update the asset name to the label with uppercase asset name
    def update_asset_name(self, asset_name = ""):
        self.asset_name_output_label.config(text = "Asset name is: " + asset_name.upper())

    # Update the SLE result to the label
    def update_sle_result(self, result):
        self.sle_output_label.config(text = "SLE result is: " + str(result))

    # Update the ALE result to the label
    def update_ale_result(self, result):
        self.ale_output_label.config(text = "ALE result is: " + str(result))

    # Display error when invalid input data is provided
    def display_error(self):
        self.sle_output_label.config(text = "Unable to calculate SLE due to input error, please try again")
        self.ale_output_label.config(text = "Unable to calculate ALE due to input error, please try again")

    # Update the calculation result to the labels
    def update_result(self, sle, ale):
        self.update_sle_result(sle)
        self.update_ale_result(ale)
        
    def run(self):
        self.window.mainloop()

    # Function to retrieve the values from the input text boxes and invoke the calculation function
    # Then update the result to the output labels
    def calculate_button_is_clicked(self, event):
        try:
            asset_name = self.get_asset_name()
            self.update_asset_name(asset_name)
            (SLE, ALE) = self.calculate()
            self.update_result(SLE, ALE)
        except ValueError as e:
            print("Error occurred:", e)
            self.display_error()

    # Function to clear all the input text boxes
    def clear_button_is_clicked(self, event):
        self.clear_asset_name()
        self.clear_asset_value()
        self.clear_exposure_value()
        self.clear_annualised_rate()
        self.update_asset_name("")
        self.update_sle_result("")
        self.update_ale_result("")

    # Function to close the application
    def close_button_is_clicked(self, event):
        self.window.destroy()

if __name__ == "__main__":
    cra = CybersecurityRiskAssessment()
    cra.run()
