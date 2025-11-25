import { motion } from 'framer-motion';
import { useState, useEffect } from 'react';
import { Heart, Menu, X } from 'lucide-react';
import '../styles/Navigation.css';

function Navigation() {
  const [scrolled, setScrolled] = useState(false);
  const [isAuthenticated] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { name: 'How It Works', href: '/know_more' },
    { name: 'Our Therapists', href: '#therapists' },
    { name: 'Resources', href: '#resources' },
    { name: 'Careers', href: '/internship' },
  ];

  return (
    <motion.header
      className={`navigation ${scrolled ? 'scrolled' : ''}`}
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
    >
      <div className="nav-container">
        <motion.a
          href="/"
          className="logo"
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
        >
          <div className="logo-icon">
            <Heart size={24} fill="currentColor" />
          </div>
          <span className="logo-text">MindEase</span>
        </motion.a>

        <nav className="nav-links">
          {navLinks.map((link, index) => (
            <motion.a
              key={link.name}
              href={link.href}
              className="nav-link"
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 + 0.2, duration: 0.5 }}
              whileHover={{ y: -2 }}
            >
              {link.name}
            </motion.a>
          ))}
        </nav>

        <div className="nav-actions">
          {isAuthenticated ? (
            <>
              <span className="user-badge">👤</span>
              <motion.a
                href="/logout"
                className="btn btn-outline"
                whileHover={{ scale: 1.05, y: -1 }}
                whileTap={{ scale: 0.95 }}
              >
                Logout
              </motion.a>
            </>
          ) : (
            <>
              <motion.a
                href="/create/login/"
                className="nav-link-cta"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                Sign In
              </motion.a>
              <motion.a
                href="/create/"
                className="btn btn-primary"
                whileHover={{ scale: 1.05, y: -1 }}
                whileTap={{ scale: 0.95 }}
              >
                Get Started
              </motion.a>
            </>
          )}
        </div>

        <motion.button
          className="mobile-menu-btn"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          whileTap={{ scale: 0.9 }}
        >
          {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
        </motion.button>
      </div>

      {mobileMenuOpen && (
        <motion.div
          className="mobile-menu"
          initial={{ opacity: 0, height: 0 }}
          animate={{ opacity: 1, height: 'auto' }}
          exit={{ opacity: 0, height: 0 }}
          transition={{ duration: 0.3 }}
        >
          <div className="mobile-menu-content">
            {navLinks.map((link) => (
              <a key={link.name} href={link.href} className="mobile-link">
                {link.name}
              </a>
            ))}
            <div className="mobile-actions">
              <a href="/create/login/" className="mobile-action secondary">
                Sign In
              </a>
              <a href="/create/" className="mobile-action primary">
                Get Started
              </a>
            </div>
          </div>
        </motion.div>
      )}
    </motion.header>
  );
}

export default Navigation;
