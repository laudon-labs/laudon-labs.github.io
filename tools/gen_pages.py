#!/usr/bin/env python3
"""Generate laudonlabs.com module detail pages."""
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "modules")

MODULES = [
    dict(
        name="pickup_point_network",
        price="$499", free=False,
        group="Warehouse & Logistics",
        tagline="Deliver to community hosts on a schedule &mdash; not to every doorstep.",
        body="""<p>Customers volunteer as hosts. Their neighbours order to that address.
You deliver everything for a region in one consolidated run, on a schedule everybody
can predict. Running that on spreadsheets means missed deadlines, territory clashes
discovered too late, and commission worked out by hand every month.</p>""",
        bullets=[
            "Zones with their own schedule rule, rolled forward automatically for months ahead",
            "One run per cycle &mdash; stop sequencing, driver ETAs, signature and proof-of-delivery photo",
            "Public locator with ZIP search, and a host application form that geocodes and distance-checks on arrival",
            "Bill of lading, per-box manifest, optional separation of duties and pack-stage quality check",
            "Commission accrues per invoice onto a draft vendor bill; past-due hosts move to grace, then suspended",
            "No Enterprise apps, no CDN calls, no API key needed &mdash; 80 tests, all passing",
        ],
        depends="<code>sale_management</code>, <code>stock</code>, <code>account</code>, <code>delivery</code>, <code>fleet</code>, <code>website_sale</code>",
        edition="Community &amp; Enterprise", license="OPL-1",
    ),
    dict(
        name="warehouse_zip_routing",
        price="$199", free=False,
        group="Warehouse & Logistics",
        tagline="Every warehouse knows the territory it serves.",
        body="""<p>Odoo already lets a delivery method declare the ZIP prefixes it covers.
This gives warehouses the same idea, then answers the question Odoo leaves to whoever
is typing: which warehouse ships this, and by what method? Orders stop shipping from
the wrong side of the country because somebody accepted the default.</p>""",
        bullets=[
            "ZIP prefixes, states and countries per warehouse &mdash; longest prefix wins, so a region and a town inside it don't fight",
            "A prefix can belong to only one active warehouse; reuse one and it names the warehouse that already owns it",
            "Customers resolve from their address, visibly on the contact, and stay overridable by hand",
            "Re-resolves on the programmatic paths too &mdash; website carts, imports, wizards &mdash; where onchanges never fire",
            "Ship-to beats bill-to; an explicit choice always wins; a confirmed order is never re-routed",
            "Restrict a product to certain warehouses or methods &mdash; 33 tests, all passing",
        ],
        depends="<code>sale_stock</code>, <code>delivery</code>, <code>purchase</code>",
        edition="Community &amp; Enterprise", license="OPL-1",
    ),
    dict(
        name="stock_expiring_lots",
        price="$59", free=False,
        group="Warehouse & Logistics",
        tagline="What's about to go bad, soonest first.",
        body="""<p>Odoo tracks expiration dates but never gives you the one screen you
actually want: everything on hand, soonest to expire first, with how many days
are left.</p>""",
        bullets=[
            "Days to Expiry on every lot &mdash; negative once expired, in the user's own timezone",
            "Inventory &gt; Reporting &gt; Expiring Stock, filtered to lots with stock on hand",
            "Red once expired, amber inside two weeks, no configuration needed",
            "Read-only &mdash; a watchlist, not another place to edit stock",
            "Pairs with Odoo's own FEFO removal strategy",
        ],
        depends="<code>stock</code>, <code>product_expiry</code>",
        edition="Community &amp; Enterprise", license="OPL-1",
    ),
    dict(
        name="barcode_parser_guard",
        price="Free", free=True, price_note="because it's twenty lines",
        group="Warehouse & Logistics",
        tagline="One empty scan can't wedge the scanner screen.",
        body="""<p>Odoo's barcode parser reads <code>barcode.length</code> without checking
a barcode was passed. Callers can reach it with <code>undefined</code>, the JavaScript
throws, and the scanner screen stops responding &mdash; operator at a cart, gun in hand,
no way forward but a page reload.</p>""",
        bullets=[
            "Guards the falsy case, defers to core for every valid scan",
            "Standard <code>patch()</code> helper &mdash; no core file touched",
            "Installs automatically alongside <code>barcodes</code>",
        ],
        depends="<code>barcodes</code>",
        edition="Community &amp; Enterprise", license="OPL-1",
    ),
    dict(
        name="cost_guardrail",
        price="$199", free=False,
        group="Accounting & Finance",
        tagline="One fat-fingered cost can't rewrite your margins.",
        body="""<p>A wrong unit cost on a PO receipt quietly rewrites the product's
standard price, and every later sale books nonsense COGS. Nobody notices until the
month-end margin report looks insane and somebody spends two days working out why.</p>""",
        bullets=[
            "Per-category percentage threshold blocks an abnormal receipt cost before it lands",
            "Per-category maximum multiple clamps runaway COGS on invoices, with an alert",
            "Optionally block credit notes that reverse COGS with no goods return",
            "Scoped COGS cleanup wizard &mdash; preview, then post through a clearing account",
            "All guards off by default; installing changes nothing",
            "Ships with its own test suite &mdash; 8 tests, all passing",
        ],
        depends="<code>stock_account</code>, <code>purchase</code>, <code>sale_stock</code>",
        edition="Community &amp; Enterprise", license="OPL-1",
    ),
    dict(
        name="bounced_payment_return",
        price="$149", free=False,
        group="Accounting & Finance",
        tagline="One-click workflow for bounced checks, NSF, and ACH returns.",
        body="""<p>Handling a bounced check in vanilla Odoo takes four to five steps
and is easy to get wrong. This module collapses the workflow into a single wizard
with a full audit trail.</p>""",
        bullets=[
            "Reverses the payment entry &mdash; keeps original bank deposit matching intact",
            "Reopens the original invoice, restores amount due automatically",
            "Optional bank-fee invoice, posted and ready to collect",
            "Full chatter audit on payment, invoice, partner, and fee invoice",
            "Outstanding-Receipts lines pre-positioned for next bank statement",
        ],
        extra="""<div class="terminal terminal-sm">
  <div class="terminal-chrome">
    <span class="tc-dot tc-red"></span>
    <span class="tc-dot tc-yellow"></span>
    <span class="tc-dot tc-green"></span>
    <span class="terminal-title">odoo-shell &mdash; bounced_payment_return</span>
  </div>
  <pre class="terminal-body"><span class="t-prompt">&gt;&gt;&gt;</span> <span class="t-cmd">payment.action_return_payment()</span>
<span class="t-out">{</span>
<span class="t-out">    "reversal_move_id": 8423,       <span class="t-comment"># reopens the invoice</span></span>
<span class="t-out">    "fee_invoice_id":   1092,       <span class="t-comment"># optional, bills the customer</span></span>
<span class="t-out">    "is_returned":      True,</span>
<span class="t-out">    "return_reason":    "bounced",</span>
<span class="t-out">    "chatter":          ["payment", "invoice", "partner", "fee_invoice"]</span>
<span class="t-out">}</span>
<span class="t-prompt">&gt;&gt;&gt;</span> <span class="t-comment"># one wizard, one click, bookkeeping done right</span></pre>
</div>""",
        depends="<code>account</code>, <code>account_check_printing</code>",
        edition="Community &amp; Enterprise", license="OPL-1",
    ),
    dict(
        name="bank_feed_receipt_required",
        price="$99", free=False,
        group="Accounting & Finance",
        tagline="No receipt, no memo, no posting &mdash; enforced at the bank feed.",
        body="""<p>The moment a bank charge is reconciled is the only moment anyone
remembers what it was for. A month later, at close, nobody does &mdash; and the
bookkeeper is emailing five people about a $348 charge from a vendor no one
recognizes.</p>""",
        bullets=[
            "Blocks manual bank-feed lines hitting an expense account with no receipt or no memo",
            "One combined error listing everything missing &mdash; fixed in a single pass",
            "Receipt drop zone rendered right on the Manual Operations tab",
            "Never blocks AR/AP, bill matches, or reconcile-model lines",
            "Background auto-reconciliation runs untouched",
        ],
        depends="<code>account_accountant</code>",
        edition="Enterprise", license="OPL-1",
    ),
    dict(
        name="bank_rec_match_filter",
        price="$79", free=False,
        group="Accounting & Finance",
        tagline="The reconciliation tab, back to being useful.",
        body="""<p>Match Existing Entries lists every unreconciled journal item in the
database. On a real ledger that is thousands of rows, so nobody scrolls it &mdash;
they type in the search box instead, which defeats the point of the tab.</p>""",
        bullets=[
            "Line has a partner &rarr; that partner's open receivables and payables only",
            "No partner &rarr; the journal's own outstanding payments, on the correct side",
            "Batch Payments tab appears on deposits only",
            "Domain is appended to the standard one, never replaced &mdash; safe next to other modules",
        ],
        depends="<code>account_accountant</code>, <code>account_accountant_batch_payment</code>",
        edition="Enterprise", license="OPL-1",
    ),
    dict(
        name="hr_self_onboarding",
        price="$129", free=False,
        group="People & Productivity",
        tagline="New hires fill it in. You stop retyping it.",
        body="""<p>New-hire data arrives as a scan, a phone photo, or a form on someone's
desk &mdash; and then a manager types it into Odoo, getting the bank details wrong often
enough to matter. The person who knows the answers should be the one entering them,
without needing an Odoo account.</p>""",
        bullets=[
            "One button emails a secure link &mdash; and doubles as the resend",
            "Address, DOB, national ID, emergency contact, direct deposit, clock-in PIN",
            "No portal user, no password, no licence seat",
            "256-bit token, single use, 14-day expiry, CSRF-protected, explicit field allowlist",
            "Nothing sensitive reaches the chatter &mdash; tracking suppressed on the submission",
            "Labels and state list follow the company's country, not hardcoded US",
        ],
        depends="<code>hr</code>, <code>website</code>, <code>mail</code>",
        edition="Community &amp; Enterprise", license="OPL-1",
    ),
    dict(
        name="google_calendar_private_sync",
        price="$79", free=False,
        group="People & Productivity",
        tagline="Google Calendar, without the leaks.",
        body="""<p>The first thing that happens after you connect a staff calendar is
that a colleague opens the calendar view and reads a dentist appointment. The second
is a support ticket about two hundred thousand imported events.</p>""",
        bullets=[
            "Events synced from Google are forced private &mdash; the slot still blocks, the details stay the owner's",
            "Appointments booked natively in Odoo are untouched",
            "Forward-only first sync &mdash; no more importing a year of past events",
            "Look-ahead still honours <code>google_calendar.sync.range_days</code>",
            "A user's own synced Google copy no longer blocks their own bookings",
        ],
        depends="<code>google_calendar</code>, <code>appointment</code>",
        edition="Enterprise", license="OPL-1",
    ),
    dict(
        name="chatter_mention_dm",
        price="$69", free=False,
        group="People & Productivity",
        tagline="@mentions become Discuss DMs. #channel mentions get posted to the channel.",
        body="""<p>Chatter mentions land in the Inbox, and in a busy database the Inbox
is where notifications go to die. This pushes them somewhere people actually look
&mdash; without asking anyone to change how they work.</p>""",
        bullets=[
            "@mention a user &rarr; direct message in Discuss, posted as you",
            "Mention a #channel &rarr; the same message posted to that channel",
            "Clickable link back to the source record, every time",
            "Works on every model with a Chatter &mdash; no configuration, no model list",
            "Discuss failures can never block the original Chatter post",
        ],
        depends="<code>mail</code>",
        edition="Community &amp; Enterprise", license="OPL-1",
    ),
    dict(
        name="log_quiet",
        price="Free", free=True, price_note="a narrow fix for a narrow annoyance",
        group="People & Productivity",
        tagline="Twelve noisy messages, silenced. Everything else untouched.",
        body="""<p>A log you have stopped reading is not a log. Odoo emits a handful of
harmless messages at ERROR and WARNING until a real failure is just one more line in
the scroll &mdash; and once people learn to scroll past them, they scroll past the
real one too.</p>""",
        bullets=[
            "Serialization retries the ORM already handles drop to WARNING &mdash; still logged",
            "Export / unsubscribe / import &quot;ignoring args&quot; noise, gone",
            "Crawler junk, stale sourcemaps, Studio boot warnings, gone",
            "No filter matches on level or logger alone &mdash; every one matches a named message",
            "Nine core loggers; the root logger is never touched",
            "Any filter switched off with one env var. No uninstall",
        ],
        depends="<code>base</code>",
        edition="Community &amp; Enterprise", license="LGPL-3",
    ),
]

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} &middot; Laudon Labs</title>
<meta name="description" content="{meta_desc}">
<meta name="theme-color" content="#f6f5f2">
<meta property="og:title" content="{name} &middot; Laudon Labs">
<meta property="og:description" content="{meta_desc}">
<meta property="og:image" content="/logo-mark.png">
<link rel="icon" href="/logo-mark.png?v=2" type="image/png">
<link rel="apple-touch-icon" href="/logo-mark.png?v=2">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
</head>
<body>

