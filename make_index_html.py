import os

# Folder containing the images
image_folder = 'meet_images'
image_files = [img for img in os.listdir(image_folder) if img.endswith(('.jpg', '.jpeg', '.png', '.webp'))]

# HTML template
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://kit.fontawesome.com/9a00545b44.js" crossorigin="anonymous"></script>

    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="dist/css/lightbox.css">
    <link rel="stylesheet" href="css/style.css">
    <title>Document</title>
</head>
<body>
    <a href="#main" class="skip">Skip to Main Content</a>
    <nav>
        <ul>
            <li><a href="./index.html">Home Page</a></li>
            <li><a href="./mens_team.html">Men's Team</a></li>
            <li><a href="./womens_team.html">Women's Team</a></li>
        </ul>
    </nav>
    <header>
        <h1>Welcome to the Ann Arbor Skyline Athletes Page!</h1>
        <img src="./images/logo.jpg" class="top-image" alt="Athlete headshot" width="200">
    </header>
    <main id="main">
    <section id = "cards">
        <a href="./mens_team.html" class="card-text">
            <div class="card">
                <img src="images/male_runner.webp" alt="">
                <p>Men's Team</p>
            </div>
        </a>
    </section>
        <a href="./womens_team.html" class="card-text">
            <div class="card">
                <img src="images/female_runner.webp" alt="">
                <p>Women's Team</p>
            </div>
        </a>
        <h2>Gallery</h2>
        <section id="gallery">
            """

# Adding each image from meet_images to the Gallery section with alt text and data-alt attributes
for index, img_file in enumerate(image_files, start=1):
    alt_text = f"Runner {index} during cross country meet"
    html_content += f'\n            <a href="{image_folder}/{img_file}" target="_blank" data-lightbox="meet_images"><img src="{image_folder}/{img_file}" alt="{alt_text}" data-alt="{alt_text}"></a>'

# Closing the Gallery section and completing the HTML content
html_content += """
        <button class="ShowMoreButton" onclick="showMorePhotos()">See More Photos</button>
        </section>
    
    </main>
    <footer>
        <p>
            Skyline High School<br>
            <address>
                2552 North Maple Road<br>
                Ann Arbor, MI 48103<br><br>
                <a href="https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
                <a href="https://www.instagram.com/a2skylinexc/"><i class="fa-brands fa-instagram" aria-label="Instagram"></i> Follow us on Instagram</a>
            </address>
        </p>
    </footer>
    <script src="dist/js/lightbox-plus-jquery.js"></script>
    <script src="js/javascript.js"></script>
</body>
</html>"""

# Write the HTML content to index.html file
with open("index.html", "w") as file:
    file.write(html_content)

print("index.html has been created successfully.")