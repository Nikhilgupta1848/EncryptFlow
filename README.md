# EncryptFlow

EncryptFlow is a web application built using Flask, designed to demonstrate encryption and decryption of messages using the Caesar Cipher technique. This app allows users to encrypt a message with a Caesar Cipher, send it through a queue, and decrypt the message using the same shift value.

## Features

- **Message Encryption**: Encrypt any message with a Caesar Cipher using a user-defined shift.
- **Message Decryption**: Retrieve encrypted messages from the queue and decrypt them using the same shift value.
- **Queue Management**: Messages are queued after encryption and can be retrieved for decryption.

## Technologies Used

- **Backend**: Python (Flask) for server-side logic and API handling.
- **Frontend**: HTML, CSS, and JavaScript for the user interface and asynchronous operations.
- **Encryption**: Caesar Cipher for message encryption and decryption.

## Installation

Follow these steps to get the project up and running on your local machine.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Nikhilgupta1848/EncryptFlow.git
   cd EncryptFlow

2. **Install Dependencies**:

Make sure you have Python and pip installed. Then, install the required Python packages:

pip install Flask

This will install Flask, the main framework for the backend of this project.



3. **Run the Application**:

To run the Flask server, use the following command:

python app.py
This will start the Flask development server, and the application will be accessible at http://127.0.0.1:5000/ in your browser.

4. **How It Works** :
- **Encryption**: The user enters a message and selects a shift value for the Caesar Cipher. The message is encrypted and added to the queue.
- **Decryption**: The user can retrieve encrypted messages from the queue and decrypt them using the same shift value.


## Screenshots
1.This Shows message is Encrypted


 ![a1aaaaEy](https://github.com/user-attachments/assets/b491100c-5715-4b7a-9434-ab6cc76116c1)


2.This Shows message is Decrypted  


![a2adewdfsd](https://github.com/user-attachments/assets/ed4d9e54-26fc-411c-a7ca-d647970c7c4d)

                                                                                                                            
## Contributing
1. - **Fork the repository**.
2. - **Create your branch (git checkout -b feature-name)**.
3.-  **Commit your changes (git commit -am 'Add new feature')**.
4. - **Push to the branch (git push origin feature-name)**.
5. - **Create a new Pull Request**.


Contact
For questions or feedback, you can reach me at nikhilkrkanti@gmail.com .
