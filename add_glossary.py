import os
import re

co_dir = r"c:\Users\PC\Downloads\rnfc_gen_web-2\co"

# 1. Create glossaire.html based on rnfc_3.html
rnfc3_path = os.path.join(co_dir, "rnfc_3.html")
with open(rnfc3_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace title
content = re.sub(r'<title>Conclusion \[.*?\]</title>', r'<title>Glossaire [Guide d’exploitation de la plate-forme RNFC]</title>', content)

# Replace navigation (Précédent = rnfc_3.html, Suivant = plan.html)
content = re.sub(r'<li class="pagePrev">.*?</li>', r'<li class="pagePrev"><a rel="prev" target="_self" href="rnfc_3.html" class="btnNav prev" title="Précédent (Conclusion)"><span>Précédent</span></a></li>', content)
content = re.sub(r'<li class="pageNext">.*?</li>', r'<li class="pageNext"><a rel="next" target="_self" href="plan.html" class="btnNav next" title="Suivant (Outils)"><span>Suivant</span></a></li>', content)

# Replace main content
new_content = """<section class="hBk article conclu"><h2 class="hBk_ti noIndex"><span>Glossaire du RNFC</span></h2><div class="hBk_co "><div class="rBk "><p><strong class="txt_emp_is ">B</strong></p><ul><li><strong class="txt_emp_is ">Branche professionnelle (شعبة مهنية)</strong> : Groupe ou ensemble de spécialités couvrant un ou plusieurs secteurs d’activités.</li><li><strong class="txt_emp_is ">Bloc de compétences (أساس الكفاءات)</strong> : Ensemble de savoirs, savoir-être et savoir-faire fondamentaux pour exercer un métier ou une profession.</li></ul><p><strong class="txt_emp_is ">C</strong></p><ul><li><strong class="txt_emp_is ">Compétence (كفاءة)</strong> : Ensemble intégré de savoirs, savoir-faire, savoir-être et savoir-évoluer permettant de réaliser adéquatement une tâche ou une activité de travail.</li><li><strong class="txt_emp_is ">Compétence complémentaire (كفاءة تكميلية)</strong> : Connaissances ou savoirs de base qui contribuent à l’exercice d'une activité professionnelle.</li><li><strong class="txt_emp_is ">Compétence professionnelle (كفاءة مهنية)</strong> : Aptitude à exercer efficacement un métier, une fonction ou certaines tâches spécifiques.</li><li><strong class="txt_emp_is ">Compétences soft skills (كفاءات الحياة)</strong> : Aptitudes personnelles, sociales et comportementales qui permettent à une personne d’interagir efficacement avec les autres.</li></ul><p><strong class="txt_emp_is ">D</strong></p><ul><li><strong class="txt_emp_is ">Débouché professionnel (فرص مهنية)</strong> : Opportunité de travail ou de carrière offerte à la suite d’une formation.</li><li><strong class="txt_emp_is ">Domaine (مجال)</strong> : Ensemble de qualifications professionnelles se rapportant à un ou plusieurs domaines structurés.</li></ul><p><strong class="txt_emp_is ">E</strong></p><ul><li><strong class="txt_emp_is ">Exigence du métier (متطلبات المهنة)</strong> : Connaissances, compétences, qualités personnelles requises.</li></ul><p><strong class="txt_emp_is ">F</strong></p><ul><li><strong class="txt_emp_is ">Formation (تكوين)</strong> : Action d’instruire et d’éduquer.</li><li><strong class="txt_emp_is ">Formation diplômante (تكوين متوج بشهادة)</strong> : Formation professionnelle de longue durée débouchant sur un diplôme.</li><li><strong class="txt_emp_is ">Formation professionnelle (تكوين مهني)</strong> : Vise l'acquisition de qualifications pratiques.</li><li><strong class="txt_emp_is ">Formation de qualification (تكوين تأهيلي)</strong> : Formation de courte durée.</li></ul><p><strong class="txt_emp_is ">M</strong></p><ul><li><strong class="txt_emp_is ">Métier (مهنة)</strong> : Ensemble d’emplois ou de situations de travail.</li><li><strong class="txt_emp_is ">Modalité d’évaluation (طريقة التقييم)</strong> : Techniques et outils utilisés pour mesurer les connaissances.</li><li><strong class="txt_emp_is ">Module qualifiant (وحدة تأهيلية)</strong> : Connaissances techniques nécessaires.</li></ul><p><strong class="txt_emp_is ">N</strong></p><ul><li><strong class="txt_emp_is ">Niveau d’accès (مستوى الولوج)</strong> : Niveau scolaire ou professionnel requis.</li><li><strong class="txt_emp_is ">Nomenclature (مدونة الشعب)</strong> : Document de référence.</li></ul><p><strong class="txt_emp_is ">Q</strong></p><ul><li><strong class="txt_emp_is ">Qualification (تأهيل)</strong> : Ensemble de compétences et capacités nécessaires.</li></ul><p><strong class="txt_emp_is ">R</strong></p><ul><li><strong class="txt_emp_is ">Référentiel (مرجع)</strong> : Inventaire de compétences.</li></ul><p><strong class="txt_emp_is ">S</strong></p><ul><li><strong class="txt_emp_is ">Sanction (تتويج)</strong> : Délivrance d’une attestation officielle.</li><li><strong class="txt_emp_is ">Secteur (قطاع)</strong> : Ensemble d’activités.</li><li><strong class="txt_emp_is ">Sous-domaine (مجال فرعي)</strong> : Subdivision d’un domaine.</li><li><strong class="txt_emp_is ">Spécialité (تخصص)</strong> : Dénomination de la formation.</li></ul></div></div></section>"""
content = re.sub(r'<section class="hBk article conclu">.*?</section>', new_content, content, flags=re.DOTALL)

with open(os.path.join(co_dir, "glossaire.html"), "w", encoding="utf-8") as f:
    f.write(content)

# 2. Update all HTML files menu
menu_rnfc3_pattern = re.compile(r'(<li class="(?:sel_no|sel_yes) anc_no type_l\s+dpt_0 conclu"><div class="lbl type_l" id="rnfc_3\.html">.*?</li>)')
glossaire_li = r'<li class="sel_no anc_no type_l  dpt_0 conclu"><div class="lbl type_l" id="glossaire.html"><a href="glossaire.html" target="_self" class="item"><span>Glossaire</span></a></div></li>'

for file in os.listdir(co_dir):
    if file.endswith(".html"):
        filepath = os.path.join(co_dir, file)
        with open(filepath, "r", encoding="utf-8") as f:
            file_content = f.read()
        
        # update menu
        if "id=\"glossaire.html\"" not in file_content:
            file_content = menu_rnfc3_pattern.sub(r'\1' + glossaire_li, file_content)
        
        # In rnfc_3.html, update "Suivant" button to point to glossaire.html instead of plan.html
        if file == "rnfc_3.html":
            file_content = re.sub(r'<li class="pageNext"><a rel="next" target="_self" href="plan\.html" class="btnNav next" title="Suivant \(Outils\)"><span>Suivant</span></a></li>', r'<li class="pageNext"><a rel="next" target="_self" href="glossaire.html" class="btnNav next" title="Suivant (Glossaire)"><span>Suivant</span></a></li>', file_content)

        # In glossaire.html, update menu selection
        if file == "glossaire.html":
            file_content = file_content.replace('id="rnfc_3.html"><span class="item"><span>Conclusion</span></span>', 'id="rnfc_3.html"><a href="rnfc_3.html" target="_self" class="item"><span>Conclusion</span></a>')
            file_content = re.sub(r'<li class="sel_yes anc_no type_l\s+dpt_0 conclu"><div class="lbl type_l" id="rnfc_3\.html">', r'<li class="sel_no anc_no type_l  dpt_0 conclu"><div class="lbl type_l" id="rnfc_3.html">', file_content)
            
            # Make glossaire selected
            file_content = file_content.replace('<li class="sel_no anc_no type_l  dpt_0 conclu"><div class="lbl type_l" id="glossaire.html"><a href="glossaire.html" target="_self" class="item"><span>Glossaire</span></a></div></li>', '<li class="sel_yes anc_no type_l  dpt_0 conclu"><div class="lbl type_l" id="glossaire.html"><span class="item"><span>Glossaire</span></span></div></li>')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(file_content)

print("HTML files updated")
