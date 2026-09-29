import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="KidsDrive - Transporte Escolar",
    page_icon="🚘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .profile-card {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white; padding: 20px; border-radius: 16px;
        text-align: center; margin-bottom: 20px;
    }
    .price-card {
        background-color: #ffffff; padding: 15px; border-radius: 12px;
        border: 1px solid #e0e0e0; margin-bottom: 10px;
    }
    .badge {
        background-color: #e8f5e9; color: #2e7d32; padding: 4px 10px;
        border-radius: 20px; font-size: 12px; font-weight: bold;
    }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown("""
<div class="profile-card">
    <h2>🚘 KidsDrive Condomínio</h2>
    <p>Transporte Escolar VIP & Atividades</p>
    <div class="badge">✓ Rastreamento em Tempo Real via WhatsApp</div>
</div>
""", unsafe_allow_html=True)

# Tabela de Valores Transparente
st.subheader("💳 Tabela de Valores")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="price-card">
        <h4>🚌 Mensal Integral</h4>
        <p style="font-size: 20px; font-weight: bold; color: #2a5298;">R$ 480 <span style="font-size: 12px; color: #666;">/mês</span></p>
        <p style="font-size: 12px; color: #555;">Ida e Volta diária (Seg a Sex)</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="price-card">
        <h4>🕐 Meio Período</h4>
        <p style="font-size: 20px; font-weight: bold; color: #2a5298;">R$ 300 <span style="font-size: 12px; color: #666;">/mês</span></p>
        <p style="font-size: 12px; color: #555;">Apenas Ida ou Apenas Volta</p>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="price-card">
        <h4>⚽ Atividades</h4>
        <p style="font-size: 20px; font-weight: bold; color: #2a5298;">R$ 250 <span style="font-size: 12px; color: #666;">/mês</span></p>
        <p style="font-size: 12px; color: #555;">Natação, Inglês, Futebol (2x a 3x/sem)</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="price-card">
        <h4>⚡ Corrida Avulsa</h4>
        <p style="font-size: 20px; font-weight: bold; color: #2a5298;">R$ 25 <span style="font-size: 12px; color: #666;">/trajeto</span></p>
        <p style="font-size: 12px; color: #555;">Emergências e imprevistos</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Formulário de Reserva
st.subheader("📅 Solicitar Orçamento / Reservar Vaga")

with st.form(key="agendamento_form"):
    nome_mae = st.text_input("Seu Nome (Responsável):")
    nome_filho = st.text_input("Nome da Criança e Idade:")
    escola_destino = st.text_input("Escola ou Local da Atividade:")
    
    modalidade = st.selectbox(
        "Selecione o Plano Desejado:",
        [
            "Plano Mensal Integral (Ida e Volta - R$ 480/mês)",
            "Plano Meio Período (Apenas Entrada 12:30 ou Saída - R$ 300/mês)",
            "Plano Atividades Extracurriculares (R$ 250/mês)",
            "Corrida Avulsa / Emergencial (R$ 25/trajeto)"
        ]
    )
    
    dias_semana = st.multiselect(
        "Dias da Semana:",
        ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"],
        default=["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
    )
    
    observacoes = st.text_area("Observações (Ex: Necessita assento elevação, horário específico)")
    
    # Substitua pelo seu número com DDD (ex: 5535999999999)
    SEU_NUMERO_WHATSAPP = "5535999400824"

    submit_button = st.form_submit_button(label="📱 Solagendar via WhatsApp")

if submit_button:
    if not nome_mae or not nome_filho or not escola_destino:
        st.error("Por favor, preencha o Nome, Nome da criança e o Destino.")
    else:
        dias_str = ", ".join(dias_semana) if dias_semana else "A combinar"
        
        mensagem = (
            f"*Olá Mateus! Gostaria de confirmar uma vaga/orçamento.*\n\n"
            f"👤 *Responsável:* {nome_mae}\n"
            f"👦 *Criança:* {nome_filho}\n"
            f"📍 *Destino:* {escola_destino}\n"
            f"💳 *Plano Escolhido:* {modalidade}\n"
            f"📅 *Dias:* {dias_str}\n"
            f"📝 *Obs:* {observacoes if observacoes else 'Nenhuma'}\n\n"
            f"Aguardo confirmação da vaga!"
        )
        
        mensagem_encoded = urllib.parse.quote(mensagem)
        whatsapp_url = f"https://api.whatsapp.com/send?phone={SEU_NUMERO_WHATSAPP}&text={mensagem_encoded}"
        
        st.success("Solicitação gerada! Clique no botão abaixo para enviar.")
        st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank">
                <button style="
                    background-color: #25D366; color: white; padding: 14px 20px;
                    border: none; border-radius: 8px; width: 100%; font-size: 16px;
                    font-weight: bold; cursor: pointer; margin-top: 10px;">
                    🟢 Enviar Solicitação no WhatsApp
                </button>
            </a>
        ''', unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px;">
    📍 <b>Segurança e Rastreamento:</b> Acompanhamento do trajeto em tempo real via compartilhamento de localização ao vivo do WhatsApp durante todo o percurso.
</div>
""", unsafe_allow_html=True)
