import { motion } from 'framer-motion';
import { Brain, Clock, Shield, Users, Video, Award } from 'lucide-react';
import '../styles/Features.css';

function Features() {
  const features = [
    {
      icon: Brain,
      title: 'Expert Therapists',
      description: 'Our licensed professionals bring years of experience to help you overcome challenges.',
      color: '#06b6d4',
    },
    {
      icon: Clock,
      title: 'Flexible Scheduling',
      description: 'Choose from in-person or virtual sessions at times that work best for you.',
      color: '#7c3aed',
    },
    {
      icon: Shield,
      title: 'Confidential & Safe',
      description: 'Your privacy is our priority with secure and confidential counseling sessions.',
      color: '#06b6d4',
    },
    {
      icon: Video,
      title: 'Virtual Sessions',
      description: 'Connect with therapists from anywhere through secure video calls.',
      color: '#7c3aed',
    },
    {
      icon: Users,
      title: 'Personalized Care',
      description: 'Tailored treatment plans designed specifically for your unique needs.',
      color: '#06b6d4',
    },
    {
      icon: Award,
      title: 'Proven Results',
      description: 'Evidence-based approaches that have helped thousands achieve their goals.',
      color: '#7c3aed',
    },
  ];

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
      },
    },
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 50 },
    visible: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.6,
        ease: 'easeOut',
      },
    },
  };

  return (
    <section className="features">
      <div className="features-container">
        <motion.div
          className="features-header"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <h2 className="features-title">Everything You Need for Mental Wellness</h2>
          <p className="features-subtitle">
            Comprehensive support designed to help you thrive
          </p>
        </motion.div>

        <motion.div
          className="features-grid"
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '-100px' }}
        >
          {features.map((feature, index) => (
            <motion.div
              key={index}
              className="feature-card"
              variants={itemVariants}
              whileHover={{
                y: -10,
                boxShadow: '0 20px 40px rgba(0, 0, 0, 0.1)',
              }}
              transition={{ duration: 0.3 }}
            >
              <motion.div
                className="feature-icon-wrapper"
                style={{ backgroundColor: `${feature.color}15` }}
                whileHover={{ scale: 1.1, rotate: 5 }}
                transition={{ duration: 0.3 }}
              >
                <feature.icon
                  size={32}
                  color={feature.color}
                  strokeWidth={2}
                />
              </motion.div>
              <h3 className="feature-title">{feature.title}</h3>
              <p className="feature-description">{feature.description}</p>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  );
}

export default Features;
