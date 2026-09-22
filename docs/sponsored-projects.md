# Sponsored projects — CPSC 490 / 491, 2026–2027

Three companies proposed the nine projects below for this year's capstone.
Each one has an **industry mentor** who is your team's technical contact at
the sponsor for the whole year — the proposal semester (CPSC 490) and the
implementation semester (CPSC 491).

Every summary here is condensed from the sponsor's own written proposal, and
the project codes (`EL-1`, `RTX-1` … `SNX-4`) are the ones used on the
Canvas **Sponsored Projects** page and on the HW #3 preference form. The
full sponsor documents and slide decks are in Canvas under *Pages →
Sponsored Projects*; read your project's original before you write
proposal §1.

> **A summary is a starting point, not a requirement set.** The sponsor's
> paragraph is one paragraph. Turning it into stated problems (proposal
> §1.2), measurable objectives (§2), and specifications you can test (§4)
> is the work of this semester — and the first thing to ask your mentor
> about.

---

## Contacting your mentor

| | |
|---|---|
| **One voice per team** | Your team lead sends the email. Nine students emailing the same engineer separately is how a sponsor stops answering. |
| **Copy the instructor** | Always cc <kshin@fullerton.edu>. If a mentor goes quiet, I can follow up through the company. |
| **Batch your questions** | Collect them across the sprint and send five at once, each answerable in a sentence. Do not send one question a day. |
| **Allow a week** | These are working engineers. Assume a 3–5 business-day reply, and never let a mentor's silence be the reason a sprint missed — build against synthetic or public data and keep going (that is risk **R1** in [`development-plan.md`](development-plan.md)). |
| **Write down the answer** | A mentor's answer is a source. Record it in the proposal with the date, and convert anything still open into an issue so it cannot be quietly forgotten. |
| **Never commit sponsor data** | No sample files, credentials, internal document scans, or network details in the repository — public or private. Ask your mentor what is shareable *before* you put it anywhere near Git. |

---

## Edwards Lifesciences

**Mentor: Jeremy Valdecanas — <Jeremy_Valdecanas@edwards.com>**

Medical-device manufacturer (Irvine, CA); heart valves and hemodynamic
monitoring. The project is an internal engineering-data tool, so expect real
constraints around IT access and document handling.

### EL-1 · Online Materials Database

R&D and manufacturing engineers verify material compliance from
Certificates of Conformance (CoCs) and internal test reports that today
exist only as scans and PDFs — so historical data cannot be searched,
compared, or trended. This project builds two halves of one system: an
automated extraction tool that batch-processes those documents, validates
what it pulled out, and loads it into a database; and a materials database
with a GUI that lets an engineer search, filter, and visualize by vendor,
material type, and raw-material form, keeping references to material
specifications and process-control requirements, and accepting new records
by scan or upload.

**Success means** extraction and validation work with minimal manual
intervention, results stay accurate and repeatable *across vendor-specific
document formats* (not just the sample you tuned on), and the database
actually answers an engineer's question quickly.

**Out of scope:** materials characterization — you are not testing
materials, you are making existing test records usable.

**Known constraint (from the sponsor):** the database may have to be built
outside Edwards' IT environment and imported later while your access is
arranged, and IT security requirements may need to be discussed with their
IT team. Treat access as a risk with a dated early-warning sign in your
risk register, not an assumption.

---

## RTX

