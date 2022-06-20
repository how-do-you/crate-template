import argparse
import os
import shutil

def main(owner, name):
    output = "output"
    print("Owner name:\t\t", owner)
    print("Crate name:\t\t", name)
    print("Output path:\t\t", output)
    print("")
    os.makedirs(output, exist_ok=True)

    # Generate output
    for root, dirs, files in os.walk('template'):
        for f in files:
            target_file = os.path.join(output,os.path.sep.join(os.path.join(root,f).split(os.path.sep)[1:]))
            print("Creating:\t\t",target_file)
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            with open(os.path.join(root,f)) as source:
                with open(target_file,'w') as file:
                    text = source.read()
                    text = text.replace("${{OWNER}}",owner)
                    text = text.replace("${{NAME}}",name)
                    file.write(text)    

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
            with open(os.path.join(root,f)) as source:
                with open(target_file,'w') as file:
                    file.write(source.read())
    # Remove output folder
    print("Deleting:\t\t", output)
    shutil.rmtree(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create project from template')
    parser.add_argument('name', type=str, help='an integer for the accumulator')

    args = parser.parse_args()
    main(args.name.split('/')[0], args.name.split('/')[1])
