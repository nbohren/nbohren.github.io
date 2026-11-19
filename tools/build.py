"""Generates the static pages of nbohren.github.io from one shared layout."""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])

NAV = [
    ("index.html", "About"),
    ("experience.html", "Experience"),
    ("research.html", "Research"),
    ("ml-golf.html", "ML Golf"),
    ("golf.html", "Golf"),
    ("docs/CV_Noah_Bohren.pdf", "CV"),
]

def page(filename, title, description, body):
    links = "\n".join(
        f'      <a href="{href}"{" aria-current=\"page\"" if href == filename else ""}>{label}</a>'
        for href, label in NAV
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <div class="inner">
    <a class="brand" href="index.html">Noah Bohren</a>
    <nav>
{links}
    </nav>
  </div>
</header>
<main>
{body}
</main>
<footer>
  <div class="inner">Noah Bohren &middot; Z&uuml;rich &middot; <a href="mailto:bohren.noah@gmail.com">bohren.noah@gmail.com</a></div>
</footer>
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")

# ── About ─────────────────────────────────────────────────────
page("index.html", "Noah Bohren", "Applied economist and data scientist in Zürich.", """
<section class="hero">
  <div>
    <h1>Noah Bohren</h1>
    <p class="lede">Applied economist and data scientist in Z&uuml;rich. I build data pipelines, automation and analytics that take manual work out of operational processes, and I use experiments and causal methods to check whether a change actually delivered.</p>
    <p>I hold a PhD in economics from HEC Lausanne, where my thesis on artificial intelligence, information and human behaviour received the BCV Prize 2026. Before the PhD I spent three years building reporting and BI for Mikron&rsquo;s production sites. Today I develop digital products at media-link, and in my own time I build ML Golf, a golf analytics app.</p>
    <p class="contact"><a href="mailto:bohren.noah@gmail.com">bohren.noah@gmail.com</a><a href="docs/CV_Noah_Bohren.pdf">CV (PDF)</a></p>
  </div>
  <div class="stats" style="margin:0">
    <div class="stat"><div class="num">4,000+</div><div class="lbl">participants in randomized experiments I designed and ran</div></div>
    <div class="stat"><div class="num">5</div><div class="lbl">production sites consolidated into one reporting system at Mikron</div></div>
    <div class="stat"><div class="num">+1.3</div><div class="lbl">handicap, Swiss National Team (Mid-Amateur)</div></div>
  </div>
</section>

<h2>On this site</h2>
<div class="cards">
  <a class="card" href="experience.html"><span class="kicker">Experience</span><h3>Data, automation and products</h3><p>AI expense processing at media-link, BI at Mikron, experiments at UNIL.</p></a>
  <a class="card" href="research.html"><span class="kicker">Research</span><h3>Humans working with AI</h3><p>Three experimental papers and the prize-winning thesis.</p></a>
  <a class="card" href="ml-golf.html"><span class="kicker">ML Golf</span><h3>A golf analytics app</h3><p>Strokes gained, course mapping, and an AI writer held to the facts.</p></a>
  <a class="card" href="golf.html"><span class="kicker">Golf</span><h3>Competitive golf</h3><p>Swiss National Team, four European Championships, U25 national title.</p></a>
</div>
""")

# ── Experience ────────────────────────────────────────────────
page("experience.html", "Experience · Noah Bohren", "Work experience of Noah Bohren.", """
<div class="narrow">
<h1>Experience</h1>
<p class="lede">The common thread: taking a process that runs on manual work or intuition, measuring it properly, and building the tool that improves it.</p>
</div>

<h2>Work</h2>

<div class="entry">
  <div class="entry-head"><h3>Head of Business Development &amp; Digital Products</h3><span class="meta">media-link, Neuch&acirc;tel &middot; since Sept 2026 &middot; 60%</span></div>
  <p><strong>ML Terrain.</strong> A custom mobile app for field staff that records working time and expense receipts. An AI model reads each receipt, assigns the accounting category and posts it to bookkeeping, so expenses no longer have to be typed in and checked by hand.</p>
  <p><strong>ML Sport.</strong> A new business line bringing LED display solutions to sports venues, from product concept to client acquisition. I prepare business cases for club executives and sponsors, develop new applications with engineering, such as LED screens integrated into the protective nets of hockey arenas, and evaluated hardware suppliers in China. <a href="https://nbohren.github.io/ml-sport/">See the ML Sport presentation</a>.</p>
</div>

<div class="entry">
  <div class="entry-head"><h3>Doctoral Researcher, Experimental Economics &amp; AI</h3><span class="meta">University of Lausanne &middot; 2021&ndash;2026</span></div>
  <ul>
    <li>Designed and ran randomized experiments with over 4,000 participants, using econometric methods to identify causal effects on behaviour and decisions.</li>
    <li>Built end-to-end experimental platforms and automated data pipelines in Python and R; used machine learning (NLP) and LLM APIs to process and score text data.</li>
    <li>Benchmarked generative AI against human performance on creative and strategic tasks, and studied how training with or without AI changes how people later work alongside it. <a href="research.html">Research</a>.</li>
    <li>Ran projects independently, secured grant funding, and taught exercise sessions for 50&ndash;150 students.</li>
  </ul>
</div>

<div class="entry">
  <div class="entry-head"><h3>Business Intelligence Analyst</h3><span class="meta">Mikron SA, Boudry &amp; Berlin &middot; 2018&ndash;2021</span></div>
  <ul>
    <li>Built ETL processes consolidating ERP and financial data from five international production sites into standardised reporting, automating recurring workflows with SQL, VBA and Power BI.</li>
    <li>Developed Power BI dashboards used for operational and financial decisions: project profitability, order intake, labour costs and competitor performance.</li>
    <li>Supported the Navision ERP rollout in Berlin, turning business requirements into data models and reports.</li>
  </ul>
</div>

<h2>Teaching</h2>

<div class="entry">
  <div class="entry-head"><h3>Lecturer, <em>Empirical Methods for Lawyers</em></h3><span class="meta">University of Lausanne &middot; from Fall 2027</span></div>
</div>
<div class="entry">
  <div class="entry-head"><h3>Substitute Teacher</h3><span class="meta">Lower and upper secondary schools, Canton of Neuch&acirc;tel &middot; 2014&ndash;2026</span></div>
</div>

<h2>Skills</h2>
<p>
<span class="pill">Python</span><span class="pill">R</span><span class="pill">SQL</span><span class="pill">VBA</span><span class="pill">ETL &amp; data pipelines</span><span class="pill">LLM APIs</span>
<span class="pill">Power BI</span><span class="pill">Excel</span><span class="pill">Microsoft Dynamics NAV</span><span class="pill">Git</span><span class="pill">Supabase</span><span class="pill">React Native</span>
<span class="pill">Causal inference</span><span class="pill">A/B testing</span><span class="pill">Experimental design</span><span class="pill">Econometrics</span><span class="pill">Machine learning (NLP)</span>
</p>
<p class="meta">Languages: French (native), English (C2), German (B2), Arabic (A1).</p>
""")

# ── Research ──────────────────────────────────────────────────
page("research.html", "Research · Noah Bohren", "Research papers and PhD thesis of Noah Bohren.", """
<div class="narrow">
<h1>Research</h1>
<p class="lede">My research uses large online experiments to study how people make decisions with information and with AI: when AI helps, when it misleads, and how the design of a tool changes how people rely on it.</p>
</div>

<h2>Papers</h2>

<div class="paper">
  <div class="entry-head"><h3>Training Apart, Working Together: How AI Exposure During Learning Shapes Human-AI Complementarity</h3><span class="meta">2026</span></div>
  <p class="meta">Single-authored</p>
  <p>Does training without AI produce people who are better at working with AI later? In a pre-registered experiment with 901 participants, people learned a classification task with no AI, with an AI assistant, or with the same assistant plus a badge marking its most confident suggestions, and then all worked alongside the same AI. Training with AI did not hurt later performance. The certainty badge did: participants read an unflagged suggestion as a sign the AI was wrong and overrode correct advice, which lowered their earnings.</p>
  <div class="links"><a href="https://drive.google.com/file/d/1BhfTeZSW5SOq10197jQscM5-AFH-Xc4W/view?usp=sharing">Paper (PDF)</a></div>
</div>

<div class="paper">
  <div class="entry-head"><h3>Beyond the Stars: Welfare Effects of Ratings in Differentiated Markets</h3><span class="meta">2025</span></div>
  <p class="meta">with Rustamdjan Hakimov and Lu&iacute;s Santos-Pinto</p>
  <p>Star ratings help consumers when everyone agrees which product is better. When products instead suit different tastes, standard ratings do not improve how well people are matched to products. Combining a Bayesian model with a large pre-registered experiment, we show that filtered ratings and algorithmic recommendations recover the lost welfare.</p>
  <div class="links"><a href="https://people.unil.ch/luispedrosantospinto/files/2025/12/beyond_the_stars_2025_12_15-1.pdf">Paper (PDF)</a></div>
</div>

<div class="paper">
  <div class="entry-head"><h3>Creative and Strategic Capabilities of Generative AI: Evidence from Large-Scale Experiments</h3><span class="meta">2024</span></div>
  <p class="meta">with Rustamdjan Hakimov and Rafael Lalive &middot; Revise &amp; resubmit at <em>Experimental Economics</em></p>
  <p>We compare AI chatbots with a representative sample of US adults. Ideas from ChatGPT were rated more creative than human ideas, and AI assistance raised human creativity, though not to ChatGPT&rsquo;s level. Raters could not tell AI from human ideas but scored the ones they believed were AI-generated lower. In a strategic game, ChatGPT adapted to its opponent, but humans adapted more successfully on average.</p>
  <div class="links"><a href="https://www.iza.org/publications/dp17302">IZA Discussion Paper 17302</a><a href="https://ideas.repec.org/p/cpr/ceprdp/19507.html">CEPR Discussion Paper 19507</a></div>
</div>

<h2>PhD thesis</h2>
<div class="paper">
  <div class="entry-head"><h3>Three Experiments on the Economics of Artificial Intelligence, Information, and Human Behavior</h3><span class="meta">HEC Lausanne, 2026</span></div>
  <p class="meta">Supervised by Rustamdjan Hakimov and Lu&iacute;s Santos-Pinto</p>
  <p>Awarded the <strong>BCV Prize 2026</strong> (Prix de la Banque Cantonale Vaudoise) for an outstanding doctoral thesis at HEC Lausanne.</p>
  <div class="links"><a href="https://iris.unil.ch/entities/publication/d401e9a3-a9f8-4bf3-a355-f189f85e8ec5">Thesis</a></div>
</div>

<h2>Training</h2>
<p>Swiss Doctoral Programme in Economics, Study Center Gerzensee (2021&ndash;2022): intensive first-year core training in microeconomics, macroeconomics and econometrics.</p>
<p>Causal inference and synthetic control with Alberto Abadie (Gerzensee, 2025); data analytics and causal machine learning (University of Fribourg, 2024); behavioural economics and experimental research (CUSO, 2023 and 2026).</p>
""")

# ── ML Golf ───────────────────────────────────────────────────
page("ml-golf.html", "ML Golf · Noah Bohren", "ML Golf, an iOS golf analytics app built by Noah Bohren.", """
<div class="narrow">
<h1>ML Golf</h1>
<p class="lede">A golf analytics app that shows a player where they actually gain and lose strokes, built end to end: data pipeline, back end, AI layer and the iOS app.</p>
</div>

<div class="shots">
  <figure><img src="assets/img/golf-analysis.jpg" alt="Analysis screen: strokes gained by part of the game" loading="lazy"><figcaption>Strokes gained by part of the game, against a chosen handicap benchmark.</figcaption></figure>
  <figure><img src="assets/img/golf-tee.jpg" alt="Tee shot analysis with a dispersion plot of drives" loading="lazy"><figcaption>Tee shots: where the drives land, and what they are worth.</figcaption></figure>
  <figure><img src="assets/img/golf-trends.jpg" alt="Trends screen with a score trend line" loading="lazy"><figcaption>Trends: each measure flagged as clearly changing or still too early to tell.</figcaption></figure>
</div>

<h2>The problem</h2>
<p class="narrow">A scorecard tells a golfer how many strokes they took, not where they lost them. Strokes gained, the method used to rank PGA Tour players, answers that by comparing every shot with what a benchmark player would need from the same position. It needs the position of every shot, and entering that by hand is the reason most amateurs never do it.</p>

<h2>What I built</h2>
<div class="entry">
  <h3>Shot data with little typing</h3>
  <p>Each shot is stored as a GPS position on a satellite map of the hole. The app infers the lie (fairway, rough, bunker, green) from course polygons, so the golfer taps where the ball is rather than describing it.</p>
</div>
<div class="entry">
  <h3>A course database</h3>
  <p>The official Swiss clubs are mapped from OpenStreetMap, refreshed monthly by a GitHub Action, with a world course directory for search. A Python pipeline refines stale map data against current swisstopo aerial imagery using Meta&rsquo;s Segment Anything model: where the two agree the polygon is accepted automatically, where they diverge it is flagged for review.</p>
</div>
<div class="entry">
  <h3>Statistics that say how sure they are</h3>
  <p>Strokes gained per part of the game, against a benchmark handicap the golfer chooses. Trends are labelled as clearly changing or too early to tell, and every measure has a plain-language explanation of its method.</p>
</div>
<div class="entry">
  <h3>An AI writer held to the facts</h3>
  <p>The app decides which facts about a round are true and worth saying; the Claude API only phrases them, in a voice the golfer picks, and the app checks every line against the facts before showing it. Each call&rsquo;s cost is metered against monthly per-user and daily global caps. The same back end uses Claude to moderate anything other golfers can see, text and photos, and nothing is shown until it passes.</p>
</div>
<div class="entry">
  <h3>Stack</h3>
  <p><span class="pill">React Native (Expo)</span><span class="pill">MapLibre</span><span class="pill">Supabase: Postgres, auth, edge functions</span><span class="pill">Claude API</span><span class="pill">RevenueCat</span><span class="pill">Python</span><span class="pill">Segment Anything</span><span class="pill">OpenStreetMap</span><span class="pill">swisstopo</span><span class="pill">GitHub Actions</span></p>
</div>

<h2>Open question</h2>
<p class="narrow">Strokes gained is only as good as its benchmark, and amateur baselines are commercially locked. Building my own from users&rsquo; shot data is a statistics problem as much as an engineering one, and one where the tools of an economist apply directly.</p>
""")

# ── Golf ──────────────────────────────────────────────────────
page("golf.html", "Golf · Noah Bohren", "Competitive golf: Swiss National Team (Mid-Amateur).", """
<div class="narrow">
<h1>Golf</h1>
<p class="lede">I play competitive amateur golf for Switzerland, and it is the sport behind <a href="ml-golf.html">ML Golf</a>.</p>
</div>

<div class="stats">
  <div class="stat"><div class="num">+1.3</div><div class="lbl">handicap index</div></div>
  <div class="stat"><div class="num">4</div><div class="lbl">European Championships for Switzerland</div></div>
  <div class="stat"><div class="num">2021</div><div class="lbl">Swiss U25 National Champion</div></div>
</div>

<h2>Competition</h2>
<div class="entry">
  <div class="entry-head"><h3>Swiss National Team, Mid-Amateur</h3><span class="meta">SwissGolf &middot; since 2024</span></div>
  <p>Selected to represent Switzerland internationally; competed in four European Championships.</p>
</div>
<div class="entry">
  <div class="entry-head"><h3>Swiss U25 National Champion</h3><span class="meta">Swiss Golf National Final U25, Golfclub Lipperswil &middot; 2021</span></div>
</div>

<h2>Club</h2>
<div class="entry">
  <div class="entry-head"><h3>Vice-Captain, Golf &amp; Country Club de Neuch&acirc;tel</h3><span class="meta">2022&ndash;2025</span></div>
  <p>Member of the six-person executive board of a club with annual revenues of CHF 2.5 million.</p>
</div>

<figure style="margin-top:32px">
  <img class="wide" src="assets/img/course-neuchatel.jpg" alt="Aerial view of a hole at Golf &amp; Country Club de Neuch&acirc;tel" loading="lazy">
  <figcaption>Golf &amp; Country Club de Neuch&acirc;tel, as rendered in ML Golf. Imagery: Federal Office of Topography swisstopo (SWISSIMAGE).</figcaption>
</figure>
""")

print("built", sorted(p.name for p in OUT.glob("*.html")))
