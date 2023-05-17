# Certificate Generation and Verification

This project aims to facilitate the generation and verification of certificates using the provided details, such as the name and roll number of a person. The process involves signing the certificate, generating a public key and signature, and sending the necessary information to the verifying party for authentication.

## Prerequisites

To run this project, ensure you have the following installed:

- Python (version 3.6 or higher)
- pycryptodome

## Getting Started

1. Clone the project repository from GitHub:

   ```shell
   git clone https://github.com/barath-sk17/Certificategenerator___Sign-Verify.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```


## Generating a Certificate

To generate a certificate, follow these steps:

1. After Running the Project.

2. Initially, it asks for the information, such as name and rollnumber from the user and

3. It opens the `Certificate.txt` file.

4. The Algorithm, replaces the marked field (i.e Certificate.txt fields) with the gathered information, and

5. The certificate will be generated and saved as a txt file.

6. Public and private key are generated from an Algorithm

7. The certificate will be signed using the private key (i.e. generated earlier.) and a `signature.pem` file is created

8. After generation 
    - message (txt file)
    - `public.key`
    - `signature.pem` would be send to the verifier through mail for further processing

## Verifying a Certificate

To verify a certificate, the recipient should follow these steps:

1. Request the sender to provide the following information:
   - Certificate file (in PDF format)
   - Public key file (`public.key`)
   - Signature file (generated during the certificate generation process)

2. Save the certificate file, public key file, and signature file in a directory.

3. Upload the file(through front-end) 

6. The script will verify the certificate using the provided details and display the result (i.e. Valid/ Not Valid).

## Additional Notes

- Ensure the private key (`private.key`) remains secure and is not shared with anyone other than the certificate generator.

- For secure transmission of the public key, signature, and message, consider using secure file transfer protocols or encryption techniques.

- It is recommended to store backups of important certificates and keys in a secure location.

- This project serves as a starting point and can be extended to include additional features such as email notifications and database storage.
