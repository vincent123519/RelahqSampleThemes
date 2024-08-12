import argparse
import requests
import os

# Step 1: Set up argument parsing
def parse_args():
    parser = argparse.ArgumentParser(description="Generate a website with a given name, theme, and job number.")
    parser.add_argument("website_name", type=str, help="The name of the website")
    parser.add_argument("theme", type=str, help="The theme from the completed list")
    parser.add_argument("job_number", type=int, help="The job number to extract images")
    return parser.parse_args()

# Step 2: Interact with the API to get job images
def get_job_images(job_number):
    api_url = f"https://api.revastaff.com/jobs/{job_number}/images"
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an error if the request failed
    return response.json()  # Assuming the API returns JSON data

# Step 3: Generate the HTML file
def generate_html(website_name, theme, images):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{website_name}</title>
        <link rel="stylesheet" href="{theme}.css">
    </head>
    <body>
        <h1>{website_name}</h1>
        <div class="images">
    """
    for img in images:
        html_content += f'<img src="{img["url"]}" alt="{img["description"]}">\n'
    
    html_content += """
        </div>
    </body>
    </html>
    """
    
    output_dir = "sprop"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{website_name}-{theme}-{job_number}.htm")
    with open(output_file, "w") as file:
        file.write(html_content)

# Main function
def main():
    args = parse_args()
    images = get_job_images(args.job_number)
    generate_html(args.website_name, args.theme, images)
    print(f"Website generated at https://proptour.app/sprop/{args.website_name}-{args.theme}-{args.job_number}.htm")

if __name__ == "__main__":
    main()
