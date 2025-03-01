import React from 'react';
import '../styles/About.css';

function About() {
  return (
    <div className="about">
      <h1>About New Rose Society</h1>
      
      <div className="about-content">
        <section>
          <h2>Our Story</h2>
          <p>The New Rose Society was founded with a vision to create a community that celebrates innovation and beauty.</p>
          <p>Our organization brings together people from diverse backgrounds to collaborate on projects that inspire and transform.</p>
        </section>
        
        <section>
          <h2>What We Do</h2>
          <p>We focus on projects that combine technology, art, and social impact to create meaningful change.</p>
          <p>Through our initiatives, we aim to educate, inspire, and build a better future for all.</p>
        </section>
      </div>
    </div>
  );
}

export default About;
