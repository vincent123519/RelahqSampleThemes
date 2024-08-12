import os
import json
from jinja2 import Template

def generate_html(config_file, template_file, output_file):
    # Define paths
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', config_file))
    template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates', template_file))

    try:
        # Load configuration data
        with open(config_path, 'r') as cfg_file:
            config_data = json.load(cfg_file)
            
        home_data = config_data.get('HOME', {})
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return
    except FileNotFoundError as e:
        print(f"Error loading file: {e}")
        return

    # Prepare output folder and file path
    output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'output'))
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, output_file)

    # Count elements
    openHouseCount = len(home_data.get('openHouse', []))
    imageCount = len(home_data.get('images', []))

    try:
        # Load and render template
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()

        template = Template(template_content)

        rendered_html = template.render(
            propertyAddress=home_data.get('propertyAddress', ''),
            images=home_data.get('images', {}),
            imageCount=imageCount,
            homeVideo=home_data.get('homeVideo', ''),
            title=home_data.get('title', ''),
            menu=home_data.get('menu', []),
            openHouse=home_data.get('openHouse', []),
            openHouseCount=openHouseCount,
            price=home_data.get('price', ''),
            extendedAddress=home_data.get('extendedAddress', ''),
            details=home_data.get('details', []),
            file=home_data.get('file', []),
            propertyDescription=home_data.get('propertyDescription', ''),
            featureTitle=home_data.get('featureTitle', ''),
            features=home_data.get('features', []),
            videos=home_data.get('videos', ''),
            tours=home_data.get('tours', []),
            plans=home_data.get('plans', []),
            propertyRealtor=home_data.get('propertyRealtor', []),
            googleMapAddress=home_data.get('googleMapAddress', ''),
            inquiry=home_data.get('inquiry', []),
            inquiryButtons=home_data.get('inquiryButtons', []),
            emailRecipient=home_data.get('emailRecipient', ''),
            footerDetails=home_data.get('footerDetails', []),
            footerImage=home_data.get('footerImage', ''),
            socialMedias=home_data.get('socialMedias', []),
            socialShare=home_data.get('socialShare', []),
            revaLogo=home_data.get('revaLogo', ''),
            icons=home_data.get('icons', {})  # Ensure icons is passed to the template
        )

        # Write the rendered HTML to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(rendered_html)

        print(f"Generated HTML saved to: {output_file_path}")

    except Exception as e:
        print(f"Error rendering template: {e}")

if __name__ == "__main__":
    generate_html('dy_config.cfg', 'sixth_dollar.html', 'dy6_final.html')
