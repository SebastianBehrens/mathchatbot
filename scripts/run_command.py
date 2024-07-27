from pathlib import Path
import logging
import subprocess

def run_command(command: list, flg_sudo: int = 0):

    # check good practice of using list of args to subprocess
    if not isinstance(command, list):
        raise ValueError(f"Supplied argument to 'command' is not a list, it is of type {type(command)}. Please supply a list of arguments to comply with good practice.")

    logging.debug(f"└─ Running command: '{' '.join(command)}.")

    process = subprocess.Popen(
            '/usr/bin/bash',
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True)

    out, err = process.communicate(" ".join(command))

    # running as sudo is not implemented, as not necessary as of right now.
        # if flg_sudo:
        #     # maybe used if copying not possible without root access
        #     password = getpass.getpass(prompt = '\nPlease enter your password.\nIt is needed to execute commands to copy files from different user as sudo.\nPassword:')
        #     call = subprocess.run(command, capture_output=True, input=password)


    # handle bad return code
    if err is not None:
        print(err)
        logging.error(out)
        logging.error(err)
        raise Exception(f"Command: '{' '.join(command)}' did not run successfully.")

    # return output if return code 0 (successful execution)
    else:
        # return output
        logging.debug(f"└─ Command ran successfully.")
        return out
