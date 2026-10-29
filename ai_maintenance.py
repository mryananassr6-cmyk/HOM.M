def classify_maintenance_request(issue_description):
    desc_lower = issue_description.lower()
    
    # 1. الكلمات المفتاحية للحالات العاجلة جداً (HIGH / URGENT)
    urgent_keywords = ["حريق", "fire", "leak", "تسريب", "غاز", "gas", "انفجار", "electricity", "كهرباء", "누수", "화재", "wasser"]
    
    # 2. فحص الأولوية وتوليد الرد متعدد اللغات
    if any(keyword in desc_lower for keyword in urgent_keywords):
        return (
            "🚨 **الأولوية: عاجلة جداً (URGENT)**\n"
            "تم تسجيل بلاغ طارئ! تم إشعار فريق الصيانة الفوري وستصلك استجابة خلال ساعة واحدة.\n\n"
            "🚨 **Priority: HIGH / URGENT**\n"
            "Emergency request logged! Emergency team notified. Response expected within 1 hour."
        )
    else:
        return (
            "ℹ️ **الأولوية: اعتيادية (NORMAL)**\n"
            "تم تسجيل طلب الصيانة العامة بنجاح. سيتم مراجعة الطلب مع الموردين خلال 24 ساعة.\n\n"
            "ℹ️ **Priority: NORMAL**\n"
            "General maintenance request logged. Will be reviewed within 24 hours.")