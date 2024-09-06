import React from 'react';
import './FeatureDashboard.css';

function FeatureDashboard() {
  const features = [
    { title: 'PRD Generation', description: 'Automatically generate PRDs.', icon: 'icon-prd' },
    { title: 'Prototype Drawing Generation', description: 'Generate prototypes.', icon: 'icon-prototype' },
    { title: 'Flow Chart Generation', description: 'Create flow charts.', icon: 'icon-flowchart' },
    { title: 'Sequence Diagram Generation', description: 'Generate sequence diagrams.', icon: 'icon-sequence' },
    { title: 'Page Structure Diagram', description: 'Generate page structure diagrams.', icon: 'icon-page' },
    { title: 'Test Case Generation', description: 'Generate test cases.', icon: 'icon-testcase' },
    { title: 'Data Fields', description: 'Generate data fields.', icon: 'icon-datafields' },
    { title: 'PRD Inspection', description: 'Inspect PRDs for quality.', icon: 'icon-inspection' },
    { title: 'Value Analysis', description: 'Perform value analysis.', icon: 'icon-value' },
    { title: 'SQL Generation', description: 'Generate SQL code.', icon: 'icon-sql' },
    { title: 'Prototype Diagram to Function Description', description: 'Convert prototypes to functions.', icon: 'icon-prototype-function' },
    { title: 'Weekly Report Generation', description: 'Generate weekly reports.', icon: 'icon-weeklyreport' },
  ];

  return (
    <div className="feature-dashboard">
      {features.map((feature, index) => (
        <div key={index} className="feature-card">
          <div className={`feature-icon ${feature.icon}`}></div>
          <h3>{feature.title}</h3>
          <p>{feature.description}</p>
        </div>
      ))}
    </div>
  );
}

export default FeatureDashboard;
