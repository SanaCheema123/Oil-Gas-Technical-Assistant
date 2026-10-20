"""Design tokens and injected CSS for the app's visual theme.

Light, card-based aesthetic built on pink + white: white surfaces, deep-pink
headings, pink/rose accents, flat bordered cards. Risk/status indicators
(online dot, risk badges) keep their functional red/amber/green so severity
stays legible. Copy, icons and layout are original to this project.
"""

COLOR_BG = "#ffffff"
COLOR_SIDEBAR_BG = "#fff5f9"
COLOR_CARD_BG = "#ffffff"
COLOR_CARD_BG_SOFT = "#fff5f9"
COLOR_NAVY = "#9d174d"
COLOR_ORANGE = "#ec4899"
COLOR_BLUE = "#db2777"
COLOR_TEAL = "#f472b6"
COLOR_TEXT_BODY = "#404040"
COLOR_TEXT_MUTED = "#666666"
COLOR_BORDER = "#f6d9e6"
COLOR_SUCCESS = "#2eb872"
COLOR_SUCCESS_TEXT = "#1a7a4c"
COLOR_WARNING = "#f2a219"
COLOR_DANGER = "#e3423a"
COLOR_DANGER_TEXT = "#b3261e"

RADIUS_PILL = "8px"
RADIUS_BADGE = "4px"
RADIUS_CARD = "10px"
RADIUS_SM = "4px"

SHADOW_CARD = "rgba(0, 0, 0, 0.05) 0px 2px 15px 0px"
SHADOW_SOFT = "rgba(0, 0, 0, 0.05) 0px 2px 8px 0px"
SHADOW_LIFT = "rgba(0, 0, 0, 0.1) 0px 5px 7px 0px"

FONT_STACK = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'

