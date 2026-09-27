# Interview Guides — Four Short Conversations

Written Sept 27, 2026. The team asks each teammate to try for one 15–20 minute conversation before Sept 30, so the answers can feed the model's assumptions. Each guide lists the numbers the model needs from that conversation.

## Rules for every conversation

1. **Say what the project is.** "We are MBA students in a Carnegie Mellon case competition about how a drug company could help primary care find patients with a genetic kidney disease." Do not share or read from the case PDF or the analyst reports; they are licensed for the competition only.
2. **Do not contact Vertex employees about the case.** Vertex staff may be judges.
3. **Ask permission before quoting.** Ask: "May we quote you, and how should we describe you (for example, 'a primary care physician in Pittsburgh')?" Write down the answer. A quote appears in the deck only with that permission, in the person's own words, and attributed as they agreed.
4. **Collect no personal health information.** Do not ask anyone to describe a named patient or their own medical history.
5. **Record numbers as ranges.** When someone gives a number, ask for a low and a high ("What would surprise you on the low side? On the high side?"). The model uses ranges.
6. **Write notes within an hour** in `work/research/interviews/<date>_<role>.md`: who (as they agreed to be described), date, the answers, the numbers with ranges, and whether quoting is allowed. Only notes the team took may be used; the agent will never write or fill in an interview.

---

## Guide 1: Primary care physician (or nurse practitioner or physician assistant)

**What the model needs:** how often primary care orders an APOL1 test; what triggers a kidney referral; how long a nephrology referral takes; what a rep visit changes.

1. About how many of your patients have chronic kidney disease? About how many of those are Black, Afro-Caribbean, or Hispanic with African ancestry?
2. Have you ever ordered an APOL1 genetic test? If yes, what prompted it, and how did you order it? If no, what stops you?
3. Did you know that free APOL1 testing is available through labs such as Labcorp? Where would you expect to hear about it?
4. When you find protein in the urine of a patient without diabetes, what do you do next? At what point do you refer to nephrology?
5. How long does a routine nephrology referral take in your area, from referral to first visit? What is the shortest and the longest you have seen?
6. How often do drug-company reps visit your practice? Which visits change what you do, and which do you skip?
7. Would a prompt in your electronic health record (for example, "consider APOL1 testing") help or annoy you? What would make it useful?
8. If a patient asked you for a genetic kidney test after seeing an ad, what would you do?
9. What would make you worried about ordering a genetic test for a patient (cost, insurance, consent, time)?

## Guide 2: Nephrologist

**What the model needs:** the share of AMKD-eligible patients who arrive from primary care; the biopsy and workup step; clinic capacity; how inaxaplin might be prescribed.

1. Of your patients with non-diabetic proteinuric kidney disease who are of African ancestry, about what share have had an APOL1 test?
2. How do most of these patients reach you: from primary care, the hospital, or another route? At what stage of disease do they usually arrive?
3. For a patient with two APOL1 variants and heavy proteinuria, would you perform a kidney biopsy? When would you skip it?
4. If insurers required a biopsy before covering a new APOL1 drug, how many weeks would that add, and how many patients would decline the biopsy?
5. How long is the wait for a new patient in your clinic today? Could you absorb 10% more referrals? 50% more?
6. Do you use e-consults (written consultations inside the health record) with primary care? What share of referrals could an e-consult handle?
7. How often do you test family members of a patient with two APOL1 variants? What stops it?
8. How do your patients react when you suggest genetic testing? What concerns do they raise?

## Guide 3: Pharma sales or marketing professional (current or former)

**What the model needs:** the cost and speed of hired versus contracted reps; calls per rep; response rates; the cost of direct-to-patient campaigns.

1. What does a fully loaded primary care sales rep cost per year (salary, bonus, benefits, car, expenses, management)? What is the range?
2. How long does it take to hire and train a new primary care team of 50–100 reps? How long for a contract sales organization to deploy the same number?
3. How do contract rep costs compare with hired reps, per rep per year? What are the usual contract terms (length, exit fees, conversion-to-hire clauses)?
4. How many calls does a primary care rep make per day and per year? How many target physicians does one rep cover?
5. For a condition primary care physicians rarely diagnose, what share of targeted physicians change behavior after a year of calls? How does that differ between the top-decile physicians and the rest?
6. What can a sales team do before a drug is approved? Who handles disease education before approval?
7. What does an unbranded disease-awareness campaign cost per year at national scale and at the scale of 10 metro areas? What measures show whether it worked?
8. Have you seen electronic health record prompts or lab-report messages used to drive testing? What did they cost, and what did they achieve?
9. When a company already has a specialist sales force, when does it make sense to add primary care physicians to their call lists instead of building a new team?

## Guide 4: Patient advocate (kidney health, genetic testing, or community health)

**What the model needs:** what raises or lowers willingness to take a genetic test; which messengers and channels reach at-risk adults; privacy concerns.

1. In the communities you work with, how aware are people that some kidney disease is genetic?
2. What would make someone willing to take a genetic test for kidney disease? What would make them refuse?
3. Which messengers do people trust on health questions (physicians, pharmacists, churches, barbershops, community health workers, athletes, social media)?
4. What concerns about genetic data come up (insurance, employment, police databases, research use)? How much does it help that a test program shares no identifiable data with the drug maker?
5. How should family testing be offered, so that relatives do not feel pressured?
6. What wording about race and genetics feels respectful and accurate to the people you work with, and what wording causes harm?
7. Have you seen awareness campaigns (for example, Power Forward or American Kidney Fund campaigns)? What worked and what did not?
