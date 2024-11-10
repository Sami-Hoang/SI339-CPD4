import csv
import os 
import re


# Define the directory to scan for HTML files
directory = os.getcwd()

def extract_athlete_name(filename):
    # Remove the .html extension
    name = filename[:-5]
    # Remove trailing numbers
    name = re.sub(r'\d+$', '', name)
    # Handle underscores if there are any (in this example, underscores are not expected in names)
    name = name.replace('_', ' ')
    return name.strip()  # Remove any extra spaces

# MEN'S TEAM
# Initialize a list to hold links to HTML files
html_files = [f for f in os.listdir(directory+"/mens_team") if f.endswith('.html')]


# Generate HTML content containing links to each HTML file
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://kit.fontawesome.com/9a00545b44.js" crossorigin="anonymous"></script>

   <link rel = "stylesheet" href = "../css/reset.css">
   <link rel = "stylesheet" href = "../css/style.css">
    
    <title>Men's Team</title>
</head>
<body>
<a href = "#main" class = "skip" >Skip to Main Content</a>
   <nav>
     <ul>
        <li><a href="../index.html">Home Page</a></li>
        <li><a href="../mens_team.html">Men's Team</a></li>
        <li><a href="../womens_team.html">Women's Team</a></li>
     </ul>
     </nav>
<header>
    <h1>Men's Team</h1>
    </header>

    <main id="main">
    <table>
        <thead>
            <tr>
                <th>Athlete Name</th>
            </tr>
        </thead>
        <tbody>
'''

for html_file in html_files:
    athlete_name = extract_athlete_name(html_file)  # Extract athlete's name
    html_content += f'            <tr>\n'
    html_content += f'                <td><a href="mens_team/{html_file}">{athlete_name}</a></td>\n'
    html_content += f'            </tr>\n'

html_content += '''        </tbody>
    </table>
</main>

<footer>
        <p>
        Skyline High School<br>
        <address>
        2552 North Maple Road<br>
        Ann Arbor, MI 48103<br><br>

        <a href = "https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
        <a href = "https://www.instagram.com/a2skylinexc/"><i class="fa-brands fa-instagram" aria-label="Instagram"></i> Follow us on Instagram </a> 


        </footer>
        
</body>
</html>
'''

# Define the output file name
output_file = 'mens_team.html'

# Write the generated HTML content to the output file
with open(output_file, 'w') as file:
    file.write(html_content)

print(f'HTML file {output_file} has been generated with links to all HTML files in the directory.')


# WOMEN'S TEAM
# Initialize a list to hold links to HTML files
html_files_womens = [f for f in os.listdir(directory+"/womens_team") if f.endswith('.html')]

# Generate HTML content containing links to each HTML file
html_content_womens = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://kit.fontawesome.com/9a00545b44.js" crossorigin="anonymous"></script>

   <link rel = "stylesheet" href = "../css/reset.css">
   <link rel = "stylesheet" href = "../css/style.css">
    
    <title>Women's Team</title>
</head>
<body>
<a href = "#main" class = "skip" >Skip to Main Content</a>
   <nav>
     <ul>
        <li><a href="../index.html">Home Page</a></li>
        <li><a href="../mens_team.html">Men's Team</a></li>
        <li><a href="../womens_team.html">Women's Team</a></li>
     </ul>
     </nav>

    <header>
    <h1>Women's Team</h1>
    </header>

    <main id="main">
    <table>
        <thead>
            <tr>
                <th>Athlete Name</th>
            </tr>
        </thead>
        <tbody>
'''

for html_file in html_files_womens:
    athlete_name = extract_athlete_name(html_file)  # Extract athlete's name
    html_content_womens += f'            <tr>\n'
    html_content_womens += f'                <td><a href="womens_team/{html_file}">{athlete_name}</a></td>\n'
    html_content_womens += f'            </tr>\n'

html_content_womens += '''        </tbody>
    </table>
</main>

<footer>
        <p>
        Skyline High School<br>
        <address>
        2552 North Maple Road<br>
        Ann Arbor, MI 48103<br><br>

        <a href = "https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
        <a href = "https://www.instagram.com/a2skylinexc/"><i class="fa-brands fa-instagram" aria-label="Instagram"></i> Follow us on Instagram </a> 


        </footer>

</body>
</html>
'''

# Define the output file name
output_file = 'womens_team.html'

# Write the generated HTML content to the output file
with open(output_file, 'w') as file:
    file.write(html_content_womens)

print(f'HTML file {output_file} has been generated with links to all HTML files in the directory.')




