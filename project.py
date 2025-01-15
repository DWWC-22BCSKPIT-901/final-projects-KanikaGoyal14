import tkinter as tk
from tkinter import messagebox

# Function to calculate the Ease of Living Index (EoI)
def calculate_eoi():
    try:
        # Extracting user inputs for each sub-indicator
        health = float(health_entry.get())
        education = float(education_entry.get())
        housing = float(housing_entry.get())
        safety = float(safety_entry.get())
        
        employment = float(employment_entry.get())
        income = float(income_entry.get())
        business_opportunity = float(business_entry.get())
        
        waste_management = float(waste_entry.get())
        air_quality = float(air_quality_entry.get())
        green_spaces = float(green_spaces_entry.get())
        
        public_services = float(public_services_entry.get())
        corruption = float(corruption_entry.get())
        transparency = float(transparency_entry.get())
        
        public_transport = float(public_transport_entry.get())
        traffic_management = float(traffic_entry.get())
        road_quality = float(road_quality_entry.get())

        # Weights for each category (you can adjust these weights based on priority)
        quality_of_life_weight = 0.2
        economic_ability_weight = 0.2
        sustainability_weight = 0.2
        governance_weight = 0.2
        mobility_weight = 0.2

        # Calculating category scores as the average of sub-indicators
        quality_of_life_score = (health + education + housing + safety) / 4
        economic_ability_score = (employment + income + business_opportunity) / 3
        sustainability_score = (waste_management + air_quality + green_spaces) / 3
        governance_score = (public_services + corruption + transparency) / 3
        mobility_score = (public_transport + traffic_management + road_quality) / 3

        # Calculating the overall Ease of Living Index (EoI)
        eoi = (quality_of_life_score * quality_of_life_weight +
               economic_ability_score * economic_ability_weight +
               sustainability_score * sustainability_weight +
               governance_score * governance_weight +
               mobility_score * mobility_weight)

        # Display the result
        messagebox.showinfo("Ease of Living Index", f"The calculated Ease of Living Index score is: {eoi:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Ease of Living Index Calculator")

# Create the labels and input fields
tk.Label(root, text="Health (0-10)").grid(row=0, column=0)
health_entry = tk.Entry(root)
health_entry.grid(row=0, column=1)

tk.Label(root, text="Education (0-10)").grid(row=1, column=0)
education_entry = tk.Entry(root)
education_entry.grid(row=1, column=1)

tk.Label(root, text="Housing (0-10)").grid(row=2, column=0)
housing_entry = tk.Entry(root)
housing_entry.grid(row=2, column=1)

tk.Label(root, text="Safety (0-10)").grid(row=3, column=0)
safety_entry = tk.Entry(root)
safety_entry.grid(row=3, column=1)

tk.Label(root, text="Employment (0-10)").grid(row=4, column=0)
employment_entry = tk.Entry(root)
employment_entry.grid(row=4, column=1)

tk.Label(root, text="Income (0-10)").grid(row=5, column=0)
income_entry = tk.Entry(root)
income_entry.grid(row=5, column=1)

tk.Label(root, text="Business Opportunities (0-10)").grid(row=6, column=0)
business_entry = tk.Entry(root)
business_entry.grid(row=6, column=1)

tk.Label(root, text="Waste Management (0-10)").grid(row=7, column=0)
waste_entry = tk.Entry(root)
waste_entry.grid(row=7, column=1)

tk.Label(root, text="Air Quality (0-10)").grid(row=8, column=0)
air_quality_entry = tk.Entry(root)
air_quality_entry.grid(row=8, column=1)

tk.Label(root, text="Green Spaces (0-10)").grid(row=9, column=0)
green_spaces_entry = tk.Entry(root)
green_spaces_entry.grid(row=9, column=1)

tk.Label(root, text="Public Services (0-10)").grid(row=10, column=0)
public_services_entry = tk.Entry(root)
public_services_entry.grid(row=10, column=1)

tk.Label(root, text="Corruption Level (0-10)").grid(row=11, column=0)
corruption_entry = tk.Entry(root)
corruption_entry.grid(row=11, column=1)

tk.Label(root, text="Transparency (0-10)").grid(row=12, column=0)
transparency_entry = tk.Entry(root)
transparency_entry.grid(row=12, column=1)

tk.Label(root, text="Public Transport (0-10)").grid(row=13, column=0)
public_transport_entry = tk.Entry(root)
public_transport_entry.grid(row=13, column=1)

tk.Label(root, text="Traffic Management (0-10)").grid(row=14, column=0)
traffic_entry = tk.Entry(root)
traffic_entry.grid(row=14, column=1)

tk.Label(root, text="Road Quality (0-10)").grid(row=15, column=0)
road_quality_entry = tk.Entry(root)
road_quality_entry.grid(row=15, column=1)

# Button to calculate the EoI
calculate_button = tk.Button(root, text="Calculate EoI", command=calculate_eoi)
calculate_button.grid(row=16, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
