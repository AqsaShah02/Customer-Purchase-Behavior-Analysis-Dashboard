import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog, messagebox

# Load and clean the dataset
def load_and_clean_data():
    global data
    file_path = filedialog.askopenfilename(title="Select Dataset", filetypes=(("CSV Files", "*.csv"),))
    if not file_path:
        return
    data = pd.read_csv(file_path)

    # Handle missing values
    data['Review Rating'] = data['Review Rating'].fillna(data['Review Rating'].mean())

    # Ensure correct data types
    data['Age'] = data['Age'].astype(int)
    data['Purchase Amount (USD)'] = data['Purchase Amount (USD)'].astype(float)

    messagebox.showinfo("Data Load", "Dataset loaded and cleaned successfully!")

# Visualizations in separate windows
def show_gender_distribution():
    plt.figure()
    sns.countplot(x='Gender', data=data, palette='pastel')
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.show()

def show_category_analysis():
    plt.figure()
    sns.barplot(x='Category', y='Purchase Amount (USD)', data=data, estimator=np.sum, palette='viridis')
    plt.title("Total Purchase Amount by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Purchase Amount (USD)")
    plt.xticks(rotation=45)
    plt.show()

def show_season_trends():
    plt.figure()
    season_trends = data.groupby('Season')['Purchase Amount (USD)'].sum()
    season_trends.plot(kind='bar', color='skyblue')
    plt.title("Seasonal Purchase Trends")
    plt.ylabel("Total Purchase Amount (USD)")
    plt.xlabel("Season")
    plt.show()

def show_age_distribution():
    plt.figure()
    sns.histplot(data['Age'], bins=10, kde=True, color='purple')
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

def show_payment_methods():
    plt.figure()
    sns.countplot(y='Preferred Payment Method', data=data, palette='cool', 
                  order=data['Preferred Payment Method'].value_counts().index)
    plt.title("Preferred Payment Methods")
    plt.xlabel("Count")
    plt.ylabel("Payment Method")
    plt.show()

# Export cleaned data
def export_cleaned_data():
    export_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV Files", "*.csv"),))
    if not export_path:
        return
    data.to_csv(export_path, index=False)
    messagebox.showinfo("Export Data", f"Cleaned data exported to {export_path}")

# Tkinter UI
root = tk.Tk()
root.title("Customer Purchase Analysis Dashboard")
root.geometry("500x400")

# Buttons for features
btn_load = tk.Button(root, text="Load & Clean Data", command=load_and_clean_data, width=30, bg="lightblue")
btn_load.pack(pady=10)

btn_gender = tk.Button(root, text="Show Gender Distribution", command=show_gender_distribution, width=30, bg="lightgreen")
btn_gender.pack(pady=10)

btn_category = tk.Button(root, text="Show Category Analysis", command=show_category_analysis, width=30, bg="lightgreen")
btn_category.pack(pady=10)

btn_season = tk.Button(root, text="Show Seasonal Trends", command=show_season_trends, width=30, bg="lightgreen")
btn_season.pack(pady=10)

btn_age = tk.Button(root, text="Show Age Distribution", command=show_age_distribution, width=30, bg="lightgreen")
btn_age.pack(pady=10)

btn_payment = tk.Button(root, text="Show Payment Methods", command=show_payment_methods, width=30, bg="lightgreen")
btn_payment.pack(pady=10)

btn_export = tk.Button(root, text="Export Cleaned Data", command=export_cleaned_data, width=30, bg="lightcoral")
btn_export.pack(pady=10)

# Main loop
root.mainloop()
