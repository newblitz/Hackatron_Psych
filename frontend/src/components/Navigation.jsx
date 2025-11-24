import { motion } from 'framer-motion';
import { useState, useEffect } from 'react';
import { Brain } from 'lucide-react';
import '../styles/Navigation.css';

function Navigation() {
  const [scrolled, setScrolled] = useState(false);
  const [isAuthenticated] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { name: 'How It Works', href: '/know_more' },
    { name: 'Psychologists', href: '#' },
    { name: 'Initiatives', href: '#' },
    { name: 'Careers', href: '/internship' },
  ];

  return (
    <motion.header
      className={`navigation ${scrolled ? 'scrolled' : ''}`}
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ duration: 0.6, ease: 'easeOut' }}
    >
      <div className="nav-container">
        <motion.a
          href="/"
          className="logo-link"
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
        >
          <div className="logo-icon">
            <Brain size={24} strokeWidth={2} />
          </div>
          <span className="logo-text">MindEase</span>
        </motion.a>

        <nav className="nav-links">
          {navLinks.map((link, index) => (
            <motion.a
              key={link.name}
              href={link.href}
              className="nav-link"
              initial={{ opacity: 0, y: -20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 + 0.3 }}
              whileHover={{ y: -2 }}
            >
              {link.name}
            </motion.a>
          ))}
        </nav>

        <div className="nav-actions">
          {isAuthenticated ? (
            <>
              <span className="welcome-text">Welcome, User!</span>
              <motion.a
                href="/logout"
                className="btn btn-outline"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                Logout
              </motion.a>
            </>
          ) : (
            <>
              <motion.a
                href="/create/login/"
                className="btn btn-text"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                Sign in
              </motion.a>
              <motion.a
                href="/create/"
                className="btn btn-primary"
                whileHover={{ scale: 1.05, boxShadow: '0 10px 30px rgba(6, 182, 212, 0.3)' }}
                whileTap={{ scale: 0.95 }}
              >
                Sign up
              </motion.a>
            </>
          )}
        </div>
      </div>
    </motion.header>
  );
}

export default Navigation;
