import streamlit as st
import urllib.parse

# 1. Configuração da Página para Mobile
st.set_page_config(
    page_title="MateusDrive - Mobilidade & Serviços VIP",
    page_icon="🚘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. CSS Personalizado para Visual Profissional
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .profile-card {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white; padding: 22px; border-radius: 16px;
        text-align: center; margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .profile-card h2 { color: #ffffff; margin-bottom: 5px; font-size: 24px; font-weight: 700; }
    .profile-card p { color: #e0e0e0; font-size: 14px; margin-bottom: 0px; }
    
    .trust-badge {
        background-color: #10b981; color: white; padding: 6px 14px;
        border-radius: 20px; font-size: 13px; font-weight: bold;
        display: inline-block; margin-top: 10px;
    }
    
    .service-card {
        background-color: #ffffff; padding: 14px; border-radius: 12px;
        border-left: 5px solid #203a43; margin-bottom: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .service-card h4 { margin: 0 0 4px 0; color: #0f2027; font-size: 16px; }
    .service-card p { margin: 0; font-size: 13px; color: #555; }
    .service-price { font-size: 12px; font-weight: bold; color: #2563eb; margin-top: 4px; }
    
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. Cabeçalho Principal e Selo de Responsabilidade
st.markdown("""
<div class="profile-card">
    <h2>🚘 MateusDrive VIP</h2>
    <p>Mobilidade, Eventos, Entregas Expressas & Assistência</p>
    <div class="trust-badge">🛡️ Motorista Altamente Responsável, Pontual & De Confiança</div>
</div>
""", unsafe_allow_html=True)

# 4. Mensagem de Confiança do Motorista
st.info("💡 **Compromisso & Segurança:** Trabalho com total responsabilidade, respeito e pontualidade. Veículo revisado (Prisma Sedan 4P com ar-condicionado) e opção de entregas ágeis de moto.")

# 5. Apresentação das Modalidades de Serviços
st.subheader("🛠️ Nossos Serviços")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="service-card">
        <h4>🚌 Transporte Escolar / Atividades</h4>
        <p>Levar e buscar crianças em escolas e cursos no condomínio.</p>
        <div class="service-price">Planos Mensais ou Avulsos</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <h4>🪩 Festas, Eventos & Baladas</h4>
        <p>Leva e traz seguro para jovens e adultos em festas, shows e confraternizações.</p>
        <div class="service-price">Valores A Combinar</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <h4>🛵 Motoboy / Entregas Rápidas</h4>
        <p>Documentos, exames, farmácia, mercado e encomendas locais.</p>
        <div class="service-price">A partir de R$ 15 / entrega</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <h4>👵 Acompanhamento de Idosos</h4>
        <p>Consultas médicas, exames, laboratórios e ida ao banco com paciência e apoio.</p>
        <div class="service-price">Valores A Combinar</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <h4>🏥 Apoio Hospitalar / Pernoite</h4>
        <p>Acompanhamento de turnos, esperas e altas médicas com total suporte.</p>
        <div class="service-price">Valores A Combinar</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <h4>🌟 Planos Personalizados</h4>
        <p>Precisa de um serviço específico? Monte sua rotina conosco!</p>
        <div class="service-price">Sob Medida nas Observações</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 6. Formulário Unificado de Solicitação
st.subheader("📅 Solicitar Orçamento / Agendar Serviço")

with st.form(key="solicitacao_form"):
    nome_cliente = st.text_input("Seu Nome Completo:")
    telefone_cliente = st.text_input("Seu Telefone / WhatsApp com DDD:", placeholder="(35) 9XXXX-XXXX")
    
    categoria_servico = st.selectbox(
        "Selecione o Serviço Desejado:",
        [
            "🚌 Transporte Escolar / Atividades Infantis",
            "🪩 Festas, Baladas, Shows (Leva e Traz de Jovens/Adultos - A Combinar)",
            "👵 Transporte com carro / Acompanhamento de Idosos (Consultas, Banco, Exames - A Combinar)",
            "🛵 Serviços/ Entregas Rápidas, neste caso utilizo moto (Documentos, Farmácia, Mercado)",
            "🏥 Acompanhamento Hospitalar / Pernoite / Altas (A Combinar)",
            "🚘 Outro Plano Personalizado / Corrida Avulsa (Detalhar Abaixo)"
        ]
    )
    
    data_horario = st.text_input("Data e Horário Pretendido:", placeholder="Ex: Sábado às 23:30 / Terça às 14:00")
    
    detalhes = st.text_area(
        "Observações e Pedidos Especiais (Ajustamos conforme sua necessidade):",
        placeholder="Ex: Preciso buscar meus filhos na festa às 03h da manhã no local X / Acompanhar minha mãe no hospital durante a tarde / Levar pacote para o cartório."
    )
    
    # Seu número de WhatsApp cadastrado
    SEU_NUMERO_WHATSAPP = "5535999400824"

    submit_button = st.form_submit_button(label="📱 Enviar Solicitação para o Mateus")

# 7. Lógica de Envio para o WhatsApp
if submit_button:
    if not nome_cliente or not telefone_cliente or not detalhes:
        st.error("Por favor, preencha o seu Nome, Telefone e as Observações/Detalhes do pedido.")
    else:
        mensagem = (
            f"*Olá Mateus! Vi o aplicativo MateusDrive e gostaria de agendar/cotar um serviço.*\n\n"
            f"👤 *Cliente:* {nome_cliente}\n"
            f"📞 *Contato:* {telefone_cliente}\n"
            f"🛠️ *Serviço:* {categoria_servico}\n"
            f"⏰ *Data/Horário:* {data_horario if data_horario else 'A combinar'}\n"
            f"📝 *Observações/Detalhes:* {detalhes}\n\n"
            f"Aguardo sua confirmação e valor!"
        )
        
        mensagem_encoded = urllib.parse.quote(mensagem)
        whatsapp_url = f"https://api.whatsapp.com/send?phone={SEU_NUMERO_WHATSAPP}&text={mensagem_encoded}"
        
        st.success("Solicitação pronta! Clique no botão abaixo para abrir o seu WhatsApp e enviar ao Mateus.")
        st.markdown(f'''
            <a href="{whatsapp_url}" target="_blank">
                <button style="
                    background-color: #25D366; color: white; padding: 14px 20px;
                    border: none; border-radius: 8px; width: 100%; font-size: 16px;
                    font-weight: bold; cursor: pointer; margin-top: 10px;">
                    🟢 Confirmar e Enviar no WhatsApp
                </button>
            </a>
        ''', unsafe_allow_html=True)

# 8. Rodapé Profissional
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px;">
    🛡️ <b>MateusDrive VIP:</b> Segurança, pontualidade e sigilo. Veículo  higienizado, ar-condicionado e suporte direto via WhatsApp.
</div>
""", unsafe_allow_html=True)
