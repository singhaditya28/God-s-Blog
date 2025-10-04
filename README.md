# TechInsights Pro(formerly God's Blog)

> Blogging platform for technology.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0.3-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Overview

TechInsights Pro is a modern, enterprise-grade blog platform designed for technology leaders, CTOs, and engineering professionals. Built with Flask and featuring a sophisticated 2025 UI design, it delivers premium insights into AI, cloud architecture, cybersecurity, and emerging technologies.

### ✨ Key Features

- **🎨 Modern UI Design** - Professional 2025 design standards with smooth animations
- **📱 Fully Responsive** - Optimized for desktop, tablet, and mobile devices
- **🔐 Secure Authentication** - User registration, login, and password reset functionality
- **📝 Rich Content Management** - Create, edit, and delete blog posts with ease
- **👤 User Profiles** - Customizable profiles with image uploads
- **📧 Email Integration** - Password reset via email notifications
- **🔍 Advanced Pagination** - Efficient content browsing
- **⚡ Performance Optimized** - Fast loading with modern CSS and animations

## 🛠️ Technology Stack

- **Backend**: Flask 2.0.3, SQLAlchemy, Flask-Login
- **Frontend**: Bootstrap 5, Custom CSS3, JavaScript ES6+
- **Database**: SQLite (development), PostgreSQL (production)
- **Authentication**: Flask-Bcrypt, Flask-WTF
- **Email**: Flask-Mail with SMTP
- **Image Processing**: Pillow for profile pictures

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/singhaditya28/TechInsights-Pro.git
   cd TechInsights-Pro
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables** (optional)
   ```bash
   export SECRET_KEY="your-secret-key"
   export EMAIL_USER="your-email@gmail.com"
   export EMAIL_PASS="your-app-password"
   ```

5. **Initialize database**
   ```bash
   python deploy.py
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

7. **Access the application**
   Open your browser and navigate to `http://localhost:5000`


## 📁 Project Structure

```
TechInsights-Pro/
├── flaskblog/
│   ├── __init__.py          # App factory and extensions
│   ├── config.py            # Configuration settings
│   ├── models.py            # Database models
│   ├── static/
│   │   ├── main.css         # Custom styles
│   │   ├── main.js          # JavaScript functionality
│   │   └── profile_pics/    # User uploaded images
│   ├── templates/           # Jinja2 templates
│   ├── users/              # User authentication routes
│   ├── posts/              # Blog post routes
│   ├── main/               # Main application routes
│   └── errors/             # Error handling
├── requirements.txt         # Python dependencies
├── run.py                  # Application entry point
├── deploy.py               # Database initialization
├── Procfile                # Deployment configuration
└── README.md               # Project documentation
```

## 🎨 Design Features

### Modern UI Components
- **Glass morphism effects** with backdrop blur
- **Gradient accents** and professional color palette
- **Smooth animations** with staggered entrance effects
- **Professional typography** using Inter font family
- **Responsive grid layouts** with CSS Grid and Flexbox

### User Experience
- **Intuitive navigation** with sticky header
- **Professional forms** with inline validation
- **Loading states** and micro-interactions
- **Accessible design** with proper contrast ratios
- **Mobile-first** responsive approach

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Flask secret key for sessions | Yes |
| `DATABASE_URL` | Database connection string | No (defaults to SQLite) |
| `EMAIL_USER` | SMTP email username | No |
| `EMAIL_PASS` | SMTP email password | No |

### Email Setup (Optional)

For password reset functionality, configure Gmail SMTP:

1. Enable 2-factor authentication on your Gmail account
2. Generate an app-specific password
3. Set `EMAIL_USER` and `EMAIL_PASS` environment variables

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask** community for the excellent web framework
- **Bootstrap** team for the responsive CSS framework
- **Inter** font family for professional typography
- **Font Awesome** for the comprehensive icon library

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/singhaditya28/TechInsights-Pro/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

---

**Built with ❤️ for the technology community**

*TechInsights Pro - Where enterprise technology meets strategic intelligence*
