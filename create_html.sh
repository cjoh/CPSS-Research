#!/bin/bash

# This script creates HTML files for each state
# Usage: ./create_html.sh

echo "Creating HTML files for all states..."

# Array to track completion
declare -a completed_states

# Function to track state completion
track_state() {
    completed_states+=("$1")
}

# Colorado
cat > Colorado/recovery_coaching.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colorado - Recovery Coaching Legal Information</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Roboto', sans-serif; font-size: 11pt; color: #333333; line-height: 1.6; background: #f5f5f5; }
        h1 { font-family: 'Bebas Neue', sans-serif; font-size: 20pt; font-weight: 300; color: #1d4486; margin-bottom: 20px; }
        h2 { font-family: 'Bebas Neue', sans-serif; font-size: 16pt; font-weight: 300; color: #1d4486; margin: 30px 0 15px 0; }
        h3 { font-family: 'Bebas Neue', sans-serif; font-size: 14pt; font-weight: 300; color: #1d4486; margin: 20px 0 10px 0; }
        h4 { font-family: 'Roboto', sans-serif; font-size: 12pt; text-transform: uppercase; color: #1d4486; margin: 15px 0 10px 0; font-weight: 700; }
        .container { max-width: 1200px; margin: 0 auto; background: white; }
        header { background: #1d4486; color: white; padding: 40px; text-align: center; }
        header h1 { color: white; margin: 0; }
        .nav { background: #f8f9fa; padding: 15px 40px; border-bottom: 2px solid #1d4486; }
        .nav a { color: #1d4486; text-decoration: none; font-weight: 700; margin-right: 20px; }
        .content { padding: 40px; }
        .warning-box { background: #fff3cd; border-left: 4px solid #ffc107; padding: 20px; margin: 20px 0; }
        .legal-box { background: #1d4486; color: white; padding: 20px; border-radius: 8px; margin: 20px 0; }
        .info-box { background: #f8f9fa; border-left: 4px solid #1d4486; padding: 20px; margin: 20px 0; }
        .prohibited-box { background: #f8d7da; border-left: 4px solid #dc3545; padding: 20px; margin: 20px 0; }
        .allowed-box { background: #d4edda; border-left: 4px solid #28a745; padding: 20px; margin: 20px 0; }
        ul, ol { margin-left: 20px; margin-bottom: 15px; }
        li { margin-bottom: 8px; }
        footer { background: #f8f9fa; padding: 30px 40px; text-align: center; border-top: 2px solid #1d4486; font-size: 10pt; }
        @media (max-width: 768px) { .content { padding: 20px; } header { padding: 20px; } }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Colorado Recovery Coaching Legal Information</h1>
            <p>Research Date: January 5, 2025</p>
        </header>

        <nav class="nav">
            <a href="../index.html">← Back to State Index</a>
            <a href="peer_support_certification.html">Peer Support Certification →</a>
        </nav>

        <div class="content">
            <div class="allowed-box">
                <h2>Legal Status Overview</h2>
                <p><strong>Status:</strong> Legally defined in statute</p>
                <p><strong>Independent Practice:</strong> YES currently; Medicaid credentialing required 2026</p>
                <p><strong>Certification:</strong> NOT required currently (changes January 1, 2026)</p>
            </div>

            <h2>Legal Definition</h2>
            <p><strong>Status:</strong> Legally defined in statute</p>
            
            <div class="legal-box">
                <p>C.R.S. § 27-60-108 defines "peer support professional" to include recovery coaches.</p>
                <p><strong>Citation:</strong> Colorado Revised Statutes § 27-60-108 (enacted 2021, HB 21-1021)</p>
            </div>

            <h2>Coaching vs. Therapy Boundaries</h2>
            <p>Peer support professionals help people achieve recovery goals through shared understanding, respect, and empowerment. Distinct from clinical treatment.</p>

            <h2>Independent Practice Requirements</h2>

            <div class="warning-box">
                <h3>IMPORTANT CHANGE - Effective January 1, 2026</h3>
                <p>All Peer Support Professionals delivering Medicaid behavioral health services must be credentialed by nationally recognized organization (by July 1, 2026).</p>
            </div>

            <div class="info-box">
                <h3>Current Requirements (2024-2025)</h3>
                <ul>
                    <li>Combined Core Competencies training (state requirement)</li>
                    <li>COPA (Colorado Providers Association) certification available but not mandatory</li>
                    <li>IC&RC credential provides portability</li>
                </ul>

                <h3>Future Requirements (Starting 2026)</h3>
                <ul>
                    <li>Credentialing required for Medicaid services</li>
                    <li>Must be completed by July 1, 2026</li>
                    <li>Nationally recognized organization credential</li>
                </ul>
            </div>

            <h2>Legal Citations</h2>

            <div class="legal-box">
                <h3>Primary Authority</h3>
                <ul>
                    <li><strong>C.R.S. § 27-60-108</strong> - Peer Support Professional definition</li>
                    <li>HCPF (Health Care Policy & Financing) regulations</li>
                </ul>
            </div>

            <h2>Practical Guidance</h2>

            <div class="info-box">
                <h3>Summary</h3>
                <ul>
                    <li><strong>Legally defined?</strong> YES - in statute</li>
                    <li><strong>Independent practice?</strong> YES currently; Medicaid credentialing required 2026</li>
                    <li><strong>Interventionists different?</strong> No information found</li>
                </ul>
            </div>

            <h3>Additional Resources</h3>
            <ul>
                <li>Colorado Behavioral Health Administration: <a href="http://bha.colorado.gov">bha.colorado.gov</a></li>
            </ul>
        </div>

        <footer>
            <p><strong>Legal Disclaimer:</strong> This information is for educational purposes only and does not constitute legal advice. Laws and regulations change frequently. Always consult with a licensed attorney in your state for specific legal guidance regarding recovery coaching practice.</p>
            <p>Last Updated: January 5, 2025</p>
        </footer>
    </div>
</body>
</html>
EOF

track_state "Colorado"

echo "Created: ${completed_states[@]}"

