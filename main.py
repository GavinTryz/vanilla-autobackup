import schedule
import time
import subprocess
import signal
import traceback

server_process = None

def warn_server(seconds_until_restart):
    if seconds_until_restart > 60:
        time_remaining_string = f"{seconds_until_restart // 60} minutes"
    else:
        time_remaining_string = f"{seconds_until_restart} seconds"

    global server_process
    server_process.stdin.write(f"say \"The server will restart in {time_remaining_string} to backup the world.\"\n".encode())
    server_process.stdin.flush()

def job(timeout_seconds: int = 30):
    global server_process

    print("#### Stopping server")
    server_process.send_signal(signal.SIGTERM)
    server_process.wait(timeout_seconds)
    print("#### Server stopped")

    # do backup
    print("#### Doing backup")
    time.sleep(3)

    # start server again
    print("#### Starting server")
    server_process = subprocess.Popen(['./rng.sh'], stdin=subprocess.PIPE)
    print("#### Server started")

if __name__ == "__main__":
    try:
        print("#### Starting server")
        server_process = subprocess.Popen(['./rng.sh'], stdin=subprocess.PIPE)

        print("#### Starting scheduler")
        schedule.every(4).seconds.do(job)

        while True:
            schedule.run_pending()
    except Exception as e:
        print("#### Ran into error:")
        traceback.print_exc()

        print("#### Stopping server")
        p.send_signal(signal.SIGTERM)
        p.wait()
        print("#### Server stopped")
