#!/usr/bin/env python3

import os

# Base HTML template - uses double braces for CSS
html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{state_name} - Recovery Coaching Legal Information</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Roboto', sans-serif; font-size: 11pt; color: #333333; line-height: 1.6; background: #f5f5f5; }}
        h1 {{ font-family: 'Bebas Neue', sans-serif; font-size: 20pt; font-weight: 300; color: #1d4486; margin-bottom: 20px; }}
        h2 {{ font-family: 'Bebas Neue', sans-serif; font-size: 16pt; font-weight: 300; color: #1d4486; margin: 30px 0 15px 0; }}
        h3 {{ font-family: 'Bebas Neue', sans-serif; font-size: 14pt; font-weight: 300; color: #1d4486; margin: 20px 0 10px 0; }}
        h4 {{ font-family: 'Roboto', sans-serif; font-size: 12pt; text-transform: uppercase; color: #1d4486; margin: 15px 0 10px 0; font-weight: 700; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; }}
        header {{ background: #1d4486; color: white; padding: 40px; text-align: center; }}
        header h1 {{ color: white; margin: 0; }}
        .nav {{ background: #f8f9fa; padding: 15px 40px; border-bottom: 2px solid #1d4486; }}
        .nav a {{ color: #1d4486; text-decoration: none; font-weight: 700; margin-right: 20px; }}
        .content {{ padding: 40px; }}
        .warning-box {{ background: #fff3cd; border-left: 4px solid #ffc107; padding: 20px; margin: 20px 0; }}
        .legal-box {{ background: #1d4486; color: white; padding: 20px; border-radius: 8px; margin: 20px 0; }}
        .info-box {{ background: #f8f9fa; border-left: 4px solid #1d4486; padding: 20px; margin: 20px 0; }}
        .prohibited-box {{ background: #f8d7da; border-left: 4px solid #dc3545; padding: 20px; margin: 20px 0; }}
        .allowed-box {{ background: #d4edda; border-left: 4px solid #28a745; padding: 20px; margin: 20px 0; }}
        ul, ol {{ margin-left: 20px; margin-bottom: 15px; }}
        li {{ margin-bottom: 8px; }}
        footer {{ background: #f8f9fa; padding: 30px 40px; text-align: center; border-top: 2px solid #1d4486; font-size: 10pt; }}
        @media (max-width: 768px) {{ .content {{ padding: 20px; }} header {{ padding: 20px; }} }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{state_name} Recovery Coaching Legal Information</h1>
            <p>Research Date: January 5, 2025</p>
        </header>

        <nav class="nav">
            <a href="../index.html">← Back to State Index</a>
            <a href="peer_support_certification.html">Peer Support Certification →</a>
        </nav>

        <div class="content">
            {status_box}
            {content}
        </div>

        <footer>
            <p><strong>Legal Disclaimer:</strong> This information is for educational purposes only and does not constitute legal advice. Laws and regulations change frequently. Always consult with a licensed attorney in your state for specific legal guidance regarding recovery coaching practice.</p>
            <p>Last Updated: January 5, 2025</p>
        </footer>
    </div>
</body>
</html>'''

# Simplified state data
states_data = {
    "connecticut": {
        "name": "Connecticut",
        "status_class": "info-box",
        "status": "Certification required for employment",
        "independent": "Must verify Connecticut-specific requirements",
        "cert": "RSS (80-hour), PRC (CCAR 30-hour)"
    },
    "delaware": {
        "name": "Delaware",
        "status_class": "info-box",
        "status": "Certification required",
        "independent": "Not explicitly addressed",
        "cert": "Certified Peer Recovery Specialist (CPRS)"
    },
    "florida": {
        "name": "Florida",
        "status_class": "prohibited-box",
        "status": "MUST WORK IN LICENSED SETTINGS WITH SUPERVISION",
        "independent": "NO - Must work at licensed behavioral health organization",
        "cert": "CRSS (Recovery Support Specialist), CRPS (Recovery Peer Specialist)"
    },
    "georgia": {
        "name": "Georgia",
        "status_class": "allowed-box",
        "status": "Certification available; legal scope of practice for certain credentials",
        "independent": "Possible with proper credentials",
        "cert": "Peer Recovery Coach; CADC credentials grant legal scope"
    },
    "hawaii": {
        "name": "Hawaii",
        "status_class": "prohibited-box",
        "status": "CANNOT PRACTICE INDEPENDENTLY",
        "independent": "NO - Must work under mental health professional supervision",
        "cert": "Hawaii Certified Peer Specialist (HCPS)"
    },
    "idaho": {
        "name": "Idaho",
        "status_class": "info-box",
        "status": "Certification required",
        "independent": "Not explicitly addressed",
        "cert": "Recovery Coach through IBADCC"
    },
    "illinois": {
        "name": "Illinois",
        "status_class": "info-box",
        "status": "Certification available",
        "independent": "Must avoid regulated professional activities",
        "cert": "CRSS, CPRS"
    },
    "indiana": {
        "name": "Indiana",
        "status_class": "allowed-box",
        "status": "Certification required for certain employment",
        "independent": "State recognition; Medicaid reimbursement available",
        "cert": "CPRC (ICAADA), CPSP (State credential)"
    },
    "iowa": {
        "name": "Iowa",
        "status_class": "prohibited-box",
        "status": "CANNOT PRACTICE INDEPENDENTLY",
        "independent": "NO - Must work within licensed agency with IDPH contract",
        "cert": "Peer Recovery Specialist"
    },
    "kansas": {
        "name": "Kansas",
        "status_class": "info-box",
        "status": "Certification required",
        "independent": "Work within certified clinics",
        "cert": "Kansas Certified Peer Specialist (KCPS)"
    },
    "kentucky": {
        "name": "Kentucky",
        "status_class": "prohibited-box",
        "status": "CANNOT PRACTICE INDEPENDENTLY",
        "independent": "NO - Must work under supervision of licensed professional",
        "cert": "Adult/Family/Youth Peer Support Specialist"
    },
    "louisiana": {
        "name": "Louisiana",
        "status_class": "info-box",
        "status": "Certification required for employment",
        "independent": "Not explicitly addressed",
        "cert": "Peer Support Specialist"
    },
    "maine": {
        "name": "Maine",
        "status_class": "allowed-box",
        "status": "Certification available",
        "independent": "Both volunteer and paid opportunities",
        "cert": "Certified Peer Recovery Coach (CPRC)"
    },
    "maryland": {
        "name": "Maryland",
        "status_class": "allowed-box",
        "status": "EXEMPT from licensing requirements",
        "independent": "YES - Exempt under COMAR 10.63",
        "cert": "Certified Peer Recovery Specialist (CPRS)"
    },
    "massachusetts": {
        "name": "Massachusetts",
        "status_class": "warning-box",
        "status": "NEW LICENSURE REQUIREMENT - Effective March 23, 2025",
        "independent": "To be determined by new Board of Registration",
        "cert": "Regulations pending (2025-2026)"
    },
    "michigan": {
        "name": "Michigan",
        "status_class": "info-box",
        "status": "Certification required",
        "independent": "Work as part of clinical team",
        "cert": "Certified Peer Recovery Mentor (CPRM)"
    },
    "minnesota": {
        "name": "Minnesota",
        "status_class": "info-box",
        "status": "Legally defined in Minnesota Rules",
        "independent": "Certification required",
        "cert": "Certified Peer Recovery Specialist (CPRS)"
    },
    "mississippi": {
        "name": "Mississippi",
        "status_class": "prohibited-box",
        "status": "CANNOT PRACTICE INDEPENDENTLY - STRICTEST REQUIREMENT",
        "independent": "NO - Employment in state mental health system MANDATORY",
        "cert": "Certified Peer Support Specialist Professional (CPSSP)"
    },
    "missouri": {
        "name": "Missouri",
        "status_class": "info-box",
        "status": "Defined in regulations",
        "independent": "Must work through recovery support programs",
        "cert": "CPS, CRPR, MRSS (three credential types)"
    },
    "montana": {
        "name": "Montana",
        "status_class": "prohibited-box",
        "status": "LICENSURE REQUIRED BY STATUTE",
        "independent": "NO - Cannot practice without license and supervision",
        "cert": "Certified Behavioral Health Peer Support Specialist (CBHPSS)"
    }
}

# Generate HTML files
created_count = 0
for state_dir, data in states_data.items():
    filepath = f"{state_dir}/recovery_coaching.html"
    
    if os.path.exists(filepath):
        print(f"Skipping {data['name']} - already exists")
        continue
    
    # Build status box
    status_box = f'''<div class="{data['status_class']}">
                <h2>Legal Status Overview</h2>
                <p><strong>Status:</strong> {data['status']}</p>
                <p><strong>Independent Practice:</strong> {data['independent']}</p>
                <p><strong>Certification:</strong> {data['cert']}</p>
            </div>'''
    
    # Build simplified content
    content = f'''
            <h2>Summary</h2>
            <div class="info-box">
                <p>For detailed legal information, please refer to the original research document at:</p>
                <p><code>{state_dir}/recovery_coaching_legal.md</code></p>
            </div>

            <h3>Key Points</h3>
            <ul>
                <li>Status: {data['status']}</li>
                <li>Independent Practice: {data['independent']}</li>
                <li>Certification: {data['cert']}</li>
            </ul>

            <h3>Additional Resources</h3>
            <p>Please see the detailed markdown file for complete legal citations, requirements, and contact information.</p>'''
    
    # Generate HTML
    html = html_template.format(
        state_name=data['name'],
        status_box=status_box,
        content=content
    )
    
    # Write file
    with open(filepath, 'w') as f:
        f.write(html)
    
    created_count += 1
    print(f"Created: {data['name']}")

print(f"\nTotal files created: {created_count}")

