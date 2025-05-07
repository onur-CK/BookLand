# BookLand - Deployment Guide

## Table of Contents

- [Introduction](#introduction)
- [Deployment Overview](#deployment-overview)
- [Prerequisites](#prerequisites)
  - [Required Accounts](#required-accounts)
  - [Required Software](#required-software)
  - [Environment Variables](#environment-variables)
- [Local Development Setup](#local-development-setup)
  - [Clone Repository](#clone-repository)
  - [Virtual Environment Setup](#virtual-environment-setup)
  - [Installing Dependencies](#installing-dependencies)
  - [Database Setup](#database-setup)
  - [Running the Development Server](#running-the-development-server)
- [Heroku Deployment](#heroku-deployment)
  - [Creating a Heroku App](#creating-a-heroku-app)
  - [Configuring Resources](#configuring-resources)
  - [Setting Environment Variables](#setting-environment-variables)
  - [Deployment Method Configuration](#deployment-method-configuration)
  - [Manual Deployment Steps](#manual-deployment-steps)
  - [Automatic Deployment Setup](#automatic-deployment-setup)
- [Database Configuration](#database-configuration)
  - [Local SQLite Database](#local-sqlite-database)
  - [Production PostgreSQL Database](#production-postgresql-database)
  - [Database Migrations](#database-migrations)
- [Static and Media Files (AWS S3)](#static-and-media-files-aws-s3)
  - [AWS Account Setup](#aws-account-setup)
  - [S3 Bucket Configuration](#s3-bucket-configuration)
  - [IAM Configuration](#iam-configuration)
  - [Django AWS Configuration](#django-aws-configuration)
- [Stripe Integration](#stripe-integration)
  - [Stripe Account Setup](#stripe-account-setup)
  - [API Keys Configuration](#api-keys-configuration)
  - [Webhook Configuration](#webhook-configuration)
- [Email Configuration](#email-configuration)
  - [Gmail SMTP Setup](#gmail-smtp-setup)
  - [Testing Email Functionality](#testing-email-functionality)
- [Final Deployment Checklist](#final-deployment-checklist)
- [Post-Deployment Tasks](#post-deployment-tasks)
  - [Adding Initial Data](#adding-initial-data)
  - [Admin Account Setup](#admin-account-setup)
  - [Security Checks](#security-checks)


# BookLand - Deployment Guide

## Introduction

This document provides comprehensive instructions for deploying the BookLand e-commerce platform. It covers both development environment setup and production deployment procedures, ensuring a smooth transition from local development to a live, customer-facing application.

BookLand is built using Django with PostgreSQL database integration, AWS S3 for static and media file storage, Stripe for payment processing, and Gmail for email communications. The deployment process involves configuring these services and connecting them properly for a secure, reliable application.

## Deployment Overview

The BookLand deployment process consists of several key stages:

1. Setting up the local development environment
2. Configuring necessary external services (AWS, Stripe, Email)
3. Deploying to Heroku for production
4. Connecting to the production database
5. Configuring static and media file storage
6. Final verification and testing

This guide will walk you through each step in detail, providing instructions for both new deployments and updates to the existing application.

## Prerequisites

### Required Accounts

Before beginning the deployment process, ensure you have accounts with the following services:

- **GitHub**: For version control and code repository
- **Heroku**: For application hosting
- **AWS**: For static and media file storage
- **Stripe**: For payment processing
- **Gmail**: For sending transactional emails

### Required Software

Ensure the following software is installed on your local development machine:

- **Python 3.9+**: The programming language used for the application
- **Git**: For version control
- **pip**: Python package manager
- **PostgreSQL** (optional for local development): Database system

### Environment Variables

The following environment variables are required for both development and production:

#### Development Environment Variables
Create a `.env` file in the root directory with the following variables:
```python
SECRET_KEY=your_django_secret_key
DEBUG=True
DEVELOPMENT=True
EMAIL_HOST_USER=your_gmail_address
EMAIL_HOST_PASSWORD=your_gmail_app_password
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WH_SECRET=your_stripe_webhook_secret
```

#### Production Environment Variables

These will be configured in Heroku and should include:
```python
SECRET_KEY=your_django_secret_key
DEBUG=False
EMAIL_HOST_USER=your_gmail_address
EMAIL_HOST_PASSWORD=your_gmail_app_password
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WH_SECRET=your_stripe_webhook_secret
DATABASE_URL=your_postgres_database_url
USE_AWS=True
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
```

## Local Development Setup

### Clone Repository

1. Navigate to the [BookLand repository](https://github.com/onur-CK/BookLand)
2. Click the "Code" button and copy the repository URL
3. Open your terminal and run:
git clone https://github.com/onur-CK/BookLand.git
cd bookland

### Virtual Environment Setup

Creating a virtual environment isolates the project dependencies:

**For Windows:**
python -m venv venv
venv\Scripts\activate

**For macOS/Linux:**
python3 -m venv venv
source venv/bin/activate

### Installing Dependencies

Install all required packages:
pip install -r requirements.txt

The key dependencies include:
- Django
- dj-database-url
- psycopg2-binary
- django-allauth
- Pillow
- stripe
- django-crispy-forms
- django-countries
- boto3
- django-storages
- gunicorn
- whitenoise

### Database Setup

For local development, Django uses SQLite by default:

1. Run migrations to set up the database:
python manage.py makemigrations
python manage.py migrate

2. Create a superuser for admin access:
python manage.py createsuperuser
Follow the prompts to create your admin user.

### Running the Development Server

Start the Django development server:
python manage.py runserver

The application should now be running at `http://127.0.0.1:8000/`.

## Heroku Deployment

### Creating a Heroku App

1. Log in to your [Heroku account](https://dashboard.heroku.com/)
2. Click "New" > "Create new app"
3. Enter a unique app name (e.g., "bookland-e-commerce")
4. Select the region closest to you
5. Click "Create app"

### Configuring Resources

Add a PostgreSQL database to your Heroku app:

1. In the Heroku dashboard, go to the "Resources" tab
2. In the "Add-ons" search field, type "postgres"
3. Select "Heroku Postgres"
4. Choose the "Hobby Dev - Free" plan
5. Click "Submit Order Form"

### Setting Environment Variables

Configure environment variables in Heroku:

1. Go to the "Settings" tab in your Heroku dashboard
2. Click "Reveal Config Vars"
3. Add the following variables:

| Key | Value |
|-----|-------|
| SECRET_KEY | your_django_secret_key |
| DEBUG | False |
| EMAIL_HOST_USER | your_gmail_address |
| EMAIL_HOST_PASSWORD | your_gmail_app_password |
| STRIPE_PUBLIC_KEY | your_stripe_public_key |
| STRIPE_SECRET_KEY | your_stripe_secret_key |
| STRIPE_WH_SECRET | your_stripe_webhook_secret |
| USE_AWS | True |
| AWS_ACCESS_KEY_ID | your_aws_access_key |
| AWS_SECRET_ACCESS_KEY | your_aws_secret_key |

The `DATABASE_URL` should be automatically added when you provisioned the Postgres database.

### Deployment Method Configuration

You can deploy to Heroku using either the Heroku CLI or GitHub integration. We'll cover both methods:

### Manual Deployment Steps

1. Create a `Procfile` in your project root with the following content:
web: gunicorn bookland.wsgi

2. Ensure your `requirements.txt` is up to date:
pip freeze > requirements.txt

3. Log in to Heroku CLI:
heroku login

4. Add the Heroku remote to your Git repository:
heroku git -a your-heroku-app-name

5. Push to Heroku:
git push heroku main

6. Run migrations on Heroku:
heroku run python manage.py migrate

### Automatic Deployment Setup

For automatic deployments from GitHub:

1. Go to the "Deploy" tab in your Heroku dashboard
2. In the "Deployment method" section, select "GitHub"
3. Connect your GitHub repository
4. Scroll down to "Automatic deploys" and select the branch to deploy
5. Click "Enable Automatic Deploys"


## Database Configuration

### Local SQLite Database

For development, Django uses SQLite by default. This configuration is in `settings.py`:

```python
# settings.py
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
### Production PostgreSQL Database

In production, the PostgreSQL database is used through the DATABASE_URL environment variable configured in Heroku.

### Database Migrations

Run migrations to set up the database schema:

1. For local development:
python manage.py makemigrations
python manage.py migrate

2. For Heroku:
heroku run python manage.py migrate

