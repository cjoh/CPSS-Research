#!/usr/bin/env python3
"""
Script to add Professional Practice Guidelines to all state pages
"""

import os
from pathlib import Path

# State regulation tiers
HIGHLY_REGULATED = [
    'connecticut', 'florida', 'georgia', 'louisiana', 'massachusetts',
    'michigan', 'new_jersey', 'new_york', 'pennsylvania', 'tennessee',
    'texas', 'vermont', 'virginia', 'washington'
]

MODERATELY_REGULATED = [
    'arizona', 'arkansas', 'california', 'colorado', 'illinois', 'iowa',
    'kansas', 'maryland', 'minnesota', 'missouri', 'nevada', 'new_hampshire',
    'new_mexico', 'north_carolina', 'ohio', 'oklahoma', 'oregon', 'rhode_island',
    'south_carolina', 'utah', 'wisconsin'
]

UNREGULATED = [
    'alabama', 'alaska', 'delaware', 'district_of_columbia', 'hawaii', 'idaho',
    'indiana', 'kentucky', 'maine', 'mississippi', 'montana', 'nebraska',
    'north_dakota', 'south_dakota', 'west_virginia', 'wyoming'
]

def get_state_name(state_dir):
    """Convert directory name to display name"""
    name = state_dir.replace('_', ' ').title()
    if name == 'District Of Columbia':
        return 'District of Columbia'
    return name

