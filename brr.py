import requests
import re

username = "your_roblox_username"


url = f"https://www.roblox.com/ForgotPassword"
payload = {
    "username": username,
    "client_id": "5243180973",
    "redirect_uri": "https://www.roblox.com/ForgotPassword",
    "response_type": "code",
    "scope": "email",
}
response = requests.post(url, data=payload)


if re.search(r'Please check your email', response.text):
    print("Password reset successful!")
else:
    print("Error: Password reset failed")

url = "https://www.roblox.com/ForgotPassword/Reset"
payload = {
    "username": username,
    "code": "your_password_reset_code",
    "client_id": "5243180973",
    "redirect_uri": "https://www.roblox.com/ForgotPassword",
    "response_type": "code",
    "scope": "email",
}
response = requests.post(url, data=payload)

pattern = r'code=([^&]+)'
password = re.search(pattern, response.text).group(1)
print(f"Password: {password}")
