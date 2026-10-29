
import streamlit as st
from translations import TRANSLATIONS
from ai_maintenance import classify_maintenance_request
from chat import handle_user_query
from searsh_engine import filter_properties, mock_database

# 1. Page Configuration
st.set_page_config(
    page_title="HOM.M - PropTech Ecosystem",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Styles
st.markdown("""
<style>
.stApp {
    background-color: #0b0f19;
}

.stApp p, .stApp span, .stApp label, .stApp div {
    color: #ffffff;
}

section[data-testid="stSidebar"] {
    background-color: #111622 !important;
    border-right: 1px solid #2d3748;
}

section[data-testid="stSidebar"] *, 
section[data-testid="stSidebar"] span, 
section[data-testid="stSidebar"] p, 
section[data-testid="stSidebar"] label, 
section[data-testid="stSidebar"] div {
    color: #ffffff !important;
    opacity: 1 !important;
}

/* Fix Selectbox Background, Text Color, and Opacity */
div[data-testid="stSelectbox"] label, 
div[data-testid="stSelectbox"] div,
div[data-testid="stSelectbox"] span,
div[data-testid="stSelectbox"] p {
    color: #ffffff !important;
    font-weight: bold !important;
    opacity: 1 !important;
}

div[data-baseweb="select"] {
        background-color: #161b26 !important;
        color: #ffffff !important;
        border: 1px solid #00c3ff !important;
        border-radius: 8px !important;
        opacity: 1 !important;
    }

    div[data-baseweb="select"] div {
        background-color: #161b26 !important;
        color: #ffffff !important;
    }

    div[data-baseweb="select"] span {
        color: #ffffff !important;
    }

    div[data-baseweb="select"] svg {
        fill: #ffffff !important;
    }
}

/* Fix Dropdown options menu */
div[data-baseweb="popover"], 
div[data-baseweb="menu"],
ul[role="listbox"] {
    background-color: #161b26 !important;
    opacity: 1 !important;
}

div[data-baseweb="option"], li[role="option"] {
    background-color: #161b26 !important;
    color: #000000 !important;
    opacity: 1 !important;
}

div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] div,
div[data-testid="stMetricLabel"] p {
    color: #d4af37 !important;
    font-size: 1.15rem !important;
    font-weight: bold !important;
    opacity: 1 !important;
}

div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] div {
    color: #ffffff !important;
    font-weight: bold !important;
    opacity: 1 !important;
}

div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #111622 0%, #18202c 100%);
    border: 1px solid #d4af37;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.2);
}

div.stButton > button {
    background: linear-gradient(90deg, #d4af37 0%, #009628 100%);
    color: #0b0f19;
    font-weight: bold;
    border: none;
    border-radius: 8px;
    padding: 10px 24px;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #00c3ff 0%, #0099cc 100%);
    color: #ffffff;
    box-shadow: 0px 0px 12px #00c3ff;
}
</style>
""", unsafe_allow_html=True)
# 1. اعدادات الصفحة الاسلسية
st.set_page_config(
    page_title="HOM.M - PropTech Ecosystem",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. القائمة الجانبية واختيار اللغة
with st.sidebar:
    st.title("HOM.M 👁️ 🔑")
    st.caption("PropTech Ecosystem")
    st.divider()

    lang_choice = st.selectbox(
        "🌐 Language / اللغة",
        options=list(TRANSLATIONS.keys())
    )

    t = TRANSLATIONS[lang_choice]
    st.divider()

    NAV_HOME = t.get("nav_home", "Dashboard")
    NAV_CHAT = t.get("nav_chat", "AI Chatbot")
    NAV_FINANCE = t.get("nav_finance", "Finance")
    NAV_MAINTENANCE = t.get("nav_maintenance", "AI Maintenance")
    NAV_SEARCH = t.get("nav_search", "Smart Search")

    menu = st.radio(
        t.get("select_service", "Select Service:"),
        [NAV_HOME, NAV_CHAT, NAV_FINANCE, NAV_MAINTENANCE, NAV_SEARCH]
    )

# 3. محتوى لوحة التحكم الرئيسية (Dashboard)
if menu == NAV_HOME:
    home_texts = {
        "العربية": {"title": "🏠 لوحة التحكم الرئيسية", "welcome": "مرحباً بك في منصة HOM.M PropTech Ecosystem المتكاملة.", "m1": "العقارات المتاحة", "m2": "طلبات الصيانة", "m3": "التحصيلات المالية"},
        "English": {"title": "🏠 Dashboard", "welcome": "Welcome to the HOM.M PropTech Ecosystem platform.", "m1": "Available Properties", "m2": "Maintenance Requests", "m3": "Financial Collections"},
        "Français": {"title": "🏠 Tableau de bord", "welcome": "Bienvenue sur HOM.M.", "m1": "Propriétés", "m2": "Maintenance", "m3": "Finances"},
        "Deutsch": {"title": "🏠 Dashboard", "welcome": "Willkommen bei HOM.M.", "m1": "Immobilien", "m2": "Wartung", "m3": "Finanzen"},
        "한국어": {"title": "🏠 대시보드", "welcome": "HOM.M에 오신 것을 환영합니다.", "m1": "부동산", "m2": "유지보수", "m3": "재무"}
    }
    cur_home = home_texts.get(lang_choice, home_texts["English"])
    
    st.subheader(cur_home["title"])
    st.write(cur_home["welcome"])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(cur_home["m1"], "12", "+2")
    with col2:
        st.metric(cur_home["m2"], "3", "-1")
    with col3:
        st.metric(cur_home["m3"], "$45,200", "+12%")

# 4. مساعد الذكاء الاصطناعي (AI Chatbot)
elif menu == NAV_CHAT:
    chat_texts = {
        "العربية": {"title": "💬 مساعد الذكاء الاصطناعي العقاري", "placeholder": "اكتب استفسارك هنا...", "btn": "إرسال الاستفسار", "resp": "رد النظام الذكي:"},
        "English": {"title": "💬 AI Real Estate Assistant", "placeholder": "Type your query here...", "btn": "Send Query", "resp": "AI System Response:"},
        "Français": {"title": "💬 Assistant IA", "placeholder": "Tapez votre question...", "btn": "Envoyer", "resp": "Réponse:"},
        "Deutsch": {"title": "💬 KI-Assistent", "placeholder": "Frage eingeben...", "btn": "Senden", "resp": "Antwort:"},
        "한국어": {"title": "💬 AI 어시스턴트", "placeholder": "질문을 입력하세요...", "btn": "보내기", "resp": "응답:"}
    }
    cur_chat = chat_texts.get(lang_choice, chat_texts["English"])

    st.subheader(cur_chat["title"])
    user_query = st.text_input(cur_chat["placeholder"])
    
    if st.button(cur_chat["btn"]):
        if user_query:
            response = handle_user_query(user_query)
            st.success(cur_chat["resp"])
            st.info(response)
        else:
            st.warning("الرجاء كتابة استفسار أولاً.")

# 5. الإدارة المالية (Finance)
elif menu == NAV_FINANCE:
    fin_texts = {
        "العربية": {"title": "💳 الإدارة المالية وحساب الإيجارات", "rent": "قيمة الإيجار الشهري ($):", "serv": "رسوم الخدمات الإضافية ($):", "calc": "حساب الإيجار الكلي", "status": "التحقق من حالة الدفع", "total": "إجمالي المبلغ المستحق:", "paid": "حالة الدفع: تم السداد بنجاح ✅"},
        "English": {"title": "💳 Financial Management & Rent", "rent": "Monthly Rent ($):", "serv": "Service Fees ($):", "calc": "Calculate Total Rent", "status": "Check Payment Status", "total": "Total Amount Due:", "paid": "Payment Status: Paid Successfully ✅"}
    }
    cur_fin = fin_texts.get(lang_choice, fin_texts["English"])

    st.subheader(cur_fin["title"])
    r_val = st.number_input(cur_fin["rent"], value=2500)
    s_val = st.number_input(cur_fin["serv"], value=300)
    
    if st.button(cur_fin["calc"]):
        total = calculate_monthly_rent(r_val, s_val)
        st.success(f"{cur_fin['total']} ${total}")
        
    if st.button(cur_fin["status"]):
        st.info(cur_fin["paid"])

# 6. صيانة الذكاء الاصطناعي (AI Maintenance)
elif menu == NAV_MAINTENANCE:
    maint_texts = {
        "العربية": {"title": "🔧 نظام صيانة الذكاء الاصطناعي", "desc": "وصف المشكلة أو العطل العقاري:", "btn": "تصنيف وإرسال الطلب"},
        "English": {"title": "🔧 AI Maintenance System", "desc": "Describe the property issue:", "btn": "Classify & Submit Request"}
    }
    cur_maint = maint_texts.get(lang_choice, maint_texts["English"])

    st.subheader(cur_maint["title"])
    issue_desc = st.text_area(cur_maint["desc"])
    
    if st.button(cur_maint["btn"]):
        if issue_desc:
            classification = classify_maintenance_request(issue_desc)
            st.warning(classification)
        else:
            st.warning("الرجاء كتابة وصف المشكلة.")

# 7. محرك البحث والفلترة العقارية (Smart Search)
elif menu == NAV_SEARCH:
    search_texts = {
        "العربية": {
            "title": "🔍 محرك البحث والفلترة العقارية",
            "city": "اختر المدينة:",
            "price": "السعر الأقصى ($):",
            "btn": "بحث عن عقارات",
            "found": "تم العثور على نتائج مطابقة:",
            "none": "لا توجد نتائج تطابق خيارات البحث.",
            "city_label": "المدينة",
            "price_label": "السعر"
        },
        "English": {
            "title": "🔍 Smart Property Search & Filter Engine",
            "city": "Select City:",
            "price": "Maximum Monthly Price ($):",
            "btn": "Search Properties",
            "found": "Found matching properties:",
            "none": "No properties match your exact criteria.",
            "city_label": "City",
            "price_label": "Price"
        },
        "Français": {
            "title": "🔍 Recherche Immobilière",
            "city": "Ville:",
            "price": "Prix max ($):",
            "btn": "Rechercher",
            "found": "Propriétés trouvées:",
            "none": "Aucun résultat.",
            "city_label": "Ville",
            "price_label": "Prix"
        },
        "Deutsch": {
            "title": "🔍 Immobiliensuche",
            "city": "Stadt wählen:",
            "price": "Max. Preis ($):",
            "btn": "Suchen",
            "found": "Gefundene Objekte:",
            "none": "Keine Ergebnisse.",
            "city_label": "Stadt",
            "price_label": "Preis"
        },
        "한국어": {
            "title": "🔍 스마트 부동산 검색",
            "city": "도시 선택:",
            "price": "최대 가격 ($):",
            "btn": "부동산 검색",
            "found": "일치하는 부동산:",
            "none": "검색 결과가 없습니다.",
            "city_label": "도시",
            "price_label": "가격"
        }
    }
    cur_search = search_texts.get(lang_choice, search_texts["English"])
    
    prop_translations = {
        "Luxury Apartment with Burj Khalifa View": {
            "العربية": "شقة فاخرة بإطلالة على برج خليفة",
            "Français": "Appartement de luxe avec vue sur le Burj Khalifa",
            "Deutsch": "Luxusapartment mit Blick auf den Burj Khalifa",
            "한국어": "버즈 칼리파 뷰가 있는 럭셔리 아파트"
        },
        "Modern Budget Studio": {
            "العربية": "استوديو حديث واقتصادي",
            "Français": "Studio moderne et économique",
            "Deutsch": "Modernes Budget-Studio",
            "한국어": "모던한 버짓 스튜디오"
        },
        "Marina Luxury Villa": {
            "العربية": "فيلا مارينا الفاخرة",
            "Français": "Villa de luxe à Marina",
            "Deutsch": "Luxusvilla in Marina",
            "한국어": "마리나 럭셔리 빌라"
        },
        "Sharjah Family Flat": {
            "العربية": "شقة عائلية في الشارقة",
            "Français": "Appartement familial à Sharjah",
            "Deutsch": "Familienwohnung in Sharjah",
            "한국어": "샤르자 패밀리 플랫"
        }
    }

    st.subheader(cur_search["title"])
    target_city = st.selectbox(cur_search["city"], ["Dubai", "Abu Dhabi", "Sharjah"])
    max_price = st.slider(cur_search["price"], 1000, 10000, 4000, step=500)
    
    if st.button(cur_search["btn"]):
        results = filter_properties(mock_database, target_city, max_price, 2)
        if results:
            st.success(cur_search["found"])
            for prop in results:
                orig_title = prop['title']
                translated_title = prop_translations.get(orig_title, {}).get(lang_choice, orig_title)
                st.info(f"🏡 **{translated_title}** | 📍 {cur_search['city_label']}: {prop['city']} | 💰 {cur_search['price_label']}: ${prop['price']}")
        else:
            st.warning(cur_search["none"])