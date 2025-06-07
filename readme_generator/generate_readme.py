import jinja2
import csv
import os
from datetime import datetime

solution_area_mapping = {
    "application-innovation": "Application Innovation",
    "infrastructure": "Infrastructure",
    "data-ai": "Data & AI",
    "security": "Security",
    "modern-workplace": "Modern Workplace",
    "dynamics-365": "Dynamics 365",
    "other": "Other",
}

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
            "owner": row.get("repo-url", "").split("/")[-2],
            "title": row.get("repo-url", "").split("/")[-1],
            "url": row.get("repo-url", ""),
            "application-innovation": row.get("application-innovation", "").lower() == "true",
            "infrastructure": row.get("infrastructure", "").lower() == "true",
            "data-ai": row.get("data-ai", "").lower() == "true",
            "security": row.get("security", "").lower() == "true",
            "modern-workplace": row.get("modern-workplace", "").lower() == "true",
            "dynamics-365": row.get("dynamics-365", "").lower() == "true",
            "other": row.get("other", "").lower() == "true",
            "description": row.get("repo-description", ""),
        })


# Generate a string with the current date and time
last_generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Render the template with repository data
output = template.render(repos=repos, solution_area_mapping=solution_area_mapping, last_generated=last_generated)

print(output)

readme_file_path = os.path.join(os.path.dirname(__file__), "..", "profile/README.md")
# Write the rendered content to README.md
with open(readme_file_path, "wb") as readme_file:
    readme_file.write(output.encode("utf-8"))

