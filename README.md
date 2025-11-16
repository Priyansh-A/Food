🍕 Heaven's Door - Django E-commerce Food Delivery Platform

A modern, dockerized food delivery e-commerce platform built with Django, featuring real-time cart management, coupon system, and restaurant management.

🚀 Features
🛒 Shopping Experience

Smart Cart System: Persistent cart with session management

Coupon & Discounts: Apply promotional codes and discounts

Real-time Cart Updates: Instant cart modifications and calculations

Order Management: Complete order processing and tracking

💰 Payment & Promotions

Coupon System: Time-based and usage-limited discount coupons
    
Promotional Campaigns: Support for various discount strategies

🏗️ Modern Architecture

Dockerized: Easy deployment with Docker Compose

Production Ready: Nginx and Gunicorn setup

Scalable: PostgreSQL database with optimized queries

Session Management: Secure cart and user session handling

🛠️ Tech Stack

Backend:

Django 4.2+ (Python)

Django Sessions (Cart Management)

PostgreSQL (Database)

Redis (Optional caching)

Frontend:

HTML5, CSS3, JavaScript

Servers:

Gunicorn (WSGI HTTP Server)

Nginx (Reverse Proxy & Static Files)

Infrastructure:

Docker & Docker Compose

Multi-container architecture

📦 Quick Start
Prerequisites

Docker & Docker Compose

Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Priyansh-A/Food.git
   cd myshop
2. **Build in Docker**
   ```bash
   docker-compose up --build
3. **Create Superuser for admin privilages**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   


