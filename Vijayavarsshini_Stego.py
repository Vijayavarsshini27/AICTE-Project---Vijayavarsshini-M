import cv2
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("="*60)
    print("{:^60}".format("Secure Data Hiding in Image Using Steganography"))
    print("{:^60}".format("A project by Your Name"))
    print("="*60)

def print_menu():
    print("[1] Encrypt and Decrypt File")
    print("[2] Exit")
    print("-"*60)

def process_steganography():
    img = cv2.imread("mypic.jpg")

    if img is None:
        print("\nError: Image file 'mypic.jpg' not found!")
        input("\nPress Enter to continue...")
        return

    msg = input("\nEnter secret message: ")
    password = input("Enter a passcode: ")

    d = {chr(i): i for i in range(256)}
    c = {i: chr(i) for i in range(256)}

    # Encryption
    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg" if os.name == "nt" else "xdg-open encryptedImage.jpg")

    # Decryption
    message = ""
    n, m, z = 0, 0, 0

    pas = input("\nEnter passcode for Decryption: ")
    if password == pas:
        for _ in range(len(msg)):
            message += c[img[n, m, z]]
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
            z = (z + 1) % 3
        print("\nDecrypted message:", message)
    else:
        print("\nAuthentication failed!")

    input("\nPress Enter to continue...")

def main():
    while True:
        clear_screen()
        print_header()
        print_menu()

        choice = input("\nEnter your choice (1/2): ")

        if choice == '1':
            process_steganography()
        elif choice == '2':
            print("\nThank you for using my program!")
            print("Exiting...")
            break
        else:
            print("\nInvalid choice! Please select 1 or 2.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
