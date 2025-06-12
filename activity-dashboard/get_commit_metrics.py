import requests
import json
import csv
from collections import defaultdict
import datetime
import jinja2
import os
import pytz

# Read GitHub handles to include from ghhandles.csv
def read_handles(filepath):
    handles = set()
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                handles.add(row[0].strip())
    return handles

# Read repo URLs from repo-urls.csv
def read_repo_urls(filepath):
    repos = []
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                url = row[0].strip()
                if url.startswith('https://github.com/'):
                    parts = url.replace('https://github.com/', '').split('/')
                    if len(parts) >= 2:
                        owner, repo = parts[0], parts[1]
                        repos.append((owner, repo))
    return repos

# Optional: Add your GitHub token here for higher rate limits
GITHUB_TOKEN = os.environ.get("ORG_METRICS_TOKEN")  # Added GitHub token for higher rate limits

headers = {}
if GITHUB_TOKEN:
    headers["Authorization"] = f"token {GITHUB_TOKEN}"

# Main logic
handles = read_handles('./activity-dashboard/gh-handles.csv')  # Use the correct filename
repos = read_repo_urls('repo-urls.csv')

total_commits = {h: 0 for h in handles}

# Calculate the date 31 days ago in ISO format
# since_date = (datetime.datetime.utcnow() - datetime.timedelta(days=31)).isoformat() + 'Z'

for github_owner, github_repo in repos:
    api_url = f"https://api.github.com/repos/{github_owner}/{github_repo}/commits"
    # params = {"per_page": 100, "page": 1, "since": since_date}
    params = {"per_page": 100, "page": 1}
    while True:
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch commits for {github_owner}/{github_repo}: {response.status_code} {response.text}")
            break
        commits = response.json()
        if not commits:
            break
        for commit in commits:
            author = commit.get("author")
            if author and author.get("login"):
                login = author["login"]
            else:
                login = commit["commit"]["author"]["name"]
            if login in handles:
                total_commits[login] += 1
        params["page"] += 1

# Save the top 5 contributors as a separate JSON file
sorted_top5 = sorted(total_commits.items(), key=lambda x: x[1], reverse=True)[:5]
top5_dict = {k: v for k, v in sorted_top5}

# Render the README.md using Jinja2
with open('./activity-dashboard/readme_template_dashboard.jinja', 'r', encoding='utf-8') as template_file:
    template_content = template_file.read()

template = jinja2.Template(template_content)
cet = pytz.timezone('Europe/Brussels')
current_date = datetime.datetime.now(cet).strftime('%d-%m-%Y %H:%M:%S')
rendered = template.render(results=total_commits, generated_on=current_date, top5=top5_dict)

with open('./activity-dashboard/README.md', 'w', encoding='utf-8') as out_file:
    out_file.write(rendered)

print("Top 5 contributors:")
print(json.dumps(top5_dict, indent=2))

print(json.dumps(total_commits, indent=2))