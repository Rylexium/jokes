import subprocess
import traceback


def powershell(command):
    if command == "" or command is None:
        return
    output = subprocess.check_output(f"powershell.exe -c \"{command}\"", stderr=subprocess.STDOUT, shell=True).decode("cp866").strip()
    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        try:
            command = input("ps > ")
            if command == "exit":
                break

            output = powershell(command)
            if output == "":
                print("Ok")
            elif output is not None:
                print(output)
        except subprocess.CalledProcessError:
            row_of_exception = traceback.format_exc().split("\n")
            exception = row_of_exception[len(row_of_exception) - 2]\
                .replace("subprocess.CalledProcessError: Command 'powershell.exe -c \"", "")\
                .replace("\"' returned non-zero exit status 1.", "")
            print(f"Exception in command: {exception}")
