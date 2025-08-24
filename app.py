import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Pinouts", layout="wide")
st.title("📐 Pinouts & Notas")

images_dir = Path("images")
if not images_dir.exists():
    st.info("Cria a pasta 'images' e coloca lá as imagens (png/jpg/webp).")
else:
    # lista imagens suportadas
    files = sorted([p for ext in ("*.png","*.jpg","*.jpeg","*.webp") for p in images_dir.glob(ext)])
    query = st.text_input("🔎 Pesquisa por nome do ficheiro", placeholder="ex: ecu, conector, bdm...").strip().lower()

    if query:
        files = [p for p in files if query in p.stem.lower()]

    if not files:
        st.warning("Nenhuma imagem encontrada com esse filtro.")
    else:
        cols = st.columns(3)
        for i, p in enumerate(files):
            with cols[i % 3]:
                st.caption(p.stem.replace("_", " "))
                img = Image.open(p)
                st.image(img, use_container_width=True)

with st.sidebar:
    st.subheader("Notas rápidas")
    st.write("Podes guardar apontamentos no README do repositório ou usar comentários nas imagens (nome do ficheiro bem descritivo ajuda).")

