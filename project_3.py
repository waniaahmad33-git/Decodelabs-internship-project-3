job_roles = {
    "Data Scientist": ["python", "sql", "machine learning", "statistics", "data analysis"],
    "Web Developer": ["html", "css", "javascript", "react", "nodejs"],
    "Backend Developer": ["python", "java", "sql", "apis", "databases"],
    "DevOps Engineer": ["aws", "docker", "linux", "automation", "cloud"],
    "AI Engineer": ["python", "deep learning", "tensorflow", "nlp", "neural networks"],
    "Mobile Developer": ["flutter", "android", "ios", "dart", "kotlin"],
    "Cybersecurity": ["networking", "linux", "python", "ethical hacking", "cryptography"]
}

print("="*45)
print("  AI Career Recommender - Project 3")
print("      DecodeLabs | Batch 2026")
print("="*45)

print("\nApni 3 skills batao:")
skill1 = input("Skill 1: ").lower()
skill2 = input("Skill 2: ").lower()
skill3 = input("Skill 3: ").lower()

user_skills = [skill1, skill2, skill3]
print("\nTumhari skills:", user_skills)

print("\nMatching ho raha hai...")

scores = {}

for role in job_roles:
    match_count = 0
    for skill in user_skills:
        if skill in job_roles[role]:
            match_count = match_count + 1
    scores[role] = match_count

print("\n" + "="*45)
print("  Results:")
print("="*45)

best_role = ""
best_score = -1

for role in scores:
    print(f"{role}: {scores[role]} skill(s) match")
    if scores[role] > best_score:
        best_score = scores[role]
        best_role = role

print("\n" + "="*45)
print(f"  Best Match: {best_role}!")
print(f"  Matched Skills: {best_score} out of 3")
print("="*45)
