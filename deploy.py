#!/usr/bin/env python3
"""
Deployment script for TechInsights Pro
Run this after deploying to initialize the database
"""

from flaskblog import create_app, db
from flaskblog.models import User, Post
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
import random

app = create_app()
bcrypt = Bcrypt(app)

def init_database():
    """Initialize database with sample data"""
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Check if data already exists
        if User.query.first():
            print("Database already initialized!")
            return
        
        # Create sample users
        users_data = [
            {'username': 'techguru', 'email': 'tech@example.com', 'password': 'password123'},
            {'username': 'airesearcher', 'email': 'ai@example.com', 'password': 'password123'},
            {'username': 'webdev', 'email': 'web@example.com', 'password': 'password123'},
            {'username': 'datasci', 'email': 'data@example.com', 'password': 'password123'},
        ]
        
        users = []
        for user_data in users_data:
            hashed_password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
            user = User(
                username=user_data['username'],
                email=user_data['email'],
                password=hashed_password
            )
            db.session.add(user)
            users.append(user)
        
        db.session.commit()
        
        # Computer Science posts
        posts_data = [
            {
                'title': 'The Future of Quantum Computing in 2025',
                'content': '''Quantum computing is rapidly evolving from theoretical concept to practical reality. In 2025, we're seeing breakthrough developments in quantum error correction, making quantum computers more stable and reliable than ever before.

Key developments include:
• IBM's 1000+ qubit processors achieving quantum advantage in optimization problems
• Google's quantum AI solving protein folding challenges in minutes
• Microsoft's topological qubits showing unprecedented stability

The implications for cryptography, drug discovery, and financial modeling are profound. As quantum computers become more accessible through cloud platforms, we're entering a new era of computational possibilities.

What excites me most is how quantum machine learning is beginning to outperform classical algorithms in specific domains, particularly in pattern recognition and optimization tasks.''',
                'author_id': 1
            },
            {
                'title': 'Large Language Models: Beyond ChatGPT',
                'content': '''The landscape of Large Language Models has exploded beyond ChatGPT, with specialized models emerging for specific domains and use cases.

Recent breakthroughs include:
• Multimodal models that seamlessly integrate text, images, and code
• Domain-specific models trained on scientific literature outperforming general models
• Efficient fine-tuning techniques making custom models accessible to smaller teams

The most exciting development is the emergence of "reasoning models" that can break down complex problems step-by-step, showing their work like a human expert.

We're also seeing significant progress in reducing hallucinations through techniques like retrieval-augmented generation (RAG) and constitutional AI training methods.

The future isn't just about bigger models—it's about smarter, more specialized, and more reliable AI systems.''',
                'author_id': 2
            },
            {
                'title': 'Modern Web Development: The Rise of Edge Computing',
                'content': '''Edge computing is revolutionizing how we build and deploy web applications. By processing data closer to users, we're achieving unprecedented performance and user experiences.

Key trends shaping web development in 2025:
• Edge-first architectures with CDN-based compute
• WebAssembly enabling near-native performance in browsers
• Progressive Web Apps becoming indistinguishable from native apps
• Server-side rendering at the edge for optimal SEO and performance

Frameworks like Next.js, SvelteKit, and Remix are leading the charge with built-in edge support. The developer experience has never been better, with tools that automatically optimize for performance and user experience.

The most game-changing aspect is how edge computing enables real-time collaboration features that were previously impossible due to latency constraints.''',
                'author_id': 3
            },
            {
                'title': 'Data Science in the Age of Privacy',
                'content': '''Privacy-preserving data science is no longer optional—it's essential. With regulations like GDPR and CCPA, data scientists must balance insights with privacy protection.

Emerging techniques include:
• Differential privacy ensuring individual data points remain anonymous
• Federated learning training models without centralizing data
• Homomorphic encryption enabling computation on encrypted data
• Synthetic data generation for safe model training and testing

The most promising development is federated learning, where models are trained across distributed datasets without ever sharing the raw data. This enables collaboration between organizations while maintaining strict privacy controls.

Tools like PySyft and TensorFlow Federated are making these advanced techniques accessible to practitioners, democratizing privacy-preserving machine learning.''',
                'author_id': 4
            }
        ]
        
        # Add posts with varied dates
        base_date = datetime.utcnow() - timedelta(days=30)
        for i, post_data in enumerate(posts_data):
            post_date = base_date + timedelta(days=random.randint(0, 25), hours=random.randint(0, 23))
            post = Post(
                title=post_data['title'],
                content=post_data['content'],
                date_posted=post_date,
                user_id=post_data['author_id']
            )
            db.session.add(post)
        
        db.session.commit()
        print("Database initialized successfully with sample data!")

if __name__ == '__main__':
    init_database()