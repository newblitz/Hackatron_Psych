import { motion } from 'framer-motion';
import { ArrowRight } from 'lucide-react';
import '../styles/Benefits.css';

function Benefits() {
  return (
    <section className="section benefits">
      <div className="container">
        <h2 className="section-title">Ready to Start Your Journey?</h2>
        <p className="section-subtitle">
          Join thousands who have transformed their mental health with MindEase
        </p>
        <motion.div
          style={{ textAlign: 'center' }}
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
        >
          <a href="/appointment" className="btn btn-primary">
            Book Your First Session
            <ArrowRight size={20} />
          </a>
        </motion.div>
      </div>
    </section>
  );
}

export default Benefits;
