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