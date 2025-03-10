import subprocess
import signal

print("#### PYTHON: activating subprocess")

try:
    p = subprocess.Popen(['./rng.sh'])
    # p = subprocess.Popen(['python', 'rng.py'])
    p.wait()
except KeyboardInterrupt:
    p.send_signal(signal.SIGTERM)
    p.wait()

print("#### PYTHON: Done! Exiting.")