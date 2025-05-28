import os

def run_command(cmd):
    os.system("ping " + cmd)  # ⚠️ Command Injection
