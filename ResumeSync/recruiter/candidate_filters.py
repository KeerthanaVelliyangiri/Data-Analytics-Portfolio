import streamlit as st


def filter_candidates(candidates):
    if not candidates:
        return []
    c1, c2, c3 = st.columns(3)
    qualifications = sorted({str(x.get("qualification", "Not stated")) for x in candidates})
    experiences = sorted({str(x.get("experience_level", "Not stated")) for x in candidates})
    with c1:
        q = st.multiselect("Qualification", qualifications, default=qualifications)
    with c2:
        e = st.multiselect("Experience", experiences, default=experiences)
    with c3:
        minimum = st.slider("Minimum match score", 0, 100, 0)
    skill = st.text_input("Filter by skill (optional)").strip().lower()
    out = []
    for x in candidates:
        skills = [str(s).lower() for s in x.get("matched_skills", [])]
        if x.get("qualification", "Not stated") not in q: continue
        if x.get("experience_level", "Not stated") not in e: continue
        if int(x.get("match_percentage", 0)) < minimum: continue
        if skill and not any(skill in s for s in skills): continue
        out.append(x)
    return out
