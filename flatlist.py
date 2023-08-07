import re
import subprocess

def remove_newlines(l):
    return list(map(lambda line: line.strip(), l))

result = subprocess.run(['flatpak', 'list', '--app', '--columns=application'], capture_output=True, text=True)

app_ids = remove_newlines(result.stdout.splitlines())

apps_installed = []
with open('./flatpaks.txt', 'r', encoding='utf-8') as f:
    apps_installed = remove_newlines(f.readlines())
    print(apps_installed)

    #Install apps that are specified in the flatpak file but aren't already installed
    for app in apps_installed:
        print(f'Checking {app}...', end='')
        if app not in app_ids:
            print(f'{app} not installed. Installing...')
            result = subprocess.run(['flatpak', 'install', '-y', app], capture_output=True, text=True)
            print(result.stdout)
            #If app fails to be installed, print the error message
            if result.stderr:
                print(result.stderr)
                continue

        print(f' ✓')
    
with open('./flatpaks.txt', 'a') as f:
    #Add apps to the flatpak.txt list that are installed but not yet in the file
    for app in app_ids:
        if app not in apps_installed:
            print(f'Added {app} to flatpak list.')
            f.write(app + "\n")

result = subprocess.run(['flatpak', 'update'])
print(result.stdout)
