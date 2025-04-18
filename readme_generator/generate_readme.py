import jinja2
import csv
import os

environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(searchpath="readme_generator"),  # Adjusted search path
    autoescape=jinja2.select_autoescape(['html', 'xml', 'jinja'])
)

template = environment.get_template("readme_template.jinja")

# Get the absolute path of the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "repo-urls.csv")

# Load repository data from CSV
repos = []
with open(csv_file_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        repos.append({
            "title": row["repo-url"].split("/")[-1],
            "url": row["repo-url"],
            "main_contributor": "Unknown"  # Placeholder for main contributor
        })

# Render the template with repository data
output = template.render(repos=repos)

readme_file_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
# Write the rendered content to README.md
with open(readme_file_path, "w") as readme_file:
    readme_file.write(output)

