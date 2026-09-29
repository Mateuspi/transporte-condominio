import base64
import urllib.parse
from pathlib import Path

import streamlit as st

# ---------------- CONFIG ----------------
WHATS = "5535999400824"
WHATS_FMT = "(35) 99940-0824"

st.set_page_config(
    page_title="MateusDrive VIP | Mobilidade & Assistência",
    page_icon="🚘",
    layout="centered",
    initial_sidebar_state="collapsed",
)

SERVICOS = [
    ("🚌", "Transporte Escolar & Atividades", "Escolas, natação, inglês e esportes, com poucos alunos por viagem.", "Planos mensais ou avulsos"),
    ("🎉", "Leva e Traz de Festas & Eventos", "Transporte seguro para jovens e adultos: baladas, shows e confraternizações.", "Valores a combinar"),
    ("👵", "Acompanhamento de Idosos", "Consultas, exames, laboratórios e banco, com paciência e suporte.", "Valores a combinar"),
    ("🛵", "Motoboy & Entregas Rápidas", "Documentos, remédios e compras com coleta e entrega urgente.", "A partir de R$ 15 / entrega"),
    ("🏥", "Apoio Hospitalar", "Acompanhamento de turnos, pernoites e altas médicas.", "Valores a combinar"),
    ("⭐", "Planos Personalizados", "Precisa de algo específico? Montamos a rotina ideal para você.", "Sob medida"),
]

