#!/bin/python3

import random
import os
import webbrowser

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#₦%^&*()_-+=><?/][}{"
Random = lower + upper + numbers + symbols

length = int(input("Enter a length: "))
if length <= 5:
           print("password is too short.")
           exit()

password = ''.join(random.choice(Random) for i in range(length))
print(password)
save_choice = input("Do you want to save the password to a file? (yes/no): ").lower()
if save_choice =='no':
        exit()
if save_choice =='yes':
 file_name = input("Enter the desired file name (e.g 'mypassword.txt'): ")
 directory = input("Enter the directory path to save (leave blank for current directory): ")
if directory:
          file_path = os.path.join(directory, file_name)
else:
           file_path = file_name
           
try:
       with open(file_path, 'w') as f:
            f.write(password)
       print(f"password successfully saved to {file_path}")
except IOError as e:
       print(f"Error saving password to file: {e}")
else:
       print("exiting program without saving.")
       
       
print("\n--- Social Media Account Password ---")
social_media_choice = input("Do you want to use this as a social media account password? (yes/no): ").lower()

if social_media_choice == 'yes':
    print("\nSelect a social media platform:")
    print("1. Facebook")
    print("2. Twitter (X)")
    print("3. Instagram")
    print("4. LinkedIn")
    print("5. Reddit")
    print("6. Other (will ask for URL)")

    social_platform_number = input("Enter the number of your choice: ")

    social_media_urls = {
        '1': 'https://www.facebook.com/reg/', # Facebook sign-up page
        '2': 'https://twitter.com/i/flow/signup', # Twitter (X) sign-up page
        '3': 'https://www.instagram.com/accounts/emailsignup/', # Instagram sign-up page
        '4': 'https://www.linkedin.com/signup/', # LinkedIn sign-up page
        '5': 'https://www.reddit.com/register/', # Reddit sign-up page
    }

    url_to_open = ""
    if social_platform_number in social_media_urls:
        url_to_open = social_media_urls[social_platform_number]
    elif social_platform_number == '6':
        custom_url = input("Enter the full URL of the social media signup page (e.g., https://example.com/signup): ")
        if custom_url.startswith('http://') or custom_url.startswith('https://'):
            url_to_open = custom_url
        else:
            print("Invalid URL format. Please include http:// or https://")
    else:
        print("Invalid social media choice.")

    if url_to_open:
        print(f"\nOpening {url_to_open} in your default browser.")
        print("Please manually paste the generated password into the sign-up field:")
        print(f"Your password is: {password}") # Remind user of the password
        webbrowser.open(url_to_open)
    else:
        print("Could not open social media page due to invalid input.")

elif social_media_choice == 'no':
    print("Not setting up as a social media account password.")
else:
    print("Invalid choice for social media password. Exiting.")
