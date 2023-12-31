
## Overview

This Python script is designed to perform SSH brute force attacks on a range of IP addresses using a list of usernames and passwords. It utilizes the Paramiko library to establish SSH connections, attempting various username and password combinations until a successful connection is made or authentication fails.

## Prerequisites

Before running this script, ensure you have the following prerequisites:

1.  Python installed on your system.
    
2.  The Paramiko library installed. You can install it using `pip`:
    
    Copy code
    
    `pip install paramiko` 
    
3.  Create two text files in the same directory as the script:
    
    -   `users.txt`: A list of usernames to be used for SSH authentication, one per line.
    -   `passwords.txt`: A list of passwords to be used for SSH authentication, one per line.

## Usage

1.  Open the script in a Python code editor or IDE.
2.  Configure the script by setting the `host_prefix` variable to the desired IP address prefix and adjusting the IP range within the loop as needed.
3.  Ensure that the `users.txt` and `passwords.txt` files contain the usernames and passwords you want to test.
4.  Run the script.

## Script Behavior

-   The script iterates through a range of IP addresses, combining the `host_prefix` with a range specified in the loop.
-   For each IP address and for each combination of usernames and passwords:
    -   It attempts to establish an SSH connection using Paramiko's `SSHClient`.
    -   If the connection is successful, it prints that the connection was established.
    -   If authentication fails, it prints an authentication failure message.
    -   If an SSH-related error occurs, it prints an SSH error message.
    -   If any other exception is raised, it prints an error message with a description of the exception.

## Important Notes

-   This script is for educational and informational purposes only. Unauthorized brute force attacks on SSH servers are illegal and unethical. Ensure you have proper authorization before attempting to access any SSH server.
-   Be cautious when running this script, as it may trigger security alerts on the target systems and potentially lead to IP bans.
-   Using weak or easily guessable passwords for SSH authentication is highly discouraged. Always use strong, unique passwords and consider using key-based authentication for increased security.

## Disclaimer

The authors of this script are not responsible for any misuse, damage, or illegal activities conducted using this script. Use it responsibly and only on systems for which you have explicit authorization.

**Note:** This script should not be used for malicious purposes or in violation of applicable laws and regulations. Always obtain proper authorization and follow ethical guidelines when conducting security testing or assessments.