def process_athlete_data(file_path):

   # Extracting athlete stats by year
   records = []

   # Extracting athlete races
   races = []           

   athlete_name = ""
   athlete_id = ""
   comments = ""

   with open(file_path, newline='', encoding='utf-8') as file:
      reader = csv.reader(file)
      data = list(reader)

      athlete_name = data[0][0]
      athlete_id = data[1][0]
      print(f"The athlete id for {athlete_name} is {athlete_id}")

      for row in data[5:-1]:
         if row[2]:
            records.append({"year": row[2], "sr": row[3]})
         else:
            races.append({
               "finish": row[1],
               "time": row[3],
               "meet": row[5],
               "url": row[6],
               "comments": row[7]
            })

   return {
      "name": athlete_name,
      "athlete_id": athlete_id,
      "season_records": records,
      "race_results": races,
      "comments": comments
   }    

def gen_athlete_page(data, outfile):
   # template 
   # Start building the HTML structure
   html_content = f'''<!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <!-- Get your own FontAwesome ID -->
       <script src="https://kit.fontawesome.com/9a00545b44.js" crossorigin="anonymous"></script>


      <link rel = "stylesheet" href = "../css/reset.css">
      <link rel = "stylesheet" href = "../css/style.css">
      

      <title>{data["name"]}</title>
   </head>
   <body>
   <a href = "#main" class = "skip" >Skip to Main Content</a>
   <nav>
     <ul>
        <li><a href="../index.html">Home Page</a></li>
        <li><a href="../mens_team.html">Men's Team</a></li>
        <li><a href="../womens_team.html">Women's Team</a></li>
     </ul>
   </nav>
   <header>
      <!--Athlete would input headshot-->
       <h1>{data["name"]}</h1>
      <img src="../images/profiles/{data["athlete_id"]}.jpg" class = "top-image" alt="Athlete headshot" width="200"> 
   </header>
   <main id = "main">
      <section id= "athlete-sr-table">
         <h2>Athlete's Seasonal Records (SR) per Year</h2>
            <table>
                  <thead>
                     <tr>
                        <th> Year </th>
                        <th> Season Record (SR)</th>
                     </tr>
                  </thead>
                  <tbody>
                  '''
   
   for sr in data["season_records"]:
      sr_row = f'''
                     <tr>
                        <td>{sr["year"]}</td>
                        <td>{sr["sr"]}</td>
                     </tr>                  
               '''
      html_content += sr_row

   html_content += '''                   
                </tbody>
                  </table>
                     </section>

                        <h2>Race Results</h2>

                        <section id="athlete-result-table">
                           

                           <table id="athlete-table">
                              <thead>
                                 <tr>
                                    <th>Race</th>
                                    <th>Athlete Time</th>
                                    <th>Athlete Place</th>
                                    <th>Race Comments</th>
                                 </tr>
                              </thead>

                              <tbody>
                  '''

   # add each race as a row into the race table 
   for race in data["race_results"]:
      race_row = f'''
                                 <tr class="result-row">
                                    <td>
                                       <a href="{race["url"]}">{race["meet"]}</a>
                                    </td>
                                    <td>{race["time"]}</td>
                                    <td>{race["finish"]}</td>
                                     <td>{race["comments"]}</td>
                                 </tr>
      '''
      html_content += race_row

   html_content += '''
                              </tbody>

                        </table>
                     </section>
                     </main>
                     <footer>
                     <p>
                     Skyline High School<br>
                     <address>
                     2552 North Maple Road<br>
                     Ann Arbor, MI 48103<br><br>

                     <a href = "https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
                     <a href = "https://www.instagram.com/a2skylinexc/"><i class="fa-brands fa-instagram" aria-label="Instagram"></i>Follow us on Instagram</a> 


                     </footer>
                     <script src="js/javascript.js"></script>
                     <script>
                        document.querySelectorAll('img').forEach(img => {
   img.onerror = function() {
    this.onerror = null; // Prevents infinite loop if the default image is missing
    this.style.display = 'none'; // Hide the image if not found
  };
});
                     </script>
               </body>
         </html>
   '''

   with open(outfile, 'w') as output:
      output.write(html_content)


def main():

   import os
   import glob

   # Define the folder path
   folder_path = 'mens_team/'
   # Get all csv files in the folder
   csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

   # Extract just the file names (without the full path)
   csv_file_names = [os.path.basename(file) for file in csv_files]

   # Output the list of CSV file names
   print(csv_file_names)
   for file in csv_file_names:

      # read data from file
      athlete_data = process_athlete_data("mens_team/"+file)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data, "mens_team/"+file.replace(".csv",".html"))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")


   # Define the folder path
   folder_path = 'womens_team/'
   # Get all csv files in the folder
   csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

   # Extract just the file names (without the full path)
   csv_file_names = [os.path.basename(file) for file in csv_files]

   # Output the list of CSV file names
   print(csv_file_names)
   for file in csv_file_names:

      # read data from file
      athlete_data = process_athlete_data("womens_team/"+file)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data, "womens_team/"+file.replace(".csv",".html"))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")

if __name__ == '__main__':
    main()
