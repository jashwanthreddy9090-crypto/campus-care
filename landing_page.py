"""Public Campus Care 360 landing page shown to visitors before sign-in."""

LANDING_PAGE = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f7f1e8">
<meta name="description" content="Campus Care 360 — one place to raise campus concerns, follow updates and find support.">
<title>Campus Care 360 | Your campus, cared for</title>
<style>
:root{--cream:#f7f1e8;--paper:#fffdf9;--ink:#211d1a;--muted:#716960;--red:#a92f2b;--red-dark:#84231f;--gold:#c8a66a;--line:#e9dfd2;--shadow:0 22px 70px rgba(57,37,25,.09)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--cream);color:var(--ink);font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.6}a{color:inherit;text-decoration:none}.wrap{width:min(1160px,calc(100% - 44px));margin:auto}
header{height:82px;display:flex;align-items:center;border-bottom:1px solid rgba(120,91,65,.13);background:rgba(247,241,232,.92);position:sticky;top:0;z-index:10;backdrop-filter:blur(14px)}.nav{display:flex;align-items:center;justify-content:space-between;gap:24px}.brand{display:flex;align-items:center;gap:12px;font-weight:800;letter-spacing:-.5px}.mark{width:43px;height:43px;border-radius:14px;background:var(--ink);display:grid;place-items:center;color:var(--gold);font-size:15px;font-weight:900;letter-spacing:-1px}.brand small{display:block;color:var(--muted);font-size:10px;letter-spacing:2px;text-transform:uppercase;font-weight:700;margin-top:-4px}.navlinks{display:flex;align-items:center;gap:28px;color:#5e554d;font-size:14px;font-weight:650}.navlinks a:hover{color:var(--red)}.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;border-radius:999px;padding:13px 22px;font-weight:750;font-size:14px;transition:.2s;border:1px solid transparent}.btn-red{background:var(--red);color:white;box-shadow:0 8px 22px rgba(169,47,43,.18)}.btn-red:hover{background:var(--red-dark);transform:translateY(-2px)}.btn-light{border-color:#d8cabb;background:transparent}.btn-light:hover{background:#fffaf2}
.hero{padding:86px 0 76px;overflow:hidden}.hero-grid{display:grid;grid-template-columns:1.08fr .92fr;gap:54px;align-items:center}.eyebrow{display:inline-flex;align-items:center;gap:9px;color:var(--red);font-size:11px;letter-spacing:2.1px;text-transform:uppercase;font-weight:850}.eyebrow:before{content:"";width:24px;height:2px;background:var(--gold)}h1{font-size:clamp(42px,6vw,72px);line-height:1.04;letter-spacing:-3.8px;margin:20px 0 22px;max-width:690px}h1 span{color:var(--red)}.hero-copy{max-width:550px;color:var(--muted);font-size:17px;line-height:1.8}.hero-actions{display:flex;gap:13px;flex-wrap:wrap;margin-top:30px}.micro{display:flex;align-items:center;gap:10px;color:#776d62;font-size:12px;margin-top:23px}.dot{width:7px;height:7px;border-radius:50%;background:#6d9a70;box-shadow:0 0 0 4px #6d9a7020}
.visual{position:relative;min-height:440px;display:grid;place-items:center}.orb{position:absolute;width:390px;height:390px;border-radius:50%;background:#eadbca;right:12px;top:20px}.orb:after{content:"";position:absolute;inset:28px;border:1px solid rgba(169,47,43,.2);border-radius:50%}.mock{position:relative;width:min(390px,100%);background:var(--paper);border:1px solid #e8ded1;border-radius:24px;padding:22px;box-shadow:var(--shadow);transform:rotate(2deg)}.mock-top{display:flex;justify-content:space-between;align-items:center;padding-bottom:18px;border-bottom:1px solid var(--line)}.mock-label{font-size:11px;color:var(--muted);font-weight:750;letter-spacing:1.3px}.mock-pill{background:#edf3e9;color:#52764e;border-radius:99px;padding:6px 10px;font-size:10px;font-weight:800}.mock h3{font-size:20px;margin:20px 0 4px}.mock p{color:var(--muted);font-size:12px;margin:0}.ticket{margin-top:18px;border:1px solid var(--line);border-radius:15px;padding:15px}.ticket-row{display:flex;justify-content:space-between;align-items:center;gap:10px}.ticket strong{font-size:13px}.ticket small{display:block;color:var(--muted);font-size:10px;margin-top:4px}.tag{font-size:10px;padding:5px 8px;border-radius:7px;background:#f8e8e4;color:var(--red);font-weight:800}.progress{height:5px;background:#eee5dc;border-radius:8px;margin-top:14px;overflow:hidden}.progress i{display:block;width:68%;height:100%;background:var(--gold);border-radius:8px}.stat-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}.stat{background:#f8f3eb;border-radius:13px;padding:13px}.stat b{font-size:18px;display:block}.stat span{font-size:10px;color:var(--muted)}
.section{padding:76px 0}.section-white{background:var(--paper)}.section-head{text-align:center;max-width:650px;margin:0 auto 38px}.section-head h2{font-size:clamp(30px,4vw,44px);line-height:1.13;letter-spacing:-1.8px;margin:13px 0}.section-head p{color:var(--muted);margin:0}.features{display:grid;grid-template-columns:repeat(3,1fr);gap:17px}.feature{background:#fff;border:1px solid var(--line);border-radius:19px;padding:25px;min-height:205px}.feature-icon{width:43px;height:43px;border-radius:13px;background:#f8e9e4;color:var(--red);display:grid;place-items:center;font-size:19px}.feature h3{font-size:17px;margin:17px 0 7px}.feature p{font-size:13px;color:var(--muted);margin:0;line-height:1.7}.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:30px}.step{border-top:1px solid var(--line);padding-top:20px}.step-no{color:var(--red);font-size:12px;font-weight:900;letter-spacing:1.5px}.step h3{font-size:18px;margin:9px 0 5px}.step p{font-size:13px;color:var(--muted);margin:0}
.cta{padding:0 0 76px}.cta-panel{background:var(--ink);color:white;border-radius:24px;padding:46px;display:flex;justify-content:space-between;align-items:center;gap:30px}.cta-panel h2{font-size:clamp(26px,4vw,38px);line-height:1.15;letter-spacing:-1.2px;margin:0 0 9px}.cta-panel p{color:#c5bbb0;margin:0;font-size:14px}.cta-panel .btn{background:var(--gold);color:#211d1a;white-space:nowrap}
footer{border-top:1px solid var(--line);padding:25px 0;color:var(--muted);font-size:12px}.foot{display:flex;justify-content:space-between;gap:15px;flex-wrap:wrap}
@media(max-width:800px){.hero{padding:60px 0 35px}.hero-grid{grid-template-columns:1fr;gap:12px}.visual{min-height:390px}.orb{right:calc(50% - 185px);width:350px;height:350px}.mock{max-width:370px}.features{grid-template-columns:1fr 1fr}.navlinks{gap:14px}.navlinks a:not(.btn){display:none}.cta-panel{padding:32px;align-items:flex-start;flex-direction:column}}
@media(max-width:520px){.wrap{width:min(100% - 30px,1160px)}header{height:70px}.brand{font-size:14px}.mark{width:39px;height:39px}.nav .btn{padding:10px 15px}.hero{padding-top:48px}h1{letter-spacing:-2.5px}.hero-copy{font-size:15px}.visual{min-height:355px}.orb{width:310px;height:310px;right:calc(50% - 155px)}.mock{padding:17px;border-radius:20px}.features,.steps{grid-template-columns:1fr}.section{padding:58px 0}.cta{padding-bottom:55px}.cta-panel{padding:27px 23px}}
</style>
</head>
<body>
<header><div class="wrap nav">
<a class="brand" href="/" aria-label="Campus Care 360 home"><span class="mark">C360</span><span>Campus Care 360<small>Campus support, connected</small></span></a>
<nav class="navlinks" aria-label="Main navigation"><a href="#features">Features</a><a href="#how-it-works">How it works</a><a class="btn btn-red" href="/login">Student / Admin Login <span aria-hidden="true">→</span></a></nav>
</div></header>
<main>
<section class="hero"><div class="wrap hero-grid">
<div><div class="eyebrow">A better campus experience</div><h1>Your campus.<br><span>Cared for.</span></h1>
<p class="hero-copy">A simpler way to raise campus concerns, keep track of updates and find the support you need — all in one place.</p>
<div class="hero-actions"><a class="btn btn-red" href="/login">Get started <span aria-hidden="true">→</span></a><a class="btn btn-light" href="#features">Explore features</a></div>
<div class="micro"><span class="dot"></span> A dedicated space for your campus community</div></div>
<div class="visual" aria-label="Preview of the Campus Care 360 complaint tracking dashboard"><div class="orb"></div><div class="mock">
<div class="mock-top"><div class="brand"><span class="mark">C360</span><span style="font-size:12px">Campus Care<small>STUDENT SPACE</small></span></div><span class="mock-pill">● Updates</span></div>
<h3>Good things start with being heard.</h3><p>Keep your campus requests organised.</p>
<div class="ticket"><div class="ticket-row"><div><strong>Hostel maintenance</strong><small>Request #CC360-1024</small></div><span class="tag">In progress</span></div><div class="progress"><i></i></div></div>
<div class="stat-grid"><div class="stat"><b>01</b><span>Raise a concern</span></div><div class="stat"><b>02</b><span>Follow its status</span></div></div>
</div></div>
</div></section>
<section class="section section-white" id="features"><div class="wrap"><div class="section-head"><div class="eyebrow">One campus. One place.</div><h2>Support that keeps campus life moving.</h2><p>Useful tools to help students connect with the people and services that keep campus running.</p></div>
<div class="features">
<article class="feature"><div class="feature-icon">✦</div><h3>Raise complaints</h3><p>Submit hostel or campus concerns with the details needed to help the right team respond.</p></article>
<article class="feature"><div class="feature-icon">↗</div><h3>Track progress</h3><p>Check the status of your submitted complaints and stay informed as they move forward.</p></article>
<article class="feature"><div class="feature-icon">⌕</div><h3>Lost &amp; Found</h3><p>Post lost or found belongings, add a photo and connect with the campus community.</p></article>
<article class="feature"><div class="feature-icon">▤</div><h3>Campus notices</h3><p>Keep important campus information and announcements easy to find.</p></article>
<article class="feature"><div class="feature-icon">♡</div><h3>Help &amp; emergency contacts</h3><p>Find the support information and essential contact details you may need.</p></article>
<article class="feature"><div class="feature-icon">◎</div><h3>One connected portal</h3><p>A clear place for students and authorised administrators to access their respective tools.</p></article>
</div></div></section>
<section class="section" id="how-it-works"><div class="wrap"><div class="section-head"><div class="eyebrow">Simple by design</div><h2>From concern to clarity.</h2><p>Get started in a few straightforward steps.</p></div>
<div class="steps"><article class="step"><span class="step-no">01 / SIGN IN</span><h3>Access your account</h3><p>Use the account credentials provided by your campus administrator.</p></article><article class="step"><span class="step-no">02 / TAKE ACTION</span><h3>Submit or explore</h3><p>Raise a concern, browse campus information or post a Lost &amp; Found listing.</p></article><article class="step"><span class="step-no">03 / STAY INFORMED</span><h3>Follow the updates</h3><p>Return to your portal to check progress and view relevant information.</p></article></div></div></section>
<section class="cta"><div class="wrap"><div class="cta-panel"><div><h2>Make your campus experience smoother.</h2><p>Sign in to continue to your Campus Care 360 portal.</p></div><a class="btn" href="/login">Continue to login <span aria-hidden="true">→</span></a></div></div></section>
</main>
<footer><div class="wrap foot"><span>© Campus Care 360. Built for a more connected campus.</span><span>Student support · Campus services · Community care</span></div></footer>
</body>
</html>
"""
