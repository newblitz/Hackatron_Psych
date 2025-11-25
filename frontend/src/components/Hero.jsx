import { motion, useScroll, useTransform } from 'framer-motion';
import { ArrowRight, Heart, Sparkles, Shield } from 'lucide-react';
import { useRef } from 'react';
import '../styles/Hero.css';

function Hero() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ['start start', 'end start'],
  });

  const y = useTransform(scrollYProgress, [0, 1], ['0%', '30%']);
  const opacity = useTransform(scrollYProgress, [0, 0.5], [1, 0]);

  return (
    <section ref={ref} className="hero">
      <div className="hero-background">
        <motion.div
          className="blob blob-1"
          style={{ y }}
          animate={{
            scale: [1, 1.2, 1],
            rotate: [0, 90, 0],
          }}
          transition={{
            duration: 20,
            repeat: Infinity,
            ease: "easeInOut"
          }}
        />
        <motion.div
          className="blob blob-2"
          animate={{
            scale: [1, 1.1, 1],
            rotate: [0, -90, 0],
          }}
          transition={{
            duration: 15,
            repeat: Infinity,
            ease: "easeInOut",
            delay: 2
          }}
        />
        <motion.div
          className="blob blob-3"
          animate={{
            scale: [1, 1.15, 1],
            rotate: [0, 45, 0],
          }}
          transition={{
            duration: 25,
            repeat: Infinity,
            ease: "easeInOut",
            delay: 5
          }}
        />
      </div>

      <div className="hero-container">
        <motion.div
          className="hero-content"
          style={{ opacity }}
        >
          <motion.div
            className="hero-badge"
            initial={{ opacity: 0, scale: 0.8, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            transition={{ duration: 0.6, type: "spring", bounce: 0.5 }}
          >
            <Sparkles size={16} />
            <span>Your Safe Space for Mental Wellness</span>
          </motion.div>

          <motion.h1
            className="hero-title"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            Find peace, one
            <br />
            <span className="gradient-text">conversation</span> at a time
          </motion.h1>

          <motion.p
            className="hero-description"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            Connect with compassionate therapists who truly understand you.
            Start your journey to a healthier, happier you today.
          </motion.p>

          <motion.div
            className="hero-actions"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.6 }}
          >
            <motion.a
              href="/appointment"
              className="btn btn-primary"
              whileHover={{ scale: 1.05, y: -2 }}
              whileTap={{ scale: 0.95 }}
            >
              Start Free Session
              <ArrowRight size={20} />
            </motion.a>

            <motion.a
              href="/know_more"
              className="btn btn-ghost"
              whileHover={{ scale: 1.05, y: -2 }}
              whileTap={{ scale: 0.95 }}
            >
              How It Works
            </motion.a>
          </motion.div>

          <motion.div
            className="hero-stats"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 1, delay: 0.8 }}
          >
            <div className="stat-item">
              <Heart size={20} className="stat-icon" />
              <div>
                <div className="stat-value">10,000+</div>
                <div className="stat-label">Lives Changed</div>
              </div>
            </div>
            <div className="stat-divider" />
            <div className="stat-item">
              <Sparkles size={20} className="stat-icon" />
              <div>
                <div className="stat-value">4.9/5</div>
                <div className="stat-label">Client Rating</div>
              </div>
            </div>
            <div className="stat-divider" />
            <div className="stat-item">
              <Shield size={20} className="stat-icon" />
              <div>
                <div className="stat-value">100%</div>
                <div className="stat-label">Confidential</div>
              </div>
            </div>
          </motion.div>
        </motion.div>

        <motion.div
          className="hero-visual"
          initial={{ opacity: 0, scale: 0.8, x: 50 }}
          animate={{ opacity: 1, scale: 1, x: 0 }}
          transition={{ duration: 1, delay: 0.3 }}
        >
          <div className="illustration-container">
            <motion.div
              className="glass-card main-card"
              animate={{
                y: [0, -15, 0],
              }}
              transition={{
                duration: 6,
                repeat: Infinity,
                ease: "easeInOut"
              }}
            >
              <div className="card-icon-wrapper">
                <div className="meditation-icon">🧘‍♀️</div>
              </div>
              <h3>Begin Your Journey</h3>
              <p>Personalized care from licensed professionals</p>
              <div className="progress-bar">
                <motion.div
                  className="progress-fill"
                  initial={{ width: 0 }}
                  animate={{ width: "80%" }}
                  transition={{ duration: 2, delay: 1 }}
                />
              </div>
              <div className="card-footer">
                <span className="progress-text">80% Complete</span>
                <span className="progress-emoji">✨</span>
              </div>
            </motion.div>

            <motion.div
              className="glass-card floating-card card-1"
              animate={{
                y: [0, -20, 0],
                rotate: [-2, 2, -2],
              }}
              transition={{
                duration: 5,
                repeat: Infinity,
                ease: "easeInOut",
                delay: 0.5
              }}
            >
              <div className="mini-icon">💬</div>
              <div className="mini-text">
                <strong>Chat Anytime</strong>
                <span>24/7 Support</span>
              </div>
            </motion.div>

            <motion.div
              className="glass-card floating-card card-2"
              animate={{
                y: [0, -25, 0],
                rotate: [2, -2, 2],
              }}
              transition={{
                duration: 7,
                repeat: Infinity,
                ease: "easeInOut",
                delay: 1
              }}
            >
              <div className="mini-icon">🎯</div>
              <div className="mini-text">
                <strong>Track Goals</strong>
                <span>See Progress</span>
              </div>
            </motion.div>

            <motion.div
              className="glass-card floating-card card-3"
              animate={{
                y: [0, -18, 0],
                rotate: [-3, 3, -3],
              }}
              transition={{
                duration: 6,
                repeat: Infinity,
                ease: "easeInOut",
                delay: 1.5
              }}
            >
              <div className="mini-icon">🌟</div>
              <div className="mini-text">
                <strong>Feel Better</strong>
                <span>Real Results</span>
              </div>
            </motion.div>

            <motion.div
              className="decoration-circle circle-1"
              animate={{
                scale: [1, 1.2, 1],
                opacity: [0.3, 0.6, 0.3],
              }}
              transition={{
                duration: 4,
                repeat: Infinity,
                ease: "easeInOut"
              }}
            />
            <motion.div
              className="decoration-circle circle-2"
              animate={{
                scale: [1, 1.3, 1],
                opacity: [0.2, 0.5, 0.2],
              }}
              transition={{
                duration: 5,
                repeat: Infinity,
                ease: "easeInOut",
                delay: 1
              }}
            />
          </div>
        </motion.div>
      </div>
    </section>
  );
}

export default Hero;
