# hcs_app
Beta version of a reporting tool to submit a business to be reviewed by an internal AI for possible scams or attackts

## Getting Started

First create a virtualenv
``virtualenv venv``
``source venv/bin/activate``

Then install requirements
``pip3 install -r requirements.txt``

Then Run Migrations
``python manage.py migrate``

Then Run the Test server
``python manage.py runserver``

Create a SuperUser
``python manage.py createsuperuser``


## Reporting APIs
- Anti-Phishing Working Group (APWG) - Provides a reporting API for phishing attacks:
    - Website: https://www.antiphishing.org/
- Federal Trade Commission (FTC) - Offers an online reporting form for reporting scams and identity theft. While they don't provide a public API, you can explore the possibility of reporting through their Consumer Sentinel Network API:
    - Website: https://www.ftc.gov/
- Internet Crime Complaint Center (IC3) - Allows reporting of cybercrime incidents:
    - Website: https://www.ic3.gov/
- National Cybersecurity and Communications Integration Center (NCCIC) - Provides a reporting mechanism for cyber incidents and threats:
    - Website: https://www.dhs.gov/topic/cybersecurity
- Better Business Bureau (BBB) - Offers a platform to report scams and fraudulent activities. While they don't provide a public API, you can check their resources for reporting scams:
    - Website: https://www.bbb.org/
- Google Safe Browsing - Provides an API to report phishing and malware websites:
    - Website: https://developers.google.com/safe-browsing
