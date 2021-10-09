import memcache, time, os, subprocess, bindings
shared = memcache.Client(['192.168.1.120:11211'], debug=0)
prev_data = shared.get('input')

bindings = bindings.bindings

while True:
    data = shared.get('input')
    if not prev_data == data:
        prev_data = data
        try:
            key = bindings[data[8:]]
            try:
                subprocess.Popen(['python.exe', 'D:\Code\keysender\keypress.py', key], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            except:
                print("Something wrong with keypress emulate...")
        except:
            print("There is no binding for " + data[8:])
        

    time.sleep(0.01)