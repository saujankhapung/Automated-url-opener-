#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sys
import os
import webbrowser

def open_links_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                url = line.strip()
                if url.startswith("http://") or url.startswith("https://"):
                    webbrowser.open(url)
                else:
                    print(f"Ignoring invalid URL: {url}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the directory where the executable is located
    exe_dir = os.path.dirname(sys.executable)
    # Define the path to the "url.txt" file in the same directory
    url_file_path = os.path.join(exe_dir, "url.txt")
    # Open links from the "url.txt" file
    open_links_from_file(url_file_path)


# In[ ]:




