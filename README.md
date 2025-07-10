# PasscodeGen 🔐

PasscodeGen is a Python-based tool that generates secure, random passwords on demand. It was built to help busy professionals who frequently update work passwords and want strong, hassle-free passcodes at the push of a button.

## 🧠 Why I Built This

As a working professional in law enforcement, I’m required to update my work passwords every few months. After running out of creative ideas, I decided to build this tool to quickly generate strong, base64-style passwords that meet security standards. My long-term goal is to turn this into a simple website that both I and my coworkers can use anytime, anywhere.

## 🚀 Features

- Secure random password generation using `os.urandom` and `base64`
- User-defined password length
- Generates 5 different password options each run
- Option to regenerate until satisfied

## 🛠 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/5H4D0W86/passcodegen.git
   cd passcodegen
````

2. Run the script using Python:

   ```bash
   python password_generator.py
   ```

3. Enter your desired password length when prompted, and view 5 strong passwords instantly.

## 🗂 Project Structure

```
passcodegen/
├── password_generator.py   # Python script that runs the generator
├── README.md               # This file - project documentation
└── .gitignore              # (Optional) ignores system/cache files
```

## 💡 Example Output

```
Please enter the length of the password: 12

#1: 7$Km2FxqG#bZ
#2: R!9pTq1@WvF#
#3: x#ZR0!j72NmA
#4: $b4YwLt!Xp9Q
#5: A@Lr6P%8NzWd
```

If none of the options work for you, you can simply re-run the script and generate 5 new ones instantly.

## 📈 Future Improvements

* Build a lightweight front-end using Flask
* Add password strength meter
* Add "copy-to-clipboard" functionality
* Deploy as a web app for coworkers to use via browser
* Add option to export passwords to a secure text file

## 👨‍💻 Author

**Jared M. Rollins**
[LinkedIn Profile](https://www.linkedin.com/in/jared-r-71b71a233)
Anaheim, CA

## 📄 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 Jared M. Rollins

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
