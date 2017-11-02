# Slugify Utilities

Provides a lightweight utility for generating permalink slugs based on WordPress's sanitize_title and Yoast SEO's strip stop words.

## Installation

1. (Optional) Create a virtual environment where you want the library to live
2. Clone the code into the virtual environment (or if you skipped step 1, wherever you want the library to live).
3. (Optional if virtualenv): Source your virtual environment from within the project folder: `source ../bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. (Optional): Add to your bash PATH:
    a. Open your bash_profile: `vim ~/.bash_profile`
    b. Add the following line: `export PATH=$PATH":/path/to/library/bin"`
6. Run the utility. E.g. `slugify "This is a test"`
