# Automated Marriage Loan SignUp (ve.cbi.ir)

This repository contains a fully functional Python program designed to automate the sign-up process for the Marriage Loan application on the ve.cbi.ir website. The primary goal of this tool is to streamline the sign-up process, making it faster and easier for users.

## Technologies and Libraries

The code in this project utilizes the following technologies and libraries:

- **Python**: The main programming language used to develop this automation script.
- **Selenium**: A powerful tool for web browser automation, used to interact with web elements during the sign-up process.
- **Requests**: A library for sending HTTP requests, used for making web requests to the ve.cbi.ir server.
- **TwoCaptcha**: A service to automatically solve captchas, necessary for bypassing CAPTCHA challenges on the website.

## Requirements To Run the Code

To run this code successfully, you will need:

- A **TwoCaptcha** paid account and API key.
- **Chrome WebDriver** installed and configured.
- Install the required Python packages listed in `requirements.txt`.

## Deployment Guide

Follow the steps below to deploy the code and get it running on your local machine:

### 1. Clone the Repository

First, clone the repository to your local machine using the following command:

```bash
git clone git@github.com:m-hasan-2004/ve.cbi.ir_Auto_SignUp.git
```

Navigate into the cloned directory:

```bash
cd ve.cbi.ir_Auto_SignUp
```

### 2. Install Required Python Packages

Make sure you have Python installed on your system. Install the necessary packages by running:

```bash
pip install -r requirements.txt
```

### 3. Set Up Chrome WebDriver

Download the Chrome WebDriver that matches your version of Chrome from the [official ChromeDriver site](https://sites.google.com/a/chromium.org/chromedriver/downloads). Once downloaded, place the WebDriver in a directory that's included in your system's PATH or specify its location in the code.

### 4. Set Up TwoCaptcha Solver

To handle CAPTCHA challenges automatically, you'll need a TwoCaptcha account. Follow these steps:

1. **Sign up for an account**: Go to the [2Captcha website](https://2captcha.com/) and sign up for a new account.
2. **Add funds to your account**: After registration, you'll need to add funds to your account to use their CAPTCHA-solving service. You can do this through various payment methods available on the platform.
3. **Get your API key**: Once you've added funds, navigate to your account dashboard and copy your unique API key.
4. **Configure the API key**: Add the API key to the code by replacing the placeholder with your actual key. Locate the relevant part in the code where the TwoCaptcha API is initialized, and insert your key like this:

    ```python
    API_KEY = 'your_2captcha_api_key_here'
    ```
> **Note**: The CAPTCHA solver requires a paid subscription to TwoCaptcha. Ensure you have sufficient funds in your account to avoid interruptions during the sign-up process.
### 5. Running the Script

After setting up everything, you can run the script with:

```bash
python main.py
```

Ensure that the Chrome WebDriver is correctly configured and accessible, and that you've entered your TwoCaptcha API key as described above.

## To-Do List

The following tasks are planned for future updates:

- Develop a captcha solver for Cloudflare or any other CAPTCHA encountered at the start of the process.
- Complete the development of the second page of the sign-up process.
- Implement phone number verification code handling.
- Optimize the code for compatibility with Windows OS.
- Create an executable file or develop a GUI to enhance user-friendliness.
