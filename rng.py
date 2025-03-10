import random
import sys
import time
import select


input_buffer = ""
while True:
    number = random.randint(1000, 9999)
    print("STDOUT:", number)

    if number % 3 == 0:
        print("STDERR: Divisible by 3!", file=sys.stderr)

    if sys.platform == "win32":
        import msvcrt
        while msvcrt.kbhit():
            char = msvcrt.getche().decode('utf-8')
            if char == '\r':
                char = '\n'
            if char == '\n':
                print("STDIN :", input_buffer)
                input_buffer = ''
            else:
                input_buffer += char
    else:
        if select.select([sys.stdin], [], [], 1)[0]:
            user_input = sys.stdin.readline().strip()
            print("STDIN: ", user_input)

    time.sleep(1)

