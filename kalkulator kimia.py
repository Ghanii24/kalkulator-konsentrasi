import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="⚗️ Kalkulator Konsentrasi Larutan",
    page_icon="🧪",
    layout="centered"
)

# Judul utama
st.title("⚗️💧 Kalkulator Konsentrasi Larutan 🧪")
st.markdown("""
Aplikasi ini membantu Anda menghitung berbagai jenis konsentrasi larutan:

- 🔹 *PPM (Part per Million)*
- 🧪 *Molaritas (mol/L)*
- ⚖️ *Molalitas (mol/kg)*
- 📏 *Normalitas (N)*
- 📘 *Molaritas dari Massa & Mr*

Silakan pilih jenis perhitungan dan masukkan data yang diperlukan. 📥
""")

# Pilihan jenis perhitungan
choice = st.selectbox("🔍 Pilih jenis konsentrasi yang ingin dihitung:", 
                      ["🟦 PPM (part per million)", 
                       "🧪 Molaritas (mol/L)", 
                       "⚖️ Molalitas (mol/kg)", 
                       "📏 Normalitas (N)",
                       "📘 Molaritas (dari massa & Mr)"])

st.divider()

# Fungsi perhitungan
def hitung_ppm(massa_zat, volume_larutan):
    return (massa_zat / volume_larutan)

def hitung_molaritas(mol_zat, volume_larutan):
    return mol_zat / volume_larutan

def hitung_molalitas(mol_zat, massa_pelarut):
    return mol_zat / massa_pelarut

def hitung_normalitas(ekivalen, volume_larutan):
    return ekivalen / volume_larutan

def hitung_molaritas_dari_massa(massa_zat, mr, volume_larutan):
    mol = massa_zat / mr
    return mol / volume_larutan

# Input dan output berdasarkan pilihan
if "PPM" in choice:
    st.subheader("🟦 Perhitungan PPM")
    massa_zat = st.number_input("📦 Massa zat terlarut (mg)", min_value=0.0, step=0.01)
    volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)
    
    if st.button("🧮 Hitung PPM"):
        ppm = hitung_ppm(massa_zat, volume_larutan)
        st.success(f"✅ Konsentrasi PPM: {ppm:.2f} mg/L")

elif "Molaritas (mol/L)" in choice:
    st.subheader("🧪 Perhitungan Molaritas")
    mol_zat = st.number_input("🧬 Jumlah mol zat (mol)", min_value=0.0, step=0.01)
    volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)

    if st.button("🧮 Hitung Molaritas"):
        molaritas = hitung_molaritas(mol_zat, volume_larutan)
        st.success(f"✅ Konsentrasi Molaritas: {molaritas:.2f} mol/L")

elif "Molalitas" in choice:
    st.subheader("⚖️ Perhitungan Molalitas")
    mol_zat = st.number_input("🧬 Jumlah mol zat (mol)", min_value=0.0, step=0.01)
    massa_pelarut = st.number_input("💧 Massa pelarut (kg)", min_value=0.0001, step=0.01)

    if st.button("🧮 Hitung Molalitas"):
        molalitas = hitung_molalitas(mol_zat, massa_pelarut)
        st.success(f"✅ Konsentrasi Molalitas: {molalitas:.2f} mol/kg")

elif "Normalitas" in choice:
    st.subheader("📏 Perhitungan Normalitas")
    ekivalen = st.number_input("🧪 Jumlah ekivalen zat (mol ekivalen)", min_value=0.0, step=0.01)
    volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)

    if st.button("🧮 Hitung Normalitas"):
        normalitas = hitung_normalitas(ekivalen, volume_larutan)
        st.success(f"✅ Konsentrasi Normalitas: {normalitas:.2f} N")

elif "Molaritas (dari massa & Mr)" in choice:
    st.subheader("📘 Perhitungan Molaritas dari Massa & Mr")
    massa_zat = st.number_input("⚖️ Massa zat (gram)", min_value=0.0, step=0.01)
    mr = st.number_input("🔬 Massa molar (Mr) zat (g/mol)", min_value=0.01, step=0.01)
    volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)

    if st.button("🧮 Hitung Molaritas dari Massa"):
        molaritas_massa = hitung_molaritas_dari_massa(massa_zat, mr, volume_larutan)
        st.success(f"✅ Konsentrasi Molaritas: {molaritas_massa:.2f} mol/L")

# Watermark dengan emotikon
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 16px;'>
        🧪✨ Dibuat dengan cinta kimia oleh: <br>
        👩‍🔬 <b>Andika</b>, 👨‍🔬 <b>Audrey</b>, 🧑‍🔬 <b>Maqdalene</b>, 👩‍🔬 <b>Raihan</b>, 👨‍🔬 <b>Rifa</b> <br>
        🔬🤝🌟 #TimKimiaHebat
    </div>
    """, unsafe_allow_html=True
)
