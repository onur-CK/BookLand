# **Deployment**

## **Table of Contents**

* [**Deployment**](#deployment)
  * [**Table of Contents**](#table-of-contents)
  * [**Initial Deployment**](#initial-deployment)
    * [**Create Repository**](#create-repository)
    * [**Setting up the Workspace**](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)
    * [**Create Heroku App**](#create-heroku-app)
    * [**AWS S3 Bucket Configuration**](#aws-s3-bucket-configuration) 
    * [**Creating Environmental Variables Locally**](#creating-environmental-variables-locally)
    * [**Setting up settings.py File**](#setting-up-settingspy-file)
    * [**Set up Heroku for Use via Console**](#set-up-heroku-for-use-via-console)
  * [**Project Maintenance**](#project-maintenance)
    * [**Forking the Repository**](#forking-the-repository)
    * [**Cloning the Repository**](#cloning-the-repository)
    * [**Making Changes**](#making-changes)

## **Initial Deployment**

Below are the steps taken to deploy the BookLand site to Heroku and any console commands required to initiate it.

### **Create Repository**

1. Create a new repository in GitHub and clone it locally following [these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    * ***Note*** - If you are cloning my project, you can skip all pip installs below and just run the following command in the terminal to install all the required libraries/packages at once:
       * ```pip install -r requirements.txt```
    * ***IMPORTANT*** - If developing locally on your device, ensure you set up/activate the virtual environment ([see below](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)) before installing/generating the requirements.txt file; failure to do this will pollute your machine and put other projects at risk

### **Setting up the Workspace** (To be done locally via the console of your chosen editor)

1. Create a virtual environment on your machine (Can be skipped if using gitpod):
    * ```python -m venv venv```
1. To ensure the virtual environment is not tracked by version control, add venv to the .gitignore file.
1. Install Django with version 5.1.7:
    * ```pip install django==5.1.7```
1. Install gunicorn for handling HTTP requests:
    * ```pip install gunicorn```
1. Install supporting libraries:
    * ```pip install dj_database_url```
    * ```pip install psycopg2-binary```
    * ```pip install whitenoise```
    * ```pip install crispy-forms```
    * ```pip install crispy-bootstrap5```
    * ```pip install django-countries```
    * ```pip install stripe```
1. Create requirements.txt:
    * ```pip freeze --local > requirements.txt```
1. Create a new Django project:
    * ```django-admin startproject bookland```
1. Create the necessary apps:
    * ```python manage.py startapp home```
    * ```python manage.py startapp products```
    * ```python manage.py startapp profiles```
    * ```python manage.py startapp cart```
    * ```python manage.py startapp checkout```
    * ```python manage.py startapp extra_pages```
1. Add the new apps to the list of installed apps in settings.py
1. Migrate changes:
    * ```python manage.py migrate```
1. Test server works locally:
    * ```python manage.py runserver```  (You should see the default Django success page)

### **Create Heroku App**

The below works on the assumption that you already have an account with [Heroku](https://id.heroku.com/login) and are already signed in.

1. Create a new Heroku app:
    * Click "New" in the top right-hand corner of the landing page, then click "Create new app."
1. Give the app a unique name:
    * Will form part of the URL (in this case, "bookland-store")
1. Select the nearest location:
    * For me, this was Europe.
1. Add Database to the Heroku app:
    * Navigate to the Resources tab of the app dashboard. Under the heading "Add-ons," search for "Heroku Postgres" and click on it when it appears.
    * Select "Hobby Dev - Free" from the "plan name" drop-down menu and click "Submit Order Form."
1. From your editor, go to your project's settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    * Variable KEY = SECRET_KEY
    * Variable VALUE = Value copied from settings.py in project.

### **AWS S3 Bucket Configuration**

The below works on the assumption that you already have an account with [AWS](https://aws.amazon.com/) and are already signed in.

1. Create a new S3 bucket:
    * Click "Services" in the top left-hand corner of the landing page, click on "Storage" then click "S3."
    * Click "Create bucket."
    * Give the bucket a unique name:
        * For this project, I called the S3 bucket "bookland-e-commerce"
    * Select the nearest location:
        * For me, this was EU (Ireland) eu-west-1.
    * Under the "Object Ownership" section, select "ACLS enabled"
    * Under the "Block Public Access settings for this bucket" section, untick "Block all public access" and tick the box to acknowledge that this will make the bucket public.
    * Click "Create bucket."
1. Amend Bucket settings:
    * Bucket Properties:
       * Click on the bucket name to open the bucket.
       * Click on the "Properties" tab.
       * Under the "Static website hosting" section, click "Edit."
       * Under the "Static website hosting" section select "Enable".
       * Under the "Hosting type" section ensure "Host a static website" is selected.
       * Under the "Index document" section enter "index.html".
       * Click "Save changes."
    * Bucket Permissions:
       * Click on the "Permissions" tab.
       * Scroll down to the "CORS configuration" section and click edit.
       * Enter the following snippet into the text box:

       ```JSON
            [
                {
                    "AllowedHeaders": [
                    "Authorization"
                    ],
                    "AllowedMethods": [
                    "GET"
                    ],
                    "AllowedOrigins": [
                    "*"
                    ],
                    "ExposeHeaders": []
                }
            ]
        ```

       * Click "Save changes."
       * Scroll back up to the "Bucket Policy" section and click "Edit."
       * Take note of the "Bucket ARN" click on the "Policy Generator" button to open the AWS policy generator in a new tab.
       * In the newly opened tab under Step 1 "Select Policy Type" select "S3 Bucket Policy." from the drop down menu.
       * Under Step 2 "Add Statement(s)" enter " * " in the "Principal" text box.
       * From the "s3:Action" drop down menu select "s3:GetObject".
       * Enter the "ARN" noted from the bucket policy page into the "Amazon Resource Name (ARN)" text box.
       * Click "Add Statement."
       * Under Step 3 "Generate Policy" click "Generate Policy."
       * Copy the resultant policy and paste it into the bucket policy text box on the previous tab.
       * In the same text box add "/*" to the end of the resource key to allow access to all resources in this bucket.
       * Click "Save changes."
       * When back on the bucket's permissions tab, scroll down to the "Access Control List" section and click "Edit."
       * Enable "List" for "Everyone (public access)", tick the box to accept that "I understand the effects of these changes on my objects and buckets."  and click "Save changes."

1. Create AWS static files User and assign to S3 Bucket:
    * Create "User Group":
        * Click "Services" in the top left-hand corner of the landing page, from the left side of the menu click on "Security, Identity, & Compliance" and select "IAM" from the right side of the menu.
        * Under "Access management" click "User Groups."
        * Click "Create Group."
        * Enter a user name (for this project, I called the user group "manage-bookland-files").
        * Scroll to the bottom of the page and click "Create Group."
    * Create permissions policy for the new user group:
        * Click "Policies" in the left-hand menu.
        * Click "Create Policy."
        * Click "Import managed policy."
        * Search for "AmazonS3FullAccess", select this policy, and click "Import".
        * Click "JSON" under "Policy Document" to see the imported policy
        * Copy the bucket ARN from the bucket policy page and paste it into the "Resource" section of the JSON snippet. Be sure to remove the default value of the resource key ("*") and replace it with the bucket ARN.
        * Copy the bucket ARN a second time into the "Resource" section of the JSON snippet. This time, add "/*" to the end of the ARN to allow access to all resources in this bucket.
        * Click "Next: Tags."
        * Click "Next: Review."
        * Click "Review Policy."
        * Enter a name for the policy (for this project, I called the policy "bookland-s3-policy").
        * Enter a description for the policy.
        * Click "Create Policy."
    * Attach Policy to User Group:
        * Click "User Groups" in the left-hand menu.
        * Click on the user group name created during the above step.
        * Select the "Permissions" tab.
        * click "Attach Policy."
        * Search for the policy created during the above step, and select it.
        * Click "Attach Policy."
    * Create User:
        * Click "Users" in the left-hand menu.
        * Click "Add user."
        * Enter a "User name" (for this project, I called the user "bookland-staticfiles-user").
        * Select "Programmatic access" and "AWS Management Console access."
        * Click "Next: Permissions."
        * Select "Add user to group."
        * Select the user group created during the above step.
        * Click "Next: Tags."
        * Click "Next: Review."
        * Click "Create user."
        * Take note of the "Access key ID" and "Secret access key" as these will be needed to connect to the S3 bucket.
        * Click "Download .csv" to download the credentials.
        * Click "Close."
1. Install required packages to use AWS S3 Bucket in Django:
    * ```pip install boto3```
    * ```pip install django-storages```
1. Add 'storages' to the bottom of the installed apps section of settings.py file:

   ```python
    INSTALLED_APPS = [
    …,
        'storages'
    …,
   ]
   ```

### **Creating Environmental Variables Locally**

1. Install dotenv package:
    * ```pip install python-dotenv```
1. On your local machine, create a file called ".env" at the same level as settings.py and add this to the .gitignore file.
1. From your project's settings.py file, copy the SECRET_KEY value and assign it to a variable called SECRET_KEY in your .env file
    * ``` SECRET_KEY=PastedValueFromYourProjectsSettings.pyFile ```
1. Add DEVELOPMENT variable to .env file:
    * ``` DEVELOPMENT=True ```
1. Add Stripe Environment Variables:
    * ``` STRIPE_PUBLIC_KEY=your_stripe_public_key ```
    * ``` STRIPE_SECRET_KEY=your_stripe_secret_key ```
    * ``` STRIPE_WH_SECRET=your_stripe_webhook_secret ```
1. Add Email Configuration Variables (if using Gmail):
    * ``` EMAIL_HOST_USER=your_gmail_username ```
    * ``` EMAIL_HOST_PASSWORD=your_gmail_app_password ```
    * ``` DEFAULT_FROM_EMAIL=your_default_from_email ```

### **Setting up settings.py File**

1. At the top of your settings.py file, add the following snippet immediately after the other imports:

    ```python
        import os
        import dj_database_url
        from pathlib import Path
        
        # Build paths inside the project like this: BASE_DIR / 'subdir'.
        BASE_DIR = Path(__file__).resolve().parent.parent
        
        # Load environment variables if in development mode
        if os.path.isfile('.env'):  
            from dotenv import load_dotenv  
            load_dotenv()

        # SECURITY WARNING: keep the secret key used in production secret!
        SECRET_KEY = os.environ.get("SECRET_KEY", "")
        
        # SECURITY WARNING: don't run with debug turned on in production!
        DEBUG = "DEVELOPMENT" in os.environ
    ```

1. Add a conditional in settings.py DATABASES section by replacing it with the following snippet to link up the Heroku Postgres server when in production and SQLite3 when developing locally:  

    ``` python
    if 'DATABASE_URL' in os.environ:
       DATABASES = {
           'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
       }
    else:
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.sqlite3',
               'NAME': BASE_DIR / 'db.sqlite3',
           }
       }
    ```

1. Tell Django where to store media and static files by placing this snippet under the comments indicated below:

    ``` python
       # Static files (CSS, JavaScript, Images)
       # https://docs.djangoproject.com/en/5.1/howto/static-files/
       STATIC_URL = '/static/'
       STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
       STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

       MEDIA_URL = '/media/'
       MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

1. Add the following to urls.py to serve static and media files in development:

    ``` python
       from django.conf import settings
       from django.conf.urls.static import static

       urlpatterns = [
           # Your URL patterns here
       ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

1. Configure template directories in settings.py:
   * ``` TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') ```

1. Update the TEMPLATES array:

   ```python
      TEMPLATES = [
          {
              'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [
                  os.path.join(BASE_DIR, 'templates'),
                  os.path.join(BASE_DIR, 'templates', 'allauth'),
              ],
              'APP_DIRS': True,
              'OPTIONS': {
                  'context_processors': [
                      'django.template.context_processors.debug',
                      'django.template.context_processors.request',
                      'django.contrib.auth.context_processors.auth',
                      'django.contrib.messages.context_processors.messages',
                      'profiles.contexts.wishlist_count',
                      'products.contexts.categories_processor',
                      'cart.contexts.cart_contents',
                  ],
              },
          },
      ]
   ```

1. Link S3 Bucket to Django Project by adding the following to the settings.py file:

    ``` python
        # AWS S3 configuration
        if 'USE_AWS' in os.environ:
            # Cache control
            AWS_S3_OBJECT_PARAMETERS = {
                'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                'CacheControl': 'max-age=94608000',
            }

            # Bucket Config
            AWS_STORAGE_BUCKET_NAME = 'bookland-e-commerce'
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
            AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

            # Static and media files
            # Source: Tutor Support(Tutor support shared this storages part for django 5)
            STORAGES = {
                "default": {
                    "BACKEND": "custom_storages.MediaStorage",
                },
                "staticfiles": {"BACKEND": "custom_storages.StaticStorage"},
            }
            STATICFILES_LOCATION = 'static'
            MEDIAFILES_LOCATION = 'media'

            # Override static and media URLs in production
            STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
            MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

1. Configure WhiteNoise for static files in production:
   ```python
   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware',
       # Other middleware...
   ]

   STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

1. Configure email settings in settings.py:
   ```python
   if 'DEVELOPMENT' in os.environ:
       # Use console backend for development
       EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
       DEFAULT_FROM_EMAIL = 'bookland@example.com'
   else:
       EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
       EMAIL_USE_TLS = True
       EMAIL_PORT = 587
       EMAIL_HOST = 'smtp.gmail.com'
       EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
       EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
       DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
   ```

1. Add allowed hosts to settings.py:
    * ``` ALLOWED_HOSTS = ["bookland-store.herokuapp.com", "localhost", "127.0.0.1"] ```

1. Create Procfile at the top level of the file structure and insert the following:
    * ``` web: gunicorn bookland.wsgi ```

1. Make an initial commit and push the code to the GitHub Repository.
    * ```git add .```
    * ```git commit -m "Initial deployment"```
    * ```git push```

1. Create a file called "custom_storages.py" in the root of the project and add the following code:

    ```python
        # This file tells Django where to store static and media files in production
        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage

        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION

        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION
    ```

### **Set up Heroku for Use via Console**

1. Set up the necessary Heroku config vars:
   * AWS_ACCESS_KEY_ID: Your AWS access key
   * AWS_SECRET_ACCESS_KEY: Your AWS secret access key
   * DATABASE_URL: This will be automatically set up by the Postgres add-on
   * EMAIL_HOST_PASSWORD: Your email host password
   * EMAIL_HOST_USER: Your email host user
   * SECRET_KEY: Your Django secret key
   * STRIPE_PUBLIC_KEY: Your Stripe public key
   * STRIPE_SECRET_KEY: Your Stripe secret key
   * STRIPE_WH_SECRET: Your Stripe webhook secret
   * USE_AWS: Set to True

1. Click on Account Settings (under the avatar menu)
1. Scroll down to the API Key section and click Reveal. Copy the API key.
1. Log in to Heroku via the console and enter your details.
    * ```heroku login -i```
    * When prompted, enter your Heroku username
    * Enter copied API key as the password

1. Get your app name from Heroku
    * ```heroku apps```
1. Set Heroku remote
    * ```heroku git:remote -a bookland-store```
1. Add, Commit, Push to GitHub:
    * ```git add . && git commit -m "Deploy to Heroku via CLI"```
1. Push to GitHub and Heroku
    * ```git push origin main```
    * ```git push heroku main```
1. Initialize the database on Heroku:
    * ```heroku run python manage.py migrate```
1. Create a superuser for the Django admin:
    * ```heroku run python manage.py createsuperuser```
1. Load data fixtures if available:
    * ```heroku run python manage.py loaddata categories```
    * ```heroku run python manage.py loaddata books```

## **Project Maintenance**

### **Forking the Repository**

1. Navigate to the [GitHub Repository](https://github.com/onur-CK/BookLand)
2. Click on the "Fork" button at the top right of the page
3. You will now have a copy of the repository in your GitHub account

### **Cloning the Repository**

1. Navigate to the [GitHub Repository](https://github.com/onur-CK/BookLand)
2. Click on the "Code" button
3. Copy the URL provided (either HTTPS or SSH)
4. Open a terminal window on your local machine
5. Navigate to the directory where you want to clone the repository
6. Type ```git clone``` followed by the URL you copied
7. Press Enter and the repository will be cloned to your local machine

### **Making Changes**

1. Always create a new branch for your changes
    * ```git checkout -b feature/your-feature-name```
2. Make your changes
3. Test your changes locally
4. Commit your changes
    * ```git add .```
    * ```git commit -m "Your commit message"```
5. Push your changes to GitHub
    * ```git push origin feature/your-feature-name```
6. Create a Pull Request on GitHub
7. Once your Pull Request is approved, merge it into the main branch

[Back to Readme](README.md)