<nav class="nav">
  <div class="container nav-inner">
    <a href="/" class="brand">
      <img src="/logo-mark.png" alt="Laudon Labs" class="brand-mark">
      <span class="brand-name">Laudon Labs</span>
    </a>
    <div class="nav-links">
      <a href="/#modules" class="active">Modules</a>
      <a href="/#philosophy">Philosophy</a>
      <a href="/request.html">Request</a>
      <a href="https://apps.odoo.com/apps/modules/browse?author=Laudon+Labs" target="_blank" rel="noopener" class="nav-cta">Odoo Store <span class="arrow">&rarr;</span></a>
    </div>
  </div>
</nav>

<header class="detail-hero">
  <div class="container">
    <a href="/#modules" class="breadcrumb">&larr; all modules</a>
    <h1>{name}</h1>
    <p class="detail-tagline">{tagline}</p>
    <div class="detail-meta">
      <span class="detail-price{free_cls}">{price}</span>
      <span class="sep">|</span>
      <span>{price_note}</span>
      <span class="sep">|</span>
      <span>{edition}</span>
    </div>
    <div class="cta-row" style="margin-bottom:0">
      <a href="https://apps.odoo.com/apps/modules/18.0/{name}" target="_blank" rel="noopener" class="btn btn-primary">{store_cta} <span class="arrow">&rarr;</span></a>
      <a href="mailto:tom@laudonlabs.com?subject={name}" class="btn btn-ghost">Questions?</a>
    </div>
  </div>
