# PasswordGenerator

Hi! If you’ve stumbled upon this, please keep in mind that this program is NOT meant to replace your password manager. 
However, it CAN be used as a more secure method to manage your safely generated passwords.

While not cryptographically foolproof, the passwords generated by this program are relatively safe because they are long 
and do not include dictionary words that could be susceptible to dictionary attacks. An advantage over writing down your 
passwords in a book is that you can’t lose this generator. It can easily be accessed from anywhere in the world, as long 
as there is internet access.

A drawback is that anyone who knows your username, category, and password can replicate your passwords. However, this 
requires more variables than just your password for your password database. So, use with caution, but it certainly beats 
using weak passwords.

It also CAN NOT store passwords because it does not store but generate your passwords as described below.

## How it works:
This software hashes the category-, the username- and the password-string, averages those hashes and uses that
to seed the random generator which then creates your passwords. This results in the same passwords every time. 
The name of the strings(e.g. category, password and username) do not really matter, it matters that they do not 
need to be fancy, they just need to be varied, limiting the amount of stuff you have to remember in an effort to
make it less likely to loose your access to your passwords.

## How to use it:
Run the python file on the command line and make sure you have all the necessary libraries installed(string, hash, random).
