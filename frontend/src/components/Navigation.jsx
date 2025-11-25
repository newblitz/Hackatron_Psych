import { motion } from 'framer-motion';
import { useState, useEffect } from 'react';
import { Menu, X } from 'lucide-react';
import '../styles/Navigation.css';

function Navigation() {
  const [scrolled, setScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { name: 'How It Works', href: '/know_more' },
    { name: 'Therapists', href: '#therapists' },
    { name: 'About', href: '#about' },
    { name: 'Careers', href: '/internship' },
  ];

  return (
    <motion.nav
      className={`navigation ${scrolled ? 'scrolled' : ''}`}
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ duration: 0.6 }}
    >
      <div className="container">
        <div className="nav-content">
          <a href="/" className="logo">
            <span className="logo-text">MindEase</span>
          </a>

          <div className="nav-links">
            {navLinks.map((link) => (
              <a key={link.name} href={link.href} className="nav-link">
                {link.name}
              </a>
            ))}
          </div>

          <div className="nav-actions">
            <a href="/create/login/" className="nav-login">
              Sign In
            </a>
            <a href="/create/" className="btn btn-primary">
              Get Started
            </a>
          </div>

          <button
            className="mobile-menu-btn"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          >
            {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>

        {mobileMenuOpen && (
          <motion.div
            className="mobile-menu"
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
          >
            {navLinks.map((link) => (
              <a key={link.name} href={link.href} className="mobile-link">
                {link.name}
              </a>
            ))}
            <div className="mobile-actions">
              <a href="/create/login/" className="btn btn-secondary">
                Sign In
              </a>
              <a href="/create/" className="btn btn-primary">
                Get Started
              </a>
            </div>
          </motion.div>
        )}
      </div>
    </motion.nav>
  );
}

export default Navigation;
