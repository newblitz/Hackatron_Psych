import { motion } from 'framer-motion';
import { Video, MessageCircle, Calendar, Lock, Users, TrendingUp } from 'lucide-react';
import '../styles/Features.css';

function Features() {
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
    <section className="section features">
      <div className="container">
        <h2 className="section-title">Everything You Need for Better Mental Health</h2>
        <p className="section-subtitle">
          Professional support designed to help you thrive
        </p>

        <div className="features-grid">
          {features.map((feature, index) => (
            <motion.div
              key={index}
              className="feature-card"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              <div className="feature-icon">
                <feature.icon size={28} strokeWidth={2} />
              </div>
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
