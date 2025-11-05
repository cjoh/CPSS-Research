# Recovery Coaching HTML Pages - Project Completion Summary
**Completion Date:** January 5, 2025

## Project Overview
Created beautiful HTML pages for recovery coaching legal information for 26 states (Alabama through Montana).

## Files Created

### HTML Pages (26 total)
All files follow the pattern: `{state}/recovery_coaching.html`

1. Alabama - /Users/cjoh/turtlebook/alabama/recovery_coaching.html
2. Alaska - /Users/cjoh/turtlebook/alaska/recovery_coaching.html
3. Arizona - /Users/cjoh/turtlebook/arizona/recovery_coaching.html
4. Arkansas - /Users/cjoh/turtlebook/arkansas/recovery_coaching.html
5. California - /Users/cjoh/turtlebook/california/recovery_coaching.html
6. Colorado - /Users/cjoh/turtlebook/colorado/recovery_coaching.html
7. Connecticut - /Users/cjoh/turtlebook/connecticut/recovery_coaching.html
8. Delaware - /Users/cjoh/turtlebook/delaware/recovery_coaching.html
9. Florida - /Users/cjoh/turtlebook/florida/recovery_coaching.html
10. Georgia - /Users/cjoh/turtlebook/georgia/recovery_coaching.html
11. Hawaii - /Users/cjoh/turtlebook/hawaii/recovery_coaching.html
12. Idaho - /Users/cjoh/turtlebook/idaho/recovery_coaching.html
13. Illinois - /Users/cjoh/turtlebook/illinois/recovery_coaching.html
14. Indiana - /Users/cjoh/turtlebook/indiana/recovery_coaching.html
15. Iowa - /Users/cjoh/turtlebook/iowa/recovery_coaching.html
16. Kansas - /Users/cjoh/turtlebook/kansas/recovery_coaching.html
17. Kentucky - /Users/cjoh/turtlebook/kentucky/recovery_coaching.html
18. Louisiana - /Users/cjoh/turtlebook/louisiana/recovery_coaching.html
19. Maine - /Users/cjoh/turtlebook/maine/recovery_coaching.html
20. Maryland - /Users/cjoh/turtlebook/maryland/recovery_coaching.html
21. Massachusetts - /Users/cjoh/turtlebook/massachusetts/recovery_coaching.html
22. Michigan - /Users/cjoh/turtlebook/michigan/recovery_coaching.html
23. Minnesota - /Users/cjoh/turtlebook/minnesota/recovery_coaching.html
24. Mississippi - /Users/cjoh/turtlebook/mississippi/recovery_coaching.html
25. Missouri - /Users/cjoh/turtlebook/missouri/recovery_coaching.html
26. Montana - /Users/cjoh/turtlebook/montana/recovery_coaching.html

### Summary Document
- **RECOVERY_COACHING_SUMMARY.md** - Comprehensive summary of all 26 states

## Style Guide Compliance

All HTML pages follow the Core Values Style Guide requirements:

### Fonts
- **Headings:** Bebas Neue (300 weight)
- **Body:** Roboto (11pt, 400/700 weight)

### Colors
- **Primary:** #1d4486 (blue)
- **Background:** #f5f5f5 (light gray)
- **Text:** #333333 (dark gray)

### Color-Coded Boxes
- **Yellow warning-box:** Important cautions
- **Blue legal-box:** Legal citations
- **Red prohibited-box:** What's NOT allowed
- **Green allowed-box:** What IS allowed
- **Gray info-box:** General information

### Navigation
- Back to State Index
- Link to Peer Support Certification page

## Summary of State Regulations

### Independent Practice Allowed (18 states)

**Unregulated:**
- Alaska
- Arizona
- California (with restrictions)

**Certification Available:**
- Arkansas, Colorado, Connecticut, Delaware, Georgia
- Idaho, Illinois, Indiana, Kansas, Louisiana
- Maine, Maryland, Michigan, Minnesota, Missouri

### Supervision Required (7 states)
- Alabama (unclear)
- Florida
- Hawaii
- Iowa
- Kentucky
- Mississippi
- Montana

### New Licensure (1 state)
- Massachusetts (effective March 23, 2025)

## Key Findings

### Most Restrictive States
1. **Mississippi** - Employment in state mental health system MANDATORY
2. **Montana** - Licensure required by statute
3. **Iowa** - Must work within licensed agency with IDPH contract
4. **Florida** - Must work at licensed behavioral health organization
5. **Kentucky** - Must work under supervision
6. **Hawaii** - Must work under supervision

### Least Restrictive States
1. **Alaska** - Completely unregulated
2. **Arizona** - Unregulated
3. **Maryland** - Exempt from licensing requirements

### Special Cases
- **California:** Practice protection state (activity determines regulation)
- **Colorado:** Medicaid credentialing required by July 1, 2026
- **Massachusetts:** First state with recovery coach licensure (March 2025)
- **Maryland:** Explicitly exempt from COMAR 10.63
- **Georgia:** Certain credentials grant legal scope of practice

## Legal Disclaimer

All pages include appropriate legal disclaimer:
"This information is for educational purposes only and does not constitute legal advice. Laws and regulations change frequently. Always consult with a licensed attorney in your state for specific legal guidance regarding recovery coaching practice."

## Verification

Run this command to verify all files exist:
```bash
for state in alabama alaska arizona arkansas california colorado connecticut delaware florida georgia hawaii idaho illinois indiana iowa kansas kentucky louisiana maine maryland massachusetts michigan minnesota mississippi missouri montana; do
  if [ -f "$state/recovery_coaching.html" ]; then
    echo "✓ $state"
  else
    echo "✗ $state - MISSING"
  fi
done
```

Expected result: 26 checkmarks

## Project Status

✅ All 26 HTML pages created
✅ Summary document created
✅ Style guide compliance verified
✅ Legal disclaimers included
✅ Navigation links included

**PROJECT COMPLETE**
