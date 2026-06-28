import re
from datetime import datetime

REF_DATE = datetime(2026, 6, 25)

# Comprehensive list of service-based IT consultancies (global and Indian)
CONSULTING_FIRMS = [
    r"tata consultancy", r"\btcs\b", r"\bwipro\b", r"\binfosys\b", r"\baccenture\b", 
    r"\bcognizant\b", r"\bcapgemini\b", r"tech mahindra", r"\bhcl\b", r"\bmindtree\b",
    r"\blti\b", r"l&t infotech", r"\bhexaware\b", r"\bmphasis\b", r"ust global", 
    r"persistent systems", r"\bcoforge\b", r"\bgenpact\b", r"\bibm\b", r"deloitte", 
    r"pwc", r"ey\b", r"kpmg", r"ltts", r"tata elxsi", r"cybertek", r"collabera",
    r"teksystems"
]

# Non-technical stuffer keywords in titles
STUFFER_TITLES = [
    r"marketing", r"design", r"graphic", r"writer", r"content", r"sales", r"hr\b",
    r"human resource", r"recruiter", r"operations manager", r"support", r"customer",
    r"accountant", r"finance", r"admin", r"salesperson", r"legal", r"executive assistant",
    r"business development", r"operations associate", r"social media", r"copywriter"
]

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text)
    return text.strip()
 
def parse_date(date_str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str.split("T")[0], "%Y-%m-%d")
    except Exception:
        return None

def get_months_between(start_str, end_str):
    start = parse_date(start_str)
    if not start:
        return 0
    end = parse_date(end_str) if end_str else REF_DATE
    if not end:
        end = REF_DATE
    if end < start:
        return 0
    return (end.year - start.year) * 12 + (end.month - start.month)

def is_consulting_firm(company_name):
    if not company_name:
        return False
    name_lower = company_name.lower()
    for pattern in CONSULTING_FIRMS:
        if re.search(pattern, name_lower):
            return True
    return False

def check_honeypot(c):
    skills = c.get("skills", [])
    history = c.get("career_history", [])
    profile = c.get("profile", {})
    
    # 1. Expert/Advanced skills with 0 duration
    fake_skills_count = sum(
        1 for s in skills 
        if s.get("proficiency") in ["expert", "advanced"] and s.get("duration_months", 0) == 0
    )
    if fake_skills_count >= 3:
        return True
        
    # 2. Date anomalies
    for job in history:
        start_str = job.get("start_date")
        end_str = job.get("end_date")
        desc = job.get("description", "")
        
        start_dt = parse_date(start_str)
        end_dt = parse_date(end_str) if end_str else REF_DATE
        
        if start_dt and end_dt and start_dt > end_dt:
            return True
            
        founding_match = re.search(r"\b(?:founded|est\.|established|incorporated|started)\s*(?:in\s+)?(\d{4})\b", desc.lower())
        if founding_match and start_dt:
            founding_year = int(founding_match.group(1))
            if start_dt.year < founding_year:
                return True
                
        duration = job.get("duration_months", 0)
        calc_months = get_months_between(start_str, end_str)
        if duration > calc_months + 12:
            return True

    # 3. YOE contradiction
    profile_yoe = profile.get("years_of_experience", 0.0)
    calc_yoe = sum(j.get("duration_months", 0) for j in history) / 12.0
    if profile_yoe > calc_yoe + 5.0:
        return True

    return False

def check_stuffer(profile_title, history):
    title_lower = profile_title.lower()
    for pattern in STUFFER_TITLES:
        if re.search(pattern, title_lower):
            return True
            
    if history:
        stuffer_jobs = 0
        for job in history:
            job_title = job.get("title", "").lower()
            for pattern in STUFFER_TITLES:
                if re.search(pattern, job_title):
                    stuffer_jobs += 1
                    break
        if stuffer_jobs / len(history) >= 0.75:
            return True
            
    return False

def is_non_tech_title(title):
    if not title:
        return True
    title_lower = title.lower()
    
    # 1. Explicitly non-tech/irrelevant engineering fields
    non_tech_fields = [
        "civil", "mechanical", "electrical", "chemical", "industrial", "aerospace", 
        "marine", "construction", "structural", "petroleum", "biomedical", "hardware"
    ]
    if any(re.search(r"\b" + field + r"\b", title_lower) for field in non_tech_fields):
        return True
        
    # 2. General non-tech roles
    non_tech_roles = [
        "marketing", "design", "graphic", "writer", "content", "sales", "hr", "human resource",
        "recruiter", "operations", "support", "customer", "accountant", "finance", "admin",
        "legal", "executive assistant", "business development", "social media", "copywriter",
        "project manager", "product manager", "scrum master", "business analyst", "civil engineer",
        "mechanical engineer"
    ]
    for role in non_tech_roles:
        if re.search(r"\b" + re.escape(role) + r"\b", title_lower):
            # Exception for technical managers/analysts
            if any(term in title_lower for term in ["technical", "tech", "engineering", "data", "software"]):
                continue
            return True
            
    # If it doesn't match any tech terms at all, it's probably non-tech
    tech_terms = [
        "software", "developer", "programmer", "engineer", "architect", "scientist", 
        "data", "analyst", "ai", "ml", "nlp", "vision", "retrieval", "search", 
        "recommendation", "deep learning", "machine learning", "backend", "frontend",
        "fullstack", "full stack", "cloud", "devops", "sre", "platform", "infrastructure",
        "applied science", "tech", "technical"
    ]
    if not any(re.search(r"\b" + re.escape(term) + r"\b", title_lower) for term in tech_terms):
        return True
        
    return False

def is_consulting_only(history):
    if not history:
        return False
    has_product_exp = False
    for job in history:
        if not is_consulting_firm(job.get("company", "")):
            has_product_exp = True
            break
    return not has_product_exp
