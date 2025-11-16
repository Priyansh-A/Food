# 🛒 Heaven's Door - Django E-commerce Platform

A modern, dockerized e-commerce platform built with Django, featuring shopping cart, order management, payment processing, and coupon system.

![Django](https://img.shields.io/badge/Django-5.2-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![E-commerce](https://img.shields.io/badge/E--commerce-Platform-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

## 🚀 Features

### 🛍️ Product Management
- **Categories & Organization**: Organize products by categories with SEO-friendly URLs
- **Detailed Product Pages**: Rich product information with images and descriptions

### 🛒 Shopping Cart System
- **Session-based Cart**: Persistent shopping cart across browser sessions
- **Real-time Updates**: Instant cart modifications and quantity changes
- **Cart Management**: Easy add, remove, and update cart items
- **Price Calculations**: Automatic product, discount, and total calculations

### 💳 Payment & Order Processing
- **Esewa Sandbox**: Integrated payment gateway with Esewa 
- **Order Management**: Complete order lifecycle from creation to fulfillment
- **PDF Invoices**: Automatic invoice generation for orders
- **Order Tracking**: Monitor order status and history

### 🎫 Promotions & Discounts
- **Coupon System**: Apply promotional codes and discounts
- **Flexible Campaigns**: Time-based and usage-limited coupon strategies
- **Cart Calculations**: Automatic discount application and validation

## 🛠️ Tech Stack

**Backend:**
- Django 5.2+ (Python)
- PostgreSQL (Database)
- Session-based cart management
- Payment gateway integration

**Frontend:**
- HTML5, CSS3, JavaScript
- Responsive design for all devices
- Dynamic form handling and validation

**Servers:**
- Gunicorn (WSGI HTTP Server)
- Nginx (Reverse Proxy & Static Files)

**Infrastructure:**
- Docker & Docker Compose
- Multi-container architecture
- Production-ready deployment

## 📦 Quick Start

### Prerequisites
- Docker & Docker Compose
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Priyansh-A/Food.git
   cd Food
2. **Build in Docker**
   ```bash
   docker-compose up --build
3. **bash command in case of wait-for-it.sh error**
   ```bash
   dos2unix wait-for-it.sh
4. **Create Superuser for admin privilages**
   ```bash
   docker-compose exec web python manage.py createsuperuser
5. **Filling data in the site**
   ```bash
   docker-compose exec web python manage.py loaddata products.json


