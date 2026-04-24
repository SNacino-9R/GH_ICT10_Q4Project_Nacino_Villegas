from pyscript import display, HTML
import numpy as np


photo_files = np.array(['pic1.jpg', 'pic2.jpg', 'pic3.jpg', 'pic4.jpg'])


titles = np.array([
    'Joint-Campout', 
    'Pecha-Kucha', 
    'Intramurals', 
    'Presidents Day'
])


captions = np.array([
    'INSERT CAPTION', 
    'INSERT CAPTION', 
    'INSERT CAPTION', 
    'INSERT CAPTION'
])


for i in range(len(photo_files)):
    photo_html = f"""
    <div class="photo-card">
        <img src="images/{photo_files[i]}" alt="{titles[i]}">
        <div class="caption-box">
            <div class="caption-title">{titles[i]}</div>
            <div class="caption-text">{captions[i]}</div>
        </div>
    </div>
    """
    display(HTML(photo_html), target="gallery")
