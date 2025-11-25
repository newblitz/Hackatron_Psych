import { motion, useScroll, useTransform } from 'framer-motion';
import { useRef } from 'react';
import { Video, MessageCircle, Calendar, Lock, Users, TrendingUp } from 'lucide-react';
import '../styles/Features.css';

function Features() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ['start end', 'end start'],
  });

  const y = useTransform(scrollYProgress, [0, 1], [100, -100]);

  const features = [
    {
      icon: Video,
      title: 'Video Sessions',
      description: 'Face-to-face therapy from anywhere with secure video calls',
    },
    {
      icon: MessageCircle,
      title: 'Chat Support',
      description: 'Message your therapist anytime between sessions',
    },
    {
      icon: Calendar,
      title: 'Easy Scheduling',
      description: 'Book appointments that fit your busy schedule',
    },
    {
      icon: Lock,
      title: 'Private & Secure',
      description: 'Your conversations are 100% confidential',
    },
    {
      icon: Users,
      title: 'Expert Therapists',
      description: '500+ licensed professionals ready to help',
    },
    {
      icon: TrendingUp,
      title: 'Track Progress',
      description: 'Monitor your mental health journey with insights',
    },
  ];

  return (
    <section ref={ref} className="section features">
      <motion.div className="features-background" style={{ y }} />

      <div className="container">
        <motion.h2
          className="section-title"
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-100px' }}
          transition={{ duration: 0.6 }}
        >
          Everything You Need for Better Mental Health
        </motion.h2>
        <motion.p
          className="section-subtitle"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-100px' }}
          transition={{ duration: 0.6, delay: 0.1 }}
        >
          Professional support designed to help you thrive
        </motion.p>

        <div className="features-grid">
          {features.map((feature, index) => (
            <motion.div
              key={index}
              className="feature-card"
              initial={{ opacity: 0, y: 60 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '-50px' }}
              transition={{
                duration: 0.5,
                delay: index * 0.1,
                ease: [0.21, 0.45, 0.27, 0.9]
              }}
              whileHover={{
                y: -8,
                transition: { duration: 0.2 }
              }}
            >
              <motion.div
                className="feature-icon"
                whileHover={{ scale: 1.1, rotate: 5 }}
                transition={{ duration: 0.3 }}
              >
                <feature.icon size={28} strokeWidth={2} />
              </motion.div>
              <h3>{feature.title}</h3>
              <p>{feature.description}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Features;
