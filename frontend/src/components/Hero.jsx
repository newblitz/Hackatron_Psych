import { motion } from 'framer-motion';
import { ArrowRight, CheckCircle } from 'lucide-react';
import '../styles/Hero.css';

function Hero() {
  return (
    <section className="hero">
      <div className="hero-gradient" />

      <div className="container">
        <div className="hero-content">
          <motion.div
            className="hero-text"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <h1 className="hero-title">
              Your Mental Wellness,
              <br />
              Our Priority
            </h1>
            <p className="hero-description">
              Connect with licensed therapists and counselors who understand your journey.
              Start your path to better mental health today.
            </p>
            <div className="hero-buttons">
              <motion.a
                href="/appointment"
                className="btn btn-primary"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                Book a Session
                <ArrowRight size={20} />
              </motion.a>
              <motion.a
                href="/know_more"
                className="btn btn-light"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                Learn More
              </motion.a>
            </div>
            <div className="hero-features">
              <div className="feature-item">
                <CheckCircle size={20} />
                <span>Licensed Professionals</span>
              </div>
              <div className="feature-item">
                <CheckCircle size={20} />
                <span>100% Confidential</span>
              </div>
              <div className="feature-item">
                <CheckCircle size={20} />
                <span>Available 24/7</span>
              </div>
            </div>
          </motion.div>

          <motion.div
            className="hero-visual"
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 1, delay: 0.2 }}
          >
            <div className="visual-card card-main">
              <div className="card-header">
                <div className="avatar-group">
                  <div className="avatar">👨‍⚕️</div>
                  <div className="avatar">👩‍⚕️</div>
                  <div className="avatar">🧑‍⚕️</div>
                </div>
                <span className="status-badge">Online Now</span>
              </div>
              <div className="card-body">
                <h3>Connect with Experts</h3>
                <p>Choose from 500+ licensed therapists ready to help you today</p>
                <div className="rating">
                  <span className="stars">⭐⭐⭐⭐⭐</span>
                  <span className="rating-text">4.9/5 from 10,000+ clients</span>
                </div>
              </div>
            </div>

            <motion.div
              className="visual-card card-floating card-1"
              animate={{
                y: [0, -15, 0],
              }}
              transition={{
                duration: 4,
                repeat: Infinity,
                ease: "easeInOut"
              }}
            >
              <div className="mini-stat">
                <div className="stat-number">98%</div>
                <div className="stat-label">Success Rate</div>
              </div>
            </motion.div>

            <motion.div
              className="visual-card card-floating card-2"
              animate={{
                y: [0, -20, 0],
              }}
              transition={{
                duration: 5,
                repeat: Infinity,
                ease: "easeInOut",
                delay: 1
              }}
            >
              <div className="mini-stat">
                <div className="stat-icon">🏆</div>
                <div className="stat-text">Top Rated</div>
              </div>
            </motion.div>

            <motion.div
              className="visual-card card-floating card-3"
              animate={{
                y: [0, -12, 0],
              }}
              transition={{
                duration: 3.5,
                repeat: Infinity,
                ease: "easeInOut",
                delay: 0.5
              }}
            >
              <div className="mini-stat">
                <div className="stat-icon">💬</div>
                <div className="stat-text">Chat Support</div>
              </div>
            </motion.div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}

export default Hero;