def create_professional_guidelines_section(state_dir):
    """Create the professional practice guidelines HTML section"""
    state_name = get_state_name(state_dir)

    # Determine regulation level
    if state_dir in HIGHLY_REGULATED:
        regulation_note = f"{state_name} has specific certification requirements for peer support and recovery professionals. Compliance with state regulations is mandatory."
    elif state_dir in MODERATELY_REGULATED:
        regulation_note = f"{state_name} offers voluntary certifications for recovery professionals. Following ethical guidelines is essential even when not legally required."
    else:
        regulation_note = f"{state_name} has minimal specific regulations for recovery professionals. Ethical self-regulation and professional standards are critical."

    section = f'''
    <h2>Professional Practice Guidelines for {state_name}</h2>
    <div class="highlight-box">
        <p><strong>Regulation Level:</strong> {regulation_note}</p>
        <p style="margin-top: 15px;"><strong>Important:</strong> These guidelines apply to Recovery Coaches, Life Coaches, Interventionists, and Case Managers practicing in {state_name}.</p>
    </div>

    <h3>Recovery Coaches & Peer Support Specialists</h3>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
        <div style="background-color: #d4edda; padding: 20px; border-radius: 5px; border-left: 4px solid #28a745;">
            <h4 style="font-family: 'Roboto', sans-serif; font-size: 12pt; text-transform: uppercase; color: #155724; margin: 0 0 15px 0; font-weight: 700;">✓ DO:</h4>
            <ul class="requirements-list">
                <li>Ensure all clients have concurrent licensed clinical support</li>
                <li>Maintain clear boundaries between peer support and therapy</li>
                <li>Use coaching/peer support language, not clinical terminology</li>
                <li>Obtain professional liability insurance</li>
                <li>Provide written coaching agreements defining scope</li>
                <li>Make referrals when clients need clinical intervention</li>
                <li>Pursue relevant certifications (CRSS, CPS, CPRS)</li>
                <li>Share lived experience appropriately and helpfully</li>
                <li>Maintain continuing education in recovery support</li>
                <li>Build referral network with licensed professionals</li>
            </ul>
        </div>
        <div style="background-color: #f8d7da; padding: 20px; border-radius: 5px; border-left: 4px solid #dc3545;">
            <h4 style="font-family: 'Roboto', sans-serif; font-size: 12pt; text-transform: uppercase; color: #721c24; margin: 0 0 15px 0; font-weight: 700;">✗ DON'T:</h4>
            <ul class="requirements-list">
                <li>Diagnose mental health or substance use disorders</li>
                <li>Provide therapy or clinical treatment</li>
                <li>Replace clinical care with coaching alone</li>
                <li>Work with actively using clients without medical oversight</li>
                <li>Use language that implies you're providing therapy</li>
                <li>Practice without professional liability insurance</li>
                <li>Work outside your scope of competence</li>
                <li>Handle psychiatric crises without referring to professionals</li>
                <li>Misrepresent your credentials or training</li>
                <li>Engage in dual relationships with clients</li>
            </ul>
        </div>
    </div>

    <h3>Life Coaches Working with Recovery Clients</h3>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
        <div style="background-color: #d4edda; padding: 20px; border-radius: 5px; border-left: 4px solid #28a745;">
            <h4 style="font-family: 'Roboto', sans-serif; font-size: 12pt; text-transform: uppercase; color: #155724; margin: 0 0 15px 0; font-weight: 700;">✓ DO:</h4>
            <ul class="requirements-list">
                <li>Require clients to have therapist/addiction counselor</li>
                <li>Focus on goal-setting and forward-looking coaching</li>
                <li>Stay in life coaching scope (career, relationships, wellness)</li>
                <li>Make immediate referrals for clinical issues</li>
                <li>Use clear coaching contracts specifying you're not providing therapy</li>
                <li>Maintain professional liability insurance</li>
                <li>Build strong referral network of licensed professionals</li>
                <li>Understand the line between coaching and counseling</li>
                <li>Document referrals and scope boundaries</li>
                <li>Consider ICF or other coaching certification</li>
            </ul>
        </div>
        <div style="background-color: #f8d7da; padding: 20px; border-radius: 5px; border-left: 4px solid #dc3545;">
            <h4 style="font-family: 'Roboto', sans-serif; font-size: 12pt; text-transform: uppercase; color: #721c24; margin: 0 0 15px 0; font-weight: 700;">✗ DON'T:</h4>
            <ul class="requirements-list">
                <li>Coach clients in active addiction without clinical support</li>
                <li>Address trauma or clinical issues in coaching sessions</li>
                <li>Diagnose or treat mental health conditions</li>
                <li>Position coaching as alternative to therapy</li>
                <li>Work with clients in psychiatric crisis</li>
                <li>Use therapeutic techniques requiring clinical license</li>
                <li>Coach clients who refuse to see licensed professionals</li>
                <li>Guarantee recovery outcomes</li>
                <li>Practice addiction counseling without license</li>
                <li>Cross boundaries into clinical territory</li>
            </ul>
        </div>
    </div>

    <h3>Professional Interventionists</h3>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
        <div style="background-color: #d4edda; padding: 20px; border-radius: 5px; border-left: 4px solid #28a745;">
            <h4 style="font-family: 'Roboto', sans-serif; font-size: 12pt; text-transform: uppercase; color: #155724; margin: 0 0 15px 0; font-weight: 700;">✓ DO:</h4>
            <ul class="requirements-list">
                <li>Pursue professional certification (CIP, BRI, CAI)</li>
                <li>Complete comprehensive intervention training (100+ hours)</li>
                <li>Obtain professional liability insurance (essential)</li>
                <li>Use evidence-based intervention models</li>
                <li>Provide clear service agreements to families</li>
                <li>Maintain referral relationships with treatment centers</li>
                <li>Practice family-centered, compassionate intervention</li>
                <li>Stay current on intervention best practices</li>
                <li>Document all intervention services thoroughly</li>
                <li>Follow ethical guidelines and professional standards</li>
            </ul>
        </div>
        <div style="background-color: #f8d7da; padding: 20px; border-radius: 5px; border-left: 4px solid #dc3545;">
            <h4 style="font-family: 'Roboto', sans-serif; font-size: 12pt; text-transform: uppercase; color: #721c24; margin: 0 0 15px 0; font-weight: 700;">✗ DON'T:</h4>
            <ul class="requirements-list">
                <li>Diagnose substance use or mental health disorders</li>
                <li>Provide clinical treatment or therapy</li>
                <li>Practice without professional liability insurance</li>
                <li>Use coercive or overly confrontational tactics</li>
                <li>Guarantee intervention outcomes to families</li>
                <li>Work without proper training in intervention models</li>
                <li>Misrepresent your credentials or success rates</li>
                <li>Engage in unethical referral arrangements</li>
                <li>Practice if you have active addiction issues</li>
                <li>Cross professional boundaries with clients</li>
            </ul>
        </div>
    </div>

    <h3>Case Managers</h3>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
        <div style="background-color: #d4edda; padding: 20px; border-radius: 5px; border-left: 4px solid #28a745;">
            <h4 style="font-family: 'Roboto', sans-serif; font-size: 12pt; text-transform: uppercase; color: #155724; margin: 0 0 15px 0; font-weight: 700;">✓ DO:</h4>
            <ul class="requirements-list">
                <li>Obtain underlying professional license (RN, LCSW, LPC, etc.)</li>
                <li>Pursue CCM or equivalent certification</li>
                <li>Maintain professional liability insurance</li>
                <li>Work within your professional scope of practice</li>
                <li>Coordinate care across all providers effectively</li>
                <li>Document all case management activities thoroughly</li>
                <li>Follow HIPAA and confidentiality requirements</li>
                <li>Advocate appropriately for client needs</li>
                <li>Complete continuing education requirements</li>
                <li>Join professional associations (CMSA, NASW, etc.)</li>
            </ul>
        </div>
        <div style="background-color: #f8d7da; padding: 20px; border-radius: 5px; border-left: 4px solid #dc3545;">
            <h4 style="font-family: 'Roboto', sans-serif; font-size: 12pt; text-transform: uppercase; color: #721c24; margin: 0 0 15px 0; font-weight: 700;">✗ DON'T:</h4>
            <ul class="requirements-list">
                <li>Practice without appropriate underlying license</li>
                <li>Provide clinical services outside your scope</li>
                <li>Diagnose conditions without proper credentials</li>
                <li>Bill for services without proper certification</li>
                <li>Practice across state lines without proper licensure</li>
                <li>Violate client confidentiality or HIPAA</li>
                <li>Accept inappropriate incentives from providers</li>
                <li>Misrepresent credentials or certifications</li>
                <li>Guarantee specific outcomes to clients</li>
                <li>Engage in dual relationships with clients</li>
            </ul>
        </div>
    </div>

    <div class="contact-box">
        <h3>Additional Resources</h3>
        <ul class="requirements-list">
            <li><a href="../recovery-coaching-guide.html">Recovery Coaching Ethical Practice Guide</a></li>
            <li><a href="../interventionist-guide.html">Professional Interventionist Guide</a></li>
            <li><a href="../case-management-guide.html">Case Management Certification Guide</a></li>
            <li><a href="../LIFE_COACH_RECOVERY_CLIENTS_DOS_DONTS.md">Life Coach Recovery Clients Guide</a></li>
            <li><a href="../index.html">Main CPSS Research Directory</a></li>
        </ul>
    </div>
'''
    return section

