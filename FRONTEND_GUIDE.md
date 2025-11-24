# Frontend Architecture Guide

## Overview

The MindEase frontend has been completely redesigned using React with modern animations and styling while preserving the Django backend functionality.

## Key Changes

### 1. Technology Stack
- **Framework**: React 18 with Vite
- **Animations**: Framer Motion for smooth transitions
- **Styling**: Modern CSS with gradient themes
- **Icons**: Lucide React
- **Routing**: React Router DOM

### 2. Design Philosophy
- **Color Scheme**: Cyan (#06b6d4) and Purple (#7c3aed) gradients
- **Animation**: Smooth scroll animations, floating elements, and micro-interactions
- **Responsive**: Mobile-first design with breakpoints
- **Performance**: Optimized with lazy loading and code splitting

### 3. Component Architecture

```
frontend/
├── components/
│   ├── Navigation.jsx    - Sticky header with scroll effects
│   ├── Hero.jsx          - Animated hero section with floating cards
│   ├── Features.jsx      - Feature grid with hover animations
│   ├── Benefits.jsx      - Benefits section with rotating visuals
│   └── Footer.jsx        - Footer with social links
├── pages/
│   └── HomePage.jsx      - Main landing page composition
└── styles/
    └── *.css             - Component-specific styling
```

### 4. Animation Features

#### Navigation
- Slides in from top on page load
- Changes background on scroll
- Smooth hover effects on links

#### Hero Section
- Gradient text shimmer effect
- Floating background orbs
- Animated statistics counter
- Parallax floating cards

#### Features
- Staggered card entrance animations
- Hover lift effects
- Icon rotation on hover

#### Benefits
- Rotating circular visualization
- Staggered list animations
- Smooth check icon animations

### 5. Backend Integration

The React frontend communicates with Django through:
- Vite proxy configuration for development
- CORS headers configured in Django settings
- All existing Django URLs preserved

### 6. Django CORS Configuration

Added to `prutha/prutha/settings.py`:
```python
INSTALLED_APPS = [
    ...
    "corsheaders",
    ...
]

MIDDLEWARE = [
    ...
    "corsheaders.middleware.CorsMiddleware",
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CORS_ALLOW_CREDENTIALS = True
```

### 7. Development Workflow

1. **Start Django backend**:
   ```bash
   cd prutha
   python manage.py runserver
   ```

2. **Start React frontend**:
   ```bash
   cd frontend
   npm run dev
   ```

3. **Access application**:
   Navigate to `http://localhost:5173`

### 8. Production Build

Build the frontend for production:
```bash
cd frontend
npm run build
```

The production build will be in `frontend/dist/` and can be served by Django or any static hosting service.

### 9. Key Features Preserved

- User authentication flows
- Appointment booking system
- Counselor dashboard access
- Internship applications
- All Django backend functionality

### 10. Future Enhancements

Consider adding:
- Additional page routes (About, Contact, Services)
- User dashboard with animations
- Real-time notifications
- Dark mode toggle
- Advanced form validations
- Progressive Web App (PWA) features

## API Endpoints

The React frontend can communicate with these Django endpoints:

- `/create/` - User registration
- `/create/login/` - User login
- `/appointment` - Book appointments
- `/know_more` - Information page
- `/internship` - Career opportunities

## Deployment Notes

For production deployment:
1. Build the React app: `npm run build`
2. Configure Django to serve React build files
3. Update CORS settings for production domain
4. Set up proper environment variables
5. Configure static file serving

## Support

For issues or questions:
- Check the main README.md
- Review component-specific CSS files
- Inspect browser console for errors
- Verify Django backend is running
