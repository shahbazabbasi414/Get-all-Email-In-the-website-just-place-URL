import csv
import requests
import re


def extract_emails(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract email addresses using regular expressions
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        emails = re.findall(email_pattern, response.text)
        
        # Remove duplicate email addresses
        unique_emails = list(set(emails))
        
        # Export the extracted email addresses to a CSV file
        with open('emails.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Email'])
            writer.writerows([[email] for email in unique_emails])
        
        print('Emails extracted and saved to emails.csv')
    else:
        print('Error: Failed to retrieve the webpage.')

# Example usage
website_url = 'https://dellmed.utexas.edu/directory?page=9'  # Replace with the desired website URL
extract_emails(website_url)