# ---------------- ESTILO ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"], .stApp { font-family: 'Poppins', sans-serif; }
.stApp { background: #f4f9f9; }
.block-container { max-width: 760px; padding-top: 1rem; padding-bottom: 6rem; }
#MainMenu, footer, header { visibility: hidden; }

.hero { background: linear-gradient(135deg, #062f3b 0%, #0b4a56 60%, #0f6a6f 100%);
  border-radius: 24px; padding: 28px 22px 26px; color: #fff; text-align: center;
  box-shadow: 0 10px 30px rgba(6,47,59,.25); position: relative; overflow: hidden; }
.hero:before { content:""; position:absolute; right:-70px; top:-70px; width:220px; height:220px;
  border-radius:50%; background: rgba(20,184,166,.18); }
.eyebrow { font-size: 11px; letter-spacing: 2px; font-weight: 600; color: #7ee7d8; text-transform: uppercase; }
.avatar { width: 150px; height: 150px; border-radius: 50%; object-fit: cover; margin: 16px auto 10px;
  display: block; border: 5px solid #f6b246; box-shadow: 0 8px 22px rgba(0,0,0,.35); }
.avatar.ph { display:flex; align-items:center; justify-content:center; font-size:64px; background:#0f6a6f; }
.hero h1 { margin: 6px 0 2px; font-size: 34px; font-weight: 800; color:#fff; letter-spacing: -.5px; }
.hero h1 span { color: #f6b246; }
.hero .sub { font-size: 15px; color: #d6eeee; margin-bottom: 14px; }
.pill { display:inline-block; background:#14b8a6; color:#fff; padding:8px 18px; border-radius:30px;
  font-size:12px; font-weight:700; letter-spacing:1px; }
.cta { display:inline-block; margin-top:18px; background:#25D366; color:#fff !important; text-decoration:none !important;
  padding:14px 26px; border-radius:14px; font-weight:700; font-size:16px; box-shadow:0 6px 16px rgba(37,211,102,.4); }
.cta:hover { filter: brightness(1.06); }

.trust { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin:18px 0 6px; }
.trust div { background:#fff; border-radius:14px; padding:12px 6px; text-align:center; font-size:12px;
  font-weight:600; color:#0b3a46; box-shadow:0 2px 8px rgba(0,0,0,.05); }
.trust b { display:block; font-size:22px; margin-bottom:2px; }
@media (max-width:520px){ .trust{ grid-template-columns:repeat(2,1fr);} }

.title { font-size:22px; font-weight:800; color:#082d3a; margin:28px 0 4px; }
.title:after { content:""; display:block; width:54px; height:5px; border-radius:4px; background:#f6b246; margin-top:6px; }
.lead { color:#5b6b70; font-size:14px; margin-bottom:14px; }

.grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:14px; }
.card { background:#fff; border-radius:18px; padding:18px; border:1px solid #d9ecec;
  box-shadow:0 4px 14px rgba(8,45,58,.06); transition: transform .15s; }
.card:hover { transform: translateY(-3px); }
.ico { width:48px; height:48px; border-radius:14px; background:#e6f7f4; display:flex;
  align-items:center; justify-content:center; font-size:26px; margin-bottom:10px; }
.card h3 { margin:0 0 4px; font-size:16px; font-weight:700; color:#082d3a; }
.card p { margin:0 0 10px; font-size:13px; color:#5b6b70; line-height:1.5; }
.price { display:inline-block; font-size:12px; font-weight:700; color:#0b6b62; background:#e6f7f4;
  padding:4px 10px; border-radius:20px; }

.steps { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
.step { background:#fff; border-radius:16px; padding:16px 10px; text-align:center; border:1px solid #d9ecec; }
.step .n { width:34px; height:34px; border-radius:50%; background:#14b8a6; color:#fff; font-weight:800;
  display:flex; align-items:center; justify-content:center; margin:0 auto 8px; }
.step p { margin:0; font-size:13px; font-weight:600; color:#082d3a; }
@media (max-width:520px){ .steps{ grid-template-columns:1fr; } }

div[data-testid="stForm"] { background:#fff; border:1px solid #d9ecec; border-radius:20px; padding:22px;
  box-shadow:0 4px 14px rgba(8,45,58,.06); }
div[data-testid="stFormSubmitButton"] button { width:100%; background:#14b8a6; color:#fff; border:none;
  border-radius:12px; padding:.7rem 1rem; font-weight:700; font-size:16px; }
div[data-testid="stFormSubmitButton"] button:hover { background:#0f9b8c; color:#fff; }
.wa-btn { display:block; text-align:center; background:#25D366; color:#fff !important; text-decoration:none !important;
  padding:15px; border-radius:12px; font-weight:700; font-size:16px; margin-top:8px; }

.fab { position:fixed; right:18px; bottom:18px; z-index:999; background:#25D366; color:#fff !important;
  text-decoration:none !important; padding:13px 18px; border-radius:40px; font-weight:700; font-size:14px;
  box-shadow:0 8px 20px rgba(0,0,0,.28); }
.foot { text-align:center; color:#6b7b80; font-size:12px; margin-top:30px; line-height:1.7; }
</style>
""", unsafe_allow_html=True)


def wa_link(texto: str) -> str:
    return f"https://api.whatsapp.com/send?phone={WHATS}&text={urllib.parse.quote(texto)}"


def foto_base64() -> str | None:
    p = Path(__file__).parent / "motorista.jpg"
    return base64.b64encode(p.read_bytes()).decode() if p.exists() else None


# ---------------- HERO ----------------
b64 = foto_base64()
avatar = (f'<img class="avatar" src="data:image/jpeg;base64,{b64}" alt="Mateus">' if b64
          else '<div class="avatar ph">🚘</div>')
link_ola = wa_link("Olá Mateus! Vi o MateusDrive VIP e gostaria de mais informações.")

st.markdown(
    f'<div class="hero">'
    f'<div class="eyebrow">Serviço exclusivo para o condomínio</div>'
    f'{avatar}'
    f'<h1>Mateus<span>Drive</span> VIP</h1>'
    f'<div class="sub">Mobilidade, Entregas Expressas &amp; Assistência Pessoal</div>'
    f'<div class="pill">SEGURANÇA • PONTUALIDADE • CONFIANÇA</div><br>'
    f'<a class="cta" href="{link_ola}" target="_blank">💬 Chamar no WhatsApp</a>'
    f'</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="trust">'
    '<div><b>🛡️</b>Segurança</div><div><b>⏰</b>Pontualidade</div>'
    '<div><b>❄️</b>Ar-condicionado</div><div><b>🧼</b>Higienizado</div>'
    '</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="lead" style="text-align:center;">Veículo revisado (Prisma Sedan 4 portas) e '
    'opção de entregas ágeis de moto.</div>',
    unsafe_allow_html=True,
)

# ---------------- SERVIÇOS ----------------
st.markdown('<div class="title">Nossos Serviços</div>', unsafe_allow_html=True)
cards = "".join(
    f'<div class="card"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p><span class="price">{p}</span></div>'
    for i, t, d, p in SERVICOS
)
st.markdown(f'<div class="grid">{cards}</div>', unsafe_allow_html=True)

# ---------------- COMO FUNCIONA ----------------
st.markdown('<div class="title">Como funciona</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="steps">'
    '<div class="step"><div class="n">1</div><p>Escolha o serviço</p></div>'
    '<div class="step"><div class="n">2</div><p>Preencha o pedido</p></div>'
    '<div class="step"><div class="n">3</div><p>Confirme no WhatsApp</p></div>'
    '</div>',
    unsafe_allow_html=True,
)

# ---------------- FORMULÁRIO ----------------
st.markdown('<div class="title">Solicitar orçamento / agendar</div>', unsafe_allow_html=True)
st.markdown('<div class="lead">Preencha e enviaremos o pedido direto para o WhatsApp do Mateus.</div>',
            unsafe_allow_html=True)

with st.form("solicitacao"):
    nome = st.text_input("Seu nome completo")
    telefone = st.text_input("Seu WhatsApp com DDD", placeholder="(35) 9XXXX-XXXX")
    servico = st.selectbox("Serviço desejado", [
        "🚌 Transporte Escolar / Atividades Infantis",
        "🎉 Festas, Baladas, Shows e Eventos (a combinar)",
        "👵 Acompanhamento de Idosos (consultas, banco, exames)",
        "🛵 Motoboy / Entregas Rápidas",
        "🏥 Apoio Hospitalar / Pernoite / Altas (a combinar)",
        "🚘 Corrida avulsa ou plano personalizado",
    ])
    data_hora = st.text_input("Data e horário pretendido", placeholder="Ex: Sábado às 23:30")
    detalhes = st.text_area("Observações e pedidos especiais",
                            placeholder="Ex: Buscar meus filhos na festa às 3h / acompanhar minha mãe no hospital à tarde")
    enviar = st.form_submit_button("📱 Enviar solicitação para o Mateus")

if enviar:
    if not nome or not telefone or not detalhes:
        st.error("Preencha seu nome, telefone e as observações do pedido.")
    else:
        msg = (
            "*Olá Mateus! Vi o MateusDrive VIP e gostaria de agendar/cotar um serviço.*\n\n"
            f"👤 *Cliente:* {nome}\n📞 *Contato:* {telefone}\n🛠️ *Serviço:* {servico}\n"
            f"⏰ *Data/Horário:* {data_hora or 'A combinar'}\n📝 *Detalhes:* {detalhes}\n\n"
            "Aguardo sua confirmação e valor!"
        )
        st.success("Pedido pronto! Toque no botão abaixo para enviar no WhatsApp.")
        st.markdown(f'<a class="wa-btn" href="{wa_link(msg)}" target="_blank">🟢 Confirmar e enviar no WhatsApp</a>',
                    unsafe_allow_html=True)

# ---------------- RODAPÉ ----------------
st.markdown(
    f'<div class="foot"><b>MateusDrive VIP</b><br>Segurança, pontualidade e sigilo.<br>'
    f'WhatsApp direto: {WHATS_FMT}<br>Corridas avulsas ou planos mensais</div>'
    f'<a class="fab" href="{link_ola}" target="_blank">💬 WhatsApp</a>',
    unsafe_allow_html=True,
)
