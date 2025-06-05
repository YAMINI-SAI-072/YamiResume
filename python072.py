import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import io
import warnings

# Suppress SSL warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

def scrape_website(url):
    try:
        # Perform the request with SSL verification disabled
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract headings, paragraphs, and div/span text
            headings = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
            paragraphs = [p.get_text() for p in soup.find_all('p')]
            div_texts = [div.get_text() for div in soup.find_all('div')]
            scraped_text = headings + paragraphs + div_texts

            # Extract image URLs
            images = soup.find_all('img')
            img_urls = [img.get('src') for img in images if img.get('src')]

            # Clear the text box
            text_box.delete(1.0, tk.END)

            # Display scraped text
            text_box.insert(tk.END, "Scraped Text Content:\n\n")
            for text in scraped_text:
                text_box.insert(tk.END, text + "\n\n")

            # Display the first image (if available)
            if img_urls:
                img_url = img_urls[0]
                if not img_url.startswith('http'):
                    img_url = requests.compat.urljoin(url, img_url)
                img_response = requests.get(img_url, headers=headers, verify=False)
                img_data = img_response.content
                img = Image.open(io.BytesIO(img_data))
                img = img.resize((300, 200))  # Resize to fit the GUI
                img_display = ImageTk.PhotoImage(img)
                img_label.config(image=img_display)
                img_label.image = img_display
            else:
                img_label.config(image=None)
        else:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, f"Failed to retrieve the webpage. Status code: {response.status_code}")
    except Exception as e:
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, f"An error occurred: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Web Scraping Tool")
root.geometry("850x650")
root.configure(bg="#f8f9fa")

# Apply a theme
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12, "bold"), padding=5)
style.configure("TLabel", background="#F3F4F6", font=("Helvetica", 12), padding=5)
style.configure("TEntry", font=("Helvetica", 12), padding=5)
style.configure("TText", background="white", font=("Helvetica", 12), padding=5)

# Gradient Header Canvas
header_canvas = tk.Canvas(root, height=100, bg="white", highlightthickness=0)
header_canvas.pack(fill=tk.X)

header_gradient = header_canvas.create_rectangle(0, 0, 850, 100, fill="", outline="")
header_canvas.itemconfig(header_gradient, fill="#ff7f50")
header_text = header_canvas.create_text(425, 50, text="🌐 Web Scraping Tool 🌐", font=("Century Gothic", 28, "bold"), fill="Black")

def adjust_header(event):
    width = event.width
    header_canvas.coords(header_gradient, 0, 0, width, 100)
    header_canvas.coords(header_text, width // 2, 50)

header_canvas.bind("<Configure>", adjust_header)

# URL Entry Section
url_frame = ttk.Frame(root, padding=10)
url_frame.pack(pady=10)
url_label = ttk.Label(url_frame, text="Enter Website URL:")
url_label.grid(row=0, column=0, padx=5)
url_entry = ttk.Entry(url_frame, width=50)
url_entry.grid(row=0, column=1, padx=5)

# Scrape Button
scrape_button = ttk.Button(root, text="Scrape", command=lambda: scrape_website(url_entry.get()))
scrape_button.pack(pady=10)

# Text Box to Display Scraped Text
text_box_frame = ttk.LabelFrame(root, text="Scraped Text", padding=10)
text_box_frame.pack(padx=10, pady=10, fill="both", expand=True)
text_box = tk.Text(text_box_frame, wrap=tk.WORD, width=80, height=10, relief="flat")
text_box.pack(fill="both", expand=True)

# Image Label to Display Scraped Image
img_label_frame = ttk.LabelFrame(root, text="Scraped Image", padding=10)
img_label_frame.pack(padx=10, pady=10, fill="both", expand=True)
img_label = tk.Label(img_label_frame)
img_label.pack()

# Run the GUI
root.mainloop()
