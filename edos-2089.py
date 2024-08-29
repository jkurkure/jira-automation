import csv, os

from rich.console import Console
console = Console()

ACLI = "C:\\Users\\███████\\ACLI\\bin\\acli.exe"
PROFILE = "███-jira"

# Open the CSV file
with open('edos-2089.csv', 'r') as file:

    # Read the CSV file
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        # Lookup id in the edos-2089-ids.csv file
        with open('edos-2089-ids.csv', 'r') as id_file:
            id_reader = csv.reader(id_file)
            for id_row in id_reader:
                if id_row[1] == name:
                    id = id_row[0]
                    break
            else:
                id = None

        # Continue with the rest of the code
        if id is not None:
            new = row[1].replace('-', '--')
            arg = f"{id}:{new}"
            cmd = f'-a updateCustomFieldOptions --field "Release Name" --options "{arg}"'
            os.system(f'{ACLI} {PROFILE} {cmd}')
        else:
            console.print(f"[red]No id found for name:[/red] [blue]{name}[/blue]")