</header>

<section class="detail-section">
  <div class="container">
    <div class="detail-grid">
      <div class="detail-body">
        {body}
        <ul class="bullet-list">
{bullets}
        </ul>
{extra}
      </div>
      <aside class="spec-card">
        <dl>
          <dt>series</dt><dd><code>18.0</code></dd>
          <dt>depends</dt><dd>{depends}</dd>
          <dt>edition</dt><dd>{edition}</dd>
          <dt>license</dt><dd><code>{license}</code></dd>
          <dt>support</dt><dd><a href="mailto:tom@laudonlabs.com">tom@laudonlabs.com</a></dd>
        </dl>
        <div class="spec-actions">
          <a href="https://apps.odoo.com/apps/modules/18.0/{name}" target="_blank" rel="noopener" class="btn btn-primary">{store_cta}</a>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section-cta">
  <div class="container">
    <h2>Need a tweak to this module?</h2>
    <p>Customizations to any Laudon Labs module are quoted through the same
    intake form. Typical reply in under a day.</p>
    <a href="/request.html" class="btn btn-primary btn-lg">Start a request <span class="arrow">&rarr;</span></a>
  </div>
</section>

<footer class="site-footer">
  <div class="container footer-inner">
    <div class="footer-left">
      <a href="/" class="brand">
        <img src="/logo-mark.png" alt="" class="brand-mark">
        <span class="brand-name">Laudon Labs</span>
      </a>
      <p class="footer-tagline">Odoo modules, built for operators.</p>
    </div>
    <div class="footer-right">
      <p>
        <a href="https://apps.odoo.com/apps/modules/browse?author=Laudon+Labs" target="_blank" rel="noopener">Odoo App Store</a>
        &middot;
        <a href="mailto:tom@laudonlabs.com">tom@laudonlabs.com</a>
      </p>
      <p class="copyright">&copy; <span id="year"></span> Laudon Labs. All rights reserved.</p>
    </div>
  </div>
