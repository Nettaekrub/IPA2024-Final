import subprocess
import os

def showrun():
    studentID = "66070118"
    router_name = "R1-Exam"
    command = [
        "ansible-playbook",
        "-i", "inventory.ini",
        "backup_cisco_router_playbook.yml"
    ]

    # รัน playbook
    result = subprocess.run(command, capture_output=True, text=True)
    
    if "ok=2" in result.stdout or "changed=0" in result.stdout:
        filename = f"backups/show_run_{studentID}_{router_name}.txt"
        if os.path.exists(filename):
            print(f"File found: {filename}")
            return filename
        else:
            print(f"File NOT found: {filename}")
            return "Error: File not found"
    else:
        print("Playbook failed")
        return "Error: Ansible"
