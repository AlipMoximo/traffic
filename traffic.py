import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import googlemaps
from datetime import datetime

# Initialize Google Maps client with your API key
gmaps = googlemaps.Client(key='AIzaSyBlk4ZQ9NIl1stbZxDgRswZilRFbvreuVg') #AIzaSyBlk4ZQ9NIl1stbZxDgRswZilRFbvreuVg

def get_traffic_updates(origin, destination):
    try:
        # Get directions with traffic information
        directions = gmaps.directions(origin, destination, departure_time=datetime.now())

        # Extract and display traffic updates for each step
        traffic_info = ""
        for step in directions[0]['legs'][0]['steps']:
            traffic_info += step['html_instructions'] + "\n"
            if 'traffic' in step:
                traffic_info += "Traffic: " + step['traffic']['text'] + "\n\n"

        messagebox.showinfo("Traffic Updates", traffic_info)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def calculate_optimal_route(origin, destination):
    try:
        # Get optimal route
        directions = gmaps.directions(origin, destination, departure_time=datetime.now(), alternatives=True)

        # Display summary of each route
        route_info = ""
        for i, route in enumerate(directions):
            route_info += f"Route {i + 1}:\n"
            route_info += f"Summary: {route['summary']}\n"
            route_info += f"Distance: {route['legs'][0]['distance']['text']}\n"
            route_info += f"Duration in traffic: {route['legs'][0]['duration_in_traffic']['text']}\n\n"

        messagebox.showinfo("Optimal Routes", route_info)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def suggest_alternate_routes(origin, destination):
    try:
        # Get directions with traffic information for each route
        directions = gmaps.directions(origin, destination, departure_time=datetime.now(), alternatives=True)

        # Display summary of each route
        alt_route_info = ""
        for i, route in enumerate(directions):
            alt_route_info += f"Route {i + 1}:\n"
            alt_route_info += f"Summary: {route['summary']}\n"
            alt_route_info += f"Distance: {route['legs'][0]['distance']['text']}\n"
            alt_route_info += f"Duration in traffic: {route['legs'][0]['duration_in_traffic']['text']}\n\n"

        messagebox.showinfo("Alternate Routes", alt_route_info)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    root.title("Traffic Analysis Tool")

    origin_label = ttk.Label(root, text="Origin:")
    origin_label.grid(row=0, column=0, padx=5, pady=5)
    origin_entry = ttk.Entry(root, width=30)
    origin_entry.grid(row=0, column=1, padx=5, pady=5)

    dest_label = ttk.Label(root, text="Destination:")
    dest_label.grid(row=1, column=0, padx=5, pady=5)
    dest_entry = ttk.Entry(root, width=30)
    dest_entry.grid(row=1, column=1, padx=5, pady=5)

    traffic_btn = ttk.Button(root, text="Get Traffic Updates",
                              command=lambda: get_traffic_updates(origin_entry.get(), dest_entry.get()))
    traffic_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    route_btn = ttk.Button(root, text="Calculate Optimal Route",
                            command=lambda: calculate_optimal_route(origin_entry.get(), dest_entry.get()))
    route_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    alt_route_btn = ttk.Button(root, text="Suggest Alternate Routes",
                                command=lambda: suggest_alternate_routes(origin_entry.get(), dest_entry.get()))
    alt_route_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    root.mainloop()

if __name__ == "__main__":
    main()