**RTX mentor team** (updated 22 Sep 2026 — always cc <kshin@fullerton.edu>;
per-project assignments will be confirmed with your team's match):

| Mentor | Email |
|---|---|
| Kristopher Curry | <kristopher.curry@rtx.com> |
| David DeTinne | <david.detienne@rtx.com> |
| Michelle Doung | <Michelle.H.Duong@rtx.com> |
| Cara Failer | <Cara.Failer@rtx.com> |
| Tracy Nguyen | <Tracy.Nguyen@rtx.com> |
| Alan Quach | <Alan.Quach@rtx.com> |

Aerospace and defense (Collins Aerospace, Pratt & Whitney, Raytheon). All
four projects are signal-processing or AI-for-RF work.

### RTX-1 · Explainable 6G Waveform Classification
*Sponsor employees: Kristopher Curry and Michelle Duong*

Use machine learning to automatically identify how information is encoded
onto wireless signals — the modulation and coding schemes proposed for
future 6G networks — and, critically, to make that identification
**explainable** rather than a black-box label. The sponsor states this is a
new application built from scratch, so there is no legacy system to inherit:
your architecture decisions are genuinely yours, and the *explainability*
half deserves its own objective, not a sentence at the end.

### RTX-2 · Radar Over WiFi (ROW)
*Sponsor employee: Alan Quach*

Build on existing WiFi-sensing research to make commercial WiFi hardware
perform a radar function: detecting drones or other low-flying objects
within a small area. Expect a literature-heavy §1.1 — "further exploit
existing research" means your related-work section has to establish what has
already been demonstrated before you can say what is new here.

### RTX-3 · Three AIs and Literate Programming
*Sponsor employee: Dr. David Detinne*

Chain AI tools to carry an idea all the way from a handwritten equation to a
finished product — a trained model that performs the calculation. The stated
goal is **literate programming**: the code *is* the documentation. This is
the project where the course's own AI discipline is the subject matter, so
read [`aidlc/hitl-gates.md`](aidlc/hitl-gates.md) and
[`aidlc/loop-engineering.md`](aidlc/loop-engineering.md) as domain material,
not just as course policy. A supplementary notebook on the dataflow is
posted with this project in Canvas.

### RTX-4 · Distributed Signal Capture for Multi-Node Analysis
*Sponsor employees: Cara Failer and Tracy Nguyen*

Identify and coordinate multiple capture nodes — cameras and other IoT
devices — so that entering an area lets you capture the signals of every
device within range. The hard parts are distribution and correlation across
nodes, so your system and data-flow diagrams carry more of the design than
usual; see [`design/DIAGRAMS.md`](design/DIAGRAMS.md).

---

## SonarX

**Mentor for all four projects: Erel Saul — <erel@sonarx.com>**

Blockchain data infrastructure, with indexed coverage of 130-plus chains.
Every project consumes SonarX data and ends in something a user operates —
a dashboard or a framework — so "the query returns rows" is not the finish
line; a person getting an answer is.

### SNX-1 · Polygon Prediction Market PNL and Trader Profitability Analytics

Build a profit-and-loss accounting tool for Polymarket, the leading on-chain
prediction market, from SonarX's Polygon data. Parse on-chain trades, match
positions to market resolutions, compute realized and unrealized PNL per
wallet, then rank the most profitable traders and analyze what drives their
edge. **Deliverable:** a working dashboard surfacing top performers and
their trading patterns, mirroring real institutional demand for prediction-
market PNL analysis.

### SNX-2 · On-Chain Stablecoin Flow and Wash Trading Detection

Trace stablecoin movement across wallets and exchanges using SonarX's
multi-chain data to flag suspicious activity such as wash trading and
circular transfers. Construct a transaction graph, apply heuristics and
simple machine learning to detect anomalous patterns, and visualize fund
flows over time. **Deliverable:** a dashboard that lets a user follow the
money and surfaces wallets behaving manipulatively — the sponsor names
compliance and forensics teams among their institutional clients as the real
audience.

### SNX-3 · Cross-Chain Bridge Activity and Exploit Detection

Monitor cross-chain bridge activity across SonarX's 130-plus chains and
detect the early signals of an exploit or drain **in real time**. Ingest
bridge transaction data, establish baseline flow patterns for the major
bridges, and build detection logic that fires the moment withdrawals or
liquidity movements deviate. **Deliverable:** an alerting dashboard that
could have caught recent bridge hacks as they unfolded. Note the two things
that make this hard and belong in your objectives: a *baseline* of normal,
and a false-alarm rate a human would tolerate.

### SNX-4 · Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting

Reconstruct full historical order books from SonarX's Hyperliquid data to a
standard a hedge fund would backtest against. Rebuild order-book state from
on-chain and trade data, **validate its accuracy against known market
events**, then design and backtest several algorithmic strategies on top of
it. **Deliverable:** a backtesting framework plus documented strategies with
performance results — evaluating Hyperliquid as a venue the way a
quantitative fund would. The validation step is the spine of this project;
strategy results computed on an order book nobody verified mean nothing.

---

## What to do with this page in week 1

1. Read the **original** sponsor document for your project in Canvas. This
   page is a condensation and cannot substitute for it.
2. Draft your questions, then send **one** email from your team lead, cc'ing
   the instructor.
3. Write proposal §1.2 (problem statements) from the sponsor's own words,
   then §2 (goals and objectives) as epics and user stories on the board —
   [setup guide §3 and §4](../README.md#3-the-proposal-proposalproposalmd).
4. Put every unanswered sponsor question on the board as an issue with an
   owner, and every access dependency in the risk register in
   [`development-plan.md`](development-plan.md).

---

Project selection and team assignment are governed by the syllabus and the
HW #3 preference form in Canvas, not by this page. Sponsor summaries are
reproduced from the companies' own 2026–2027 capstone proposal documents for
course use.

*Maintained by Kyoung Shin · <kshin@fullerton.edu> · terms: [all rights reserved](https://github.com/kyoungshin/CPSC490/blob/main/LICENSE) — the licence lives in the course repository, not in your copy.*
