from tkinter import *

# CybersecurityRiskAssessment class is a single page GUI Cybersecurity Risk Assessment calculator to evaluate 
# the probability of Cybersecurity incidents using the Single Loss Expectancy (SLE) and Annual Loss Expectancy (ALE) fomulas.
# The SLE is caculated by multiplying the asset value (AV) with the exposure value (EV), and the ALE is calcualted by
# multiplying the SLE with the annualised rated of occurrence (AR)
class CybersecurityRiskAssessment():

    def __init__(self):
        # Instantiate window object
        self.window = Tk()

        # Set the title of window and size
        self.window.title("Cybersecurity Risk Assessment")
        self.window.geometry("700x400")

        # Add asset name to the layout
        self.asset_name_label = Label(self.window, text="Enter the asset name:", anchor='w', width=20)
        self.asset_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.asset_name_input = Entry(self.window, width=10)
        self.asset_name_input.grid(row=0, column=1, padx=10, pady=10)

        # Add asset value to the layout
        self.asset_value_label = Label(self.window, text="Enter the asset value:", anchor='w', width=20)
        self.asset_value_label.grid(row=1, column=0, padx=10, pady=10)
        self.asset_value_input = Entry(self.window, width=10)
        self.asset_value_input.grid(row=1, column=1, padx=10, pady=10)

        # Add exposure value to the layout
        self.exp_label = Label(self.window, text="Enter the exposure value:", anchor='w', width=20)
        self.exp_label.grid(row=2, column=0, padx=10, pady=10)
        self.exp_input = Entry(self.window, width=10)
        self.exp_input.grid(row=2, column=1, padx=10, pady=10)

        # Add annularised rate to the layout
        self.annualarised_rate_label = Label(self.window, text="Enter the annualarised rate of occurance:", anchor='w', width=20)
        self.annualarised_rate_label.grid(row=3, column=0, padx=10, pady=10)
        self.annualarised_rate_input = Entry(self.window, width=10)
        self.annualarised_rate_input.grid(row=3, column=1, padx=10, pady=10)

        # Add the calculate button to the layout
        self.calculate_button = Button(self.window, text="Calculate", anchor='center', width=5)
        self.calculate_button.grid(row=4, column=0, padx=5, pady=10)

        # Add the clear button to the layout
        self.clear_button = Button(self.window, text="Clear", anchor='center', width=5)
        self.clear_button.grid(row=4, column=1, padx=5, pady=10)

        # Add the close button to the layout
        self.close_button = Button(self.window, text="Exit", anchor='center', width=5)
        self.close_button.grid(row=4, column=2, padx=5, pady=10)

        # Add asset name label for the output to the layout
        self.asset_name_output_label = Label(self.window, text="Asset name is:", anchor='w', width=30)
        self.asset_name_output_label.grid(row=5, column=1, padx=10, pady=10)

        # Add SLE value label for the output to the layout
        self.sle_output_label = Label(self.window, text="SLE result is:", anchor='w', width=30)
        self.sle_output_label.grid(row=6, column=1, padx=10, pady=10)

        # Add ALE value label for the output to the layout
        self.ale_output_label = Label(self.window, text="ALE result is:", anchor='w', width=30)
        self.ale_output_label.grid(row=7, column=1, padx=10, pady=10)

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

    def run(self):
        self.window.mainloop()

cra = CybersecurityRiskAssessment()
cra.run()


# Function setAssetName(assetName an)
#     Set user input AssetName = an

# Function setAssetValue(assetValue av)
#     Set user input AssetValue = av

# Function setExposureValue(exposureValue ev)
#     Set user input ExposureValue = ev

# Function setAnnualisedRate(annualisedRate ar)
#     Set user input AnnualisedRate = ar

# Function updateSelectedAssetName(asset a)
#     Set Asset Name text with a

# Function updateSLEResult(result r)
#     Set SLE result text with r

# Function updateALEResult(result r)
#     Set ALE result text with r

# Function calculate()
#     av = getAssetValue()
#     ev = exposureValue()
#     ar = getAnnualisedRate()

#     SLE = av X ev
#     ALE = SLE X ar

#     Return SLE, ALE

# Function displayError()
#     updateSLEResult(“Unable to calculate SLE due to input error, please try again”)
#     updateALEResult(“Unable to calculate ALE due to input error, please try again”)

# Function calculateButtonClicked()
#     Try
#         an = getAssetName() and convert to uppercase
#         assetNameText = “Asset name is: “ + an
#         updateSelectedAssetName(assetNameText)
#         SLE, ALE = calculate()
#         SLE_TEXT = convert SLE to string
#         ALE_TEXT = convert ALE to string
#         updateSLEResult(“SLE result is: “ + SLE_TEXT)
#         updateALEResult(“ALE result is: “ + ALE_TEXT)
#     Catch Error
#         displayError()

# Function closeButtonClicked()
#     Close main window

# Function clearButtonClicked()
#     setAssetName(empty value)
#     setAssetValue(empty value)
#     setExposureValue(empty value)
#     setAnnualisedRate(empty value)

# if calculateButton is clicked
#    calculateButtonClicked()

# if clearButton is clicked
#     clearButtonClicked()

# if closeButton is clicked
#     closeButtonClicked()