def update_state_page(state_dir):
    """Update a single state page with professional guidelines"""
    index_path = Path(f'/home/user/CPSS-Research/{state_dir}/index.html')

    if not index_path.exists():
        print(f"Skipping {state_dir} - no index.html found")
        return False

    # Read the file
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already updated
    if 'Professional Practice Guidelines' in content:
        print(f"Skipping {state_dir} - already updated")
        return False

    # Create the new section
    new_section = create_professional_guidelines_section(state_dir)

    # Find the footer and insert before it - try multiple patterns
    footer_patterns = [
        ('</div>\n    <div class="footer">', '</div>\n    <div class="footer">', '{}\n    </div>\n    <div class="footer">'),
        ('<div class="footer">', '<div class="footer">', '{}\n    <div class="footer">'),
        ('</div>\n        <footer>', '</div>\n        <footer>', '{}\n        </div>\n        <footer>'),
        ('</div>\n\n    <footer class="footer">', '</div>\n\n    <footer class="footer">', '{}\n    </div>\n\n    <footer class="footer">'),
        ('<footer class="footer">', '<footer class="footer">', '{}\n\n    <footer class="footer">'),
        ('<footer>', '<footer>', '{}\n        <footer>'),
    ]

    updated = False
    for pattern_name, search_pattern, replace_template in footer_patterns:
        if search_pattern in content:
            content = content.replace(
                search_pattern,
                replace_template.format(new_section),
                1  # Only replace first occurrence
            )
            updated = True
            break

    if not updated:
        print(f"Warning: Could not find footer in {state_dir}")
        return False

    # Write back
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Updated {state_dir}")
    return True

def main():
    """Main function to update all state pages"""
    all_states = HIGHLY_REGULATED + MODERATELY_REGULATED + UNREGULATED

    print(f"Updating {len(all_states)} state pages...")
    print()

    updated_count = 0
    for state_dir in sorted(all_states):
        if update_state_page(state_dir):
            updated_count += 1

    print()
    print(f"Completed! Updated {updated_count} state pages.")

if __name__ == '__main__':
    main()