CSS = f"""
<style>
:root {{
  --bg: {COLOR_BG};
  --sidebar-bg: {COLOR_SIDEBAR_BG};
  --card-bg: {COLOR_CARD_BG};
  --card-bg-soft: {COLOR_CARD_BG_SOFT};
  --navy: {COLOR_NAVY};
  --orange: {COLOR_ORANGE};
  --blue: {COLOR_BLUE};
  --teal: {COLOR_TEAL};
  --text-body: {COLOR_TEXT_BODY};
  --text-muted: {COLOR_TEXT_MUTED};
  --border-color: {COLOR_BORDER};
  --success: {COLOR_SUCCESS};
  --success-text: {COLOR_SUCCESS_TEXT};
  --warning: {COLOR_WARNING};
  --danger: {COLOR_DANGER};
  --danger-text: {COLOR_DANGER_TEXT};
  --radius-pill: {RADIUS_PILL};
  --radius-badge: {RADIUS_BADGE};
  --radius-card: {RADIUS_CARD};
  --radius-sm: {RADIUS_SM};
  --shadow-card: {SHADOW_CARD};
  --shadow-soft: {SHADOW_SOFT};
  --shadow-lift: {SHADOW_LIFT};
}}

html, body, [class*="css"], .stApp, .stMarkdown, p, span, div {{
  font-family: {FONT_STACK};
}}

.stApp {{
  background: var(--bg);
}}

.stApp, .stApp p, .stApp span, .stApp div, .stApp label,
[data-testid="stMarkdownContainer"], [data-testid="stMarkdownContainer"] p,
[data-testid="stWidgetLabel"] p, [data-testid="stCaptionContainer"],
[data-testid="stFileUploaderDropzoneInstructions"] span,
[data-testid="stFileUploaderDropzoneInstructions"] small,
[data-testid="stChatInput"] textarea::placeholder {{
  color: var(--text-body) !important;
}}

[data-testid="stAppViewContainer"], [data-testid="stHeader"],
[data-testid="stMain"], [data-testid="stBottom"] {{
  background: var(--bg) !important;
}}

/* ---- Sidebar (document repository column) ---- */
[data-testid="stSidebar"] {{
  background: var(--sidebar-bg) !important;
  border-right: 1px solid var(--border-color);
}}
[data-testid="stSidebar"] * {{
  color: var(--text-body) !important;
}}
[data-testid="stSidebarContent"] {{
  padding-top: 20px;
}}

/* ---- Top status bar ---- */
.status-bar {{
  display: flex;
  justify-content: flex-end;
  margin-bottom: 14px;
}}
.status-bar-group {{
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}}
.status-chip {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #ffffff;
  color: var(--orange) !important;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-pill);
  padding: 5px 14px;
  font-size: 13px;
  font-weight: 600;
  box-shadow: var(--shadow-soft);
}}
.status-chip-accent {{
  border-color: {COLOR_TEAL}33;
  background: {COLOR_TEAL}0d;
}}
.status-dot {{
  width: 8px;
  height: 8px;
  border-radius: 50%;
  display: inline-block;
  background: var(--success);
}}
.status-dot-online {{
  background: var(--success);
  box-shadow: 0 0 0 2px {COLOR_SUCCESS}33;
}}

/* ---- Section intro copy ---- */
.section-intro {{
  color: var(--text-muted) !important;
  font-size: 15px !important;
  line-height: 22px !important;
  margin: 0 0 18px 0 !important;
  max-width: 760px;
}}

/* ---- Tabs ---- */
[data-testid="stTabs"] [data-baseweb="tab-list"] {{
  gap: 4px;
  border-bottom: 1px solid var(--border-color);
}}
[data-testid="stTabs"] [data-baseweb="tab"] {{
  height: 42px;
  font-weight: 700;
  font-size: 15px;
  color: var(--text-muted) !important;
}}
[data-testid="stTabs"] [aria-selected="true"] {{
  color: var(--orange) !important;
}}
[data-testid="stTabs"] [data-baseweb="tab-highlight"] {{
  background-color: var(--orange) !important;
  height: 3px;
}}

/* ---- Prediction result card ---- */
.prediction-result {{
  border-left: 4px solid var(--teal);
}}
.prediction-result-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
}}
.prediction-label {{
  font-weight: 700;
  color: var(--orange) !important;
  font-size: 15px;
}}
.prediction-probability {{
  font-size: 34px;
  font-weight: 800;
  color: var(--navy) !important;
  margin-top: 4px;
}}
.risk-badge {{
  display: inline-block;
  border-radius: var(--radius-badge);
  padding: 4px 12px;
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  color: #ffffff !important;
}}
.risk-badge.risk-low {{ background: var(--success); }}
.risk-badge.risk-medium {{ background: var(--warning); color: #3a2a00 !important; }}
.risk-badge.risk-high {{ background: var(--danger); }}

/* ---- Hero banner (deliberate dark accent block on an otherwise light page) ---- */
.hero-banner {{
  background: linear-gradient(135deg, var(--navy) 0%, #c2255c 55%, var(--orange) 100%);
  border-radius: var(--radius-card);
  padding: 27px 32px;
  margin-bottom: 20px;
  box-shadow: var(--shadow-lift);
  transition: box-shadow 250ms ease;
}}
.hero-banner h1 {{
  color: #ffffff !important;
  font-size: 32px !important;
  font-weight: 700 !important;
  margin: 0 0 7px 0 !important;
}}
.hero-banner p {{
  color: #fde3ef !important;
  font-size: 16px !important;
  line-height: 24px !important;
  margin: 0 0 15px 0 !important;
}}
.hero-badges {{
  display: flex;
  gap: 9px;
  flex-wrap: wrap;
}}
.hero-banner .badge-pill {{
  display: inline-block;
  color: #ffffff !important;
  border: 0.8px solid #ffffff;
  border-radius: var(--radius-badge);
  padding: 7px 12px;
  font-size: 14px;
  font-weight: 600;
  background: rgba(255, 255, 255, 0.08);
}}

/* ---- Headings inside the app body ---- */
h1, h2, h3 {{
  color: var(--navy) !important;
  font-weight: 700 !important;
}}

/* ---- Cards ---- */
.card {{
  background: #ffffff;
  color: var(--text-body);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-card);
  padding: 15px;
  font-size: 16px;
  box-shadow: var(--shadow-card);
  margin-bottom: 12px;
}}

/* ---- Buttons ---- */
.stButton > button, button[kind="primary"], button[kind="secondary"] {{
  background: var(--orange) !important;
  color: #ffffff !important;
  border: none !important;
  border-radius: var(--radius-pill) !important;
  padding: 2px 26px !important;
  font-size: 16px !important;
  font-weight: 700 !important;
  box-shadow: var(--shadow-soft);
  transition: box-shadow 200ms ease, transform 200ms ease;
}}
.stButton > button:hover {{
  box-shadow: var(--shadow-lift);
  transform: translateY(-1px);
}}

/* ---- File uploader: dashed drop box ---- */
[data-testid="stFileUploaderDropzone"], [data-testid="stFileUploader"] section {{
  background: var(--card-bg-soft) !important;
  border: 2px dashed {COLOR_TEAL}57 !important;
  border-radius: var(--radius-card) !important;
  transition: border-color 150ms ease;
}}
[data-testid="stFileUploaderDropzone"]:hover {{
  border-color: var(--blue) !important;
}}

/* ---- Chat input dock ---- */
[data-testid="stBottom"] > div {{
  background: var(--sidebar-bg);
  border-top: 1px solid var(--border-color);
}}
[data-testid="stChatInput"] {{
  background: #ffffff;
  border: 0.8px solid {COLOR_TEAL}57;
  border-radius: var(--radius-pill);
  box-shadow: var(--shadow-soft);
  padding: 2px 6px;
}}
[data-testid="stChatInput"] textarea {{
  font-size: 16px !important;
  color: var(--text-body) !important;
}}
[data-testid="stChatInput"]:focus-within {{
  border-color: var(--blue);
}}
[data-testid="stChatInputSubmitButton"] {{
  background: var(--orange) !important;
  border-radius: var(--radius-sm) !important;
}}
[data-testid="stChatInputSubmitButton"] svg {{
  fill: #ffffff !important;
}}

/* ---- Chat messages: bubbles, user right-aligned ---- */
[data-testid="stChatMessage"] {{
  background: transparent;
  border: none;
  box-shadow: none;
  padding: 4px 8px;
  margin-bottom: 14px;
}}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) [data-testid="stChatMessageContent"] {{
  background: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: 12px 12px 12px 2px;
  padding: 14px 16px;
  box-shadow: var(--shadow-card);
}}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {{
  flex-direction: row-reverse;
}}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {{
  background: var(--blue);
  border-radius: 12px 12px 2px 12px;
  padding: 12px 16px;
}}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] p {{
  color: #ffffff !important;
  font-weight: 500;
}}

/* ---- Citations and procedure steps (chat answers) ---- */
.citations {{
  margin-top: 12px;
  padding-top: 10px;
  border-top: 1px solid var(--border-color);
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  align-items: center;
}}
.citations span {{
  font-size: 0.75rem;
  color: var(--text-muted) !important;
}}
.citation-tag {{
  background: {COLOR_BLUE}14;
  color: var(--blue) !important;
  border: 1px solid {COLOR_BLUE}40;
  padding: 2px 8px;
  border-radius: var(--radius-sm);
  font-size: 0.75rem;
}}
.step-box {{
  background: {COLOR_TEAL}0d;
  border-left: 2px solid var(--orange);
  padding: 8px 12px;
  margin: 8px 0;
  border-radius: 0 4px 4px 0;
}}

/* ---- Expander (sources / excerpts) ---- */
[data-testid="stExpander"] {{
  border-radius: var(--radius-card) !important;
  box-shadow: var(--shadow-soft);
  border: 1px solid var(--border-color) !important;
}}

/* ---- Links ---- */
a {{
  color: var(--blue) !important;
  text-decoration: underline;
}}

/* ---- Alerts ---- */
[data-testid="stAlert"] {{
  border-radius: var(--radius-card) !important;
  box-shadow: var(--shadow-soft);
}}

/* ---- Form (prediction inputs) as a card ---- */
[data-testid="stForm"] {{
  background: var(--card-bg-soft);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-card);
  padding: 20px 24px 8px 24px;
  box-shadow: var(--shadow-soft);
}}
[data-testid="stSlider"] label p {{
  font-weight: 600 !important;
  color: var(--orange) !important;
}}

/* ---- Top navigation bar ---- */
[data-testid="stAppHeader"] {{
  background: #ffffff !important;
  border-bottom: 1px solid var(--border-color);
}}
[data-testid="stTopNavLink"] {{
  font-weight: 700 !important;
  font-size: 15px !important;
}}

/* ---- Page links styled as pill buttons (landing CTAs) ---- */
[data-testid="stPageLink"] {{
  background: #ffffff;
  border: 1.5px solid var(--orange);
  border-radius: var(--radius-pill) !important;
  padding: 10px 18px !important;
  box-shadow: var(--shadow-soft);
  transition: box-shadow 200ms ease, transform 200ms ease;
}}
[data-testid="stPageLink"]:hover {{
  box-shadow: var(--shadow-lift);
  transform: translateY(-1px);
}}
[data-testid="stPageLink"] p {{
  color: var(--orange) !important;
  font-weight: 700 !important;
  font-size: 15px !important;
}}

/* ---- Landing page section titles ---- */
.landing-section-title {{
  color: var(--navy) !important;
  font-size: 22px !important;
  font-weight: 800 !important;
  margin: 28px 0 14px 0 !important;
}}

/* ---- Feature cards (landing) ---- */
.feature-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}}
.feature-card {{
  background: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-card);
  padding: 20px;
  box-shadow: var(--shadow-card);
}}
.feature-icon {{
  font-size: 28px;
  margin-bottom: 8px;
}}
.feature-card h3 {{
  color: var(--navy) !important;
  font-size: 17px !important;
  font-weight: 800 !important;
  margin: 0 0 6px 0 !important;
}}
.feature-card p {{
  color: var(--text-muted) !important;
  font-size: 14px !important;
  line-height: 20px !important;
  margin: 0 !important;
}}

/* ---- How-it-works steps (landing) ---- */
.steps-row {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}}
.step-card {{
  display: flex;
  gap: 12px;
  background: var(--card-bg-soft);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-card);
  padding: 16px;
}}
.step-number {{
  flex-shrink: 0;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: var(--teal);
  color: #ffffff !important;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 14px;
}}
.step-card h4 {{
  color: var(--navy) !important;
  font-size: 15px !important;
  font-weight: 800 !important;
  margin: 0 0 4px 0 !important;
}}
.step-card p {{
  color: var(--text-muted) !important;
  font-size: 13px !important;
  line-height: 18px !important;
  margin: 0 !important;
}}

/* ---- Document library cards (upload page) ---- */
.doc-card {{
  display: flex;
  align-items: center;
  gap: 10px;
  background: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-card);
  padding: 10px 14px;
  margin-bottom: 8px;
  box-shadow: var(--shadow-soft);
}}
.doc-card-icon {{
  font-size: 18px;
}}
.doc-card-name {{
  flex-grow: 1;
  font-weight: 700;
  color: var(--text-body) !important;
  font-size: 14px;
}}
.doc-card-size {{
  color: var(--text-muted) !important;
  font-size: 13px;
}}

/* ---- Sidebar brand header (chat page) ---- */
.brand {{
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 8px;
}}
.brand-icon {{
  width: 36px;
  height: 36px;
  background: var(--orange);
  color: #ffffff !important;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-sm);
  font-size: 18px;
  flex-shrink: 0;
}}
.brand-text h2 {{
  font-size: 1.05rem;
  font-weight: 700;
  margin: 0 !important;
  color: var(--navy) !important;
}}
.brand-text span {{
  font-size: 0.72rem;
  color: var(--orange) !important;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}}

/* ---- Active document list (chat page sidebar) ---- */
.doc-section h3 {{
  font-size: 0.78rem;
  color: var(--text-muted) !important;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin: 18px 0 10px 0 !important;
  font-weight: 700 !important;
}}
.doc-list {{
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-height: 260px;
  overflow-y: auto;
  padding: 0;
  margin: 0;
}}
.doc-item {{
  background: #ffffff;
  border: 1px solid var(--border-color);
  padding: 9px 12px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  font-size: 0.82rem;
  box-shadow: var(--shadow-soft);
}}
.doc-item-title {{
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  color: var(--text-body) !important;
}}
.doc-badge {{
  background: {COLOR_SUCCESS}1f;
  color: var(--success-text) !important;
  font-size: 0.68rem;
  padding: 2px 7px;
  border-radius: var(--radius-sm);
  flex-shrink: 0;
}}

/* ---- Safety banner ---- */
.safety-disclaimer {{
  background: {COLOR_DANGER}14;
  border-left: 3px solid var(--danger);
  padding: 10px 12px;
  border-radius: var(--radius-sm);
  font-size: 0.75rem;
  color: var(--danger-text) !important;
  line-height: 1.4;
  margin-top: 18px;
}}
.safety-disclaimer strong {{
  color: var(--danger-text) !important;
}}

/* ---- Chat console header ---- */
.chat-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border-color);
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 10px;
}}
.chat-header h2 {{
  margin: 0 !important;
  font-size: 1.3rem !important;
}}
.chat-header-sub {{
  font-size: 0.8rem !important;
  color: var(--text-muted) !important;
  margin: 2px 0 0 0 !important;
}}
.chat-status {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.8rem;
  color: var(--text-muted);
  white-space: nowrap;
}}

@media (max-width: 900px) {{
  .feature-grid, .steps-row {{
    grid-template-columns: 1fr;
  }}
}}
</style>
"""
