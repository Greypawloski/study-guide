"""Study lessons for the Arizona Life Insurance Producer exam (Series 13-31).

Section weights follow the official PSI / Arizona DIFI content outline:
100 scored questions, 2 hours, 70% to pass.
"""

SECTIONS = [
    {
        "id": "reg",
        "num": 1,
        "title": "Insurance Regulation",
        "weight": 5,
        "icon": "⚖️",
        "summary": "Arizona licensing, DIFI powers, unfair trade practices, fraud, privacy and the federal laws that touch insurance sales.",
        "lessons": [
            {
                "title": "Who regulates insurance in Arizona",
                "html": """
<p>Insurance is regulated mainly by the <strong>states</strong>. In Arizona the regulator is the <strong>Department of Insurance and Financial Institutions (DIFI)</strong>, run by the <strong>Director</strong>. The Director enforces Title 20 of the Arizona Revised Statutes (A.R.S.), issues rules, licenses producers, examines insurers and can hold hearings and discipline licensees.</p>
<h4>Insurers must be authorized</h4>
<ul>
<li>An insurer needs a <strong>Certificate of Authority</strong> from the Director to transact insurance in Arizona (A.R.S. 20-217). An insurer that has one is <strong>authorized (admitted)</strong>; one without it is <strong>unauthorized (non-admitted)</strong>.</li>
<li><strong>Domestic</strong> insurer: formed under Arizona law. <strong>Foreign</strong>: formed in another U.S. state. <strong>Alien</strong>: formed outside the United States.</li>
</ul>
<h4>What counts as "transacting insurance"</h4>
<p>Soliciting, negotiating, selling (effecting) a contract, and transacting matters after the sale. <strong>Solicit</strong> = attempting to sell or urging someone to apply with a particular insurer. <strong>Negotiate</strong> = conferring directly with or advising a buyer about the substantive benefits, terms or conditions of a contract. <strong>Sell</strong> = exchanging a contract of insurance for money on behalf of an insurer. You need a producer license to do any of these.</p>
<p>Premium paid to a producer is treated as paid to the insurer (A.R.S. 20-191), so the producer holds that money in a <strong>fiduciary</strong> capacity and must not mix it with personal funds.</p>
""",
            },
            {
                "title": "Getting and keeping your Arizona license",
                "html": """
<h4>Getting licensed</h4>
<ul>
<li>Arizona has <strong>no required pre-licensing course</strong>; you must pass the state exam (now delivered by <strong>PSI</strong>).</li>
<li>You may take an exam <strong>up to 4 times in a 12-month period</strong>. After a fourth failure you wait one year (A.R.S. 20-284(H)).</li>
<li>You must <strong>apply within 1 year</strong> after passing the exam, or retest.</li>
<li>Residents are <strong>fingerprinted</strong> for a background check. Applicants must show <strong>lawful presence</strong> in the U.S.</li>
<li>The Director can deny a license for reasons such as lying on the application, a felony conviction, or prior license revocation.</li>
</ul>
<h4>Keeping it</h4>
<table class="facts">
<tr><th>Item</th><th>Arizona rule</th></tr>
<tr><td>License term</td><td><strong>4 years</strong>, expiring the <strong>last day of your birth month</strong> (a first license runs 3–4 years)</td></tr>
<tr><td>Renewal window</td><td>Up to <strong>90 days</strong> before expiration</td></tr>
<tr><td>Continuing education</td><td><strong>48 hours</strong> per 4-year term, including <strong>6 hours of ethics</strong> (major-line residents)</td></tr>
<tr><td>Annuity training</td><td><strong>4 hours</strong> of approved annuity training before selling annuities</td></tr>
<tr><td>Change of name, address or email</td><td>Tell the Director in writing within <strong>30 days</strong> (A.R.S. 20-286)</td></tr>
<tr><td>Administrative action in another state, or criminal conviction</td><td>Report within <strong>30 days</strong> (A.R.S. 20-301)</td></tr>
<tr><td>Assumed (business) name</td><td>Must be registered with the Director <strong>before</strong> you use it (A.R.S. 20-297)</td></tr>
<tr><td>Military service</td><td>A license can be placed on <strong>inactive status</strong> during active duty (A.R.S. 20-289.01)</td></tr>
</table>
<h4>Types of licenses</h4>
<p>Individual producers, <strong>business entity</strong> licenses (an agency must also designate a licensed producer responsible for compliance), <strong>nonresident</strong> licenses (granted reciprocally if you are in good standing in your home state), and limited licenses. Lines include Life; Accident &amp; Health; Property; Casualty; Personal Lines. Selling <strong>variable</strong> life or annuities also requires a FINRA securities registration.</p>
<h4>Commissions</h4>
<p>You may share or pay commissions <strong>only with persons licensed</strong> for that line of insurance (A.R.S. 20-298).</p>
<h4>Discipline</h4>
<p>The Director may <strong>suspend, revoke or refuse to renew</strong> a license, impose a <strong>civil penalty</strong>, or order <strong>restitution</strong>, usually after notice and a hearing. Grounds include fraud, misappropriating premiums, misrepresentation, cheating on the exam and violating insurance laws.</p>
""",
            },
            {
                "title": "Unfair trade practices, fraud and privacy",
                "html": """
<h4>Unfair trade practices (A.R.S. 20-441 to 20-465)</h4>
<dl>
<dt>Misrepresentation</dt><dd>Lying about or misstating policy terms, benefits, dividends or an insurer's financial condition.</dd>
<dt>Twisting</dt><dd>Using misrepresentation to persuade someone to drop a policy with one insurer and buy from another.</dd>
<dt>Churning</dt><dd>Replacing a policy with another <em>from the same insurer</em> mainly to generate commissions.</dd>
<dt>Rebating</dt><dd>Giving the buyer anything of value not stated in the policy (part of your commission, a gift) as an inducement to buy. Illegal except as specifically allowed by law.</dd>
<dt>False advertising</dt><dd>Untrue, deceptive or misleading statements in any advertising.</dd>
<dt>Defamation</dt><dd>False statements meant to harm the reputation or financial standing of an insurer or person.</dd>
<dt>Boycott, coercion, intimidation</dt><dd>Agreements or acts that restrain trade or create a monopoly.</dd>
<dt>Unfair discrimination</dt><dd>Treating people of the same class and life expectancy differently in rates or benefits. Arizona also bars discrimination based on blindness alone (R20-6-211).</dd>
<dt>False financial statements</dt><dd>Filing or circulating false statements about an insurer's finances.</dd>
</dl>
<p>Producers also must not use the existence of the <strong>Arizona Life and Disability Insurance Guaranty Fund</strong> to sell insurance.</p>
<h4>Insurance fraud</h4>
<p>Knowingly presenting false information to an insurer, or helping someone else do so, is fraud and a crime. Producers who know of fraud must report it to the DIFI <strong>Fraud Unit</strong>. People who report in good faith are protected from civil liability.</p>
<h4>Privacy (A.R.S. 20-2101 to 20-2122)</h4>
<ul>
<li>Insurers must give a <strong>notice of insurance information practices</strong> when collecting personal information.</li>
<li><strong>Pretext interviews</strong> (pretending to be someone else to get information) are generally prohibited.</li>
<li>An applicant may request the <strong>specific reasons for an adverse underwriting decision</strong>.</li>
<li>Personal, medical and financial information may not be disclosed without written authorization except as the law allows.</li>
</ul>
""",
            },
            {
                "title": "Federal laws you need to know",
                "html": """
<dl>
<dt>Violent Crime Control and Law Enforcement Act (18 U.S.C. 1033 &amp; 1034)</dt>
<dd>A person convicted of a <strong>felony involving dishonesty or breach of trust</strong> may not work in the business of insurance without <strong>written consent</strong> from the state regulator (a "1033 waiver"). Knowingly employing such a person without consent is also a crime.</dd>
<dt>Fair Credit Reporting Act (FCRA)</dt>
<dd>Governs <strong>consumer reports</strong> and <strong>investigative consumer reports</strong> used in underwriting. The applicant must be told a report may be requested, and if coverage is denied or rated because of a report, the insurer must say so and identify the reporting agency. Consumers can see and dispute their file.</dd>
<dt>Telemarketing Sales Rule / Do Not Call</dt>
<dd>No calls to numbers on the National Do Not Call Registry (with limited exceptions such as an existing business relationship). Calls may be made only between <strong>8 a.m. and 9 p.m.</strong> local time, and the caller must identify themselves and the purpose.</dd>
<dt>CAN-SPAM Act</dt>
<dd>Commercial emails must not use misleading headers or subject lines, must identify the message as an ad, include a physical address, and give a working <strong>opt-out</strong>, honored within <strong>10 business days</strong>.</dd>
<dt>Gramm-Leach-Bliley Act</dt>
<dd>Financial institutions, including insurers, must give customers a <strong>privacy notice</strong> explaining how nonpublic personal information is shared, and allow them to <strong>opt out</strong> of certain sharing with nonaffiliated third parties.</dd>
<dt>Terrorism Risk Insurance Program</dt>
<dd>A federal backstop that shares losses from certified acts of terrorism with insurers.</dd>
</dl>
""",
            },
        ],
        "key_facts": [
            "Regulator: Department of Insurance and Financial Institutions (DIFI), headed by the Director",
            "Up to 4 exam attempts in 12 months; then wait 1 year",
            "Apply for the license within 1 year of passing",
            "License term: 4 years, ends last day of birth month",
            "CE: 48 hours per term including 6 hours ethics",
            "Report address/name change within 30 days",
            "Report other-state actions or convictions within 30 days",
            "4 hours annuity training before selling annuities",
            "Share commissions only with licensed persons",
            "Never use the Guaranty Fund as a sales tool",
        ],
    },
    {
        "id": "general",
        "num": 2,
        "title": "General Insurance",
        "weight": 10,
        "icon": "📘",
        "summary": "Risk, insurer types, agency law and the legal features of insurance contracts.",
        "lessons": [
            {
                "title": "Risk and how it is handled",
                "html": """
<p><strong>Insurance</strong> is a contract in which one party (the insurer) agrees to indemnify or pay a specified amount to another upon determinable contingencies. It <strong>transfers risk</strong> from an individual to a large group.</p>
<dl>
<dt>Risk</dt><dd>Uncertainty about loss. <strong>Pure risk</strong> = only a chance of loss or no loss (insurable). <strong>Speculative risk</strong> = chance of loss <em>or gain</em>, like gambling or investing (not insurable).</dd>
<dt>Exposure</dt><dd>A unit of measure used to determine rates.</dd>
<dt>Peril</dt><dd>The <strong>cause</strong> of a loss (death, illness, fire).</dd>
<dt>Hazard</dt><dd>A condition that <strong>increases the chance</strong> of loss. <strong>Physical</strong> (high blood pressure), <strong>moral</strong> (dishonesty, e.g. faking a claim), <strong>morale</strong> (indifference because "I'm insured").</dd>
<dt>Loss</dt><dd>Reduction in value. In life insurance, the loss is death.</dd>
</dl>
<h4>Five ways to handle risk (remember "STARR")</h4>
<ul>
<li><strong>Sharing</strong>: a group spreads losses (e.g., a reciprocal).</li>
<li><strong>Transfer</strong>: shift the risk to another party, the main purpose of insurance.</li>
<li><strong>Avoidance</strong>: don't do the risky thing.</li>
<li><strong>Reduction</strong>: lessen the chance or severity (smoke detectors, annual checkups).</li>
<li><strong>Retention</strong>: accept the risk yourself (deductibles, self-insurance).</li>
</ul>
<h4>Elements of an insurable risk</h4>
<ol>
<li>Loss must be <strong>due to chance</strong> (accidental, not intended).</li>
<li>Loss must be <strong>definite and measurable</strong>.</li>
<li>Loss must be <strong>predictable</strong>, through the <strong>law of large numbers</strong> (the larger the group, the more accurately losses can be predicted).</li>
<li>Loss must <strong>not be catastrophic</strong> to the insurer.</li>
<li>Insured units must be <strong>large in number and similar</strong> (homogeneous).</li>
<li>Coverage must be <strong>affordable</strong>.</li>
</ol>
<p><strong>Adverse selection</strong> is the tendency of higher-risk people to seek insurance more than average risks. Underwriting protects against it.</p>
<p><strong>Reinsurance</strong>: an insurer (the ceding company) transfers part of its risk to another insurer (the reinsurer) to protect against large losses and increase capacity.</p>
""",
            },
            {
                "title": "Types of insurers",
                "html": """
<dl>
<dt>Stock company</dt><dd>Owned by <strong>stockholders</strong>; usually issues <strong>nonparticipating</strong> policies (no dividends to policyowners). Profits go to stockholders as taxable dividends.</dd>
<dt>Mutual company</dt><dd>Owned by its <strong>policyowners</strong>; issues <strong>participating</strong> policies. Policy dividends are a <strong>return of excess premium</strong> and are not guaranteed.</dd>
<dt>Fraternal benefit society</dt><dd>A nonprofit social, religious or charitable organization with a lodge system that provides insurance to its members.</dd>
<dt>Reciprocal</dt><dd>Members (subscribers) insure each other, managed by an <strong>attorney-in-fact</strong>.</dd>
<dt>Lloyd's</dt><dd>An association of individuals or groups (syndicates) who underwrite risks; not an insurer itself.</dd>
<dt>Captive</dt><dd>An insurer formed by a parent company to insure the parent's own risks.</dd>
<dt>Risk retention group</dt><dd>A liability insurer owned by its members, who share similar risks.</dd>
<dt>Government insurers</dt><dd>Social Security, Medicare, FDIC, flood insurance and similar programs.</dd>
</dl>
<h4>Distribution systems</h4>
<ul>
<li><strong>Career (captive) agency</strong>: agents represent one insurer; the company provides training and support.</li>
<li><strong>Independent agency</strong>: agents represent several insurers and own their renewals.</li>
<li><strong>Personal producing general agent (PPGA)</strong>: independent agents with higher commissions who mostly sell personally.</li>
<li><strong>Direct writing / direct response</strong>: insurer sells through its own employees or through mail, TV or the internet.</li>
</ul>
<h4>Financial strength</h4>
<p>Independent rating services (A.M. Best, Standard &amp; Poor's, Moody's, Fitch) grade insurers' financial strength.</p>
""",
            },
            {
                "title": "Agency law",
                "html": """
<p>The <strong>insurer is the principal</strong>; the producer is its <strong>agent</strong>. What the agent does within their authority is legally considered the act of the insurer, and knowledge given to the agent is presumed known by the insurer.</p>
<dl>
<dt>Express authority</dt><dd>Authority written in the producer's <strong>contract</strong> with the insurer.</dd>
<dt>Implied authority</dt><dd>Authority not written down but <strong>necessary to do the job</strong> (e.g., collecting the first premium).</dd>
<dt>Apparent authority</dt><dd>Authority the <strong>public reasonably believes</strong> the agent has, based on the insurer's actions (e.g., letting the agent use company letterhead).</dd>
</dl>
<p>The producer is a <strong>fiduciary</strong>: a position of financial trust over premiums and client information.</p>
""",
            },
            {
                "title": "Insurance contract law",
                "html": """
<h4>Four elements of a legal contract ("COLA")</h4>
<ol>
<li><strong>Consideration</strong>: something of value exchanged. The applicant's consideration is the <strong>application and first premium</strong>; the insurer's is the promise to pay.</li>
<li><strong>Offer and acceptance</strong>: usually the applicant makes the offer by submitting the application <em>with</em> premium; the insurer accepts by issuing the policy. If no premium is sent, the insurer's issued policy is the offer, and the applicant accepts by paying at delivery.</li>
<li><strong>Legal purpose</strong>: the contract can't be against public policy (insurable interest is required).</li>
<li><strong>Competent parties</strong>: of legal age and sound mind, and the insurer must be authorized.</li>
</ol>
<h4>Special features of insurance contracts</h4>
<dl>
<dt>Aleatory</dt><dd>An exchange of <strong>unequal</strong> amounts; a small premium may buy a large benefit.</dd>
<dt>Adhesion</dt><dd>The insurer writes it and the buyer takes it as is, so any <strong>ambiguity is interpreted in favor of the insured</strong>.</dd>
<dt>Unilateral</dt><dd>Only the <strong>insurer</strong> makes a legally enforceable promise.</dd>
<dt>Conditional</dt><dd>The insurer pays only if certain conditions are met (premium paid, proof of loss given).</dd>
<dt>Utmost good faith</dt><dd>Both parties rely on each other's honesty.</dd>
</dl>
<h4>Statements and their effects</h4>
<ul>
<li><strong>Representation</strong>: a statement believed true to the best of the applicant's knowledge. Answers on life applications are representations.</li>
<li><strong>Warranty</strong>: a statement guaranteed true; a breach can void the contract.</li>
<li><strong>Misrepresentation</strong>: a false statement. If <strong>material</strong> (it would have changed the insurer's decision) it may void the contract.</li>
<li><strong>Concealment</strong>: intentionally withholding a material fact.</li>
<li><strong>Fraud</strong>: intentional deception to gain something of value.</li>
<li><strong>Waiver</strong>: voluntarily giving up a known right. <strong>Estoppel</strong>: a legal bar to reasserting a right that was waived.</li>
</ul>
<p>Life insurance is a <strong>valued</strong> contract (it pays a stated amount), not a contract of <strong>indemnity</strong> (restoring someone to their prior financial position), which is how most property insurance works.</p>
""",
            },
        ],
        "key_facts": [
            "Pure risk is insurable; speculative risk is not",
            "Peril = cause of loss; hazard = condition that increases chance of loss",
            "Moral hazard = dishonesty; morale hazard = indifference",
            "Law of large numbers makes losses predictable",
            "Mutual = owned by policyowners, participating; Stock = owned by stockholders",
            "Express, implied and apparent authority",
            "Contract elements: offer & acceptance, consideration, competent parties, legal purpose",
            "Adhesion: ambiguities favor the insured",
            "Aleatory = unequal exchange; Unilateral = only insurer promises",
            "Life application answers are representations, not warranties",
        ],
    },
    {
        "id": "basics",
        "num": 3,
        "title": "Life Insurance Basics",
        "weight": 24,
        "icon": "🧭",
        "summary": "Insurable interest, needs analysis, business uses, premiums, producer duties, replacement and underwriting.",
        "lessons": [
            {
                "title": "Insurable interest and why people buy life insurance",
                "html": """
<h4>Insurable interest</h4>
<p>The policyowner must face a real financial or emotional loss from the insured's death. In life insurance, insurable interest must exist <strong>only at the time of application</strong>; it doesn't have to exist at the time of death.</p>
<ul>
<li>You have unlimited insurable interest in <strong>your own life</strong>.</li>
<li>Spouses, parents, children and other close family members are generally presumed to have it.</li>
<li>Business relationships create it: an employer for a <strong>key employee</strong>, business partners for each other, a creditor for a debtor (up to the debt).</li>
<li>If the insured applies for a policy on their own life, they can name <strong>anyone</strong> as beneficiary.</li>
<li>A policy taken out without the insured's knowledge and consent is generally not allowed (except, for example, a parent insuring a minor child).</li>
</ul>
<h4>Personal uses</h4>
<ul>
<li><strong>Survivor protection</strong>: replace income for dependents.</li>
<li><strong>Estate creation</strong>: life insurance creates an <em>immediate</em> estate the moment the first premium is paid.</li>
<li><strong>Cash accumulation</strong>: permanent policies build cash value that grows tax-deferred.</li>
<li><strong>Liquidity</strong>: provides cash quickly so heirs don't have to sell assets at a loss.</li>
<li><strong>Estate conservation</strong>: pays estate taxes and final expenses so the estate passes intact.</li>
</ul>
<h4>Viatical and life settlements</h4>
<p>A policyowner sells an existing policy to a third party for more than its cash value but less than the death benefit. The buyer becomes owner and beneficiary and pays future premiums. <strong>Viatical</strong> settlements involve an insured who is <strong>terminally or chronically ill</strong>; <strong>life</strong> settlements involve insureds who are not necessarily ill (often older). The person who sells is the <strong>viator / owner</strong>; the buyer is the <strong>provider</strong>; a <strong>broker</strong> represents the owner. In Arizona a life settlement broker must hold a life producer license.</p>
<h4>How much insurance?</h4>
<dl>
<dt>Human life value approach</dt><dd>Based on the <strong>economic value of the insured's future earnings</strong> lost to the family (income, years until retirement, minus personal expenses).</dd>
<dt>Needs approach</dt><dd>Based on what the <strong>family actually needs</strong>: final expenses and debts (lump sum), plus income needs (readjustment period, dependency period, spouse's blackout period before Social Security), mortgage, education, retirement.</dd>
</dl>
""",
            },
            {
                "title": "Business uses of life insurance",
                "html": """
<dl>
<dt>Buy-sell agreement</dt><dd>A legal agreement under which surviving owners buy a deceased owner's share of the business, funded by life insurance.
<ul><li><strong>Cross-purchase</strong>: each owner buys a policy on every other owner (owner and beneficiary of policies on the others).</li>
<li><strong>Entity (stock redemption)</strong>: the <strong>business</strong> owns one policy on each owner and buys back the shares.</li></ul></dd>
<dt>Key person insurance</dt><dd>The business insures a vital employee whose death would cost it money. The business is <strong>owner, premium payer and beneficiary</strong>. Premiums are <strong>not deductible</strong>; the death benefit is generally received <strong>income-tax free</strong>.</dd>
<dt>Executive bonus (Section 162)</dt><dd>The employer pays the premium on a policy owned by the executive. The employer <strong>deducts</strong> the bonus as compensation; the executive pays <strong>income tax</strong> on it.</dd>
<dt>Deferred compensation</dt><dd>A promise to pay an employee benefits in the future, often funded with cash-value life insurance.</dd>
<dt>Split-dollar</dt><dd>Employer and employee share premiums, cash value and death benefit.</dd>
</dl>
""",
            },
            {
                "title": "Classes of policies and how premiums work",
                "html": """
<h4>Classes</h4>
<ul>
<li><strong>Individual vs. group</strong>: group coverage is one master policy covering many people.</li>
<li><strong>Ordinary vs. industrial</strong>: industrial (home service) life is small face amounts with weekly or monthly premiums collected by an agent.</li>
<li><strong>Term vs. permanent</strong>: term is temporary protection with no cash value; permanent builds cash value and lasts for life.</li>
<li><strong>Participating vs. nonparticipating</strong>: participating policies can pay dividends.</li>
<li><strong>Fixed vs. variable</strong>: fixed products guarantee values from the insurer's <strong>general account</strong>; variable products invest in a <strong>separate account</strong>, so values aren't guaranteed and the policyowner bears the investment risk. Variable products are securities: you need a life license, a FINRA registration (Series 6 or 7) and a variable authority.</li>
</ul>
<h4>Premium factors</h4>
<ol>
<li><strong>Mortality</strong>: the expected death rate, from mortality tables. Raises the premium.</li>
<li><strong>Interest</strong>: what the insurer earns on invested premiums. <em>Lowers</em> the premium.</li>
<li><strong>Expenses (loading)</strong>: costs of running the business. Raises the premium.</li>
</ol>
<p><strong>Net single premium</strong> = mortality minus interest. <strong>Gross premium</strong> = net premium plus loading (expenses).</p>
<p><strong>Payment modes</strong>: annual, semiannual, quarterly, monthly. Paying more often costs more in total because the insurer has more administrative cost and loses investment earnings.</p>
""",
            },
            {
                "title": "Producer responsibilities, from sale to delivery",
                "html": """
<h4>Solicitation and disclosure in Arizona</h4>
<ul>
<li>When soliciting, a producer must identify themselves, the insurer, and the type of product.</li>
<li>Insurers must give buyers a <strong>Buyer's Guide</strong> and a <strong>Policy Summary</strong> (R20-6-209). These must be delivered <strong>before the initial premium is accepted</strong>, unless the policy has an unconditional refund (free-look) provision of at least 10 days, in which case they may be delivered with the policy.</li>
<li><strong>Illustrations</strong> must show guaranteed and nonguaranteed elements clearly and may not be misleading.</li>
<li>Advertising must be truthful and must not misrepresent the product.</li>
</ul>
<h4>Cost comparison methods</h4>
<ul>
<li><strong>Interest-adjusted net cost index</strong>: accounts for the time value of money. The most accurate way to compare costs; required in Buyer's Guide disclosures.</li>
<li><strong>Traditional net cost method</strong>: adds premiums and subtracts cash value and dividends, but ignores the time value of money, so it can make costs look lower than they are.</li>
</ul>
<h4>Replacement (A.R.S. 20-1241 to 20-1241.09)</h4>
<p>Replacement means buying a new policy or annuity and, as part of that, an existing one is lapsed, surrendered, converted, borrowed against, reduced or otherwise changed.</p>
<ul>
<li>The producer must submit a statement, signed by the applicant and producer, saying whether the applicant has existing coverage.</li>
<li>If so, the producer must <strong>present and read the replacement notice</strong> no later than when taking the application, have it <strong>signed by the applicant and producer</strong>, and <strong>leave a copy</strong> with the applicant.</li>
<li>The producer leaves copies of all sales materials used and submits copies to the insurer.</li>
<li>The <strong>replacing insurer</strong> must notify the existing insurer within <strong>5 business days</strong> and keep records for at least <strong>5 years</strong>.</li>
<li>The new policy has a <strong>30-day free look</strong> for a full refund.</li>
<li>The <strong>existing insurer</strong> must tell the owner of the right to information about the existing policy's values, and provide it within 5 business days of a request.</li>
</ul>
<h4>Field underwriting</h4>
<p>The producer is the insurer's first underwriter: completing the application accurately, getting the right signatures (the <strong>applicant, proposed insured if different, and producer</strong>), and reporting what they observed.</p>
<ul>
<li>If the applicant makes a mistake, <strong>correct it and have the applicant initial</strong> the change. Never use correction fluid.</li>
<li>Incomplete applications are returned to the producer.</li>
<li>Collect the initial premium with the application if possible and give a <strong>receipt</strong>. A <strong>conditional receipt</strong> provides coverage from the date of application (or medical exam, if later) <em>if</em> the applicant turns out to be insurable as applied for. A <strong>binding receipt</strong> provides temporary coverage regardless of insurability for a limited time.</li>
</ul>
<h4>Policy delivery</h4>
<ul>
<li>Deliver the policy <strong>in person</strong> when possible and explain it; constructive delivery (mailing it, or giving it to the producer without conditions) also counts legally.</li>
<li>If the premium wasn't collected with the application, collect it at delivery along with a signed <strong>statement of continued good health</strong>.</li>
<li>If the insurer issued a policy different from what was applied for (rated or modified), the change must be explained and accepted.</li>
</ul>
""",
            },
            {
                "title": "Underwriting",
                "html": """
<p>Underwriting decides whether to accept a risk and at what premium. The <strong>insurer's underwriter</strong> is responsible for risk selection.</p>
<h4>Sources of information</h4>
<ul>
<li><strong>Application</strong>: Part 1 is general information, Part 2 is medical history.</li>
<li><strong>Producer's report</strong>: the producer's observations. It is <strong>not</strong> part of the contract.</li>
<li><strong>Attending Physician's Statement (APS)</strong>: records from the applicant's own doctor.</li>
<li><strong>Medical exams</strong>: paramedical or full exams, often required based on age and amount.</li>
<li><strong>Medical Information Bureau (MIB)</strong>: a nonprofit, member-company database of coded medical impairments reported by insurers. Insurers can't decline coverage <em>solely</em> because of an MIB report.</li>
<li><strong>Inspection / consumer reports</strong>: governed by the FCRA and Arizona privacy law (A.R.S. 20-2107). The applicant must be notified.</li>
</ul>
<h4>Arizona testing rules</h4>
<ul>
<li><strong>HIV testing</strong> requires the applicant's <strong>written informed consent</strong>, and results are confidential (A.R.S. 20-448.01).</li>
<li><strong>Genetic testing</strong>: an insurer may not require a genetic test or use genetic information in underwriting except as permitted by A.R.S. 20-448, and must keep results confidential.</li>
<li>Insurers may not refuse or limit coverage <strong>solely because someone is blind</strong> (R20-6-211).</li>
</ul>
<h4>Risk classifications</h4>
<ul>
<li><strong>Preferred</strong>: better than average health and lifestyle, lower premium.</li>
<li><strong>Standard</strong>: average risk.</li>
<li><strong>Substandard (rated)</strong>: higher risk, so a higher premium (a "rating"), a flat extra charge, or a reduced benefit.</li>
<li><strong>Declined</strong>: uninsurable.</li>
</ul>
""",
            },
        ],
        "key_facts": [
            "Insurable interest must exist at the time of application only",
            "Human life value = lost future earnings; Needs approach = family's needs",
            "Key person: business is owner, payer and beneficiary; premiums not deductible",
            "Cross-purchase: owners insure each other; Entity: business insures each owner",
            "Premium factors: mortality, interest, expenses",
            "Interest-adjusted net cost index is the most accurate cost comparison",
            "Replacement: notice read and signed at application; 30-day free look",
            "Replacing insurer notifies existing insurer within 5 business days",
            "Conditional receipt: coverage from application date if insurable",
            "Statement of good health collected at delivery if no premium with app",
            "HIV test requires written informed consent",
        ],
    },
    {
        "id": "policies",
        "num": 4,
        "title": "Life Insurance Policies",
        "weight": 23,
        "icon": "📄",
        "summary": "Term, whole life, universal and variable policies, specialty policies, group and credit life.",
        "lessons": [
            {
                "title": "Term life insurance",
                "html": """
<p><strong>Term insurance</strong> gives pure protection for a set period. It pays only if the insured dies during the term and builds <strong>no cash value</strong>. It provides the most coverage per premium dollar.</p>
<dl>
<dt>Level term</dt><dd>The death benefit stays the same for the term. <strong>Level premium term</strong> also keeps the premium level (e.g., 10-, 20- or 30-year term).</dd>
<dt>Annually renewable term (ART)</dt><dd>Renewable each year without evidence of insurability, but the <strong>premium rises</strong> each year as the insured ages. The purest form of protection.</dd>
<dt>Decreasing term</dt><dd>Level premium, but the <strong>death benefit decreases</strong> over the term. Used for debts such as a mortgage (<strong>mortgage redemption</strong>) and credit life.</dd>
<dt>Increasing term</dt><dd>The death benefit rises over time; often sold as a rider (e.g., a return-of-premium or cost-of-living rider).</dd>
</dl>
<h4>Term features</h4>
<ul>
<li><strong>Renewable</strong>: can be renewed at the end of the term without proving insurability, at the premium for the insured's attained age.</li>
<li><strong>Convertible</strong>: can be exchanged for permanent insurance without proving insurability. At <strong>attained age</strong> the premium is based on age at conversion; at <strong>original age</strong> it's based on age at issue, but the owner must pay back the premium difference.</li>
<li><strong>Re-entry</strong>: the owner can renew at a lower rate by proving insurability again.</li>
</ul>
""",
            },
            {
                "title": "Whole life insurance",
                "html": """
<p><strong>Whole life</strong> covers the insured for their entire life, with a level premium, a guaranteed death benefit and guaranteed cash value. The policy <strong>endows</strong> (the cash value equals the face amount) at <strong>age 100</strong> (or 121 under newer mortality tables); the insurer then pays the face amount to the owner.</p>
<ul>
<li>Cash value grows <strong>tax-deferred</strong> and the owner can borrow against it or surrender the policy for it.</li>
<li>The level premium is more than the cost of protection in early years and less in later years. The early overpayment builds the reserve.</li>
</ul>
<dl>
<dt>Continuous premium (straight life, ordinary life)</dt><dd>Premiums are paid until death or age 100/121. The lowest annual premium of the whole life types.</dd>
<dt>Limited-pay life</dt><dd>Premiums are paid for a limited time (e.g., 20-pay life, life paid-up at 65), but coverage lasts for life. Higher premiums and faster cash value growth.</dd>
<dt>Single premium whole life</dt><dd>One lump-sum premium buys a paid-up policy. Immediate cash value. Usually a <strong>modified endowment contract (MEC)</strong>.</dd>
</dl>
<h4>Other variations</h4>
<ul>
<li><strong>Modified whole life</strong>: lower premium for the first 3–5 years, then a higher level premium.</li>
<li><strong>Graded premium whole life</strong>: premiums rise annually for 5–10 years, then level off.</li>
<li><strong>Indexed whole life</strong>: cash value growth is tied to a stock market index, with a guaranteed minimum.</li>
</ul>
""",
            },
            {
                "title": "Flexible premium policies",
                "html": """
<dl>
<dt>Adjustable life</dt><dd>The owner can change the face amount, premium, and premium period (moving between term-like and whole-life-like coverage). Increasing the face amount may require evidence of insurability.</dd>
<dt>Universal life (UL)</dt><dd>A flexible-premium policy with an "unbundled" structure: separate accounting for the <strong>cost of insurance</strong>, <strong>expenses</strong> and <strong>cash value</strong>.
<ul>
<li>Premiums are flexible as long as the cash value covers monthly charges.</li>
<li>Cash value earns a <strong>current interest rate</strong> with a <strong>guaranteed minimum</strong>.</li>
<li><strong>Option A (Option 1)</strong>: <strong>level</strong> death benefit; the cash value is part of the face amount.</li>
<li><strong>Option B (Option 2)</strong>: <strong>increasing</strong> death benefit = face amount <strong>plus</strong> cash value.</li>
<li>Partial withdrawals are allowed and reduce the death benefit.</li>
</ul></dd>
<dt>Variable life / Variable universal life (VUL)</dt><dd>Cash value is invested in the insurer's <strong>separate account</strong> (sub-accounts like mutual funds). The policyowner chooses investments and bears the risk; cash value isn't guaranteed. Variable whole life has a guaranteed minimum death benefit; VUL combines flexible premiums with variable investments. Sellers need a life license plus FINRA registration, and buyers must receive a <strong>prospectus</strong>.</dd>
<dt>Indexed universal life</dt><dd>Interest credited is tied to an index (like the S&amp;P 500), with a cap and a floor.</dd>
</dl>
""",
            },
            {
                "title": "Specialized policies",
                "html": """
<dl>
<dt>Joint life (first-to-die)</dt><dd>Covers two or more people and pays when the <strong>first</strong> one dies. Cheaper than separate policies. Common for couples with a mortgage or business partners.</dd>
<dt>Survivorship life (second-to-die, last-to-die)</dt><dd>Covers two people and pays when the <strong>second</strong> dies. Used to pay <strong>estate taxes</strong>, which often come due after the second spouse's death. Low premium.</dd>
<dt>Juvenile life</dt><dd>Written on a child, owned by a parent or guardian. Often includes a <strong>payor benefit rider</strong> that waives premiums if the payor dies or is disabled.</dd>
<dt>Family policy</dt><dd>Whole life on the primary insured plus term coverage on the spouse and children.</dd>
<dt>Return of premium</dt><dd>Term coverage that refunds premiums if the insured survives the term.</dd>
<dt>Endowment</dt><dd>Pays the face amount if the insured dies during the period, or to the owner if they survive to the endowment date.</dd>
</dl>
""",
            },
            {
                "title": "Group life and credit life",
                "html": """
<h4>Group life</h4>
<ul>
<li>One <strong>master policy</strong> is issued to the sponsor (employer, union, association). Each covered person receives a <strong>certificate of insurance</strong> (A.R.S. 20-1265).</li>
<li>Usually <strong>annually renewable term</strong>.</li>
<li>Underwritten on the <strong>group</strong> as a whole, usually with <strong>no individual evidence of insurability</strong>. The group must be formed for a purpose <strong>other than buying insurance</strong>.</li>
<li><strong>Contributory</strong> plans: employees pay part of the premium, so at least 75% of eligible employees must enroll. <strong>Noncontributory</strong>: employer pays everything, so 100% of eligible employees must be covered.</li>
<li>Employers may deduct the premiums. The cost of employer-paid coverage up to <strong>$50,000</strong> is tax-free to the employee.</li>
<li>Eligible groups in Arizona include employers, labor unions, creditors, associations and trusteed groups (A.R.S. 20-1251).</li>
</ul>
<h4>Conversion privilege</h4>
<p>When employment or membership ends, the person may convert to an <strong>individual permanent</strong> policy <strong>without evidence of insurability</strong> by applying and paying the first premium within <strong>31 days</strong> (A.R.S. 20-1266). Premium is based on attained age. If the person dies during the 31-day period, the group death benefit is paid.</p>
<h4>Credit life</h4>
<ul>
<li>Insures a borrower's life to pay off a loan if they die. The <strong>creditor</strong> is the beneficiary.</li>
<li>Usually <strong>decreasing term</strong>, and the coverage can't exceed the amount of the debt.</li>
<li>Written as individual or group. With group credit life, the lender is the master policyholder and debtors get certificates.</li>
<li>A borrower can't be required to buy it from a specific insurer.</li>
</ul>
""",
            },
        ],
        "key_facts": [
            "Term: no cash value, most coverage per dollar",
            "ART: premium rises each year; Decreasing term: used for mortgages",
            "Convertible: switch to permanent without evidence of insurability",
            "Whole life endows at age 100 (or 121)",
            "Limited pay: coverage for life, premiums for a limited period",
            "UL Option A = level; Option B = face + cash value",
            "Variable: separate account, prospectus, FINRA + life license",
            "Joint = pays at first death; Survivorship = pays at second death (estate taxes)",
            "Group conversion: 31 days, no evidence of insurability",
            "Credit life: creditor is beneficiary; can't exceed the debt",
        ],
    },
    {
        "id": "provisions",
        "num": 5,
        "title": "Policy Provisions, Options & Riders",
        "weight": 23,
        "icon": "🧩",
        "summary": "Standard provisions, beneficiaries, settlement options, nonforfeiture, loans, dividends and riders.",
        "lessons": [
            {
                "title": "Standard policy provisions in Arizona",
                "html": """
<table class="facts">
<tr><th>Provision</th><th>What it says</th></tr>
<tr><td>Insuring clause</td><td>The insurer's promise to pay. Usually on the first page.</td></tr>
<tr><td>Entire contract (A.R.S. 20-1205)</td><td>The policy plus the attached copy of the application make up the whole contract. Nothing else can be added by reference, and only an executive officer can change it.</td></tr>
<tr><td>Consideration clause</td><td>The applicant's consideration is the application and initial premium; it states premium amount and frequency.</td></tr>
<tr><td>Owner's rights</td><td>The owner (who may not be the insured) can name and change beneficiaries, assign the policy, take loans and surrender it.</td></tr>
<tr><td>Free look</td><td>The owner can return the policy within at least <strong>10 days</strong> of delivery for a full refund. Replacement policies: <strong>30 days</strong>.</td></tr>
<tr><td>Grace period (A.R.S. 20-1203)</td><td><strong>30 days</strong> (or one month of not less than 30 days) after the due date during which coverage stays in force. If the insured dies during it, the overdue premium is deducted from the benefit.</td></tr>
<tr><td>Reinstatement (A.R.S. 20-1213)</td><td>A lapsed policy (not surrendered for cash) can be reinstated within <strong>3 years</strong> by applying in writing, proving insurability, and paying overdue premiums and any loans, with interest of no more than <strong>6%</strong> per year.</td></tr>
<tr><td>Incontestability (A.R.S. 20-1204)</td><td>After the policy has been in force <strong>2 years</strong> during the insured's lifetime, the insurer can't contest it because of misstatements on the application. Nonpayment of premium can always end coverage.</td></tr>
<tr><td>Misstatement of age or sex (A.R.S. 20-1206)</td><td>The insurer <strong>adjusts the benefit</strong> to what the premium paid would have bought at the correct age or sex. It doesn't void the policy.</td></tr>
<tr><td>Suicide (A.R.S. 20-1226)</td><td>A suicide within <strong>2 years</strong> of issue or reinstatement can be excluded; the insurer then pays a limited amount (typically a refund of premiums) instead of the face amount.</td></tr>
<tr><td>Exclusions (A.R.S. 20-1226)</td><td>Allowed exclusions include war or military service, aviation (other than as a fare-paying passenger), hazardous occupations, and death outside the continental U.S. and Canada.</td></tr>
<tr><td>Payment of claims</td><td>Proceeds are paid promptly upon proof of death. Interest is owed if payment is delayed beyond the time allowed.</td></tr>
</table>
<h4>Assignment</h4>
<ul>
<li><strong>Absolute assignment</strong>: a permanent transfer of all ownership rights to another person (e.g., a gift or sale).</li>
<li><strong>Collateral assignment</strong>: a temporary, partial transfer, usually to secure a loan. The lender is repaid first and any remainder goes to the beneficiary.</li>
<li>The owner must notify the insurer in writing; the insurer isn't responsible for the validity of an assignment.</li>
</ul>
""",
            },
            {
                "title": "Beneficiaries",
                "html": """
<ul>
<li><strong>Primary beneficiary</strong>: first in line to receive proceeds.</li>
<li><strong>Contingent (secondary) beneficiary</strong>: receives proceeds only if all primaries have died.</li>
<li><strong>Tertiary</strong>: third in line.</li>
<li>If no beneficiary survives, proceeds go to the <strong>insured's estate</strong>, which can expose them to creditors and probate.</li>
</ul>
<h4>Revocable vs. irrevocable</h4>
<p>A <strong>revocable</strong> beneficiary can be changed by the owner at any time. An <strong>irrevocable</strong> beneficiary can't be changed without that beneficiary's consent, and the owner needs their consent to take loans, assign or surrender the policy.</p>
<h4>Special designations</h4>
<ul>
<li><strong>Per stirpes</strong> ("by the bloodline"): a deceased beneficiary's share passes to their children.</li>
<li><strong>Per capita</strong> ("by the head"): proceeds are split equally among the <strong>living</strong> named beneficiaries.</li>
<li><strong>Class designation</strong>: "my children" instead of naming individuals.</li>
<li><strong>Minors</strong> can't receive proceeds directly; use a <strong>trust</strong>, a court-appointed guardian, or a custodian (UTMA).</li>
<li>A <strong>trust</strong> or the <strong>estate</strong> may be named as beneficiary.</li>
</ul>
<h4>Common disaster</h4>
<p>Under the <strong>Uniform Simultaneous Death Act</strong>, if the insured and primary beneficiary die together and it can't be determined who died first, it's presumed the <strong>insured survived</strong> the beneficiary, so proceeds go to the contingent beneficiary. A <strong>common disaster clause</strong> can require the beneficiary to survive the insured by a set period (e.g., 14 or 30 days).</p>
<h4>Spendthrift clause</h4>
<p>Protects proceeds being paid in installments from the beneficiary's creditors, and stops the beneficiary from assigning future payments.</p>
""",
            },
            {
                "title": "Settlement options",
                "html": """
<p>How the death benefit is paid. The owner can choose before death, or the beneficiary can choose at claim time.</p>
<dl>
<dt>Lump sum (cash)</dt><dd>Paid all at once. The default option. Generally income-tax free.</dd>
<dt>Interest only</dt><dd>The insurer keeps the principal and pays out interest, with the principal going later to a secondary beneficiary. Interest is taxable.</dd>
<dt>Fixed period (period certain)</dt><dd>Pays principal plus interest over a <strong>specified period of time</strong>. The time is fixed, so the payment amount is calculated.</dd>
<dt>Fixed amount</dt><dd>Pays a <strong>specified amount</strong> per payment until principal and interest are used up. The amount is fixed, so the time is calculated.</dd>
<dt>Life income</dt><dd>Payments guaranteed for the beneficiary's lifetime.
<ul>
<li><strong>Life only (straight life)</strong>: the highest payment; stops at death with nothing left for others.</li>
<li><strong>Life with period certain</strong>: payments for life, but guaranteed for at least the period (e.g., 10 years) to a secondary payee.</li>
<li><strong>Life with refund</strong>: if the payee dies before receiving the principal, the remainder is refunded (cash or installments).</li>
<li><strong>Joint and survivor</strong>: payments continue as long as either of two people lives (sometimes reduced after the first death).</li>
</ul></dd>
</dl>
""",
            },
            {
                "title": "Nonforfeiture options, loans and dividends",
                "html": """
<h4>Nonforfeiture options (A.R.S. 20-1231)</h4>
<p>Permanent policies with cash value can't simply be forfeited if premiums stop. The owner may choose:</p>
<ul>
<li><strong>Cash surrender value</strong>: take the cash; coverage ends. Gain over the premiums paid is taxable.</li>
<li><strong>Reduced paid-up insurance</strong>: use the cash value to buy a smaller, fully paid-up <strong>permanent</strong> policy of the same type.</li>
<li><strong>Extended term insurance</strong>: use the cash value to buy <strong>term</strong> insurance for the <strong>same face amount</strong> for as long as the money lasts. This is usually the <strong>automatic option</strong> if the owner doesn't choose.</li>
</ul>
<h4>Loans and withdrawals (A.R.S. 20-1209)</h4>
<ul>
<li><strong>Policy loans</strong>: borrow up to the cash value. Interest is charged, and an unpaid loan plus interest is <strong>subtracted from the death benefit</strong>. If the loan balance exceeds the cash value, the policy lapses. Insurers may delay loans (except to pay premiums) for up to <strong>6 months</strong>.</li>
<li><strong>Automatic premium loan (APL)</strong>: if a premium isn't paid by the end of the grace period, the insurer automatically borrows from the cash value to pay it, keeping the policy in force.</li>
<li><strong>Withdrawals (partial surrenders)</strong>: allowed on universal life; they reduce the cash value and death benefit and aren't repaid.</li>
</ul>
<h4>Dividend options (participating policies)</h4>
<p>Dividends are a <strong>return of unused premium</strong>, aren't guaranteed, and generally aren't taxable (interest earned on them is).</p>
<ul>
<li><strong>Cash</strong>: paid directly to the owner.</li>
<li><strong>Reduction of premium</strong>: applied to the next premium.</li>
<li><strong>Accumulation at interest</strong>: left with the insurer to earn interest (the interest is taxable).</li>
<li><strong>Paid-up additions</strong>: buy small amounts of additional paid-up permanent insurance with no evidence of insurability.</li>
<li><strong>One-year term</strong>: buys one-year term coverage, often equal to the cash value.</li>
<li><strong>Paid-up option</strong>: dividends plus cash value used to pay the policy up early.</li>
</ul>
""",
            },
            {
                "title": "Riders",
                "html": """
<h4>Disability riders</h4>
<ul>
<li><strong>Waiver of premium</strong>: if the insured becomes totally disabled, premiums are waived after a <strong>waiting period (usually 6 months)</strong>, often retroactive to the disability's start. It typically expires around age 60–65.</li>
<li><strong>Waiver of cost of insurance (universal life)</strong>: waives the monthly cost-of-insurance charges, but not the full planned premium.</li>
<li><strong>Disability income rider</strong>: pays a monthly income if the insured becomes disabled.</li>
<li><strong>Payor benefit</strong>: on juvenile policies, waives premiums if the <strong>adult payor</strong> dies or is disabled until the child reaches a certain age.</li>
</ul>
<h4>Accelerated (living) benefits (A.R.S. 20-1136)</h4>
<p>Lets the insured receive part of the death benefit early for a <strong>terminal illness</strong>, chronic illness, or for <strong>long-term care</strong> needs. The amount paid out (plus any interest) <strong>reduces the death benefit</strong>. Accelerated benefits for a terminally ill insured are generally received income-tax free.</p>
<h4>Riders covering additional insureds</h4>
<ul>
<li><strong>Spouse / other insured term rider</strong>: term coverage on another person.</li>
<li><strong>Children's term rider</strong>: covers all children, usually convertible later without evidence of insurability.</li>
<li><strong>Family term rider</strong>: covers spouse and children.</li>
</ul>
<h4>Riders that change the death benefit</h4>
<ul>
<li><strong>Accidental death benefit (ADB)</strong>: pays an extra amount (often double, "double indemnity") if death is accidental and occurs within a set time (commonly 90 days) of the accident.</li>
<li><strong>Accidental death and dismemberment (AD&amp;D)</strong>: pays the <strong>principal sum</strong> for accidental death and a <strong>capital sum</strong> (often a percentage) for loss of limbs or sight.</li>
<li><strong>Guaranteed insurability</strong>: lets the owner buy additional coverage at set ages or events (marriage, birth) <strong>without evidence of insurability</strong>.</li>
<li><strong>Cost of living</strong>: increases coverage to keep up with inflation (CPI), usually without new evidence of insurability.</li>
<li><strong>Return of premium</strong>: increasing term rider that pays back premiums paid if death occurs within a set period.</li>
</ul>
""",
            },
        ],
        "key_facts": [
            "Entire contract = policy + attached application",
            "Free look: at least 10 days; 30 days on replacements",
            "Grace period: 30 days (or one month, not less than 30)",
            "Reinstatement: within 3 years, evidence of insurability, interest ≤ 6%",
            "Incontestable after 2 years",
            "Suicide exclusion: 2 years",
            "Misstated age/sex: adjust the benefit",
            "Irrevocable beneficiary must consent to changes",
            "Per stirpes = by bloodline; per capita = by the head",
            "Simultaneous death: presume insured survived",
            "Extended term is usually the automatic nonforfeiture option",
            "Life-only settlement pays the highest income",
            "Waiver of premium: usually 6-month waiting period",
        ],
    },
    {
        "id": "annuities",
        "num": 6,
        "title": "Annuities",
        "weight": 10,
        "icon": "💰",
        "summary": "How annuities work, immediate vs. deferred, payout options, fixed and indexed products, uses, and Arizona suitability rules.",
        "lessons": [
            {
                "title": "Annuity basics",
                "html": """
<p>Life insurance protects against <strong>dying too soon</strong>. An <strong>annuity</strong> protects against <strong>living too long</strong> (outliving your money). It's the systematic liquidation of an estate.</p>
<h4>Parties</h4>
<ul>
<li><strong>Owner</strong>: buys the annuity and holds all rights. Usually the annuitant.</li>
<li><strong>Annuitant</strong>: the <strong>measuring life</strong> whose life expectancy determines benefits. Must be a natural person.</li>
<li><strong>Beneficiary</strong>: receives any remaining value if the annuitant (or owner) dies during the accumulation period.</li>
</ul>
<h4>Two phases</h4>
<ul>
<li><strong>Accumulation period (pay-in)</strong>: premiums are paid and earnings grow tax-deferred.</li>
<li><strong>Annuity period (payout, liquidation)</strong>: the value is converted into income payments. Once annuitized, the decision is generally irreversible.</li>
</ul>
<h4>Immediate vs. deferred</h4>
<ul>
<li><strong>Single premium immediate annuity (SPIA)</strong>: one lump sum, with income beginning within <strong>one year</strong> of purchase.</li>
<li><strong>Deferred annuity</strong>: income starts at a later date. It can be funded by a single premium or <strong>flexible</strong> periodic premiums.</li>
<li><strong>Surrender charges</strong> apply if money is withdrawn early in a deferred annuity, usually declining over several years. Many allow a <strong>10% free withdrawal</strong> per year.</li>
<li><strong>Death benefit</strong> during accumulation: the beneficiary usually receives the greater of the premiums paid or the current value.</li>
</ul>
""",
            },
            {
                "title": "Payout options",
                "html": """
<dl>
<dt>Life only (straight life)</dt><dd>Payments for the annuitant's life, ending at death with nothing left for beneficiaries. The <strong>highest</strong> monthly payment.</dd>
<dt>Life with period certain</dt><dd>Payments for life, but guaranteed for a minimum period (e.g., 10 years). If the annuitant dies early, the beneficiary gets the rest of the guaranteed payments.</dd>
<dt>Refund life (installment or cash refund)</dt><dd>Guarantees that the total paid out will at least equal the premium; any shortfall goes to the beneficiary.</dd>
<dt>Joint life</dt><dd>Two annuitants; payments stop at the <strong>first</strong> death.</dd>
<dt>Joint and survivor</dt><dd>Payments continue until the <strong>last</strong> annuitant dies (survivor may receive 100%, 2/3 or 1/2). The <strong>lowest</strong> monthly payment of the life options.</dd>
<dt>Annuity certain (period certain)</dt><dd>Payments for a set period only (not based on life). Payments end when the period ends even if the annuitant is alive.</dd>
</dl>
<p><strong>Pure life</strong> annuities have no refund feature; <strong>guaranteed minimum (refund)</strong> annuities promise a minimum total payout.</p>
""",
            },
            {
                "title": "Fixed, indexed and variable annuities",
                "html": """
<dl>
<dt>Fixed annuity</dt><dd>Premiums go into the insurer's <strong>general account</strong>. The insurer guarantees principal and a <strong>minimum interest rate</strong> and may credit a higher <strong>current rate</strong>. Payouts are level. The insurer bears the investment risk. The risk to the buyer is losing purchasing power to inflation.</dd>
<dt>Equity-indexed (fixed indexed) annuity</dt><dd>Interest credited is linked to a market index (e.g., S&amp;P 500), with a guaranteed minimum (floor), and limited by a <strong>participation rate</strong> and <strong>cap</strong>. A fixed product, so it needs only a life license.</dd>
<dt>Market value adjusted (MVA) annuity</dt><dd>A fixed annuity where an early surrender is adjusted up or down based on interest rate changes since purchase.</dd>
<dt>Variable annuity</dt><dd>Invested in the <strong>separate account</strong>. Values and payouts vary with investment performance and the owner bears the risk. Uses <strong>accumulation units</strong> in the pay-in phase and <strong>annuity units</strong> in payout. Needs a life license and securities registration.</dd>
</dl>
""",
            },
            {
                "title": "Uses, qualified plans and Arizona suitability",
                "html": """
<h4>Common uses</h4>
<ul>
<li><strong>Retirement income</strong> and tax-deferred growth.</li>
<li><strong>Lump-sum settlements</strong> such as structured settlements from lawsuits or lottery winnings.</li>
<li><strong>Education funds</strong> (though early withdrawals can be taxed and penalized).</li>
<li>Funding <strong>qualified plans</strong> and <strong>IRAs</strong>. Since IRAs are already tax-deferred, putting an annuity inside one adds no extra tax benefit; the reason must be another feature (guarantees, lifetime income).</li>
<li>Group annuities fund employer pension plans; individual annuities are bought by individuals.</li>
</ul>
<h4>Arizona annuity rules</h4>
<table class="facts">
<tr><th>Rule</th><th>Detail</th></tr>
<tr><td>Free look (A.R.S. 20-1233)</td><td><strong>10 days</strong>, or <strong>30 days</strong> if the owner is <strong>65 or older</strong> on the application date. Full refund.</td></tr>
<tr><td>No buyer's guide / disclosure at application (A.R.S. 20-1242.02)</td><td>Free look of at least <strong>15 days</strong></td></tr>
<tr><td>Replacement</td><td>30-day free look on a replacing contract</td></tr>
<tr><td>Suitability / best interest (A.R.S. 20-1243)</td><td>Recommendations must be in the consumer's <strong>best interest</strong> based on their consumer profile: age, income, financial situation and needs, objectives, risk tolerance, liquidity needs, time horizon, tax status, existing assets and insurance.</td></tr>
<tr><td>Producer training</td><td><strong>4 hours</strong> of approved annuity training before selling</td></tr>
<tr><td>Disclosure</td><td>A <strong>disclosure document</strong> and <strong>buyer's guide</strong> must be provided, generally at or before application</td></tr>
</table>
<p>A consumer who refuses to provide information or insists on buying against the recommendation can still buy, but the producer must document it. Insurers must supervise producers' annuity recommendations.</p>
""",
            },
        ],
        "key_facts": [
            "Annuity protects against living too long",
            "Annuitant = the measuring life",
            "Accumulation period vs. annuity (payout) period",
            "Immediate annuity: income within 1 year",
            "Life only = highest payment; joint & survivor = lowest",
            "Fixed annuity: general account, insurer bears risk",
            "Variable annuity: separate account, owner bears risk, securities license",
            "AZ free look: 10 days; 30 days if 65+",
            "15-day free look if no buyer's guide/disclosure at application",
            "Best interest suitability standard; 4 hours annuity training",
        ],
    },
    {
        "id": "tax",
        "num": 7,
        "title": "Federal Tax Considerations",
        "weight": 5,
        "icon": "🧾",
        "summary": "How life insurance and annuities are taxed, MECs and Section 1035 exchanges.",
        "lessons": [
            {
                "title": "Taxation of personal life insurance",
                "html": """
<table class="facts">
<tr><th>Item</th><th>Tax treatment</th></tr>
<tr><td>Premiums for personal coverage</td><td>Not deductible</td></tr>
<tr><td>Death benefit paid in a lump sum</td><td>Generally <strong>income-tax free</strong> to the beneficiary</td></tr>
<tr><td>Death benefit under a settlement option</td><td>Principal portion tax-free; <strong>interest portion taxable</strong></td></tr>
<tr><td>Cash value growth</td><td><strong>Tax-deferred</strong> while inside the policy</td></tr>
<tr><td>Policy loans (non-MEC)</td><td>Not taxable while the policy is in force</td></tr>
<tr><td>Dividends</td><td>Not taxable (a return of premium) until they exceed total premiums paid; <strong>interest on accumulated dividends is taxable</strong></td></tr>
<tr><td>Surrender for cash</td><td>Amount above the <strong>cost basis</strong> (premiums paid minus dividends received) is taxable as <strong>ordinary income</strong></td></tr>
<tr><td>Accelerated benefits for terminal illness</td><td>Generally income-tax free</td></tr>
</table>
<h4>Estate taxation</h4>
<p>Life insurance proceeds are included in the insured's gross estate if the insured held any <strong>incidents of ownership</strong> (the right to change beneficiaries, borrow, surrender) at death, or if proceeds are payable to the estate. Transferring a policy to someone else within <strong>3 years</strong> of death still brings it back into the estate.</p>
<h4>Business policies</h4>
<ul>
<li>Key person and buy-sell premiums: <strong>not deductible</strong>; proceeds generally tax-free.</li>
<li>Executive bonus premiums: <strong>deductible</strong> to the employer as compensation, <strong>taxable</strong> to the employee.</li>
<li>Group term life: premiums deductible to the employer; the cost of coverage above <strong>$50,000</strong> is taxable income to the employee.</li>
</ul>
""",
            },
            {
                "title": "Modified Endowment Contracts (MECs)",
                "html": """
<p>A <strong>MEC</strong> is a life policy that's funded too quickly, failing the <strong>seven-pay test</strong>: if the premiums paid in the first <strong>7 years</strong> exceed what would be needed to pay the policy up in 7 level annual premiums, it's a MEC. Once a MEC, always a MEC.</p>
<ul>
<li>The <strong>death benefit</strong> is still income-tax free.</li>
<li><strong>Distributions</strong> (withdrawals, loans, surrenders) are taxed <strong>LIFO</strong> (last in, first out): earnings come out first and are taxable as ordinary income.</li>
<li>Distributions before <strong>age 59½</strong> also generally face a <strong>10% penalty</strong> on the taxable portion.</li>
<li>Single premium whole life is usually a MEC.</li>
</ul>
""",
            },
            {
                "title": "Taxation of non-qualified annuities and 1035 exchanges",
                "html": """
<h4>Non-qualified annuities</h4>
<p>Bought with <strong>after-tax</strong> money, so the premiums are the owner's cost basis.</p>
<ul>
<li>Earnings grow <strong>tax-deferred</strong>.</li>
<li><strong>Withdrawals during accumulation</strong> are taxed <strong>LIFO</strong>: earnings come out first and are taxed as ordinary income. A <strong>10% penalty</strong> applies before age 59½ (with exceptions such as death or disability).</li>
<li><strong>Annuitized payments</strong> use the <strong>exclusion ratio</strong>: part of each payment is a tax-free return of principal and part is taxable earnings. Once all principal is recovered, payments are fully taxable.</li>
<li><strong>At death</strong>, earnings are taxable to the beneficiary as ordinary income (no step-up in basis). A surviving spouse beneficiary can continue the contract as the new owner.</li>
<li>Annuities owned by a corporation (non-natural owners) generally lose tax deferral; earnings are taxed each year.</li>
</ul>
<h4>Qualified annuities</h4>
<p>Funded with <strong>pre-tax</strong> dollars (e.g., in a traditional IRA or 401(k)), so the owner has no basis and all withdrawals are taxable. Required minimum distributions apply.</p>
<h4>Section 1035 exchanges</h4>
<p>Lets you exchange one contract for another <strong>without paying tax</strong> on the gain, if it's the same owner and insured. Allowed:</p>
<ul>
<li>Life insurance → life insurance</li>
<li>Life insurance → annuity</li>
<li>Annuity → annuity</li>
<li>Life or annuity → qualified long-term care policy</li>
</ul>
<p><strong>Not allowed:</strong> annuity → life insurance. Any cash received in the exchange ("boot") is taxable.</p>
""",
            },
        ],
        "key_facts": [
            "Lump-sum death benefit is income-tax free",
            "Interest portion of settlement options is taxable",
            "Cost basis = premiums paid minus dividends received",
            "MEC fails the 7-pay test; distributions LIFO + 10% penalty before 59½",
            "Non-qualified annuity withdrawals: LIFO, earnings taxed first",
            "Exclusion ratio for annuitized payments",
            "1035: life→life, life→annuity, annuity→annuity; NOT annuity→life",
            "Executive bonus: deductible to employer, taxable to employee",
            "Group term over $50,000: cost taxable to employee",
        ],
    },
]

