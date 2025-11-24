import { motion } from 'framer-motion';
import { ArrowRight, Sparkles } from 'lucide-react';
import '../styles/Hero.css';

function Hero() {
  const floatingAnimation = {
    y: [0, -20, 0],
    transition: {
      duration: 3,
      repeat: Infinity,
      ease: 'easeInOut',
    },
  };

  const shimmerAnimation = {
    backgroundPosition: ['0% 50%', '100% 50%', '0% 50%'],
    transition: {
      duration: 5,
      repeat: Infinity,
      ease: 'linear',
    },
  };

  return (
    <section className="hero">
      <div className="hero-background">
        <motion.div
          className="gradient-orb orb-1"
          animate={{
            scale: [1, 1.2, 1],
            opacity: [0.3, 0.5, 0.3],
          }}
          transition={{
            duration: 8,
            repeat: Infinity,
            ease: 'easeInOut',
          }}
        />
        <motion.div
          className="gradient-orb orb-2"
          animate={{
            scale: [1, 1.3, 1],
            opacity: [0.2, 0.4, 0.2],
          }}
          transition={{
            duration: 10,
            repeat: Infinity,
            ease: 'easeInOut',
            delay: 1,
          }}
        />
      </div>

      <div className="hero-content">
        <motion.div
          className="hero-badge"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <Sparkles size={16} />
          <span>Professional Mental Health Support</span>
        </motion.div>

        <motion.h1
          className="hero-title"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
        >
          Begin Your Journey to{' '}
          <motion.span
            className="gradient-text"
            animate={shimmerAnimation}
          >
            Inner Peace
          </motion.span>
        </motion.h1>

        <motion.p
          className="hero-description"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.4 }}
        >
          Professional counseling to help you navigate life's challenges with confidence
          and clarity. Book a consultation in minutes.
        </motion.p>

        <motion.div
          className="hero-actions"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.6 }}
        >
          <motion.a
            href="/appointment"
            className="btn btn-large btn-primary"
            whileHover={{
              scale: 1.05,
              boxShadow: '0 20px 40px rgba(6, 182, 212, 0.4)',
            }}
            whileTap={{ scale: 0.95 }}
          >
            Book Consultation
            <ArrowRight size={20} />
          </motion.a>

          <motion.a
            href="/know_more"
            className="btn btn-large btn-outline"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            Learn More
          </motion.a>
        </motion.div>

        <motion.div
          className="hero-stats"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1, delay: 0.8 }}
        >
          <div className="stat-item">
            <motion.span
              className="stat-number"
              initial={{ opacity: 0, scale: 0.5 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5, delay: 1 }}
            >
              500+
            </motion.span>
            <span className="stat-label">Clients Helped</span>
          </div>
          <div className="stat-divider" />
          <div className="stat-item">
            <motion.span
              className="stat-number"
              initial={{ opacity: 0, scale: 0.5 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5, delay: 1.1 }}
            >
              50+
            </motion.span>
            <span className="stat-label">Expert Therapists</span>
          </div>
          <div className="stat-divider" />
          <div className="stat-item">
            <motion.span
              className="stat-number"
              initial={{ opacity: 0, scale: 0.5 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5, delay: 1.2 }}
            >
              4.9/5
            </motion.span>
            <span className="stat-label">Average Rating</span>
          </div>
        </motion.div>
      </div>

      <motion.div
        className="hero-image"
        initial={{ opacity: 0, x: 100 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 1, delay: 0.4 }}
      >
        <motion.div className="floating-card card-1" animate={floatingAnimation}>
          <div className="card-icon">💙</div>
          <div className="card-text">Mental Wellness</div>
        </motion.div>
        <motion.div
          className="floating-card card-2"
          animate={{
            ...floatingAnimation,
            transition: { ...floatingAnimation.transition, delay: 0.5 },
          }}
        >
          <div className="card-icon">🌟</div>
          <div className="card-text">Personal Growth</div>
        </motion.div>
        <motion.div
          className="floating-card card-3"
          animate={{
            ...floatingAnimation,
            transition: { ...floatingAnimation.transition, delay: 1 },
          }}
        >
          <div className="card-icon">🎯</div>
          <div className="card-text">Goal Achievement</div>
        </motion.div>
      </motion.div>
    </section>
  );
}

export default Hero;
