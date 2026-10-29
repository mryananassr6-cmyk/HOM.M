def handle_user_query(query):
    # تحويل النص إلى حروف صغيرة مع إضافة أقواس الدالة () لتجنب TypeError
    query_lower = query.lower()
    
    # 1. التحية (Greetings)
    if any(w in query_lower for w in ["مرحبا", "أهلا", "hello", "hi", "bonjour", "hallo", "안녕하세요"]):
        return "أهلاً بك في HOM.M! كيف يمكنني مساعدتك؟ / Welcome to HOM.M! How can I help you?"
    
    # 2. أوقات الصيانة (Maintenance Hours)
    elif any(w in query_lower for w in ["صيانة", "أوقات", "عمل", "maintenance", "hours", "horaires", "öffnungzeiten", "유지보수"]):
        return "ساعات عمل الصيانة: من الإثنين للجمعة (8:00 ص - 6:00 م).\nMaintenance hours: Mon-Fri (8:00 AM - 6:00 PM)."
    
    # 3. الإيجار والدفع (Rent & Payment)
    elif any(w in query_lower for w in ["إيجار", "دفع", "مالية", "rent", "pay", "loyer", "miete", "임대료"]):
        return "يمكنك إدارة الدفعات والإيجار من قسم الإدارة المالية.\nYou can manage payments in the Finance section."
    
    # 4. البحث العقاري (Property Search)
    elif any(w in query_lower for w in ["عقار", "بحث", "شقة", "property", "search", "recherche", "suche", "검색"]):
        return "يمكنك البحث عن العقارات وتصفيتها من قسم البحث العقاري الذكي.\nYou can search properties in the Smart Search section."
    
    # 5. رد افتراضي متعدد اللغات للأدوار الأخرى
    else:
        return f"تم استقبال استفسارك: '{query}'. سيقوم المساعد الذكي بمعالجته فوراً."