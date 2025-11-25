import { motion, useScroll, useTransform } from 'framer-motion';
import { ArrowRight, CheckCircle } from 'lucide-react';
import { useRef } from 'react';
import spotifySticker from '../assets/spotify_sticker.png';
import '../styles/Hero.css';

function Hero() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ['start start', 'end start'],
  });

  const y = useTransform(scrollYProgress, [0, 1], ['0%', '50%']);
  const opacity = useTransform(scrollYProgress, [0, 0.5], [1, 0]);
  const scale = useTransform(scrollYProgress, [0, 1], [1, 1.1]);

  return (
    <section ref={ref} className="hero">
      <motion.div className="hero-gradient" style={{ scale }} />

      <div className="container">
        <div className="hero-content">
          <motion.div
            className="hero-text"
            style={{ y, opacity }}
          >
            <motion.h1
              className="hero-title"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8 }}
            >
              Your Mental Wellness,
              <br />
              Our Priority
            </motion.h1>
            <motion.p
              className="hero-description"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.2 }}
            >
              Connect with licensed therapists and counselors who understand your journey.
              Start your path to better mental health today.
            </motion.p>
            <motion.div
              className="hero-buttons"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.4 }}
            >
              <motion.a
                href="/appointment"
                className="btn btn-primary"
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
              >
                Book a Session
                <ArrowRight size={20} />
              </motion.a>
              <motion.a
                href="/know_more"
                className="btn btn-light"
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
              >
                Learn More
              </motion.a>
            </motion.div>
            <motion.div
              className="hero-features"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.8, delay: 0.6 }}
            >
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
            </motion.div>
          </motion.div>

          <motion.div
            className="hero-visual"
            style={{ y: useTransform(scrollYProgress, [0, 1], ['0%', '30%']) }}
          >
            <motion.div
              className="visual-card card-main"
              initial={{ opacity: 0, scale: 0.8, rotateY: -15 }}
              animate={{ opacity: 1, scale: 1, rotateY: 0 }}
              transition={{ duration: 1, delay: 0.3 }}
            >
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
            </motion.div>

            <motion.div
              className="floating-image"
              initial={{ opacity: 0, x: 50, rotate: -10 }}
              animate={{ opacity: 1, x: 0, rotate: 0 }}
              transition={{ duration: 1.2, delay: 0.5 }}
              style={{ y: useTransform(scrollYProgress, [0, 1], ['0%', '-20%']) }}
            >
              <img src={spotifySticker} alt="Mental wellness illustration" />
            </motion.div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}

export default Hero;
