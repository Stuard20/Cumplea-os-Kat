import streamlit as st
import streamlit.components.v1 as components
import base64
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Feliz Cumpleaños Kat", page_icon="🧬")

# --------- FUNCIÓN PARA EL FONDO ---------
def set_background(image_file):
    try:
        with open(image_file, "rb") as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        # CORRECCIÓN: Se cambió la coma por punto y se ajustó el formato data:image
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"No se pudo cargar el fondo: {e}")

# --- APLICA TU IMAGEN DE FONDO AQUÍ ---
# Asegúrate de que el nombre del archivo sea exacto
set_background('acuarela-corazones-patrones-fisuras_1108-561.jpeg')

# --------- ESTILOS CSS ACTUALIZADOS ---------
st.markdown("""
<style>
/* Título en un tono fucsia/oscuro para que resalte sobre el blanco */
.title-text {
    color: #d63384; 
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

/* Subtítulo en gris oscuro/negro */
.subtitle-text {
    color: #444444;
    font-size: 22px;
    font-weight: 500;
    text-align: center;
    margin-bottom: 30px;
}

/* La carta: fondo semi-transparente claro para que se vea el fondo de corazones 
   pero el texto sea negro y legible */
.letter {
    background: rgba(255, 255, 255, 0.85);
    color: #222222;
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #ffb6c1; /* Borde rosa pastel */
    font-size: 19px;
    line-height: 1.6;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-top: 20px;
    white-space: pre-wrap;
    font-weight: 450;
}

/* Botones con colores que combinen con el rosa */
.stButton>button {
    background: linear-gradient(45deg, #ff9a9e, #fad0c4);
    color: #333333;
    border: none;
    font-weight: bold;
    border-radius: 10px;
    width: 100%;
    transition: 0.3s;
}

.stButton>button:hover {
    border-color: #ff9a9e;
    color: #000000;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)
st.markdown('<h1 class="title-text">🧬 ¡Feliz Cumpleaños Kat! 🧪</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Hoy celebramos una mente brillante llena de vida 💚</p>', unsafe_allow_html=True)

# --------- PARTÍCULAS (Moléculas) ---------
components.html(
    """
    <style>
    .molecule { position: fixed; width: 8px; height: 8px; background: #00ffe0; border-radius: 50%; box-shadow: 0 0 10px #00ffe0; animation: float 10s linear infinite; z-index: -1; }
    @keyframes float { 0% { transform: translateY(100vh); opacity: 0; } 50% { opacity: 1; } 100% { transform: translateY(-10vh); opacity: 0; } }
    </style>
    <script>
    setInterval(() => {
        const mol = document.createElement("div");
        mol.className = "molecule";
        mol.style.left = Math.random() * 100 + "vw";
        mol.style.animationDuration = (Math.random() * 5 + 5) + "s";
        document.body.appendChild(mol);
        setTimeout(() => mol.remove(), 10000);
    }, 500);
    </script>
    """, height=0,
)

# --------- LÓGICA DE LA CARTA ---------
if "mostrar_carta" not in st.session_state:
    st.session_state.mostrar_carta = False

if st.button("💌 Abrir carta"):
    st.session_state.mostrar_carta = True

if st.session_state.mostrar_carta:
    mensaje = "Feliz cumpleaños cientificaaa 🧬💚.\n\nEspero te la pases muy bien con las personas que quieres mucho.\n\nDisfruta siempre de todo, y se feliz Kat, aca siempre te deseo lo mejor, tqm mi cientifica favorita.\n\nAtentamente tu amigo el sistemas:)"
    
    placeholder = st.empty()
    texto_acumulado = ""

    for letra in mensaje:
        texto_acumulado += letra
        placeholder.markdown(f'<div class="letter">{texto_acumulado}</div>', unsafe_allow_html=True)
        time.sleep(0.03)
    
    # Imagen después de la carta
    st.image("WhatsApp Image 2026-04-11 at 10.03.07 AM.jpeg", 
             caption="¡Que me invite a comer la cumpleañeraa! <3", 
             use_container_width=True)

# --------- EXTRAS ---------
st.write("")
if st.button("🎈 Más sorpresa"):
    st.balloons()
    st.success("¡Que todos tus deseos se hagan realidad, y que seas muy muy feliz! ✨")

st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWxhb21mOTE1ZWVyYjAxa2tqeXJtZHYwZWd3cXh5bDBkZmtvbDljNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hktQ1EEDYax9o7puSD/giphy.gif", width=300)