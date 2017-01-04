import os

num_threads = 10

if __name__ == "__main__":
    for i in range(10):
        os.system("curl --data 'text=world' http://127.0.0.1:5000/greet")
        