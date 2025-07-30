import os
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def format_hub_content(content_lines):
    """ Ensure correct formatting of the hub file content. """
    if not content_lines or content_lines[0].strip() != '#hub':
        content_lines.insert(0, '#hub\n')
    if len(content_lines) == 1 or content_lines[1].strip() != '':
        content_lines.insert(1, '\n')
    return content_lines

def remove_duplicate_links(content_lines):
    """ Remove duplicate links from the hub file content. """
    seen_links = set()
    unique_content = []
    for line in content_lines:
        stripped_line = line.strip()
        if stripped_line.startswith('[[') and stripped_line in seen_links:
            logging.info(f"Removed duplicate link: {stripped_line}")
            continue
        seen_links.add(stripped_line)
        unique_content.append(line)
    return unique_content

def update_hub_file(hub_path, content_lines):
    """ Update the hub file with new content and log changes. """
    with open(hub_path, 'r+', encoding='utf-8') as f:
        original_content = f.readlines()
        
        content_lines = remove_duplicate_links(content_lines)
        if original_content != content_lines:
            f.seek(0)
            f.truncate()
            f.writelines(content_lines)
            logging.info(f"Updated hub file: {hub_path}")

def clean_and_update_hub_links(hub_path, child_hubs_and_notes):
    """ Clean and update links in a given hub file """
    needed_links = set()
    for child in child_hubs_and_notes:
        basename = os.path.basename(child)
        if child.endswith('.pdf'):
            needed_links.add(f"[[{basename}]]")
        else:
            needed_links.add(f"[[{basename.replace('.md', '')}]]")

    with open(hub_path, 'r+', encoding='utf-8') as f:
        existing_content = f.readlines()
        new_content = format_hub_content(existing_content)

        existing_links = set(line.strip() for line in existing_content if line.strip().startswith('[['))
        for link in needed_links:
            if link not in existing_links:
                new_content.append(link + '\n')
                logging.info(f"Added link: {link} to {hub_path}")

        update_hub_file(hub_path, new_content)

def ensure_hub_exists(directory, parent_hub=None):
    """ Ensure a hub exists for each directory and manage links """
    hub_name = f"{os.path.basename(directory)} Hub.md"
    hub_path = os.path.join(directory, hub_name)

    # Normalize hub name if required
    for filename in os.listdir(directory):
        if 'Hub.md' in filename and filename != hub_name:
            os.rename(os.path.join(directory, filename), hub_path)
            logging.info(f"Renamed {filename} to {hub_name}")

    child_hubs_and_notes = []

    if not os.path.exists(hub_path):
        with open(hub_path, 'w', encoding='utf-8') as f:
            f.write("#hub\n\n")
        logging.info(f"Created new hub: {hub_path}")

    for item in os.listdir(directory):
        sub_path = os.path.join(directory, item)
        if os.path.isdir(sub_path):
            child_hub = ensure_hub_exists(sub_path, hub_path)
            if child_hub:
                child_hubs_and_notes.append(child_hub)
        elif item.endswith('.md') and 'Hub.md' not in item:
            child_hubs_and_notes.append(sub_path)
        elif item.endswith('.pdf'):  # Add PDFs as links
            child_hubs_and_notes.append(sub_path)

    clean_and_update_hub_links(hub_path, child_hubs_and_notes)

    if parent_hub:
        clean_and_update_hub_links(parent_hub, [hub_path] if hub_path else [])

    return hub_path

def delete_all_hubs(directory):
    """ Delete all existing hub files in the given directory and its subdirectories """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('Hub.md'):
                hub_file_path = os.path.join(root, file)
                os.remove(hub_file_path)
                logging.info(f"Deleted hub file: {hub_file_path}")

def clean_unused_images(vault_path):
    """ Move unused images to a 'Remove Me' folder based on identifier checking """
    image_dir = os.path.join(vault_path, 'Images')
    remove_dir = os.path.join(vault_path, 'Images', 'Remove Me')

    if not os.path.exists(image_dir):
        return

    if not os.path.exists(remove_dir):
        os.makedirs(remove_dir)
        logging.info(f"Created folder for unused images: {remove_dir}")

    # Collect all image identifiers
    image_identifiers = {file.split(' ')[2].split('.')[0] for file in os.listdir(image_dir) if file.startswith('Pasted image')}

    # Search for these identifiers in all Markdown files
    used_identifiers = set()
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    for identifier in image_identifiers:
                        if identifier in content:
                            used_identifiers.add(identifier)

    # Move unreferenced images to the 'Remove Me' folder
    for file in os.listdir(image_dir):
        if file.startswith('Pasted image'):
            identifier = file.split(' ')[2].split('.')[0]
            if identifier not in used_identifiers:
                src_path = os.path.join(image_dir, file)
                dest_path = os.path.join(remove_dir, file)
                os.rename(src_path, dest_path)
                logging.info(f"Moved unused image: {file} to {remove_dir}")

def main():
    # Loop through the dir and delete all existing hubs
    vault_path = r'D:\Quant_Notes'
    delete_all_hubs(vault_path)
    
    # Ensure hubs are correctly recreated
    ensure_hub_exists(vault_path)
    
    # Clean up unused images
    image_path = r'Images'
    clean_unused_images(image_path)

if __name__ == "__main__":
    main()