SECTION_BY_ID = {s["id"]: s for s in SECTIONS}

EXAM_INFO = {
    "name": "Arizona Life Insurance Producer",
    "series": "13-31",
    "questions": 100,
    "minutes": 120,
    "passing": 70,
    "vendor": "PSI",
}

ARIZONA_NUMBERS = [
    ("Exam", "100 questions, 2 hours, 70% to pass (plus 5–10 unscored pretest items)"),
    ("Exam attempts", "4 in a 12-month period, then wait 1 year"),
    ("Apply after passing", "Within 1 year"),
    ("License term", "4 years, expires last day of birth month"),
    ("Renew", "Up to 90 days before expiration"),
    ("Continuing education", "48 hours per term, including 6 ethics"),
    ("Annuity training", "4 hours before selling annuities"),
    ("Report address/name change", "30 days"),
    ("Report out-of-state action or conviction", "30 days"),
    ("Life free look", "At least 10 days"),
    ("Annuity free look", "10 days; 30 days if 65+"),
    ("No annuity buyer's guide at application", "15-day free look"),
    ("Replacement free look", "30 days"),
    ("Replacing insurer notifies existing insurer", "Within 5 business days"),
    ("Replacement records kept", "At least 5 years"),
    ("Grace period (life)", "30 days, or one month not less than 30 days"),
    ("Reinstatement", "Within 3 years; interest max 6%"),
    ("Incontestability", "2 years"),
    ("Suicide exclusion", "2 years from issue or reinstatement"),
    ("Group conversion", "31 days, no evidence of insurability"),
    ("Policy loan deferral", "Up to 6 months"),
    ("Guaranty Fund (life)", "$300,000 death benefit; $100,000 cash value"),
    ("Guaranty Fund (annuity)", "$250,000 present value"),
    ("Do Not Call hours", "8 a.m. to 9 p.m."),
    ("CAN-SPAM opt-out", "Honor within 10 business days"),
    ("MEC test", "7-pay test; 10% penalty before 59½"),
    ("Group term tax-free", "First $50,000 of coverage"),
]
