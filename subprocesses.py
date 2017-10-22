import subprocess

subprocess.call(["python2", "labels.py", "labels", "./car2.jpg"])
subprocess.call(["python2", "labels.py", "text", "./car2.jpg"])
subprocess.call(["python2", "labels.py", "properties", "./car2.jpg"])
