import re
SKILL_KEYWORDS = [
    "Python", "Java", "C++", "Go",
    "FastAPI", "Django", "Flask",
    "MySQL", "Redis", "MongoDB",
    "Docker", "Kubernetes", "Git", "Linux",
    "RAG", "Agent", "LangChain",
]


def extract_skills(text: str) -> list[str]:
    """从 JD 文本中找出出现过的技能关键词"""
    skill = []
    for k in SKILL_KEYWORDS:
        if k in text:
            skill.append(k)
    return skill

def extract_years(text: str) -> int | None:
    """从 JD 文本中抽取经验年限，找不到返回 None"""
    match = re.search(r"(?<!\d)(\d{1,2})\s*年", text)
    if match is None:
        return None
    return int(match.group(1))

def extract_skills(text: str) -> list[str]:
    """从 JD 文本中找出出现过的技能关键词"""
    skills = []
    for kw in SKILL_KEYWORDS:
        pattern = rf"(?<![A-Za-z]){re.escape(kw)}(?![A-Za-z])"
        if re.search(pattern, text, re.IGNORECASE) is not None:
            skills.append(kw)
    return skills

def extract_title(text: str) -> str:
    """找到以“岗位名称：”开头的那一行，返回后面的内容"""
    for line in text.splitlines(): #按换行切开，得到一个“每行一项”的列表
        line = line.strip() #去掉开头和结尾的空格、换行
        if line.startswith("岗位名称："):
            return line.removeprefix("岗位名称：").strip()
    return "未知岗位"

def extract_education(text: str) -> str | None:
    if "博士" in text:
        return "博士"
    elif "硕士" in text:
        return "硕士"
    elif "本科" in text:
        return "本科"
    return None