</footer>

<script>
  document.getElementById('year').textContent = new Date().getFullYear();
</script>

</body>
</html>
"""

import re

def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    for a, b in [("&mdash;", "—"), ("&amp;", "&"), ("&rarr;", "→"), ("&gt;", ">"), ("&quot;", '"'), ("&middot;", "·")]:
        s = s.replace(a, b)
    return s

os.makedirs(OUT, exist_ok=True)
for m in MODULES:
    bullets = "\n".join(
        f'          <li><span>&#10003;</span> {b}</li>' for b in m["bullets"]
    )
    html = PAGE.format(
        name=m["name"],
        tagline=m["tagline"],
        meta_desc=strip_tags(m["tagline"]) + " An Odoo 18 module by Laudon Labs.",
        price=m["price"],
        free_cls=" free" if m["free"] else "",
        price_note=m.get("price_note", "one-time &middot; per database"),
        store_cta="Get it free on the App Store" if m["free"] else "Buy on the Odoo App Store",
        edition=m["edition"],
        license=m["license"],
        depends=m["depends"],
        body=m["body"],
        bullets=bullets,
        extra=("\n" + m["extra"] if m.get("extra") else ""),
    )
    path = os.path.join(OUT, m["name"] + ".html")
    with open(path, "w") as f:
        f.write(html)
    print("wrote", path)
