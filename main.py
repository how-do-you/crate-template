import argparse
import os
import shutil
import requests
import json

def main(owner:str, name:str,options:dict):
    output = "output"
    print("Owner name:\t\t", owner)
    print("Crate name:\t\t", name)
    print("Template:\t\t", options["template"])
    print("Output path:\t\t", output)
    print("")
    os.makedirs(output, exist_ok=True)

    # Generate output
    for root, dirs, files in os.walk(f'templates/{options["template"]}'):
        for f in files:
            target_file = os.path.join(output,os.path.sep.join(os.path.join(root,f).split(os.path.sep)[2:]))
            print("Creating:\t\t",target_file)
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            with open(os.path.join(root,f), 'rb') as source:
                with open(target_file,'wb') as file:
                    data = source.read()
                    try:
                        text = data.decode()
                        text = text.replace("${{OWNER}}",owner)
                        text = text.replace("${{NAME}}",name)
                        text = text.replace("${{NAME_PRETTY}}",name.replace('-',' ').replace('_',' ').title())
                        file.write(text.encode('utf-8'))
                    except:
                        file.write(data)

    # Remove all unnecessary files                    
    for file in os.listdir('./'):
        if file != ".git" and file != output:
            print("Deleting:\t\t",file)
            if os.path.isdir(file):
                shutil.rmtree(file)
            else:
                os.remove(file)

    # Move output to parent folder
    for root, dirs, files in os.walk(output):
        for f in files:
            target_file = os.path.sep.join(os.path.join(root,f).split(os.path.sep)[1:])
            print("Copying file:\t\t",os.path.join(root,f),">",target_file)
            d = os.path.dirname(target_file)
            if d == "":
                d = "."
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(root,f), 'rb') as source:
                with open(target_file,'wb') as file:
                    file.write(source.read())
    # Remove output folder
    print("Deleting:\t\t", output)
    shutil.rmtree(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create project from template')
    parser.add_argument('name', type=str, help='an integer for the accumulator')

    args = parser.parse_args()

    owner = args.name.split('/')[0]
    name = args.name.split('/')[1]

    options = {
        "template":"none"
    }

    r = requests.get(f"https://api.github.com/repos/{owner}/{name}")
    if r.status_code == 200:
        data = json.loads(r.text)
        if data["description"] is not None && data["description"] != "":
            args = data["description"].split(' ')
            valid_templates = ["tauri"]
            if args[0] in valid_templates:
                options["template"] = args[0]

    main(owner,name,options)
