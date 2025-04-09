import os

# Define folders
folders = ['chapters', 'appendices']
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Define chapter names and filenames
chapters = [
    ("chapter1_introduction.tex", "Introduction — Why Field Theory for Chemistry?"),
    ("chapter2_foundations.tex", "Mathematical and Physical Foundations"),
    ("chapter3_qc_standard.tex", "Quantum Chemistry — Standard Frameworks Revisited"),
    ("chapter4_mol_ops.tex", "Molecular Creation and Annihilation Operators"),
    ("chapter5_algebra.tex", "Algebraic Structure of Molecular Operators"),
    ("chapter6_eft.tex", "Effective Field Theory (EFT) for Molecular Systems"),
    ("chapter7_path_integral.tex", "Path Integral Formulation and Statistical Ensembles"),
    ("chapter8_examples.tex", "Case Studies and Illustrative Examples"),
    ("chapter9_outlook.tex", "Outlook and Future Directions")
]

appendices = [
    ("appendix_a_derivations.tex", "Detailed Mathematical Derivations"),
    ("appendix_b_notation.tex", "Glossary and Notation Summary"),
    ("appendix_c_techniques.tex", "Review of Advanced Techniques (Optional)")
]

# Template content for chapters and appendices
def make_content(title, label):
    return f"""% {title}
\\chapter{{{title}}}
\\label{{chap:{label}}}

% --- Begin content ---

% TODO: Write content for {title}

% --- End content ---
"""

# Write chapter files
for filename, title in chapters:
    label = filename.replace("chapter", "").replace(".tex", "").replace("_", "")
    with open(os.path.join("chapters", filename), "w") as f:
        f.write(make_content(title, label))

# Write appendix files
for filename, title in appendices:
    label = filename.replace("appendix_", "").replace(".tex", "").replace("_", "")
    with open(os.path.join("appendices", filename), "w") as f:
        f.write(make_content(title, label))

print("Chapter and appendix files created successfully.")

