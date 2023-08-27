import subprocess
def run_economics():
    subprocess.run(['python', 'src/finance.py'])
def run_tech():
    subprocess.run(['python', 'src/tech.py'])
print("Choose a category:")
print("1. Economics/Finance")
print("2. Tech")
choice = input("Enter the number corresponding to your choice: ")
if choice == '1':
    run_economics()
elif choice == '2':
    run_tech()
else:
    print("Invalid choice. Please enter 1 or 2.")