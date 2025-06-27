import jinja2
import csv
import os
from datetime import datetime

solution_area_mapping = {
    "application-innovation": "Application Innovation",
    "infrastructure": "Infrastructure",
    "ai": "AI",
    "data": "Data",
    "security": "Security",
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
            "data": row.get("data", "").lower() == "true",
            "ai": row.get("ai", "").lower() == "true",
            "security": row.get("security", "").lower() == "true",
            "description": row.get("repo-description", ""),
        })

workloads_to_keep = [
    "application-innovation",
    "infrastructure",
    "ai",
    "data",
    "security"
]

workloads_dir = os.path.join(os.path.dirname(__file__), "..", "workloads")
os.makedirs(workloads_dir, exist_ok=True)

# Prepare per-workload readmes and links
workload_links = []
for workload in workloads_to_keep:
    display_name = solution_area_mapping[workload]
    folder_path = os.path.join(workloads_dir, workload)
    os.makedirs(folder_path, exist_ok=True)
    readme_path = os.path.join(folder_path, "README.md")
    # Filter repos for this workload
    workload_repos = [repo for repo in repos if repo.get(workload)]
    # Render a simple table for this workload
    table = f"## {display_name} repositories\n| Repository | Description |\n|------------------|-------------|\n"
    for repo in workload_repos:
        table += f"| [{repo['title']}]({repo['url']}) | {repo['description']} |\n"
    with open(readme_path, "w", encoding="utf-8") as wf:
        wf.write(table)
    # Add link for main readme
    rel_link = f"workloads/{workload}/README.md"
    workload_links.append((display_name, rel_link))

# Generate a string with the current date and time
last_generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Render the template with repository data and workload links
output = template.render(
    repos=repos,
    solution_area_mapping=solution_area_mapping,
    last_generated=last_generated,
    workload_links=workload_links,
    workloads_to_keep=workloads_to_keep
)

print(output)

readme_file_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
# Write the rendered content to README.md
with open(readme_file_path, "wb") as readme_file:
    readme_file.write(output.encode("utf-8"))

