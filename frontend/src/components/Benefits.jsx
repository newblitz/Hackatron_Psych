import { motion } from 'framer-motion';
import { Check } from 'lucide-react';
import '../styles/Benefits.css';

function Benefits() {
  const benefits = [
    'Licensed psychologists',
    'Confidential & secure sessions',
    'Flexible scheduling options',
    'Safe & supportive environment',
    'Evidence-based approaches',
    'Ongoing support & guidance',
  ];

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
        delayChildren: 0.3,
      },
    },
  };

  const itemVariants = {
    hidden: { opacity: 0, x: -30 },
    visible: {
      opacity: 1,
      x: 0,
      transition: {
        duration: 0.5,
      },
    },
  };

  return (
    <section className="benefits">
      <div className="benefits-container">
        <motion.div
          className="benefits-content"
          initial={{ opacity: 0, x: -50 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <motion.h2
            className="benefits-title"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            Why Choose <span className="gradient-text">MindEase</span>?
          </motion.h2>

          <motion.p
            className="benefits-description"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            Your journey to better mental health starts here with our comprehensive
            and compassionate care approach.
          </motion.p>

          <motion.div
            className="benefits-list"
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true }}
          >
            {benefits.map((benefit, index) => (
              <motion.div
                key={index}
                className="benefit-item"
                variants={itemVariants}
                whileHover={{ x: 10 }}
              >
                <motion.div
                  className="benefit-icon"
                  whileHover={{ scale: 1.2, rotate: 360 }}
                  transition={{ duration: 0.5 }}
                >
                  <Check size={20} strokeWidth={3} />
                </motion.div>
                <span className="benefit-text">{benefit}</span>
              </motion.div>
            ))}
          </motion.div>

          <motion.div
            className="benefits-cta"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.8 }}
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
              Get Started Today
            </motion.a>
          </motion.div>
        </motion.div>

        <motion.div
          className="benefits-visual"
          initial={{ opacity: 0, scale: 0.8 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <motion.div
            className="visual-circle circle-1"
            animate={{
              scale: [1, 1.1, 1],
              rotate: [0, 180, 360],
            }}
            transition={{
              duration: 20,
              repeat: Infinity,
              ease: 'linear',
            }}
          />
          <motion.div
            className="visual-circle circle-2"
            animate={{
              scale: [1, 1.2, 1],
              rotate: [360, 180, 0],
            }}
            transition={{
              duration: 15,
              repeat: Infinity,
              ease: 'linear',
            }}
          />
          <motion.div
            className="visual-circle circle-3"
            animate={{
              scale: [1, 1.15, 1],
              rotate: [0, -180, -360],
            }}
            transition={{
              duration: 25,
              repeat: Infinity,
              ease: 'linear',
            }}
          />
          <div className="visual-center">
            <motion.div
              className="center-icon"
              animate={{
                y: [0, -10, 0],
              }}
              transition={{
                duration: 3,
                repeat: Infinity,
                ease: 'easeInOut',
              }}
            >
              💚
            </motion.div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}

export default Benefits;
