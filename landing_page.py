"""Public, responsive Campus Care 360 landing page shown before sign-in."""

LANDING_PAGE = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#f7f3ec">
<meta name="description" content="Campus Care 360 is a campus complaint management and hostel support platform. Submit campus concerns, track complaint updates and access Lost &amp; Found and student support in one place.">
<meta name="keywords" content="Campus Care 360, campus complaint management, hostel complaint tracking, student support portal, campus helpdesk, Lost and Found">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://campus-care-pearl-one.vercel.app/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Campus Care 360">
<meta property="og:title" content="Campus Care 360 | Campus Complaint &amp; Hostel Support Portal">
<meta property="og:description" content="A connected campus support portal to submit concerns, track complaints and access student support services.">
<meta property="og:url" content="https://campus-care-pearl-one.vercel.app/">
<meta property="og:image" content="https://campus-care-pearl-one.vercel.app/campus-care-logo.png">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Campus Care 360 | Campus Support Portal">
<meta name="twitter:description" content="Submit campus concerns, track complaint updates and access student support in one place.">
<meta name="twitter:image" content="https://campus-care-pearl-one.vercel.app/campus-care-logo.png">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://campus-care-pearl-one.vercel.app/#website",
      "url": "https://campus-care-pearl-one.vercel.app/",
      "name": "Campus Care 360",
      "description": "Campus complaint management and student support portal."
    },
    {
      "@type": "SoftwareApplication",
      "name": "Campus Care 360",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "Web",
      "url": "https://campus-care-pearl-one.vercel.app/",
      "description": "A campus support portal for submitting campus and hostel complaints, tracking updates and managing Lost & Found listings."
    }
  ]
}
</script>
<title>Campus Care 360 | Campus Complaint &amp; Hostel Support Portal</title>
<style>
:root{--cream:#f7f3ec;--paper:#fffdfa;--ink:#241d1c;--muted:#786e68;--red:#8f2430;--red2:#a8323c;--gold:#c5a56b;--line:#e9e0d5;--sage:#647c68;--shadow:0 24px 70px rgba(58,34,27,.10)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--cream);color:var(--ink);font-family:Arial,Helvetica,sans-serif;line-height:1.6}a{color:inherit;text-decoration:none}.wrap{width:min(1160px,calc(100% - 48px));margin:auto}
.topline{height:4px;background:linear-gradient(90deg,var(--red),var(--gold),#e5d4b8)}
header{height:88px;display:flex;align-items:center;background:rgba(247,243,236,.94);border-bottom:1px solid rgba(112,85,67,.12);position:sticky;top:0;z-index:20;backdrop-filter:blur(16px)}
.nav{display:flex;align-items:center;justify-content:space-between;gap:24px}
.brand{display:flex;align-items:center;gap:13px}.brand img{width:58px;height:58px;object-fit:contain;display:block}.brand-name{font-size:17px;font-weight:800;letter-spacing:-.6px;line-height:1.2}.brand-tag{font-size:9px;letter-spacing:2px;color:#8a7770;text-transform:uppercase;font-weight:700;margin-top:5px}
.navlinks{display:flex;align-items:center;gap:32px;font-size:13px;font-weight:700;color:#685c55}.navlinks>a:not(.btn):hover{color:var(--red)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:12px;padding:14px 23px;border-radius:5px;font-size:13px;font-weight:800;letter-spacing:.1px;transition:transform .2s,background .2s,border-color .2s}.btn:hover{transform:translateY(-2px)}.btn-primary{background:var(--red);color:white;box-shadow:0 9px 22px rgba(143,36,48,.16)}.btn-primary:hover{background:#741c27}.btn-outline{border:1px solid #cfc1b2;background:transparent}.btn-outline:hover{background:#fffaf4;border-color:var(--gold)}
.hero{padding:82px 0 76px;position:relative;overflow:hidden}.hero:before{content:"";position:absolute;width:570px;height:570px;border:1px solid rgba(197,165,107,.24);border-radius:50%;right:-260px;top:-310px}.hero-grid{display:grid;grid-template-columns:1fr .94fr;align-items:center;gap:70px}
.kicker{display:flex;align-items:center;gap:11px;color:var(--red);font-size:10px;letter-spacing:2.6px;text-transform:uppercase;font-weight:800}.kicker:before{content:"";width:30px;height:1px;background:var(--gold)}
h1{font-family:Georgia,"Times New Roman",serif;font-size:clamp(48px,6.2vw,76px);font-weight:600;letter-spacing:-2.3px;line-height:1.06;margin:23px 0 22px;max-width:650px}h1 em{font-style:normal;color:var(--red)}
.lead{font-size:16px;color:var(--muted);line-height:1.9;max-width:510px;margin:0}.actions{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:31px}.trust{display:flex;align-items:center;gap:11px;margin-top:30px;color:#857970;font-size:11px}.trust-line{width:28px;height:1px;background:var(--gold)}
.hero-art{position:relative;min-height:470px;display:flex;align-items:center;justify-content:center}.art-halo{position:absolute;width:410px;height:410px;border-radius:50%;background:radial-gradient(circle at 45% 42%,#fdfbf6 0,#eee3d4 58%,#e7d8c5 100%);border:1px solid #e2d3c0}.art-halo:after{content:"";position:absolute;inset:18px;border:1px solid rgba(143,36,48,.13);border-radius:50%}
.dashboard{position:relative;width:min(390px,100%);background:var(--paper);border:1px solid #e8ded3;border-radius:13px;padding:23px;box-shadow:var(--shadow);transform:rotate(1.3deg)}
.dash-head{display:flex;align-items:center;justify-content:space-between;padding-bottom:17px;border-bottom:1px solid var(--line)}.dash-brand{display:flex;align-items:center;gap:9px;font-weight:800;font-size:12px}.dash-brand img{width:35px;height:35px;object-fit:contain}.live{font-size:9px;color:var(--sage);font-weight:800;letter-spacing:1px}.live:before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:#7c9c79;margin-right:6px}
.dash-title{font-family:Georgia,"Times New Roman",serif;font-size:23px;line-height:1.2;margin:21px 0 5px}.dash-sub{font-size:11px;color:var(--muted)}
.request{border:1px solid var(--line);border-radius:8px;padding:15px;margin-top:20px}.request-top{display:flex;align-items:center;justify-content:space-between;gap:10px}.request strong{font-size:12px}.request small{display:block;color:#8c8179;font-size:9px;margin-top:4px}.status{background:#f3e8df;color:var(--red);font-size:9px;font-weight:800;padding:5px 8px;border-radius:3px;white-space:nowrap}.bar{height:4px;background:#eee8df;margin-top:14px;border-radius:9px;overflow:hidden}.bar i{display:block;width:68%;height:100%;background:var(--gold)}
.dash-bottom{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}.mini{background:#f7f3ec;border-radius:7px;padding:13px}.mini b{font-family:Georgia,"Times New Roman",serif;font-size:21px;display:block;color:var(--red)}.mini span{font-size:9px;color:#81766d}
.float-note{position:absolute;right:-8px;bottom:28px;background:var(--paper);border:1px solid var(--line);padding:13px 16px;border-radius:7px;box-shadow:0 12px 32px rgba(58,34,27,.09);font-size:10px;font-weight:800}.float-note span{color:var(--sage);margin-right:7px}
.strip{background:#2b2220;color:#f8f1e8;padding:19px 0}.strip-inner{display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap}.strip-item{display:flex;align-items:center;gap:10px;font-size:11px;color:#e1d6c9;letter-spacing:.2px}.strip-mark{color:var(--gold);font-size:16px}
.section{padding:86px 0}.section-white{background:var(--paper)}.section-head{max-width:650px;margin:0 auto 43px;text-align:center}.section-head .kicker{justify-content:center}.section-head h2{font-family:Georgia,"Times New Roman",serif;font-size:clamp(34px,4.4vw,49px);font-weight:600;letter-spacing:-1.3px;line-height:1.16;margin:17px 0 12px}.section-head p{font-size:14px;color:var(--muted);margin:0}
.features{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.feature{background:#fff;border:1px solid var(--line);padding:27px 25px 29px;min-height:208px;transition:transform .2s,box-shadow .2s}.feature:hover{transform:translateY(-4px);box-shadow:0 15px 35px rgba(58,34,27,.07)}.feature-icon{width:43px;height:43px;border:1px solid #ead9c6;color:var(--red);display:grid;place-items:center;font-size:19px;border-radius:50%}.feature h3{font-size:15px;margin:18px 0 7px}.feature p{font-size:12px;line-height:1.8;color:var(--muted);margin:0}
.how-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:75px;align-items:start}.how-intro h2{font-family:Georgia,"Times New Roman",serif;font-size:43px;line-height:1.13;letter-spacing:-1px;margin:16px 0}.how-intro p{color:var(--muted);font-size:13px;line-height:1.9}.steps{display:grid;gap:0}.step{display:grid;grid-template-columns:54px 1fr;gap:16px;padding:20px 0;border-bottom:1px solid var(--line)}.step:first-child{padding-top:0}.step-no{font-family:Georgia,"Times New Roman",serif;font-size:22px;color:var(--gold)}.step h3{font-size:14px;margin:2px 0 5px}.step p{font-size:12px;color:var(--muted);margin:0;line-height:1.8}
.cta{padding:0 0 85px}.cta-box{position:relative;overflow:hidden;background:#2b2220;color:#fff8ef;padding:49px 54px;display:flex;align-items:center;justify-content:space-between;gap:28px}.cta-box:after{content:"360";position:absolute;right:220px;top:-65px;font-family:Georgia,"Times New Roman",serif;font-size:190px;color:rgba(255,255,255,.035);pointer-events:none}.cta-box h2{font-family:Georgia,"Times New Roman",serif;font-size:34px;line-height:1.2;margin:0 0 9px;position:relative}.cta-box p{font-size:12px;color:#d2c4b8;margin:0;position:relative}.cta-box .btn{background:var(--gold);color:#2b2220;white-space:nowrap;position:relative;z-index:1}
footer{border-top:1px solid var(--line);padding:24px 0;color:#857970;font-size:10px}.foot{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}.foot-brand{display:flex;align-items:center;gap:9px;font-weight:800;color:#514640}.foot-brand img{width:27px;height:27px;object-fit:contain}
@media(max-width:850px){.hero-grid{grid-template-columns:1fr;gap:20px}.hero-art{min-height:420px}.art-halo{width:370px;height:370px}.how-grid{grid-template-columns:1fr;gap:35px}.navlinks{gap:18px}.features{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.wrap{width:calc(100% - 32px)}header{height:75px}.brand img{width:48px;height:48px}.brand-name{font-size:15px}.navlinks>a:not(.btn){display:none}.navlinks .btn{padding:11px 14px;font-size:11px}.hero{padding:55px 0 38px}h1{font-size:51px;letter-spacing:-1.8px}.lead{font-size:14px}.hero-art{min-height:350px}.art-halo{width:300px;height:300px}.dashboard{padding:17px;max-width:350px}.float-note{right:-2px;bottom:10px}.strip-inner{justify-content:flex-start;gap:13px 23px}.strip-item{font-size:10px}.section{padding:63px 0}.section-head{margin-bottom:30px}.features{grid-template-columns:1fr;gap:12px}.feature{min-height:0;padding:22px}.how-intro h2{font-size:36px}.cta{padding-bottom:60px}.cta-box{padding:31px 24px;align-items:flex-start;flex-direction:column}.cta-box h2{font-size:29px}.cta-box:after{right:-5px;top:-35px}.foot{align-items:flex-start;flex-direction:column}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*:before,*:after{transition:none!important}}
</style>
</head>
<body>
<div class="topline"></div>
<header><div class="wrap nav">
<a class="brand" href="/" aria-label="Campus Care 360 home"><img src="{{ url_for('campus_care_logo', v='original-20261011') }}" alt="Original Campus Care 360 logo"><span><span class="brand-name">Campus Care 360</span><span class="brand-tag">Campus support, connected</span></span></a>
<nav class="navlinks" aria-label="Main navigation"><a href="#features">What we offer</a><a href="#how-it-works">How it works</a><a class="btn btn-primary" href="/login">Sign in <span aria-hidden="true">↗</span></a></nav>
</div></header>
<main>
<section class="hero"><div class="wrap hero-grid">
<div><div class="kicker">A more thoughtful campus experience</div><h1>A campus that<br><em>cares.</em> A place<br>to be heard.</h1>
<p class="lead">Campus life moves better when support is simple. Raise concerns, follow updates and find the help you need — all through one connected campus space.</p>
<div class="actions"><a class="btn btn-primary" href="/login">Enter your campus portal <span aria-hidden="true">→</span></a><a class="btn btn-outline" href="#features">Discover more</a></div>
<div class="trust"><span class="trust-line"></span> Designed to bring campus support closer to students</div></div>
<div class="hero-art"><div class="art-halo"></div><div class="dashboard">
<div class="dash-head"><div class="dash-brand"><img src="{{ url_for('campus_care_logo', v='original-20261011') }}" alt="">Campus Care 360</div><span class="live">CONNECTED</span></div>
<div class="dash-title">Your campus,<br>all in one place.</div><div class="dash-sub">A clearer way to stay on top of campus life.</div>
<div class="request"><div class="request-top"><div><strong>Hostel maintenance</strong><small>Example request · Status overview</small></div><span class="status">In progress</span></div><div class="bar"><i></i></div></div>
<div class="dash-bottom"><div class="mini"><b>01</b><span>Raise a concern</span></div><div class="mini"><b>02</b><span>Follow updates</span></div></div>
</div><div class="float-note"><span>●</span> Your voice matters here</div></div>
</div></section>
<div class="strip"><div class="wrap strip-inner"><div class="strip-item"><span class="strip-mark">✳</span> Student-first support</div><div class="strip-item"><span class="strip-mark">◇</span> Clear complaint tracking</div><div class="strip-item"><span class="strip-mark">⌂</span> Connected campus services</div><div class="strip-item"><span class="strip-mark">♡</span> A safer campus community</div></div></div>
<section class="section section-white" id="features"><div class="wrap"><div class="section-head"><div class="kicker">Everything in one place</div><h2>Small steps toward a better campus.</h2><p>Practical tools that make it easier to speak up, stay informed and get support.</p></div>
<div class="features">
<article class="feature"><div class="feature-icon">✳</div><h3>Campus &amp; hostel complaints</h3><p>Share concerns with the relevant details so they can be reviewed and addressed.</p></article>
<article class="feature"><div class="feature-icon">↗</div><h3>Complaint tracking</h3><p>Return to your portal to see updates and follow the progress of your requests.</p></article>
<article class="feature"><div class="feature-icon">⌕</div><h3>Lost &amp; Found</h3><p>Share lost or found belongings, add an image and help reconnect items with their owners.</p></article>
<article class="feature"><div class="feature-icon">▤</div><h3>Campus notices</h3><p>Find important announcements and useful campus information in one place.</p></article>
<article class="feature"><div class="feature-icon">♡</div><h3>Help &amp; emergency contacts</h3><p>Keep essential support information and emergency contact details within reach.</p></article>
<article class="feature"><div class="feature-icon">◎</div><h3>Dedicated campus portal</h3><p>Access the tools available to your account through a simple, organised experience.</p></article>
</div></div></section>
<section class="section" id="how-it-works"><div class="wrap how-grid"><div class="how-intro"><div class="kicker">Getting started</div><h2>Support, without the runaround.</h2><p>Use your campus account to access the services available to you. Your portal keeps your campus requests and updates together.</p><a class="btn btn-primary" href="/login">Go to login <span aria-hidden="true">→</span></a></div>
<div class="steps"><article class="step"><div class="step-no">01</div><div><h3>Sign in securely</h3><p>Use the account credentials provided by your campus administrator.</p></div></article><article class="step"><div class="step-no">02</div><div><h3>Choose what you need</h3><p>Raise a concern, explore campus information or create a Lost &amp; Found listing.</p></div></article><article class="step"><div class="step-no">03</div><div><h3>Stay in the loop</h3><p>Visit your portal to follow request progress and view relevant updates.</p></div></article></div>
</div></section>
<section class="cta"><div class="wrap"><div class="cta-box"><div><h2>Let's make campus life better.</h2><p>Your campus support space is just one sign-in away.</p></div><a class="btn" href="/login">Continue to your portal <span aria-hidden="true">→</span></a></div></div></section>
</main>
<footer><div class="wrap foot"><div class="foot-brand"><img src="{{ url_for('campus_care_logo', v='original-20261011') }}" alt="">Campus Care 360</div><span>Campus support, connected. &nbsp; © Campus Care 360</span></div></footer>
</body>
</html>
"""
